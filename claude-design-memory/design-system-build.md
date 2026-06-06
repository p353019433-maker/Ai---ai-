---
name: design-system-build
description: 设计系统构建实战 - 6 步从 0 到 1 / token 3 层架构 / 组件优先级 / 治理流程 / 7 真实案例 / AI 时代新玩法
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计系统构建实战：从 0 到可治理的工程手册

## 一句话总结
**设计系统不是"组件库 + 文档站"，而是 token 三层架构 + 组件分级 + 治理流程 + 单一事实源 的工程**；5 人以下不要建，5-15 人用 shadcn/Radix 起步，15+ 才需要专职 DesignOps。

## 1. 决策层：为什么建 / 什么时候不要建

**真正解决的问题**（按 ROI 排序）：
1. **跨产品一致性**：Atlassian 几十个产品统一语言；GitHub Primer 让 product UI / brand UI / brand toolkit 三套库共享同一份 primitive
2. **速度**：新页面从"拼一周" → "拼半天"
3. **跨产品复用**：同一套 token 同步到 web / iOS / Android / 邮件（Style Dictionary 一次定义多端输出）
4. **招聘与协作**：新人第一周就能产出合规 UI；外包/合作方拿到 token 文件即可开工

**什么时候不要建**（NN/g 与 Brad Frost 共识）：
- 团队 ≤ 5 人：直接用 Tailwind + Radix，比建系统更快
- MVP 验证期：业务方向还没定，先 shadcn/ui 复制粘贴
- 单一产品 ≤ 30 个页面：组件库 ≤ 15 个，没必要治理
- 设计师 + 开发者 ≤ 3 人：维护成本高于收益

**触发"该建了"的 3 个信号**：
- 同一按钮样式出现 ≥ 3 种
- 改主题色要改 ≥ 50 处
- 新人入职 ≥ 2 周才能上手

## 2. 设计系统 vs 组件库 vs 设计 Token

| 概念 | 定义 | 例子 |
|------|------|------|
| **设计 Token** | 命名化的设计决策（颜色值/间距值/字号） | `color.bg.brand` = `#0066FF` |
| **组件库** | 可复用 UI 单元的实现 | `<Button variant="primary">` |
| **设计系统** | Token + 组件 + 文档 + 治理 + 工具链 | Atlassian、Carbon、Primer |

**关键区分**：
- Token 是**事实**，组件是**包装**。改一个蓝色值 = 改 1 个 token；如果这个值散落在 200 个组件里，不叫系统，叫灾难
- 组件库可以独立存在（Radix、shadcn），但没 token 的组件库 = 一次性消费
- 真正的设计系统 = 单一事实源（single source of truth）+ 多端同步 + 治理流程

## 3. 6 步从 0 到 1 路线（含时间线）

**假设**：15-30 人产品团队，3-5 个前端 + 1-2 个设计师。

### Step 1：决策层签字（1-2 周）
- 找 VP/总监要一纸 mandate，明确"design system 是基础设施，不是 side project"
- 配 1 个产品经理 + 1-2 个设计师 + 2-3 个前端，占比 30%-50% 时间
- 选工具栈：Figma + Style Dictionary + Storybook/Zeroheight + GitHub

### Step 2：设计审计（2-3 周）
- 抓 30-50 个真实页面截图
- 列出所有颜色、字号、间距、圆角、阴影值
- 用 Figma Library Stats / Design System Tracker / Anima 看现有 Library 复用率
- 输出：1 张"现状矩阵"（哪类决策有多少种变体）

### Step 3：token 三层架构（3-4 周）
- **Primitive 层**：`gray.50` ~ `gray.900`、`blue.500` = `#0969DA`、spacing.0~spacing.16
- **Semantic 层**：`color.bg.primary`、`color.text.danger`、`color.border.subtle`
- **Component 层**：`button.bg.primary` → 引用 `color.action.primary`
- 用 Style Dictionary 配 build，iOS / Android / Web 自动同步

### Step 4：核心组件（4-8 周，迭代）
- 优先做 P0：Button、Input、Select、Checkbox、Radio、Modal、Toast、Tabs、Tooltip、Card
- 复用 Radix Primitives 做行为层，自己写视觉层
- 组件必须带 a11y、键盘导航、focus ring

### Step 5：文档系统（2-4 周）
- Storybook 7+ 或 Zeroheight：每个组件 1 页，含 props 表 / 预览 / 代码 / Do & Don't
- 必须含：使用示例、可访问性说明、Token 引用、变更日志
- 上线前找 3 个外部开发者盲测"能否 5 分钟上手"

