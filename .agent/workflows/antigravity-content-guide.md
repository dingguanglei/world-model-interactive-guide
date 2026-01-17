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
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
    <div style="background:#f0fae6; ...">
        <h4>🟢 通俗解读</h4>
        <p>这就是把 GTA5 喂给了一个画图 AI...</p>
    </div>
    <div style="background:#fff1f2; ...">
        <h4>🔴 专业解析</h4>
        <ul>
            <li><strong>Architecture:</strong> 基于 DiT...</li>
        </ul>
    </div>
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
| **标题** | 可点击链接到 arXiv/PDF |
| **日期** | 📅 YYYY-MM-DD |
| **来源** | arXiv ID / Conference / Preprint |
| **标签** | NEW / GitHub / Conference |
| **双视角解读** | 🟢通俗 + 🔴专业 |
| **Commentary** | 可选，重要论文必加 |

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
- **原文引用**: 使用引用块
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
每个动态页面顶部必须有：
```html
<div class="last-updated">
    ⏰ <strong>最后更新时间</strong>: YYYY-MM-DD | 
    <a href="09_update_log.html">查看更新日志</a>
</div>
```

### 6.5 更新频率
- **最低频率**: 每天一次
- **触发式更新**: 发现重大新闻时立即更新
- **定期回顾**: 每周检查是否有遗漏

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
□ 每篇论文都有 arXiv ID 或 PDF 链接
□ 每篇论文都有双视角解读
□ 重要论文有 Commentary
□ 日期标注格式统一 (YYYY-MM-DD)
```

### 社区动态检查
```
□ 每条讨论都有平台来源标识
□ 原文使用引用块格式
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
用于展示通俗与专业解读，必须保持左右分栏结构（移动端自动堆叠）。

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
