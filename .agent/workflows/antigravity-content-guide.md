---
description: AntiGravity 高质量内容撰写规范指南
---

# AntiGravity 内容撰写规范指南 (Content Writing Standards)

本指南定义了 AntiGravity 在创建技术文档、研究报告、学习指南和交互式内容时必须遵循的高质量、高标准规范。所有输出内容必须严格符合以下要求。

---

## 一、核心原则 (Core Principles)

### 1.1 可追溯性原则 (Traceability)
> **"每一个数字、每一个结论、每一个声明，都必须可追溯到权威来源。"**

- ❌ **禁止**: 使用无来源的统计数据或声明
- ✅ **要求**: 所有关键声明必须附带 `[来源]` 超链接

**示例**:
```html
<!-- 错误 -->
<p>全球游戏市场规模预计达到 $200B。</p>

<!-- 正确 -->
<p>全球游戏市场在 2025 年预计达到 
<strong><a href="https://newzoo.com/..." target="_blank">$188B</a> - 
<a href="https://mordorintelligence.com/..." target="_blank">$269B</a></strong> 
规模 (来源: Newzoo, Mordor Intelligence)。</p>
```

### 1.2 双视角解读原则 (Dual-Perspective)
> **"让外行看得懂，让专家觉得专业。"**

对于每一篇论文、每一个核心技术概念，必须同时提供：
1. **🟢 通俗解读 (Layman)**: 用比喻和类比，让非技术人员理解
2. **🔴 专业解析 (Professional)**: 使用准确的技术术语和细节

**示例布局**:
```html
<div class="dual-view">
    <div class="layman-view">🟢 通俗解读 ...</div>
    <div class="pro-view">🔴 专业解析 ...</div>
</div>
```

### 1.3 观点标注原则 (Opinion Marking)
> **"观点就是观点，事实就是事实，两者必须清晰区分。"**

- 个人见解必须放在 **"AntiGravity's Commentary"** 专区
- 使用独特的视觉样式（如粉色背景卡片）与正文区分
- 可以辛辣、可以犀利，但不能混入事实陈述

---

## 二、引用规范 (Citation Standards)

### 2.1 必须引用的内容类型
| 内容类型 | 要求 | 示例来源 |
|---------|------|---------|
| **市场规模/增长率** | 必须引用权威研报 | Newzoo, Mordor, Statista |
| **技术规格 (FPS, 分辨率)** | 必须引用官方博客或论文 | DeepMind Blog, arXiv |
| **产品功能声明** | 必须引用官方网站 | vidu.studio, pixverse.ai |
| **论文结论** | 必须引用 arXiv/官方 PDF | arXiv:XXXX.XXXXX |
| **代码/API** | 必须引用 GitHub/官方文档 | GitHub Repo |
| **公司融资/估值** | 必须引用新闻/Tracxn/PitchBook | 36kr, Pandaily, Tracxn |

### 2.2 引用格式
**行内引用**:
```html
<p>Genie 3 可以以 <a href="https://deepmind.google/..." target="_blank">24 FPS</a> 
的帧率实时生成 <a href="https://deepmind.google/..." target="_blank">720p</a> 的交互画面。</p>
```

**原文摘录 (Blockquote)**:
```html
<blockquote>
    <strong>原文关键摘录 (Key Quote)</strong>: "Genie 3 can create and navigate 
    diverse, open-ended game-like environments...maintaining temporal consistency 
    for <strong>several minutes</strong> at 24fps and 720p."
</blockquote>
```

**表格脚注**:
```html
<p style="font-size: 0.9rem; color: var(--text-secondary);">
    <strong>数据来源</strong>: 
    Genie 3 - <a href="...">DeepMind Blog</a>; 
    Matrix-Game 2.0 - <a href="...">arXiv:2508.13009</a>.
</p>
```

---

## 三、公司调研规范 (Company Research Standards)

### 3.1 公司 Profile 必备信息
每个公司调研必须包含以下字段：

| 字段 | 来源要求 |
|------|---------|
| **成立时间** | 官网/工商信息 |
| **总部** | 官网/新闻 |
| **团队规模** | 新闻报道 (附日期) |
| **官网** | 直接链接 |
| **核心技术** | 论文链接 |
| **学术背景** | 大学/Lab 链接 |

