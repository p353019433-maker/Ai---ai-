---
name: handover
description: 设计知识库 Handover 文档 - 给接手人解释目录结构、文件用途、怎么用
metadata: 
  node_type: memory
  type: project
  addedDate: 2026-06-06
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计知识库 Handover 文档

## 这份文档是给谁的

给接手这个设计知识库的人（或未来的我自己）。读完这份你能：
- 5 分钟内知道 62 份文件怎么用
- 知道每份文件覆盖什么、不覆盖什么
- 知道"我不知道什么"，避免自信地答错

## 1. 目录结构（仅 1 个）

```
/Users/nothingfear/.claude/projects/-Users-nothingfear/memory/  (852 KB, 62 份)
├── HANDOVER.md                              ← 本文件
├── MEMORY.md                                ← 完整索引
├── design-decision-handbook.md              ← 元总纲
├── design-ultimate-handbook.md              ← 9 轮研究综合
├── design-philosophy-master.md              ← 哲学总纲
│
├── design-ai-*.md × 4 (AI 时代设计)
├── design-handoff.md (交付)
├── design-ab-testing.md (A/B 测试)
├── design-cursor-figma-loop.md (Cursor + Figma)
├── design-real-codeteardown.md (真实代码库)
│
├── design-workflow-critique.md
├── design-review-practice.md
├── design-system-build.md
├── design-systems-comparison.md
│
├── design-typography-practice.md
├── design-typography-craft.md
├── design-color-contrast.md
├── design-layout-grid.md
├── design-component-patterns.md
├── design-microcopy.md
├── design-motion-microinteractions.md
│
├── design-app-platforms.md
├── design-3d-spatial.md
├── design-i18n-rtl.md
├── design-verticals-b2b.md
├── design-web-aesthetics.md
├── design-game-ux.md
├── design-service-design.md
├── design-information-architecture.md
│
├── design-data-visualization.md
├── design-product-critique.md
├── design-studios-cases.md
├── design-history-movements.md
├── design-code-craft.md
├── design-criticism.md
│
├── design-business.md
├── design-education-career.md
├── design-startup-studio.md
├── design-font-legal.md
├── design-education-teaching.md
├── design-chinese-circle.md
├── design-ui-decisions.md
│
├── design-accessibility.md
├── design-inclusivity.md
├── design-ethics.md
├── design-user-research.md
│
├── design-philosophy-*.md × 13 (哲学)
│
├── github-design-aesthetics.md
└── method-autonomous-overnight-learning.md
```

**总 62 份 .md 文件，852 KB，0 字节脚本/日志。**

## 2. 5 分钟入门路径

### Step 1（30 秒）— 读总纲
- [design-decision-handbook.md](design-decision-handbook.md)
- 重点看 §1 索引、§3 八大元原则、§10 十三步检查

### Step 2（1 分钟）— 知道全貌
- [MEMORY.md](MEMORY.md) — 12 组分类的完整文件索引

### Step 3（按需）— 找具体文件
- 决策树走 decision-handbook §2
- 关键词搜：`grep -l "关键词" memory/*.md`

## 3. 文件怎么用

### (1) 决策型（"我该 X 还是 Y？"）
- **读**：decision-handbook §2 决策树
- **落到具体文件**：对应章节的链接

### (2) 操作型（"我要做 X 怎么开始？"）
- **读**：对应文件 5-10 节"实操"部分
- 多数文件结构：1. 一句话总结 / 2. 原则 / 3. 必做 / 4. 反模式 / 5. 案例 / 6. 模板 / 7. 资源

### (3) 灵感型（"我要看真实案例"）
- **读**：product-critique / studios-cases / real-codeteardown / 3d-spatial

### (4) 理论型（"我想了解底层"）
- **读**：design-philosophy-* (13 份) / design-history-movements / ultimate-handbook

### (5) AI 工具型（"我要用 AI 写设计"）
- **读**：design-ai-prompt + design-ai-workflow + design-cursor-figma-loop + design-real-codeteardown

