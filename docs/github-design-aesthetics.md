---
name: github-design-aesthetics
description: GitHub 设计项目漫游 - 设计系统/字体/创意编码/终端/CLI/UI - 实时学习
metadata: 
  node_type: memory
  type: project
  originSessionId: 3f38aac3-2f3d-4319-970a-92f048d2d27d
---

# GitHub 设计项目漫游

## 设计系统

### shadcn/ui (TBC)
- "beautifully designed components that you can customize, extend, and build on"
- "Start here then make it your own. Open Source. Open Code"
- **哲学**：组件不是依赖，是 copy-paste 的种子
- 用户拥有代码所有权

### Radix Primitives (workos)
- "open-source UI component library for building high-quality, accessible design systems"
- **unstyled** + **accessible**
- 维护者：原 Radix/Floating UI/Material UI 团队

### Carbon Design System (IBM)
- "A design system built by IBM"
- TypeScript 实现

### USWDS
- U.S. Web Design System
- 联邦政府标准
- 快速 + 可访问 + 移动友好

### Luminare (mrkai77)
- "modern, delightful, translucent design system made with SwiftUI"
- **macOS 应用专用**
- 强调："modularity and reusability"
- 一致设计语言 + 最小 boilerplate

### Lona
- Swift 设计系统工具
- "defining design systems and using them to generate cross-platform UI code, Sketch files"

### Headless UI (Tailwind Labs)
- "Completely unstyled, fully accessible UI components"
- 配合 Tailwind 集成

### Storybook
- "industry standard workshop for building, documenting, and testing UI components in isolation"
- 90k+ stars：UI 组件工作坊

### 98.css (jdan)
- "design system for building faithful recreations of old UIs"
- 复古设计

## 字体

### Monaspace (GitHub Next)
- "monospaced type superfamily"
- **5 个 variable axis typefaces**（5 种"声音"）
- 全部 metrics-compatible（可混合）
- 引入 **"Texture Healing"**（纹理愈合）
- 10 组编程 ligatures（ss01-ss10）
  - `!=` `===` `<=` `>=` `->` `</` `/>` `|>` 等等
- 字符变体（cv01-cv59）：`0` 斜杠 / `1` 无衬线 / `l` `i` 区分
- Nerd Fonts 支持
- Frozen 字体（预启用所有特征）
- **哲学**："Letters on a grid is how we see our code. Why not make those letters better?"
- **GitHub Next 探索项目**

### Maple Mono (subframe7536)
- "Open source monospace font with round corner, ligatures and Nerd-Font icons"
- 中英文宽度 2:1

### FlowType.JS (simplefocus)
- "font-size based on element width"
- 保持 45-75 字符/行
- "Responsive web typography at its finest"
- 现可用纯 CSS clamp() 替代

### typefaces (components-ai)
- Google fonts 数据，用于 three.js + react-three-fiber

## 创意编码

### Pts (williamngan)
- TypeScript/JavaScript 库
- "visualization and creative-coding"
- ~100KB minified / 30KB gzipped
- "import {CanvasSpace, Pt, Group, Line} from 'pts'"

### css-doodle
- Web component
- 探索 CSS 创意潜力
- 简单语法：
```css
<css-doodle>
  @grid: 5 / 200px;
  background: @p(#000, #fff);
  margin: 1px;
</css-doodle>
```

### LYGIA
- "the biggest shader library"
- 跨平台 + 多语言：GLSL / HLSL / Metal / WGSL / WEGL / CUDA
- Battle proof + 跨平台
- "granular, flexible, efficient"
- 函数式：`#include` 即用
- 集成：Unity / Unreal / Minecraft / Three.js / npm / TouchDesigner / p5 / Figma / TouchDesigner / ComfyUI

### purecss-vignes (cyanharlow)
- 1930s 复古海报艺术
- 仅 HTML + CSS
- 自我规则：
  1. 全部手打
  2. 只用 Atom + Chrome DevTools
  3. SVG 限用 + 仅手工 bezier 坐标（后放弃）
- "ongoing series"
- **哲学**：限制 = 创造

### terkelg/awesome-creative-coding
- 14k stars：generative art + data viz + interaction design 资源合集

## 终端 / CLI

### Microsoft Terminal
- Windows 终端新标准
- 含 ColorTool + 样例

### Ghostty
- "fast, feature-rich, cross-platform terminal emulator"
- 平台原生 UI + GPU 加速

### Alacritty
- "cross-platform, OpenGL terminal emulator"
- 速度优先

### Tabby (Eugeny)
- "terminal for a more modern age"
- 71k stars

### Warp
- "agentic development environment, born out of the terminal"
- AI 时代终端

### bat (sharkdp)
- "A cat(1) clone with wings"
- 语法高亮 + Git 集成

### Rich (Textualize / Will McGugan)
- Python rich text + beautiful formatting
- 颜色/样式/表格/进度条/markdown/语法高亮
- "Rich is a Python library for _rich_ text and beautiful formatting in the terminal"
- 17+ 语言 README
- 配合 Jupyter 无配置

### LazyGit
- "simple terminal UI for git commands"
- 78k stars

### lsd / eza / btm / zoxide / fd / ripgrep
- 现代 Unix 工具复兴

## 排版工具

### Héti (sivan)
- 中文排版样式增强
- 基于通行中文排版规范
- "为网站的读者带来更好的文章阅读体验"

### Tailwind CSS Typography
- "Beautiful typographic defaults for HTML you don't control"
- prose 类

### tints.dev
- "11-color Palette Generator and API for Tailwind CSS"

### palx (jxnblk)
- "Automatic UI Color Palette Generator"

## AI/设计工具

### design-extract
- 提取任何网站完整设计系统
- 单条命令
- DTCG tokens + 语义+原子+复合
- 多平台发射器（iOS SwiftUI / Android Compose / Flutter / WordPress）
- Tailwind v4 + Figma variables + shadcn/ui
- MCP server for Claude Code/Cursor/Windsurf

### google-labs-code/design.md
- "format specification for describing a visual identity to coding agents"
- DESIGN.md 给 agents 持久结构化理解
- "DESIGN.md gives agents a persistent, structured understanding of a design system"

### awesome-design-md (VoltAgent)
- 86k stars
- 流行品牌 design systems 的 DESIGN.md 集合
- "Drop one into your project and let coding agents generate a matching UI"

## 设计系统哲学（来自这些项目）

1. **shadcn/ui**：开源 + 自拥有（你 copy 代码到项目）
2. **Radix / Headless UI**：unstyled 给你，styled 给你选择
3. **Monaspace**：5 种声音兼容 = 表达自由
4. **LYGIA**：granular functions, include as needed
5. **Pts**：轻量，import 你需要的
6. **purecss-vignes**：手打限制 = 创造
7. **Rich**：让"丑"终端变"美"
8. **Microsoft Terminal**：跨平台美感标准
9. **design.md / awesome-design-md**：AI 时代设计 = 可被结构化描述

## 对 AI 去 AI 化的启示
1. **shadcn/ui 哲学**：不是 npm 依赖，是 copy-paste 种子
2. **Monaspace 5 字体**：表达 = 风格选择，不是"一个标准字体"
3. **LYGIA 颗粒度**：选你要的，不要全包
4. **Radix unstyled**：让用户决定样子
5. **design.md 模式**：设计 = 可被文本化、可被 AI 理解
6. **purecss-vignes 限制**：手打 = 工艺感
7. **Rich Python**：CLI 也可以美
8. **AI 缺"主观声音"**：5 种字体 vs 1 个 = 个性差异

## 来源
2026-06-03；GitHub 漫游（gh search + 多个 repo READMEs）
