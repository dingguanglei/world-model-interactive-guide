---
description: AntiGravity「每日例行完整更新」固化流程（可重复执行）
---

## Skill: Daily Comprehensive Update（每日例行完整更新）

本 skill 用于把“每天例行完整更新”固化为可重复执行的操作流程与质量规则，适用于本仓库 `world_model_interactive_guide/` 的“具身智能单领域”主站维护。

> 核心原则：**宁缺毋滥**。如果当天没有**高价值、可追溯**的新信息，允许不更新对应章节，但必须保持规范合规（尤其是 last-updated 与引用）。

---

## 0. 前置约束（必须满足）

- **规范来源（最高优先级）**：`.agent/workflows/antigravity-content-guide.md`
- **可追溯性**：任何关键结论/数字/主张必须有**可点击权威来源**（论文优先 arXiv/PDF/Project Page，其次官方 GitHub/官方博客/官方发布）。
- **范围约束**：
  - 主站更新对象：`index.html` + `01~10` + `11_edge_chip.html` + `references.html`
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
2) `01_industry.html` 行业全景  
3) `02_product.html` 产品调研  
4) `03_architecture.html` 技术架构方案  
5) `11_edge_chip.html` 端侧芯片调研  
6) `04_data.html` 数据工程（采集与合成）  
7) `05_roadmap.html` 落地路线（含仿真环境）  
8) `06_companies.html` 公司调研  
9) `07_paper_tracker.html` 论文追踪  
10) `10_benchmarks.html` 评测基准  
11) `08_community.html` 社区讨论  
12) `09_update_log.html` 更新日志  
13) `references.html` 参考资料

---

## 2. 信息源扫描（建议每日最小集合）

### 2.1 论文（Papers）

- **arXiv API**：`http://export.arxiv.org/api/query`
- **关键词建议**：
  - `embodied intelligence`, `robot learning`, `policy learning`, `sim2real`, `manipulation`, `VLA`
- **分类建议**：`cs.CV`, `cs.LG`, `cs.AI`（按需要扩展）

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

---

## 3. 是否更新：价值判据（必须显式判断）

只有满足以下之一，才更新对应章节（否则跳过并不“水更”）：

- **新增**：出现新的论文/项目/产品版本，并且能给出权威链接
- **纠错**：发现现有内容引用错误、数字不一致、链接失效，需要修正
- **补全关键缺口**：例如某条目缺 GitHub/权重/数据集状态、缺来源定位、缺主图、缺三段解读
- **重大变化**：官方博客更新（例如页面 `dateModified` 变化且新增了关键口径）

---

## 4. 章节级硬性规则（重点）

### 4.1 `07_paper_tracker.html`（论文追踪）

- **排序**：按发布日期从新到旧
- **年月折叠**：`<details>`，默认展开最近 3 个月
- **标题**：必须可点击跳转原文（优先 arXiv/PDF/Project Page）
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