### Step 6：治理上线（持续）
- 周会制：propose → review → merge → release → measure → deprecate
- 季度 audit：找出"僵尸组件"（< 3 个调用方），进入 deprecated 队列
- 引入 DesignOps 角色（1-2 人），专职维护

**总计**：3-4 个月到 v1.0；v2.0 一年后

## 4. 设计审计：3 个轴 + 工具

**轴 1：视觉一致性**
- 工具：Figma Library Stats（看组件复用率）、Design System Tracker
- 检查项：同一类元素是否 ≤ 3 种样式？主色是否唯一？字号梯度是否 ≤ 5 档？
- 目标：组件复用率 ≥ 60%

**轴 2：交互模式**
- 工具：手动梳理 + 用户旅程地图
- 检查项：表单错误提示位置是否统一？Modal 关闭行为？Loading 状态？
- 输出：交互 pattern 文档（每种 pattern 1 屏说明）

**轴 3：代码 token**
- 工具：Style Dictionary 报表 / 自写脚本扫 hex 值
- 检查项：代码里硬编码颜色 / 间距出现几次？应该 = 0
- 目标：硬编码值 ≤ 5%

**审计产物**：1 张"现状矩阵" + 1 份"问题清单" + 1 份"token 命名草案"

## 5. token 体系架构（3 层 + 命名 + 同步）

### 三层架构

```
Primitive (原始值)        Semantic (语义)              Component (组件)
─────────────────         ──────────────                ──────────────
gray.50  = #F6F8FA        color.bg.subtle               button.bg.primary
gray.900 = #24292F        color.text.primary            button.bg.hover
blue.500 = #0969DA        color.border.default          card.bg.surface
red.500  = #CF222E        color.action.danger           input.border.focus
spacing.4 = 16px          spacing.compact                modal.overlay
font.size.14 = 14px       font.body                      nav.item.padding
```

### 命名约定（GitHub Primer / Atlassian 风格）

**Primitive 层**：`{category}.{scale}.{shade}` → `gray.50`、`blue.500`、`spacing.4`

**Semantic 层**：`{css-property}.{role}.{state}` →
- `color.bg.subtle` / `color.text.primary` / `color.text.danger`
- `color.border.default` / `color.action.primary` / `elevation.surface.hovered`
- `font.body` / `space.compact`

**Component 层**：`{component}.{css-property}.{variant}` →
- `button.bg.primary` / `button.text.on-primary` / `card.padding`
- `modal.overlay` / `input.border.focus` / `nav.item.padding`

### 跨平台同步

- **定义**：JSON（Style Dictionary 原生）或 DTCG 格式
- **构建**：`style-dictionary build` → 输出 CSS 变量、iOS Swift、Android XML、React props
- **Figma 同步**：Figma Variables → Tokens Studio → JSON → Style Dictionary → 多端代码
- **原则**：**Figma 是 source of truth**（设计师改），code 是 consumer；不允许反向写

## 6. 组件库构建：优先级清单

### P0（先做，1-2 周内上线）
Button、Input、Select、Checkbox、Radio、Modal、Toast、Tabs、Card、Icon

### P1（第二批，1-2 月）
Dropdown、Combobox、DatePicker、Table、Pagination、Breadcrumb、Avatar、Badge、Tooltip、Progress、Skeleton、Accordion、Drawer

### P2（按需）
DateRangePicker、RichTextEditor、TreeView、ColorPicker、Slider、Command Palette

### 永远不做 / 慎做
- **业务组件**：Dashboard、Card-with-metric、用户主页 → 业务方自己组合 P0/P1
- **一次性动画**：让设计师写一次性 CSS
- **完全自定义的图表**：用 Recharts/Victory 二次封装，不要从零造

**判定原则**：组件被 ≥ 3 个产品/页面使用 → 入库；只 1 处用 → 留在业务代码里

## 7. 文档系统：选型对比

| 工具 | 适合 | 优势 | 劣势 |
|------|------|------|------|
| **Storybook** | 工程导向 | 代码即文档、a11y addon、Chromatic 视觉回归 | 设计稿展示弱 |
| **Zeroheight** | 设计师导向 | Figma 直连、Do/Don't 展示、品牌 guideline | 代码示例弱 |
| **Notion** | 小团队 | 上手快、协作好 | 不能跑代码、版本管理差 |
| **GitHub Pages + MDX** | 开源项目 | 免费、可控 | 维护成本高 |
| **自建（内部 portal）** | 大企业（50+ 人） | 定制化、统计、SSO | 投入大 |

