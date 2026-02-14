---
description: AntiGravity Skills 索引（可自动发现/导航）
---

## Skills Index（技能索引）

本目录用于沉淀“可重复执行”的工作流技能（skills）。每个 skill 都应满足：

- **可复现**：给出最小可执行步骤与依赖
- **可追溯**：输出/结论需要对应权威来源或仓库内证据
- **与仓库结构对齐**：明确作用于哪些页面/脚本/资源目录

---

## 目录

### 1) 每日例行完整更新（Daily Comprehensive Update）

- **文件**：`daily-comprehensive-update.md`
- **用途**：固化本仓库“具身智能单领域（日更）更新”流程：按主站章节顺序扫描、更新判据、结构强制项、更新日志同步、合并前自检与 git 流程。
- **适用范围**：
  - 主站（具身智能）：`world_model_interactive_guide/index.html` + `01~10` + `09_update_log.html` + `references.html`
  - 历史归档（只读）：`world_model_interactive_guide/legacy/`

### 2) 论文主图自动提取与嵌入（Paper Figure Extraction）

- **文件**：`paper-figure-extraction.md`
- **用途**：从 `07_paper_tracker.html` 识别 arXiv 论文并下载 PDF，自动提取“论文主图”（启发式：前两页最大内嵌图，兜底渲染首页），生成本地 `webp` 与 `manifest.json`，可选幂等嵌入 HTML。
- **核心脚本**：`scripts/paper_figures.py`
- **产物目录**：`world_model_interactive_guide/assets/papers/`

---

## 约定（新增 skill 时请遵守）

- **命名**：使用 `kebab-case`（如 `daily-comprehensive-update.md`）
- **结构**：目标 → 依赖 → 步骤 → 输出 → 边界/注意事项 → QA checklist
- **引用**：涉及数字/结论/产品能力时，必须附权威链接（arXiv/PDF/Project/GitHub/官方博客）