### 3.2 融资历程规范
- 按时间**从新到旧**排列
- 每轮必须标注：日期、金额、领投方、跟投方
- 金额如有范围估算，标注来源
- 使用 Timeline 可视化布局

### 3.3 核心团队规范
- 标注：职位、姓名、背景 (前公司/学历)
- 每条背景信息附 `[来源]` 链接

---

## 四、论文追踪规范 (Paper Tracker Standards)

### 4.1 排序规则
- **按发布日期从新到旧排列**
- 使用明确的日期分组 (如 "2026年1月", "2025年12月")

### 4.2 论文卡片必备信息
| 字段 | 格式 |
|------|------|
| **标题** | **必须**可点击跳转到原文（优先 `arXiv/Conference PDF/Official Project Page`） |
| **日期** | 📅 YYYY-MM-DD |
| **来源** | arXiv ID / Conference / Preprint / Project Page / GitHub（按可追溯性优先级展示） |
| **标签** | NEW / GitHub / Conference |
| **代码开源** | **必须标注**：是否有公开 GitHub（有则给可点击链接） |
| **参数开源** | **必须标注**：是否公开模型权重/检查点（优先链接到 HuggingFace/ModelScope/官方 Release/Checkpoint 指南） |
| **数据集开源** | **必须标注**：训练数据是否开源/可公开获取（有则给可点击数据集页；否则明确标注“未公开/不可获取”） |
| **论文解读模块** | **必须上下垂直排列**：🟢通俗解读 → 🔴专业解读 →（可选）🧠 ntiGravity's Commentary |
| **图文并茂** | 重要论文**建议**至少包含 1 张辅助图（可用 `SVG` 示意图/流程图/对比表） |

#### 4.2.1 标题链接规则（强制）
- **必须**提供原文跳转链接（`target="_blank"`）。
- 优先级：`arXiv/会议官方 PDF` > `官方 Project Page` > `作者/机构博客` > `官方 GitHub`。
- 若短期确实无法定位原文链接：允许先链接到**可复现的检索入口**（如 `arXiv 搜索` / `OpenReview 搜索` / `GitHub 搜索`），并在 `来源` 中明确标注 **Search（待核实）**；但**必须在后续更新中补齐原文链接**。

#### 4.2.2 三段解读规范（强制）
- **🟢 通俗解读**：1-2 段，类比/比喻优先，回答“这篇论文在解决什么问题？对读者有什么用？”。
- **🔴 专业解读**：拆解论文要点，至少覆盖：
  - **Problem / Setup**（问题定义与约束）
  - **Method**（核心方法与关键模块）
  - **Why it works**（直觉 + 关键机制）
  - **Evaluation**（指标、实验设置、对比基线）
  - **Limitations**（边界与失败模式）
  - 必要时举例，并配合图/表帮助理解。
- **🧠 ntiGravity's Commentary**：只写观点与判断，清晰标注假设与证据来源，不得混入未经来源支持的“事实”。

### 4.2.1 🔴 专业解析深度要求（强制，必须“可复现”）
> **目标**：专业解析不是“总结”，而是让读者能清楚复现/评估这篇工作的关键机制与工程代价。

**最低要求（每篇论文都必须满足）**：
- **必须逐条列出核心贡献/优化点**：每一条都要写清楚：
  - **改了什么**（模块/结构/训练/推理的哪个环节）
  - **为什么有效**（直觉 + 关键机制）
  - **带来什么变化**（速度/质量/一致性/可控性/显存/吞吐 等，尽可能引用论文数字）
  - **代价与边界**（计算/内存/数据需求/失败模式）
- **必须覆盖“从系统角度拆解”的关键链路**（按论文相关性取舍，但不能空缺）：
  - **Tokenizer/VAE**（压缩比、因果性、缓存、解码开销）
  - **Backbone**（DiT/AR/扩散、注意力形式、KV cache 是否可用）
  - **Conditioning / Control 注入**（动作/相机/几何/文本如何进入模型，注入位置与形式）
  - **训练对齐**（train-test gap 是否存在；是否 train-long/test-long、self-forcing、teacher-student 等）
  - **推理加速**（步数蒸馏/稀疏注意力/量化/缓存/算子融合/并行策略）
  - **评测与消融**（指标、基线、ablation 对应到每个优化点）

