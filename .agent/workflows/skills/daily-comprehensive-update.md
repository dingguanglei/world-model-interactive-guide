---
description: AntiGravity「每日例行完整更新」固化流程（可重复执行）
---

## Skill: Daily Comprehensive Update（每日例行完整更新）

本 skill 用于把“每天例行完整更新”固化为可重复执行的操作流程与质量规则，适用于本仓库 `world_model_interactive_guide/` 的“具身智能单领域”主站维护。自动入口为 `scripts/daily_update.sh`，默认按 Asia/Shanghai 每天执行一次。

> 核心原则：**宁缺毋滥**。如果当天没有**高价值、可追溯**的新信息，允许不更新对应章节，但必须保持规范合规（尤其是 last-updated 与引用）。

---

## 0. 前置约束（必须满足）

- **规范来源（最高优先级）**：`.agent/workflows/antigravity-content-guide.md`
- **可追溯性**：任何关键结论/数字/主张必须有**可点击权威来源**（论文优先 arXiv/PDF/Project Page，其次官方 GitHub/官方博客/官方发布）。
- **范围约束**：
  - 主站更新对象：`index.html`、`01_industry.html`、`04_data.html`、`13_world_models.html`、`12_real_world_rl.html`、`07_paper_tracker.html`、`08_community.html`、`09_update_log.html`、`10_benchmarks.html`、`references.html`
  - `02_product.html`、`03_architecture.html`、`05_roadmap.html`、`06_companies.html`、`11_edge_chip.html` 为资料/备用页；公司与芯片的日更结论优先回写 `01_industry.html`
  - 历史世界模型内容在 `legacy/` 目录，只做归档浏览，不做日更维护
  - 后续常规更新一律忽略 `legacy/`（不扫描、不改写、不做批量替换）
- **更新型章节页页头**：所有更新型页面顶部必须包含：

```html
<div class="last-updated">
    ⏰ <strong>最后更新时间</strong>: YYYY-MM-DD | 本页内容将每日更新「XXXXXX」。
</div>
```

- **样式统一约定（重要）**：
  - `last-updated` 的展示样式统一由 `world_model_interactive_guide/css/style.css` 中的 `.last-updated` 负责
  - 各章节页面 **禁止** 在内联 `<style>` 里重复定义 `.last-updated { ... }`（避免样式漂移与不一致）
  - **日期刷新口径**：只有当该章节页面发生**实质内容更新**时才刷新 `最后更新时间`；纯样式/排版统一不刷新（只在 `09_update_log.html` 记录）

- **环境约定**：
  - 项目根目录使用 `.venv`
  - 必要环境变量与参数放在根目录 `.env`
  - 所有 pip 安装用：`uv pip install ...`（如环境缺少 uv，先安装 uv）

---

## 1. 每日执行顺序（强制：具身智能主站）

按以下顺序“逐页扫描 → 决策更新/跳过 → 记录到更新日志”：

1) `index.html` 概览  
2) `01_industry.html` 行业全景（产品、公司、端上芯片）
3) `04_data.html` 数据工程（采集与合成）
4) `13_world_models.html` 模型（VLA / WAM）
5) `12_real_world_rl.html` 强化学习（Real-World RL）
6) `07_paper_tracker.html` 论文与技术报告追踪
7) `10_benchmarks.html` 评测基准
8) `08_community.html` 社区讨论
9) `09_update_log.html` 更新日志
10) `references.html` 参考资料

---

## 2. 信息源扫描（建议每日最小集合）

### 2.1 论文（Papers）

- **arXiv API**：`http://export.arxiv.org/api/query`
- **关键词建议**：
  - `embodied intelligence`, `robot learning`, `policy learning`, `sim2real`, `manipulation`, `VLA`
- **分类建议**：`cs.CV`, `cs.LG`, `cs.AI`（按需要扩展）
- **时效硬门槛**：先查最近 24 小时，再查最近 7 天，最后才补最近 30 天；条目按原始发布时间/版本更新时间倒序。旧条目只有在出现新版本、纠错或新的实机证据时才更新。
- **来源类型**：明确标注 `Paper`、`Preprint`、`Technical Report`、`Official Model Report` 或 `Project/System Report`；技术报告和官方材料不得写成“已发表论文”。
- **机构归属**：记录作者机构、发布公司或实验室；不确定时写“待核实”，不得猜测。

### 2.2 代码/权重/数据（GitHub / HF / ModelScope）

- GitHub：项目开源、release、demo、issue 里程碑
- HuggingFace：models / datasets / spaces（权重与数据集的权威入口）
- ModelScope：国内权重镜像/官方发布入口（若仓库提供）

### 2.3 官方发布（Products / Research）

