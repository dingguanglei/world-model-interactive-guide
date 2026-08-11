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
- **用途**：固化本仓库“具身智能单领域（日更）更新”流程：按主站章节顺序扫描论文、arXiv、Technical Report、官方模型报告与社区讨论，执行来源/时效校验、页面更新、更新日志同步、QA、分支推送与发布链路。
- **自动入口**：`scripts/daily_update.sh`；推荐每天 `09:00 Asia/Shanghai` 运行，先推送非 `main` 日更分支，再经 review 合并后由 GitHub Pages 发布。
- **适用范围**：
  - 主站（具身智能）：`world_model_interactive_guide/index.html` + `01~10` + `11_edge_chip.html` + `09_update_log.html` + `references.html`
  - 历史归档（只读）：`world_model_interactive_guide/legacy/`
  - 强制规则：后续常规更新一律忽略 `legacy/`（不扫描、不改写、不批量替换）
  - 时效规则：优先最近 24 小时、再查最近 7 天；每条记录显式标注来源类型、发布日期/版本日期、发布机构和原始链接
  - 关键章节清单：行业全景、公司调研、产品调研、落地路线、技术架构方案、端侧芯片调研、仿真环境、数据工程、论文追踪、评测基准、社区讨论

### 2) 论文主图自动提取与嵌入（Paper Figure Extraction）

- **文件**：`paper-figure-extraction.md`
- **用途**：从 `07_paper_tracker.html` 识别 arXiv 论文并下载 PDF，自动提取“论文主图”（启发式：前两页最大内嵌图，兜底渲染首页），生成本地 `webp` 与 `manifest.json`，可选幂等嵌入 HTML。
- **核心脚本**：`scripts/paper_figures.py`
- **产物目录**：`world_model_interactive_guide/assets/papers/`
- **范围约束**：默认仅处理主站 `world_model_interactive_guide/07_paper_tracker.html`，不处理 `legacy/`。

---

## 约定（新增 skill 时请遵守）

- **命名**：使用 `kebab-case`（如 `daily-comprehensive-update.md`）
- **结构**：目标 → 依赖 → 步骤 → 输出 → 边界/注意事项 → QA checklist
- **引用**：涉及数字/结论/产品能力时，必须附权威链接（arXiv/PDF/Project/GitHub/官方博客）
