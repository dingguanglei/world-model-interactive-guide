# Systemic Learning Guide - Embodied AI Guide
# 2026 具身智能系统性学习指南

本指南旨在帮助技术负责人、研究员及产品决策者系统理解 **具身智能 (Embodied Intelligence)** 赛道，重点关注：

- 数据采集方法（遥操作/多模态同步/失败样本回流）
- 数据合成方法（域随机化/程序化场景/自动标注）
- 仿真环境（Isaac/MuJoCo/Habitat/ManiSkill）
- 强化学习进展（离线RL/世界模型RL/安全RL）

## 在线阅读 (Live Demo)

[https://dingguanglei.github.io/world-model-interactive-guide](https://dingguanglei.github.io/world-model-interactive-guide)

## 当前站点结构（单领域）

主站已重构为 **具身智能单领域**，不再提供领域切换：

- 主站入口：`/world_model_interactive_guide/index.html`
- 章节页：`01~10` + `references.html`
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
*   **Chapter 02: 产品与系统 (Products)**
    *   Figure/1X/GR00T 等系统能力拆解与视频入口。
*   **Chapter 03: 技术架构 (Architecture)**
    *   VLA / Planner / Controller / Safety 的系统架构。
*   **Chapter 04: 数据采集与合成 (Data)**
    *   真实采集、合成数据、自动标注、数据质控。
*   **Chapter 05: 仿真环境 (Simulation)**
    *   Sim2Real 闭环、平台选型与风险清单。
*   **Chapter 06: 强化学习进展 (RL Progress)**
    *   离线RL、世界模型RL、层级RL与安全RL。
*   **Chapter 07-10**
    *   论文追踪、评测基准、社区动态、更新日志。

## 作者 (Author)

**丁光磊**
*   Email: dingguanglei.bupt@qq.com

## 版权说明

Copyright 2026 Ding Guanglei. All Rights Reserved.
