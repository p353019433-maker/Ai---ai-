---
name: design-web-ux-tech-synthesis
description: 2024-2026 web/UX/tech 设计方法论综合——CSS 复兴 + AI 化 + 原型保真度 + 游戏美术 + TUI，10 篇深读
metadata: 
  node_type: memory
  type: project
  originSessionId: a17bb2c6-8576-45e6-9fc8-c9623e50fde7
---

# Web / UX / Tech 设计方法论 2024-2026

**来源**：v5+v6 真品 10 篇深读（Smashing 7 篇 2024-2026 + GameDeveloper 1 + GamesIndustry 1 + petesqbsite TUI 1）
**生成**：2026-06-07
**完整 synthesis**：`已并入本文件（见上）`（9,890 字符）
**关联**：[design-typography-practice.md] / [design-component-patterns.md] / [design-ai-products.md]

## 一句话
**2024-2026 Smashing 序列呈现「CSS 复兴 + AI 化 + 原型保真度」三股合流**。CSS 端 border-image / View Transition API 让 vanilla 重新能做框架效果；AI 端从聊天走向"验证"；UX 端从"原型撒谎"走向"trust moment"修复；游戏美术端 Solarski 把 16 世纪动态构图翻译成 4 个游戏维度。

## 7 条具体技术/方法决策

1. **`border-image` 声明顺序坑**（Temani Afif, Smashing 2024-01）—— **永远不要把 `border` 和 `border-image` 写在同一规则里**。`border-image` 在规范里覆盖 `border`，但**写在后面**的 `border` 会盖过它。"It is painted over backgrounds and box shadows" —— 是层叠规则不是 hack。
2. **移动高亮导航条两种实现**（Blake Lundquist, Smashing 2025-06）—— 方法 A: `getBoundingClientRect()` 读 width/left + transition 滑过去；方法 B: **View Transition API** 让浏览器接管。关键 selector 过滤 `event.target.matches('nav a:not(active)')`。
3. **TUI 设计 4 种交互模型**（Stéphane Richard, petesqbsite）—— (1) Command-based (DOS) (2) Menuless (按钮直接陈列) (3) Selection List (菜单→模块→操作→表单) (4) SAA (IBM 1985, GUI 起源)。**2026 做 Claude Code 风格终端 UI = 重做一次 Selection List 范式选择**。
4. **Logo 字体三支柱 + 四分类**（Levi Honing, Smashing 2024-08）—— 三轴: **Font Choice / Font Weight / Letter Spacing**。四类: serif (纸面) / sans-serif (屏幕) / script (优雅) / display (个性)。时间轴: Gutenberg 1440s → 第一款 Slab Serif 1815 → 第一款数字字体 1968 → WhatFontIs 已 catalog 100 万+ 字体。
5. **Figma → ProtoPie 用 Scene 别用 Flattened**（Eric, Smashing 2026-05）—— Flattened 把所有图层压成 1 张图，**Scene 保留 layer hierarchy** 让每个元素可独立 target。"Rectangle 14" 这种默认名必改 "Input Username" —— 否则公式引用会"损失真正的时间"。
6. **游戏美术动态构图四元素**（Chris Solarski, GameDeveloper 2013）—— **Character shape / Character animations / Environment shapes / Pathways**。**Pathways 是 game vs oil painting 的关键差异** —— 交互本身就是构图变形。Solarski 2013 论证这应是"开发者塑造情感体验的最高优先级考量"。
7. **游戏美术就业的"细分赛道"**（Jodie Azhar, GamesIndustry 2021）—— concept/character 岗位竞争 1:几百，**technical artist / technical animator / VFX / UI artist** 申请者少但同样有创造性。新人若追求"差异化就业"应主动选细分方向。

## 6 条 2024-2026 web 设计模式
- **CSS 复兴**：border-image、View Transition API、:has()、container queries —— vanilla 重新能做事
- **AI 化**：从"能聊天" → "能验证" (Piras, Kuric)
- **原型保真度**：从"长得像产品" → "诚实代表产品" (Eric, ProtoPie)
- **Iconography as language**（Tatkan）：设计系统 = 语言（Brad Frost 原子设计 6 年后）
- **CSS 作为审查工具**：Temani 的 border-image 文章示范"声明顺序这种层叠规则"是现代 CSS 工程师的必知
- **Figma → ProtoPie handoff** 是 2026 设计师的标配

## Why it matters
- **CSS 复兴**意味着设计师+前端可以**减少对 React/Webflow 依赖**——单页 + 一些 CSS 就能做好的
- **AI 验证**意味着**"AI 能不能用"问题** = 它的判断准不准，不只是它能不能聊
- **原型保真度**意味着**"原型对用户撒了谎"** 这个行业默认妥协被正式命名 = ProtoPie 范式出现
- **细分赛道**意味着概念/角色艺术家竞争激烈，**technical artist / VFX / UI** 反而是机会赛道
