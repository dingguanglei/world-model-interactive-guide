# FRONTIER / 具身智能前沿雷达
# 2026 Embodied Intelligence Frontier Radar

本项目面向技术负责人、研究员及产品决策者，持续追踪 **具身智能 (Embodied Intelligence)** 最前沿的四条主线：

- 行业全景：产品与公司放在同一产业链中比较
- 数据工程：Ego4D、Ego-Exo4D、UMI 与真实机器人数据闭环
- 模型：VLA、WAM、世界模型与动作条件预测
- 强化学习：CQL、IQL、Residual RL、在线反馈与安全约束
- 行业全景内含：基座模型、机器人本体、系统集成，以及 Jetson Thor、Hailo-10H 等端侧部署约束

## 在线阅读 (Live Demo)

[https://dingguanglei.github.io/world-model-interactive-guide](https://dingguanglei.github.io/world-model-interactive-guide)

## 当前站点结构（前沿雷达）

主站已重构为 **浅色编辑式前沿雷达**，首页负责快速扫描，章节页负责深度调研：

- 主站入口：`/world_model_interactive_guide/index.html`
- 章节页：`01_industry`（含产品、公司、端上芯片）、`04_data`、`13_world_models`、`12_real_world_rl`；其余为论文、评测、社区、日志与参考资料
- 旧的 `02_product.html`、`03_architecture.html`、`05_roadmap.html` 保留为备用页面，不进入当前主导航
- 更新日志：`09_update_log.html`

## Legacy 归档

重构前的世界模型相关内容已整体归档至：

- `/world_model_interactive_guide/legacy/`
- Legacy 首页：`/world_model_interactive_guide/legacy/index.html`

> 说明：legacy 用于历史回溯，不作为当前主站内容。

## 技能库 (Skills)

- 论文追踪「方式 A」主图自动提取与嵌入：`.agent/workflows/skills/paper-figure-extraction.md`（脚本：`scripts/paper_figures.py`）

## 主站核心内容

本指南包含以下核心模块：

*   **Chapter 01: 行业全景 (Landscape)**
    *   具身智能产业格局、关键玩家与商业化路线。
*   **Chapter 02: 数据工程 (Data)**
    *   Ego4D / Ego-Exo4D / UMI、真实采集、合成数据、自动标注与数据质控。
*   **Chapter 04: 强化学习进展 (Real-World RL)**
    *   真实机器人反馈、在线适应、离线回放与安全 RL。
*   **Chapter 03 / 辅助页**
    *   模型（VLA / WAM），以及论文、arXiv 预印本、技术报告、官方模型报告、评测、社区与更新日志。

## 作者 (Author)

**丁光磊**
*   Email: dingguanglei.bupt@qq.com

## 版权说明

Copyright 2026 Ding Guanglei. All Rights Reserved.