**推荐组合**：
- 起步（< 20 人）：Storybook 7+ + Figma Library
- 成长期（20-50 人）：Zeroheight + Storybook
- 成熟期（50+ 人）：自建 portal + Storybook + Zeroheight

**每个组件文档必须含**：(1) 预览、(2) props/API、(3) 代码示例、(4) Do & Don't、(5) a11y 说明、(6) 相关 token、(7) 变更日志

## 8. 治理模型：DesignOps + 流程

### 角色（最小可行）
- **DesignOps Lead**（1 人）：决策、规划、跨团队协调
- **Core 贡献者**（2-3 人）：设计师 1 + 前端 2，30% 时间投入
- **Contributors**（所有团队）：提交 PR、提 issue、投票

### 提案 → 评审 → 合并流程

```
1. 提 issue (模板：动机 / 草图 / 影响范围 / 替代方案)
2. 周会 triage（30 分钟，决定是否做）
3. 指定 owner
4. 设计稿 + 代码 PR（必须 1 设计师 + 1 前端 review）
5. 在 Storybook 写文档
6. 灰度发布 + 1 周观察期
7. 全量 + 写入 changelog
8. 季度 audit
```

### 多团队版本管理
- 语义化版本：major（breaking）/ minor（新组件）/ patch（bug fix）
- 发版节奏：minor 每月、patch 随时、major 季度
- **重大变更必须**有 codemod（jscodeshift）和 migration guide

### Deprecated 流程
1. 标记 `@deprecated`，控制台 warning
2. 文档顶部横幅"将于 v{N+1} 移除"
3. 提供迁移路径：新组件名 + 1 行代码替换示例
4. 至少 2 个 minor 版本后移除
5. 维护期 ≥ 6 个月

## 9. 真实案例对比

### shadcn/ui：复制粘贴哲学
- **不是 npm 包**，是项目模板。`npx shadcn-ui@latest add button` 把代码复制到你项目里
- **好处**：你拥有全部代码、可改可改可改；无版本依赖、bundle 最小
- **适合**：B2B SaaS、Startup、追求 control 的团队
- **代价**：升级要手动同步；不像库能 lock 版本

### Radix UI：unstyled + 行为
- **提供**：可访问性、键盘导航、focus 管理、ARIA、portal、collision detection
- **不提供**：任何样式、任何颜色、任何主题
- **适合**：要完全自定义视觉、又不想重写 modal/dropdown 行为的团队
- **典型组合**：Radix Primitives + Tailwind + shadcn（shadcn 底层就是 Radix + Tailwind）

### Atlassian Design System：闭源 + token
- `color.text.accent.red` / `elevation.surface.hovered` / `color.border.brand` 命名清晰
- 强调"unified design language"，适合跨多产品的巨头
- 闭源，外部学不到具体实现

### IBM Carbon：开源 + 企业级
- Token 公开、组件 React/Vue/Angular/Web Components 多端可用
- 主题：white / gray 10 / gray 90 / gray 100 多套
- 适合：企业产品，theme 切换是刚需

### Tailwind UI：付费商业
- 基于 Tailwind 预设的组件 + 模板，付费
- 不是设计系统，是"system 的演示"
- 适合：快速做漂亮页面的独立开发者

### Material You：用户主导
- Material Design 3：用户从壁纸提取色板，动态生成主题
- 适合：Android-first、需要高个性化的产品
- 不适合：跨平台产品（B2B / Web 优先）

## 10. AI 时代的设计系统

**AI 改变了什么**：

1. **自动生成组件**：用 Figma Make / v0 / Cursor 从草图生成 React 组件 + 对应 token
2. **token 自动同步**：Style Dictionary + GitHub Action，Figma Variables 变 → 自动 PR 到代码
3. **跨代码库 audit**：用 LLM 扫代码库，找硬编码颜色 / 不一致 token；PR bot 自动建议替换
4. **LLM 友好的 token 命名**：token 名字要**语义化、具体、不缩写**（`color.action.danger.hover` 而不是 `color.d.h`），这样 LLM 知道何时该用
5. **文档自动生成**：从 Storybook stories 自动生成 markdown；从 React props 自动生成 API 文档
6. **a11y 自动检查**：axe-core + LLM 给修复建议

**但 AI 不能做**：
- (a) 定义品牌灵魂
- (b) 决策该不该建系统
- (c) 跨团队治理
- (d) 处理人际关系

## Token 命名速查

### Primitive 层（10 个）
- `gray.50` / `gray.100` / `gray.500` / `gray.900`
- `blue.500` / `red.500` / `green.500` / `yellow.500`
- `spacing.1` (4px) / `spacing.4` (16px) / `spacing.8` (32px)
- `radius.sm` / `radius.md` / `radius.lg`
- `font.size.14` / `font.weight.semibold`

