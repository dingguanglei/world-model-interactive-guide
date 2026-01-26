## Skill：论文追踪「方式 A」主图自动提取与嵌入

### 目标
- 从 `07_paper_tracker.html` 自动识别所有 `arXiv:XXXX.XXXXX` 论文条目
- 下载 arXiv PDF
- 自动提取“论文主图”（默认策略：**首页/前两页面积最大内嵌图**，通常对应 Figure 1；若无可提取内嵌图，则**渲染首页整页**兜底）
- 生成本地 `webp` 文件存入 `world_model_interactive_guide/assets/papers/`
- 可选：自动把 `<figure class="paper-figure">` 块嵌入到每篇论文卡片里（幂等）

### 为什么这样做（对静态站最友好）
- **不依赖外链**（规避链接失效、防盗链、跨域）
- `webp` 体积更小，适合 GitHub Pages
- `manifest.json` 可追溯：每张图来自哪篇论文、采用何种提取方式、来自第几页

---

### 依赖与环境（Ubuntu/Debian）
> 本仓库默认使用项目根目录的 `.venv`

1) 安装 venv 支持（如缺失）
```bash
sudo apt-get update && sudo apt-get install -y python3.12-venv
```

2) 创建虚拟环境并安装依赖（清华源）
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
.venv/bin/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymupdf pillow
```

---

### 一键执行（推荐）
#### 只做提图（生成 webp + manifest）
```bash
.venv/bin/python scripts/paper_figures.py
```

#### 提图 + 自动嵌入 HTML（幂等）
```bash
.venv/bin/python scripts/paper_figures.py --embed
```

#### 覆盖重跑
```bash
.venv/bin/python scripts/paper_figures.py --overwrite --embed
```

---

### 产物说明
- `world_model_interactive_guide/assets/papers/arxiv-<id>-fig1.webp`
- `world_model_interactive_guide/assets/papers/manifest.json`
  - `mode`：`image-...` 表示直接抽取内嵌图；`page-render` 表示整页渲染兜底
  - `page`：图来自第几页（从 0 开始）

---

### 边界与注意事项（重要）
- **版权**：学术论文图片通常可在合理引用范围内展示，但务必保留来源（figcaption 标注 “Figure X + 来源定位”）。
- **提取准确性**：以“最大内嵌图”为启发式，并不 100% 等价于 Figure 1；对排版特殊的论文可能抽到其它大图。此时建议：
  - 手动替换图片文件，或
  - 后续升级脚本：按 caption/位置/矢量图层进行更精确定位（成本更高）。
- **Tech report/项目页**：没有明确 arXiv id 的条目不在自动提取范围内；如需要，可手工指定或扩展脚本解析规则。

