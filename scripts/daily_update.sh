#!/usr/bin/env bash
set -euo pipefail

ROOT="/workspace/dgl/projects/world-model-interactive-guide"
LOCK_DIR="$ROOT/.daily-update.lock"
RUN_DIR="$ROOT/.daily-update-runs"

cd "$ROOT"
branch="$(git branch --show-current)"
if [[ "$branch" == "main" || -z "$branch" ]]; then
  echo "refusing to run daily content updates directly on main" >&2
  exit 2
fi
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "another daily update is already running" >&2
  exit 3
fi
trap 'rmdir "$LOCK_DIR"' EXIT

mkdir -p "$RUN_DIR"
run_id="$(date +%Y%m%d-%H%M%S)"
prompt=$(cat <<'EOF'
执行本仓库 .agent/workflows/skills/daily-comprehensive-update.md 的每日更新流程。

时效性优先：先查最近 24 小时，再查最近 7 天，最后查最近 30 天。处理论文、arXiv 预印本、Technical Report、Official Model Report、Project/System Report，以及 GitHub Releases/Issues/Discussions、Hugging Face Discussions、官方论坛和项目公告。

只处理具身智能主站；绝不扫描或修改 world_model_interactive_guide/legacy/。优先更新 07_paper_tracker.html 和 08_community.html，必要时同步 01_industry.html、13_world_models.html、12_real_world_rl.html、04_data.html、10_benchmarks.html、references.html、09_update_log.html。

每条新增内容必须有原始链接、来源类型、作者/发布机构、发布日期或版本日期、事实边界和开源状态。没有高价值增量时不要制造条目，在 09_update_log.html 记录今日扫描结果。完成后运行 HTML、链接、资源和 legacy 边界 QA。不要提交或推送到 main。
EOF
)

codex exec --search --cd "$ROOT" --sandbox workspace-write --ask-for-approval never \
  --output-last-message "$RUN_DIR/$run_id.codex.txt" "$prompt"

git diff --check
if git diff --name-only | grep -q '^world_model_interactive_guide/legacy/'; then
  echo "legacy was modified; refusing to commit" >&2
  exit 4
fi

if [[ -z "$(git status --short)" ]]; then
  echo "no changes to publish"
  exit 0
fi

git add README.md .agent/workflows/skills/daily-comprehensive-update.md .agent/workflows/skills/README.md world_model_interactive_guide scripts
git commit -m "chore: daily embodied AI research update $run_id"
git push -u origin "$branch"
echo "pushed daily update branch: $branch"