**图文并茂要求（重要论文强制）**：
- 对标记为 **NEW** 或对路线图有决定性意义的论文，专业解析中**至少 1 张图**（SVG/流程图/对比表均可），必须呈现：
  - **模型架构或推理流程**（数据/控制信号 → 模块 → 输出）
  - 如果涉及“交互/流式/缓存/时序窗口”，必须把**窗口、缓存刷新/读写点**画出来

**禁令（常见低质量写法，禁止）**：
- ❌ 只写“提出了一个新框架/提升了一致性/提升了速度”但不解释“怎么做、改哪里、为何有效”
- ❌ 只罗列名词（SLA/rCM/KV cache）不说明它们在 pipeline 中的位置与作用
- ❌ 没有任何数字/指标/设置的“专业解析”

### 4.3 日期标注格式
```html
<div class="paper-meta">
    <span>📅 2026-01-09</span>
    <span>📄 arXiv:2601.05232</span>
    <span class="paper-tag new">NEW</span>
</div>
```

---

## 五、社区动态规范 (Community Tracker Standards)

### 5.1 监控平台
| 平台 | 监控内容 |
|------|---------|
| **X/Twitter** | #WorldModel, @GoogleDeepMind, 关键研究者 |
| **Reddit** | r/MachineLearning, r/StableDiffusion |
| **HuggingFace** | Discussions, Model Cards |
| **Medium/Substack** | AI 技术博客 |
| **知乎/即刻** | 中文社区观点 |

### 5.2 讨论卡片必备信息
- **平台图标**: 视觉区分来源
- **日期**: 讨论发生时间
- **原文引用**: 使用引用块，并尽可能给出引用来源的跳转链接
- **引用链接**: **尽可能提供**原帖/原文的超链接（tweet/Reddit thread/HF discussion/博客文章等）
- **双视角解读**: 通俗 + 专业
- **信噪比提示**: Commentary 中提醒批判性阅读

### 5.3 批判性标注
社区内容需在 Commentary 中提醒：
- Hype vs Signal 的区分
- 需要回到论文/代码验证
- 观点 ≠ 事实

---

## 六、全面更新规范 (Comprehensive Update Protocol)

> **核心原则**: 不仅仅是论文需要更新。任何与世界模型相关的内容有变化时，都必须及时更新，并记录在更新日志中。

### 6.1 更新范围 (Update Scope)
每次调研更新必须覆盖以下**所有类别**：

| 类别 | 监控内容 | 更新触发条件 |
|------|---------|-------------|
| **论文 (Papers)** | arXiv, OpenReview, GitHub | 发现新论文或项目 |
| **公司 (Companies)** | 融资、人事、产品发布 | 任何公开新闻 |
| **产品 (Products)** | 版本更新、新功能 | 官方发布或泄露 |
| **技术 (Tech)** | 架构变化、开源代码 | 代码/模型发布 |
| **市场 (Market)** | 收购、合作、IPO | 重大商业事件 |
| **社区 (Community)** | X/Reddit/论坛讨论 | 高互动量 (>500) |
| **政策 (Policy)** | AI 监管、法规 | 政府/行业公告 |

### 6.2 更新流程 (Update Workflow)
```
1. 执行多维度搜索:
   - site:arxiv.org world model interactive video [年份]
   - [公司名] funding valuation announcement [年份]
   - [产品名] new version release
   - AI video generation regulation policy
   
2. 对比现有内容:
   - 检查是否有新信息未收录
   - 检查现有信息是否过时
   
3. 更新对应页面:
   - 添加新内容 (按日期从新到旧)
   - 标注更新日期
   
4. 同步更新日志 (09_update_log.html):
   - 记录日期、更新类别、简要描述
   - 链接到具体更新位置
```

### 6.3 更新日志规范 (Update Log Standards)
**必须维护一个独立的更新日志页面** (`09_update_log.html`)，记录所有内容变更。