- 官方博客、官方项目页、官方论文 PDF / arXiv
- **禁止**用“二手解读”替代权威来源（社区讨论只能作为社区章节素材）

### 2.4 社区（Community）

- X/Twitter、Reddit、HF Discussions、技术博客（Substack/Medium）
- 社区引用尽量提供原帖链接；观点必须与事实分离（观点只写在 Commentary）
- 每日检查 GitHub Releases/Issues/Discussions、Hugging Face Discussions、官方论坛、项目公告和公开技术博客；X/Reddit 仅作线索，性能/版本等事实必须回溯一手来源。
- 记录平台、作者/机构、发布时间、原帖链接和事实边界；无原帖、无作者或纯转述的内容不进入主站。

---

## 3. 是否更新：价值判据（必须显式判断）

只有满足以下之一，才更新对应章节（否则跳过并不“水更”）：

- **新增**：出现新的论文/项目/产品版本，并且能给出权威链接
- **纠错**：发现现有内容引用错误、数字不一致、链接失效，需要修正
- **补全关键缺口**：例如某条目缺 GitHub/权重/数据集状态、缺来源定位、缺主图、缺三段解读
- **重大变化**：官方博客更新（例如页面 `dateModified` 变化且新增了关键口径）

---

## 4. 章节级硬性规则（重点）

### 4.1 `07_paper_tracker.html`（论文与技术报告追踪）

- **排序**：按发布日期从新到旧
- **年月折叠**：`<details>`，默认展开最近 3 个月
- **标题**：必须可点击跳转原文（优先 arXiv/PDF/Project Page）
- **来源类型**：卡片中必须标注 Paper/Preprint/Technical Report/Official Model Report/Project Report。
- **时效字段**：必须写发布日期或版本日期；有更新日期时同时记录 `released` 与 `updated`，不能只写抓取日期。
- **机构归属**：标注作者机构、发布公司或实验室；不确定时写“机构待核实”。
- **必须三段垂直结构**：
  - 🟢 通俗解读
  - 🔴 专业解读（可复现：逐条贡献/机制/指标/代价/失败模式）
  - 🧠 AntiGravity’s Commentary（观点，严禁夹带事实）
- **来源定位（强制）**：Abstract / §x / Fig.x / Table.x（并给可点击链接）
- **开源状态（强制）**：代码/参数/数据集分别标注 `开源/未公开/未知`，能链接则必须链接
- **论文主图（强烈建议/重要论文强制）**：
  - 图片放到 `world_model_interactive_guide/assets/papers/`
  - `<img src="assets/papers/arxiv-<id>-fig1.webp" ...>`

### 4.2 `10_benchmarks.html`（评测基准）

- 条目沿用三段结构（🟢→🔴→🧠）
- 必须写清：What it measures / How to use / Pitfalls / 判定者（模型/人/传统算法）
- 必须给权威链接（论文/项目页/仓库/数据集）

### 4.3 `08_community.html`（社区讨论）

- 每条必须：平台来源标识 + 原文引用块 + 原帖链接（尽可能）
- 三段结构（🟢→🔴→🧠）上下排列
- Commentary 必须提醒“观点≠事实”，避免 hype
- 每条新增讨论必须标注平台、作者/机构、发布时间、原帖链接，以及“事实 / 作者观点 / 本站判断”边界。
- 社区内容不能替代论文或官方技术报告；版本、性能、发布时间等事实必须补原始仓库、公告或论文链接。

### 4.4 `09_update_log.html`（更新日志）

- 每次更新必须新增当天 log-entry，包含：
  - 日期（YYYY-MM-DD）
  - 类别 tag（论文/公司/产品/技术/社区/市场/政策）
  - 可点击跳转到具体位置（尽量用页面锚点）
- 建议同步更新统计面板（总更新天数/条目数等），并确保数字与页面内容一致
- 本页也属于更新型页面：需要 `last-updated` 模块

### 4.5 主站章节映射（具身智能）

- 当前主站中，重点章节映射如下：
  - `02_product.html`：产品调研
  - `11_edge_chip.html`：端侧芯片调研
  - `04_data.html`：数据工程（采集 + 合成）
  - `05_roadmap.html`：落地路线 + 仿真环境（Sim2Real）
  - `06_companies.html`：公司调研
- 上述章节新增关键结论必须遵守可追溯性（论文/官方项目页/官方仓库可点击链接）。
- 主站统一写入 `09_update_log.html`；`legacy/` 目录不参与日更日志。

---

## 5. 主图提取（Figure 1）与资源管理

仓库提供脚本：`scripts/paper_figures.py`

### 5.1 安装依赖（在 `.venv`）