## 4. 知识的覆盖范围

### ✅ 强覆盖
- 通用设计原则 + 哲学（35 份）
- AI 时代设计（5 份）
- 视觉工艺（7 份：字体/色彩/布局/组件/微文案/动效）
- 设计系统（2 份）
- 评审 & 工作流（2 份）
- 用户研究 & 可访问性 & 伦理（4 份）

### ✅ 中覆盖（2026-06 新增）
- 3D / visionOS（1 份）
- Cursor + Figma MCP 端到端（1 份）
- 真实代码库拆解（1 份）
- 国际化 / i18n / RTL（1 份）
- 行业垂直：医疗 / 金融 / 工业 / 车载（1 份）
- 设计师创业 / 工作室（1 份）
- 字体授权 / 法律 / 合同（1 份）
- 设计教育 / 课程（1 份）
- 中文设计圈本土实践（1 份）

### ❌ 不覆盖（明确边界）
- **代码哲学**（已删除 11 份 code-philosophy-*，与设计无关）
- **历史归档**（已删除 1 份 de-slop.md）
- **会话日志 / 工具脚本**（已删除 .jsonl + 子目录）

## 5. 怎么"应用"这份知识库

### 真实项目流
1. 接到设计任务 → 读 decision-handbook §2 决策树
2. 落到具体 memory 文件（如"做按钮" → design-ui-decisions + design-component-patterns）
3. 查 5 条反模式 + 10 条"必做"清单
4. 参考真实案例（product-critique / real-codeteardown）
5. 应用 AI 工具（ai-prompt / cursor-figma-loop）
6. 评审（review-practice + workflow-critique）
7. 走 a11y 清单（accessibility / inclusivity）

### 主动学习流
1. 读哲学（design-philosophy-master）
2. 读历史（design-history-movements）
3. 读真实案例（product-critique / studios-cases）
4. 拆解真实代码（real-codeteardown）
5. 应用 → 复盘 → 循环

## 6. 知识库的元原则

每份文件都遵循这 5 个原则：

1. **一句话总结**——> 文件开头 1 句给"为什么读"
2. **结构化**——> 数字编号 + 标题清晰
3. **可执行**——> 不仅理论，有模板 / 代码 / 清单
4. **真实**——> 引用真实产品、真实案例、真实 URL
5. **反 slop**——> 列反模式 + 5 条"如果你只能记一条"

## 7. 已知边界 / 后续建议

### 应用的盲点（不是知识盲点）
知识库 9 个原始盲点已全部填补，但**应用时仍会暴露新盲点**——这是正常的，**应用到真实项目**比继续学习更重要。

### 知识更新
- 所有文件标注了"addedDate 2026-06-06"或更早
- **建议季度更新**：每 3 个月 review 一次，过时信息标注
- 真正落地时发现的错误，直接编辑对应文件 + 在 MEMORY.md 标注

### 加新文件
当遇到新主题（如新材料、新平台、新范式）时：
1. 写一份新文件，遵循上述 5 原则
2. 更新 MEMORY.md 加入对应分类
3. 更新 decision-handbook §1 索引
4. 不删老文件——> 老文件是历史

## 8. 联系方式 / 变更历史

**原始制作者**：nothingfear（+ Claude 模型 MiniMax-M3）
**制作周期**：2026-05 至 2026-06-06（8 轮研究 + 3 轮整理/补盲 + 1 轮 Handover）
**总知识库积累字符数**：约 1.2 MB（含中英文）
**Handover 优化后**：852 KB（精简 30%）
**已删无用内容**：
- 21 个 .jsonl 会话日志（~32 MB）
- 9 个会话子目录 / 工具脚本（~10 MB）
- 11 份 code-philosophy-* 偏题文件（88 KB）
- 1 份已归档 de-slop.md（8 KB）

## 9. 一句话总结

**这是一份 60 份设计 memory + 元索引 + 13 份哲学 + 2 份辅助 = 62 份可立即应用的设计知识库。** 0 脚本 0 日志，可直接 git 仓库管理。