#### 日志条目格式:
```html
<div class="log-entry">
    <div class="log-date">📅 2026-01-18</div>
    <div class="log-category">
        <span class="cat-tag papers">📄 论文</span>
        <span class="cat-tag company">🏢 公司</span>
    </div>
    <div class="log-content">
        <ul>
            <li><strong>[论文]</strong> 新增 <a href="07_paper_tracker.html#paper-xyz">arXiv:2601.XXXXX - 论文标题</a></li>
            <li><strong>[公司]</strong> 更新 <a href="06_companies.html#shengshu">生数科技</a> B轮融资信息</li>
            <li><strong>[产品]</strong> PixVerse 发布 V6.0，新增 XXX 功能</li>
        </ul>
    </div>
</div>
```

#### 类别标签:
| 类别 | 标签颜色 | 图标 |
|------|---------|------|
| 论文 | 蓝色 | 📄 |
| 公司 | 绿色 | 🏢 |
| 产品 | 紫色 | 🚀 |
| 技术 | 橙色 | ⚙️ |
| 社区 | 粉色 | 💬 |
| 市场 | 金色 | 📈 |

### 6.4 页面更新标记
每个可更新章节页面顶部必须有（强制）：
```html
<div class="last-updated">
    ⏰ <strong>最后更新时间</strong>: YYYY-MM-DD | 
    <a href="09_update_log.html">查看更新日志</a>
</div>
```

#### 6.4.1 最后更新时间文案规则（强制）
- 每个更新型章节必须包含“每日更新”承诺文案，格式统一为：
```html
<div class="last-updated">
    ⏰ <strong>最后更新时间</strong>: YYYY-MM-DD | 本页内容将每日更新「XXXXXX」。
</div>
```
- 其中「XXXXXX」必须写清本页追踪范围，例如：
  - `产品深度`: “追踪市场上最新的交互视频产品/神经游戏引擎/相关产品动态”
  - `技术架构`: “追踪业界主流技术路线、工程架构与 AI Infra 落地进展”
  - `数据工程`: “追踪视频-动作数据的采集/合成/标注与数据 Infra 方案”
  - `论文追踪/社区动态`: 按各自页面定位填写

---

## 六点一、产品深度规范 (Product Deep Dive Standards)

> **目标**: 系统追踪并深挖市场上“基于交互视频”的新型产品形态与关键能力边界，避免只停留在 demo 级别。

### 6.1.1 更新范围（必须关注）
- **交互视频产品**：可实时/准实时交互、可控、可持续生成的产品与 demo（含网页/客户端/SDK）。
- **神经游戏引擎相关产品**：能“玩”的生成式内容（如可探索/可操作/可回滚/可存档趋势）。
- **游戏及相邻产品动态**：游戏方向的生成式交互内容，以及其它产品（如编辑器、创作工具、引擎插件、推理服务）对交互视频能力的吸收与集成；出现关键更新时需纳入追踪。

### 6.1.2 每个产品条目必备信息（建议结构）
- **产品名称 + 官网/演示链接（必须可点击）**
- **核心能力清单**：交互延迟、最长一致性时长、可控维度（动作/轨迹/编辑）、失败恢复（回滚/重锚定）等
- **技术来源可追溯**：对应论文/技术报告/官方博客/GitHub
- **对比表**：与同类产品在关键指标上的差异（至少 3 项指标）
- **ntiGravity's Commentary**：指出 hype 与真实能力边界（观点需与证据分离）

---

## 六点二、核心技术架构与关键论文规范 (Architecture Standards)

> **目标**: 在 `Architecture` 章节呈现业界主流技术路线与可落地的工程架构，覆盖模型、系统与 AI Infra。

### 6.2.1 必须覆盖的技术路线（至少包含）
- **交互世界模型主干**：action-conditioned / streaming generation / long-horizon consistency 的主流方案
- **Tokenizer / 表示学习**：视频 tokenizer、3D/4D 表示、几何控制、latent action 等
- **状态与记忆**：显式/隐式记忆、可读写 state、检索与融合、回滚与重锚定机制
- **推理加速与系统工程**：蒸馏、稀疏注意力、量化、缓存、分片/流水线并行、端到端延迟预算