### Semantic 层（10 个）
- `color.bg.subtle` / `color.bg.surface` / `color.bg.overlay`
- `color.text.primary` / `color.text.secondary` / `color.text.danger`
- `color.border.default` / `color.border.focus`
- `color.action.primary` / `color.action.danger`
- `elevation.surface.hovered` / `elevation.modal`

### Component 层（10 个）
- `button.bg.primary` / `button.text.on-primary` / `button.border.focus`
- `input.bg` / `input.border.default` / `input.border.error`
- `card.bg.surface` / `card.padding` / `card.border`
- `modal.overlay` / `modal.bg`
- `nav.item.padding` / `nav.item.text.active`

## 组件优先级清单

| 优先级 | 组件 | 上线时间 |
|--------|------|----------|
| **P0** | Button, Input, Select, Checkbox, Radio, Modal, Toast, Tabs, Card, Icon | 第 1-2 周 |
| **P1** | Dropdown, Combobox, DatePicker, Table, Pagination, Breadcrumb, Avatar, Badge, Tooltip, Progress, Skeleton, Accordion, Drawer | 第 2-8 周 |
| **P2** | DateRangePicker, RichTextEditor, TreeView, ColorPicker, Slider, Command Palette, Charts (Recharts 二次封装) | 第 3-6 月 |
| **不做** | 业务组件、一次性动画、自研图表 | 永远 |

## 10 条"在建系统，记住这些"

1. **Token 是核心，组件是包装**。先建 token，再做组件
2. **Figma 是 source of truth**，代码是 consumer，永远不反过来
3. **Primitive 数量 < 50**，多了就要抽象到 Semantic
4. **每个组件必须有 a11y、键盘、focus**，上线前 axe-core 跑一遍
5. **文档先于代码**：先写"这个组件怎么用"，再写实现
6. **每周 triage issue**，30 分钟，决定哪些做、哪些不做
7. **breaking change 必须有 codemod** + migration guide + 6 个月兼容期
8. **僵尸组件半年清一次**：< 3 个调用方 → deprecated
9. **storybook 跑 CI**：每次 PR 自动 chromatic 视觉回归
10. **design system 是产品，不是项目**：配 PM、配 OKR、配 roadmap

## 5 条反面教材（看到必改）

1. **"我们组件库有 87 个组件"** → 90% 是僵尸。砍到 25 个核心
2. **"按钮有 primary / secondary / tertiary / quaternary / ..."** → 超过 3 种就违反一致性。砍
3. **"设计师在 Figma 改颜色，前端手动改 CSS"** → 立刻接 Tokens Studio + Style Dictionary
4. **"文档在 Notion"** → 不能跑代码、不能 changelog、不能搜索 props。立刻迁 Storybook
5. **"我们想做 design system，没 PM"** → 必然烂尾。配 1 个 PM 哪怕 20% 时间

## 3 条"如果只能记一条"

1. **设计系统是 governance 工程，不是 UI 工程**——90% 的失败来自"组件做了没人用"和"改 breaking change 没人管"
2. **Token 三层是骨架**：Primitive（值）→ Semantic（意图）→ Component（位置），任何一层缺失系统都立不住
3. **shadcn + Radix + Tailwind + Style Dictionary 是 2024-2026 中小团队的最优解**：行为交给 Radix，视觉用 Tailwind，复制粘贴用 shadcn，跨端同步用 Style Dictionary——5 人小团队也能搭出可治理系统

## 资源 URL
- atlassian.design/ / primer.style/ / carbondesignsystem.com/ / polaris.shopify.com/ / m3.material.io/
- m3.material.io/foundations/design-system/architecture
- figma.com/blog/whats-new-design-systems-2024/
- smashingmagazine.com/2024/01/design-systems-2024/ / 2022/10/design-tokens/ / 2020/05/design-system-documentation/ / 2020/01/design-system-tokens/
- smashingmagazine.com/2018/06/design-systems-vs-pattern-libraries/ / 2017/03/building-design-system-2/
- styledictionary.com/
- nngroup.com/articles/design-systems/ / design-systems-skepticism/ / design-systems-2024/
- bradfrost.com/blog/post/atomic-web-design/ / responsive-design-system/ / feature-design-systems/ / pattern-library-quality/
- airbnb.design/
- uxpin.com/studio/blog/design-system-governance/ / single-source-truth-design-systems/
- shadcn-ui.com/ / ui.shadcn.com/ / radix-ui.com/primitives / colors
- vercel.com/design/guidelines
