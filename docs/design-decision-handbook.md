---
name: design-decision-handbook
description: 设计决策手册 - 把设计问题路由到对应知识文件，并给出跨领域判断清单
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计决策手册

当你面对一个设计问题不知道先看哪份文件时，先读这份。它只做路由和判断，不再维护完整文件清单；完整索引见 [MEMORY.md](MEMORY.md)，仓库统计见 [HANDOVER.md](HANDOVER.md)。

## 快速入口

- 反 AI 设计判断：[APPLIED-DESIGN-JUDGMENT.md](APPLIED-DESIGN-JUDGMENT.md)
- 核心观点“少失忆的设计”：[LESS-AMNESIAC-DESIGN.md](LESS-AMNESIAC-DESIGN.md)
- 真实项目验证：[DESIGN-LAB-PROTOCOL.md](DESIGN-LAB-PROTOCOL.md)
- 原则冲突：[DESIGN-CONFLICTS.md](DESIGN-CONFLICTS.md)
- 完整主题索引：[MEMORY.md](MEMORY.md)

## 问题路由

| 你在做什么 | 先读 |
|---|---|
| AI 产品、LLM UI、Agent UX | [design-ai-products.md](design-ai-products.md) |
| 写 AI 设计 prompt / 降低 AI 味 | [design-ai-prompt.md](design-ai-prompt.md) |
| UI 按钮、表单、状态、通知 | [design-ui-decisions.md](design-ui-decisions.md) + [design-component-patterns.md](design-component-patterns.md) |
| 字体、排版、字号、授权 | [design-typography-craft.md](design-typography-craft.md) + [design-font-legal.md](design-font-legal.md) |
| 色彩、对比度、暗色模式 | [design-color-contrast.md](design-color-contrast.md) |
| 布局、栅格、响应式 | [design-layout-grid.md](design-layout-grid.md) |
| 设计系统、token、组件治理 | [design-system-build.md](design-system-build.md) + [design-systems-comparison.md](design-systems-comparison.md) |
| App 平台约定 | [design-app-platforms.md](design-app-platforms.md) |
| 网页、landing、叙事页面 | [design-web-aesthetics.md](design-web-aesthetics.md) |
| 数据可视化 / dashboard | [design-data-visualization.md](design-data-visualization.md) |
| 信息架构、导航、搜索 | [design-information-architecture.md](design-information-architecture.md) |
| 服务流程、旅程、后台责任 | [design-service-design.md](design-service-design.md) |
| 无障碍、包容性、伦理 | [design-accessibility.md](design-accessibility.md) + [design-ethics.md](design-ethics.md) |
| 用户研究、验证、A/B 测试 | [design-user-research.md](design-user-research.md) + [design-ab-testing.md](design-ab-testing.md) |
| 评审、批评、团队协作 | [design-review-practice.md](design-review-practice.md) + [design-workflow-critique.md](design-workflow-critique.md) |
| 真实案例、设计公司、设计史 | [design-product-critique.md](design-product-critique.md) + [design-history-movements.md](design-history-movements.md) |
| 设计哲学 | [design-philosophy-master.md](design-philosophy-master.md) |

## 8 条元原则

1. 少即是多，但少得有判断。删东西之前要知道删掉的是噪音还是必要语境。
2. 风格必须继承理由。不要只复制 Swiss、brutalist、editorial、Aesop、Pentagram 的表面。
3. 结构先于表面。IA、状态、任务流、数据关系先清楚，视觉再上。
4. 诚实优先于愉悦。AI、错误、加载、权限、价格、数据图都要让用户知道真实后果。
5. 用户要能掌控和撤回。危险操作、AI 代理、批量操作、付款流程都要有停止或恢复路径。
6. 生产决定美是否能活下去。token、组件、授权、性能、响应式、可访问性、维护者都算设计材料。
7. 具体场景优先于通用漂亮。金融后台、医院表单、游戏 HUD、文化机构不该说同一种话。
8. 证据边界也是品味。深读、重复、引用、缺源、推断要分清楚。

## 13 步检查

每次做设计决策前，按顺序问：

1. 用户要完成的真实任务是什么？
2. 这个设计属于哪个平台、行业、组织语境？
3. 信息结构能不能脱离视觉说清楚？
4. 每个状态是否完整：loading、empty、error、partial、success、disabled、undo？
5. 主操作是否唯一且清楚？
6. 字体是否符合语言、密度、阅读条件和授权？
7. 颜色是否承载角色，而不只是氛围？
8. 布局是否有栅格和响应式规则？
9. 微文案是否说清动作、后果和恢复路径？
10. 动效是否解释状态变化，而不是装饰？
11. 可访问性是否覆盖标签、键盘、焦点、对比度、触控尺寸？
12. 生产模型是否明确：组件、token、所有权、维护成本？
13. 这条判断来自深读、案例、测试、用户反馈，还是只是推断？

## 反模式

- 居中大 hero、紫蓝渐变、玻璃卡片、sparkles 图标，没有解释用户任务。
- 把“现代、干净、好看”当成设计理由。
- 静态截图漂亮，但没有错误、空状态、权限、撤回和加载。
- 用内部术语命名导航。
- 用颜色作为唯一信息通道。
- 用“AI 会处理”隐藏不确定性和责任边界。
- 在没有真实验证前，把研究综合说成已证明的方法。

## 什么时候回到研究层

如果一个判断需要来源证据、阅读过程或缺源记录，去 [../research/README.md](../research/README.md)。如果只是要做一个设计决策，先留在 `docs/`，不要让研究材料干扰执行。