### 6.2.2 工程架构与落地工程（必须呈现）
- **端到端系统框图**：输入（动作/编辑）→ 状态/记忆 → 生成器 → 输出（视频/交互）
- **关键工程指标**：latency、吞吐、显存、稳定性（漂移/错误累积）、可恢复性
- **AI Infra**：训练与推理的基础设施要点（数据管线、作业编排、监控、评测基准、回归测试）
- **关键论文/项目引用**：所有路线点必须能追溯到论文/官方文档/代码仓库

---

## 六点三、数据工程规范 (Data Engineering Standards)

> **目标**: 介绍世界模型/交互视频所需的视频-动作数据相关 Infra：生成、采集、合成、标注与质量控制。

### 6.3.1 必须覆盖的数据 Infra 主题（至少包含）
- **数据生成与采集**：引擎内采集（UE/Unity 等）、自动化测试机器人、可复现实验脚本
- **数据合成**：可控环境合成、域随机化、相机/光照/材质变化、长时轨迹采样
- **动作与状态标注**：动作标签、控制信号、接触/物体状态、相机轨迹；必要时引入 VLM 辅助标注
- **数据存储与训练输入格式**：分片、索引、去重、版本化、可追溯元数据（生成配置/commit/hash）
- **质量控制与评测**：一致性检查、覆盖率、分布漂移监控、数据回归（数据变更引发的指标波动）

### 6.3.2 输出形态要求
- 尽量用“工程架构图 + 流程图 + 对比表”组织（图文并茂优先）
- 给出可复用的“方案模板”：采集 → 清洗 → 标注 → 版本化 → 训练输入 → 评测回归

### 6.5 更新频率
- **扫描频率（建议）**: 每天至少扫描一次信息源（arXiv/GitHub/官方博客/社区）
- **内容更新（规则）**: 若当天没有发现**高价值、可追溯**的新信息，则**可以不更新页面内容**（宁缺毋滥，禁止为“日更”制造低价值条目或重复信息）
- **触发式更新**: 发现重大论文/代码/官方发布时立即更新
- **定期回顾**: 每周检查是否有遗漏或需要修订的旧条目

---

## 七、质量检查清单 (QA Checklist)

在提交内容前，必须逐项确认：

### 通用检查
```
□ 所有市场数据/统计数字都有来源链接
□ 所有产品名、论文名都是可点击的超链接
□ 每个技术概念都有 Layman + Professional 双视角解读
□ 每章都有 AntiGravity's Commentary
□ 所有表格都有数据来源脚注
□ 每个更新型章节页顶部都有 last-updated 模块，包含“每日更新”范围文案
□ 如果当期没有高价值内容：允许不更新，但绝不添加“灌水/重复/无引用”的低价值条目
□ 没有任何占位符文本
□ 没有任何无效/空链接
□ 最后更新时间已刷新
```

### 公司调研检查
```
□ 融资历程按时间从新到旧排列
□ 每轮融资都有领投方和来源链接
□ 核心团队每位成员都有背景来源
□ 官网、产品链接可正常访问
```

### 论文追踪检查
```
□ 论文按日期从新到旧排列
□ 每篇论文标题都有原文跳转链接（优先 arXiv/PDF/Project Page）
□ 每条论文卡片的 meta 行包含：GitHub（如有）+ 代码开源/参数开源/数据集开源 三个标签（尽量提供可点击链接）
□ 每篇论文都有双视角解读（🟢通俗 + 🔴专业）
□ 🔴 专业解析具备“可复现”细节：逐条贡献/优化点 + 指标/设置 +（重要论文）架构/流程图
□ 重要论文有 Commentary（或采用三段解读布局）
□ 重要论文至少包含 1 张辅助图（SVG/流程图/对比表均可）
□ 日期标注格式统一 (YYYY-MM-DD)
```

### 社区动态检查
```
□ 每条讨论都有平台来源标识
□ 原文使用引用块格式
□ 尽可能为原文引用提供跳转链接（原帖/原文）
□ 有批判性阅读提示
□ 监控来源清单完整
```

---

## 八、导航结构规范 (Navigation Structure)

### 8.1 标准章节结构
```
00. 概览 (Overview)
01. 行业全景 (Landscape)
02. 产品深度 (Deep Dive)
03. 技术架构 (Architecture)
04. 数据工程 (Data Bible)
05. 落地路线 (Roadmap)
06. 公司调研 (Companies)
07. 论文追踪 (Papers)
08. 社区动态 (Community)
09. 更新日志 (Updates)       ← 新增
附录. 参考文献 (Refs)
```