```bash
uv venv .venv
source .venv/bin/activate
uv pip install pymupdf pillow
```

### 5.2 提取并生成 manifest

```bash
./.venv/bin/python scripts/paper_figures.py \
  --html world_model_interactive_guide/07_paper_tracker.html \
  --out-dir world_model_interactive_guide/assets/papers
```

- 生成 `assets/papers/arxiv-<id>-fig1.webp`
- 更新 `assets/papers/manifest.json`（用于审计/追踪）

> 注意：脚本只会扫描 HTML 中已有的 arXiv id；因此“先写卡片（含 arXiv 链接）→ 再抽图”是推荐顺序。

---

## 6. 自动化自检（合并前必须过一遍）

### 6.1 链接与资源

- 搜索并清理错误/过期链接（尤其是官方博客的旧路径）
- 校验本地资源引用是否存在（`assets/...`）
- 扫描与修复只针对主站页面，常规流程不覆盖 `legacy/`

### 6.2 规范合规

- 更新型页面顶部是否都有 `last-updated`
- 07/08/10 是否满足强制结构
- 是否存在无来源的数字/硬结论（必须补链接或删除）

---

## 7. Git 工作流（强制）

### 7.1 分支

- **不要在 `main` 直接提交**
- 每日更新在指定工作分支上进行（Cloud Agent 任务会提供分支名）

### 7.2 提交与推送（小步提交）

- 每个逻辑变更 1 个 commit（例如：论文新增、数据采集合成补充、日志更新）
- 推送：

```bash
git push -u origin <branch-name>
```

### 7.3 每日自动执行与发布

- 使用 `scripts/daily_update.sh` 作为自动入口；它调用非交互式 Codex，执行本 skill 的时效性扫描、页面更新、QA、提交和当前非 `main` 分支推送。
- 推荐每天 `09:00 Asia/Shanghai` 运行：

```cron
CRON_TZ=Asia/Shanghai
0 9 * * * /workspace/dgl/projects/world-model-interactive-guide/scripts/daily_update.sh >> /workspace/dgl/projects/world-model-interactive-guide/.daily-update.log 2>&1
```

- 发布链路：日更分支推送 → CI/人工检查 → 合并 `main` → `.github/workflows/static.yml` 自动发布 GitHub Pages。
- 默认不自动合并 `main`，不绕过来源、QA 或 review；无人值守合并必须由维护者另行配置分支保护和机器人权限。

---

## 8. PR / Review / 合并（自动化与兜底）

### 8.1 正常流程

- 创建 PR（标题建议：`例行完整更新 (YYYY-MM-DD)`）
- review：
  - 资源引用无缺失
  - 更新日志记录当天变更并可跳转
  - 无“水更/无引用”
- 合并到 `main`（merge commit 或 squash 视仓库习惯）

### 8.2 常见失败：无权限创建 PR（403）

如果出现 `Resource not accessible by integration`（403），说明当前运行环境的 GitHub 凭证缺少 PR 权限。兜底策略：

- **让维护者在 Cursor Dashboard → Cloud Agents → Secrets 注入 `GITHUB_TOKEN`**（具备 `repo` 权限，且对该 repo 有 PR/merge 权限）
- 或由维护者手动在 GitHub 上从分支创建 PR 并合并

---

## 9. 每日最小产出（Daily Minimum Output）

每天至少做到：

- **若无高价值内容**：不新增论文/社区/产品条目，但必须：
  - 维持 last-updated 合规
  - 在 `09_update_log.html` 记录“今日扫描，无高价值增量，未更新内容”
- **若有高价值内容**：按规则更新相应章节，并在更新日志中记录可追溯链接

---

## 10. QA Checklist（提交前逐条勾）

```text
□ 已按具身智能主站顺序完成“扫描 → 更新/跳过”决策
□ 所有新增/修正的关键数字与结论均有可点击权威来源
□ 07 每条论文：标题可跳原文 + 三段结构 + 来源定位 + 开源/权重/数据集状态
□ 08 每条社区：原帖链接（尽可能）+ 三段结构 + Commentary 区分事实/观点
□ 09_update_log：新增当天条目，能跳转到具体更新位置
□ 更新型页面顶部 last-updated 模块齐全且日期正确
□ 各页面不再内联定义 `.last-updated { ... }`（样式由 `css/style.css` 统一管理）
□ `最后更新时间` 仅在对应章节内容实质更新时刷新；纯样式/排版统一不刷新（只更新更新日志页）
□ 未触达 `legacy/`（强制）
□ 本地 assets 引用无缺失，新增图片已入库且 manifest 更新
□ git status 干净；commit 信息清晰；已 push 到指定分支
```
