---
name: design-philosophy-experience-ux
description: 体验设计/UX/动效/声音 - 循环9研究
metadata: 
  node_type: memory
  type: project
  originSessionId: 3f38aac3-2f3d-4319-970a-92f048d2d27d
---

# 体验设计 / UX / 动效 / 声音（循环9）

## Game Design 游戏设计
- **Robert Zubek 框架**：
  - mechanics + systems（规则与对象）
  - gameplay（玩家与机制交互）
  - player experience（玩家感受）
- **Mihaly Csikszentmihalyi Flow**：
  - 三个必要条件：清晰目标+进展、即时反馈、挑战-技能平衡
  - 6 大成分：专注、行动意识合一、失去自我意识、掌控感、时间扭曲、内在奖励
- **Meaningful choices**：消除过多随机 → 决策重要
- **Eurogames 优雅设计**：不让玩家不可逆落后、平衡 luck vs skill
- **反馈循环**：playtest → 改 → playtest

## Self-Determination Theory 自决理论
- 三大心理需求：
  1. **Autonomy 自主**：因果自我的感觉
  2. **Competence 胜任**：掌控+精通
  3. **Relatedness 关联**：与他人的连接
- 内在动机 > 外在动机
- 正面反馈 = 胜任感增强 → 内在动机
- 负面反馈 = 削弱胜任

## 12 Principles of Animation (Disney)
1. **Squash and stretch** 挤压拉伸：体重+柔性
2. **Anticipation 预备**：动作前的准备
3. **Staging 舞台化**：指引注意
4. **Straight ahead / Pose to pose** 顺绘/关键帧
5. **Follow through and overlapping** 跟随与重叠：身体各部分不同速率
6. **Slow in and slow out 缓入缓出**：开始/结束多帧
7. **Arc 弧线**：自然运动曲线
8. **Secondary action 次要动作**：补充主动作
9. **Timing 节奏**：帧数 = 速度
10. **Exaggeration 夸张**：推远现实
11. **Solid drawing 立体感**：3D 形体理解
12. **Appeal 吸引力**：角色魅力

**核心**：让动画像遵守物理又比物理更有生命力。

## Sound Design 声音设计
- 创造媒体听觉元素
- 唤起情感、反映情绪、强调动作
- **Sonic Branding**：通过声音塑造品牌
- **交互声音**：reuse + interactivity + low CPU
- **Dolby Atmos 等**：扩展创作空间
- 动态音频适配运行时
- "soundscapes that correspond to what's seen"

## Design Thinking
- **5 阶段（David M. Kelley 2004）**：Empathize / Define / Ideate / Prototype / Test (EDIPT)
- **3 空间**：Inspiration / Ideation / Implementation
- 非线性、可迭代
- 量化原型：low / mid / high fidelity
- 不要停留在第一个概念

## Interaction Design 交互设计
- **Goal-oriented design**：以目标驱动
- **Personas 角色**：用户行为原型
- **Cognitive dimensions 认知维度**：评估词汇
- 跨学科：心理学 + HCI + 用户研究

## HCI 核心原则
- **早期关注用户与任务**
- **实证测量**：用真实用户测试
- **迭代设计**
- **关键原则**：tolerance / simplicity / visibility / affordance / consistency / structure / feedback
- **Loop of interaction**：信息在人与机之间循环

## WCAG 与可访问性
- 4 大原则：**Perceivable / Operable / Understandable / Robust (POUR)**
- 3 个等级：A / AA / AAA
- **Level AA 是法律标准**（美/欧/加/澳）
- WCAG 2.1 增加：方向、输入目的、reflow、非文本对比、文本间距、悬停焦点
- WCAG 2.2 (2023.10)：9 个新标准
- 多通道访问：文本替代 + 字幕 + 适配布局
- 键盘可访问
- 充足色彩对比
- 不用颜色单独传达
- 用户对时间敏感内容有控制权
- 明确焦点指示

## Universal Design 通用设计
- 设计"无修改即可用"
- 易于适配
- 标准化接口 + 辅助技术
- **不覆盖所有场景**（如低视力+畏光需求冲突）
- 三层：无修改/可适配/辅助技术可用

## Web Design 实践
- 动画可禁用（W3C a11y 标准）
- 内容优先（progressive enhancement）
- 负空间分段
- 避免居中文本
- 平衡美学与清晰

## Don Norman Emotional Design
- 三个层次（visceral / behavioral / reflective）
- "why we love (or hate) everyday things"
- 情感 + 美学 = 整体体验

## 对 AI 去 AI 化的启示
1. **Flow 平衡**：AI 喜欢一次给所有功能 → 应渐进披露
2. **3 大心理需求**：自主（让用户选）、胜任（positive feedback）、关联（社交）
3. **动画 12 原则**：AI 默认用 linear 缓动 → 用 ease-out / ease-in-out
4. **Anticipation 预备**：hover 微动 → 告诉用户"什么会发生"
5. **Staging 舞台化**：动画指引注意
6. **Exaggeration 夸张**：反馈要"足够大"才能感知
7. **声音沉默 > 嘈杂**：默认音 = AI 套路
8. **WCAG AA 是底线**：AI 经常忘记可访问性
9. **不用颜色单独传达**：色盲友好（图标+颜色+文字）
10. **设计 thinking 是循环**：AI 给"结果"，不给"过程感"

## 来源
2026-06-03；参考：Wikipedia (Game design / Self-determination theory / 12 basic principles of animation / Sound design / Design thinking / Service design / User experience design / Interaction design / Human-computer interaction / WCAG / Universal design / Web design / Visual design / UI design / Don Norman / Flow)