### 8.2 侧边栏更新
每当添加新页面，必须同步更新所有 HTML 文件的侧边栏导航。

---

## 九、UI/UX 设计规范 (Design Standards)

为保持视觉一致性，所有 HTML 页面必须严格遵循以下设计规范。禁止随意修改 CSS 变量或引入不兼容的样式。

### 9.1 核心配色系统 (Color System)
```css
:root {
    /* 主色调 - 科技蓝 */
    --primary: #2563eb;       /* 核心操作按钮、链接 */
    --primary-light: #eff6ff; /* 浅色背景 */
    
    /* 强调色 - 活力紫 */
    --accent: #7c3aed;        /* 重点高亮、图标 */
    
    /* 功能色 */
    --text-primary: #1e293b;  /* 正文 (Slate-800) */
    --text-secondary: #64748b;/* 辅助文本 (Slate-500) */
    --bg-page: #f8fafc;       /* 页面背景 (Slate-50) */
    --border: #e2e8f0;        /* 边框 (Slate-200) */
}
```

### 9.2 标准组件样式 (Component Standards)

#### A. 双视角卡片 (Dual-View Cards)
用于展示通俗与专业解读，在论文追踪等页面必须**上下垂直堆叠**（🟢在上、🔴在下），避免左右排布导致阅读跳跃。

| 视角 | 背景色 | 边框色 | 标题色 |
|------|-------|-------|-------|
| **🟢 Layman** | `#f0fae6` | `#22c55e` | `#166534` |
| **🔴 Professional** | `#fff1f2` | `#e11d48` | `#9f1239` |

```html
<div class="dual-view">
    <div class="layman-view">...</div>
    <div class="pro-view">...</div>
</div>
```

#### B. AntiGravity 点评框 (Commentary Box)
用于展示个人观点，必须与正文有明显区分。

- **Class**: `.commentary`
- **样式**: 深色背景 (`#1e293b`)，白色文字，左侧紫色边框 (`4px solid #a78bfa`)
- **图标**: 🧠 (必须包含)

#### C. 公司/论文卡片 (Info Cards)
- **Class**: `.paper-card`, `.company-card`, `.discussion-card`
- **背景**: 白色 (`#ffffff`)
- **阴影**: `0 4px 6px -1px rgba(0, 0, 0, 0.05)` (Hover 时增强)
- **圆角**: `0.75rem`

### 9.3 标签系统 (Tag System)
所有标签必须使用圆角 (`border-radius: 9999px`) 和小字号 (`0.8rem`)。

| 类型 | 颜色组合 (背景/文字) | 用途 |
|------|---------------------|------|
| **NEW** | `#d1fae5` / `#059669` | 新增内容 |
| **HOT** | `#fee2e2` / `#b91c1c` | 热门讨论 |
| **Paper** | `#dbeafe` / `#1d4ed8` | 论文分类 |
| **Company** | `#fef3c7` / `#b45309` | 公司分类 |

### 9.4 布局规范 (Layout)
- **侧边栏 (Sidebar)**: 固定宽度 `280px`，深色背景 (`#1e293b`)。
- **主内容区 (Main Content)**: 最大宽度 `1000px`，居中对齐，左右 padding `2rem`。
- **响应式**: 当屏幕宽度 `< 768px` 时，侧边栏隐藏或转为底部导航，双视角卡片转为单列。

---

**版本**: 2.2  
**最后更新**: 2026-01-17  
**作者**: 丁光磊

### Changelog
- **v2.2 (2026-01-17)**:
  - 新增: UI/UX 设计规范 (Section 九)
  - 变更: 作者统一为 "丁光磊"
  - 锁定: 核心配色变量与组件样式
- **v2.1 (2026-01-17)**:
  - 重构: Section 六 扩展为"全面更新规范"
  - 新增: 更新日志规范 (09_update_log.html)
- **v2.0 (2026-01-17)**: 
  - 新增: 公司/论文/社区/每日更新规范
- **v1.0 (2026-01-17)**: 初版发布
