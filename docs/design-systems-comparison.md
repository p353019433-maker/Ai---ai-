---
name: design-systems-comparison
description: 5 大设计系统深度对比 - GitHub Primer / IBM Carbon / Shopify Polaris / Atlassian DS / Salesforce SLDS + 自建系统原则
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 5 大设计系统深度对比

## 一句话总结
5 大系统的核心分野不在"有多少组件"，而在"为谁服务"——Primer 给开发者、Carbon 给企业、Polaris 给商家、Atlassian 给团队协作、Lightning 给 SaaS 配置。**抄组件容易，抄"决策哲学"才能自建出真系统**。

## 一、GitHub Primer — "The design system for GitHub"

**定位**：GitHub 自家研发友好的实用主义系统，强调"system, not library"——不是一组可拼装的 UI 积木，而是**一套带决策的体系**。

**Token 三层结构**：
- **Base / Primitives**："lowest level tokens and map directly to a raw value"，如 `color-scale-pink-5`
- **Functional**："represent global UI patterns such as text, borders, shadows, and backgrounds"，如 `borderColor-sponsors-emphasis`
- **Component / Pattern**："used for values that are more specific or unique"，如 `focus-outlineColor`

**主题 9 个**：`light` / `light_tritanopia` / `light_high_contrast` / `light_colorblind` / `dark` / `dark_colorblind` / `dark_dimmed` / `dark_high_contrast` / `dark_tritanopia`。**色盲/对比度全谱覆盖**是工程师文化体现——WCAG 不是 checkbox 而是默认。

**组件规模**：68 个，分 9 类（Actions / Selection / Navigation / Containment / Display / Input / Feedback / Loading / Data）。

**Octicons 图标系统**："A scalable set of icons handcrafted by GitHub"，按 12/16/24/48/96px 网格设计，SVG 格式。

**生态数据**：primer/css 仓库 13k stars、1.3k forks、14.7k 项目使用，SCSS 占比 88.2%。

**强项**：token 命名直白（Kebab-case + 语义后缀），工程师秒懂；暗黑 + 色盲主题全开；utility-first 思维。
**弱项**：营销/品牌色克制、产品视觉惊喜度低。

## 二、IBM Carbon — "A design system built by IBM"

**定位**：开源企业级旗舰，1990s IBM Design Language 一脉相承，**4 层 token 是行业标杆**。

**Token 4 层架构**（行业最常被借鉴）：
- **Element** — 原始原子（如 IBM Blue 60 = `#0f62fe`）
- **Theme** — 浅/深主题切换
- **Semantic** — 用途（`text-primary` / `background-secondary`）
- **Component** — 组件私有（如 `button-primary-bg`）

**包结构**（12 个 monorepo）：`@carbon/react` / `@carbon/web-components` / `@carbon/styles` / `@carbon/elements` / `@carbon/colors` / `@carbon/grid` / `@carbon/icons` / `@carbon/pictograms` / `@carbon/layout` / `@carbon/motion` / `@carbon/themes` / `@carbon/type`。

**字体**：自研 **IBM Plex**（Sans / Serif / Mono 全家族），由 `@carbon/type` 包以 token 形式暴露——**企业级字体资产化的代表**。

**组件规模**：100+，覆盖 Button / DataTable / Form / Tabs / Modal / Tile / Notification 等所有企业场景。

**强项**：4 层 token 是教科书；多框架（React / Web Components / Vanilla）；网格（16 列）+ 布局（layout package）独立成包；可访问性是 IBM 强项。
**弱项**：学习曲线陡、SCSS 体系重、个性化空间小——**企业一致性是双刃剑**。

## 三、Shopify Polaris — "Components are the reusable building blocks for creating Shopify admin experiences"

**定位**：电商 SaaS 后台专用，**"merchant first" 是绝对命令**。

**组件规模**：67 个组件 + 11 个分类（Actions / Layout and structure / Selection and input / Images and icons / Feedback indicators / Typography / Tables / Lists / Navigation / Overlays / Utilities），另 24 个 deprecated。

**Token 思路**："coded names that represent design decisions for color, spacing, typography, and more"——比 Primer 更轻，不强调 base/functional 的多层，专注电商决策。`polaris-tokens` 包独立维护。

**图标**：400+ "focused on commerce and entrepreneurship"，是 5 家中最聚焦的。

**哲学证据**（来自官方 button 文档）：
- "Merchants should be able to anticipate what will happen when they select a button. Never mislead someone by mislabeling a button."
- "Use universally understood iconography instead of words wherever you can"
- "Lead with a strong, actionable verb."

**每条都把"商家"放在主语位置**。

**强项**：电商场景深耕（产品图、库存、订单专属组件）、可访问性原则贯穿文档。
**弱项**：2026.1 官方宣布 **Polaris React deprecated，全面转向 Polaris Web Components**——**纯 React 时代结束，技术选型需谨慎**。

## 四、Atlassian Design System — "Better teamwork by design"

**定位**：协作产品（Jira / Confluence / Trello）通用语，**强调"决策树"和"何时用 X"**。

**Token 命名规范**（**行业最优雅**）：`{category}.{subcategory}.{descriptor}.{value}`，例如：
- `color.text.accent.red` / `color.text.accent.blue` / `color.text.accent.purple`
- `color.text.warning` / `color.text.success` / `color.text.danger`
- `color.link`
- `color.icon.accent.teal` / `color.icon.accent.lime`
- `elevation.surface.hovered` / `elevation.surface.overlay`

**Foundations 7 大类**：Color / Typography / Iconography / Grid / **AI Patterns (Rovo)** / Accessibility / Tokens。**AI Patterns 单独成类——5 家中唯一明确为 AI 时代留位**。

**字体系统**：
- **Charlie Sans** — 品牌/营销
- **Atlassian Sans** — App/产品内
- **Atlassian Mono** — 代码

**字号阶梯**：Heading XXL 32px → XXS 12px；Body L 16px → S 12px；Metric L 28px → S 16px。

**间距系统**（**行业最规范**）：8px 基础单位。`space.100=8` / `space.150=12` / `space.200=16` / `space.250=20` / `space.300=24` / `space.400=32` / `space.500=40` / `space.600=48` / `space.800=64` / `space.1000=80`。**无 6/10/14 零碎值**。

**Elevation 5 级**：`sunken`（看板列底）/ `default`（平面）/ `raised`（可拖卡片）/ `overlay`（弹窗）/ `overflow`（滚动）。**每个 surface 配独立 shadow token**，把 `hovered` / `pressed` 提为 surface 变体而非颜色变体。

**强项**：token 命名最严谨、间距阶梯最干净、AI Patterns 提前布局。
**弱项**：组件视觉偏保守，**协作产品的高密度信息架构经验在自建系统里最难复用**。

## 五、Salesforce Lightning Design System (SLDS) — "Enterprise-grade, highly configurable"

**定位**：CRM 场景下高度可配置的企业系统，部分闭源。

**架构特征**：采用 **BEM 风格命名**（`slds-button__icon--large`），token 类别以 design tokens 包暴露，覆盖 color / spacing / typography / sizing / radius / shadow。

**组件规模**：覆盖企业 CRM 全部场景——`lightning-button` / `lightning-datatable` / `lightning-record-form` / `lightning-card` / `flow` 等。**SLDS 2 正在主推**。

**强项**：高密度数据展示（Datatable 之王）、多品牌变体（每个客户可换主题色）、表单能力极强。
**弱项**：文档散落（设计站常返回 truncated 内容），Aura vs LWC 双框架增加复杂度，部分组件闭源——**自建参考时只能学思路**。

## 六、对比表

| 维度 | GitHub Primer | IBM Carbon | Shopify Polaris | Atlassian DS | Salesforce SLDS |
|---|---|---|---|---|---|
| **Token 层数** | 3（Base/Functional/Component） | **4（Element/Theme/Semantic/Component）** | 2-3（Polaric token + 决策） | 3-4（命名带 value） | 2-3（Design tokens + BEM） |
| **组件数** | 68 | 100+ | 67 | 70+ | 100+ |
| **决策哲学** | "system, not library" 工程师优先 | **企业一致性优先** | **Merchant first 商家优先** | 团队协作 + 何时用 X | 高度可配置 + 客户品牌 |
| **强项** | 多主题色盲覆盖、SCSS 工具类 | 4 层 token 教科书、IBM Plex | 电商深耕、可访问性 | **token 命名严谨、间距干净、AI Patterns** | 数据密度、表单、多品牌 |
| **弱项** | 视觉惊喜度低 | 学习曲线陡 | React 库已 deprecated | 视觉保守、密度经验难复用 | 部分闭源、文档散 |

## 6 条可复用的"自建系统"原则

1. **从"为谁服务"写 token，不要从色卡写起**。Polaris 把"merchant"写进每条原则；Carbon 把"enterprise"写进 4 层；Atlassian 把"team"写进 token 命名。**token 是价值观的物化，不是色卡翻译**。

2. **至少 3 层 token**（Base → Functional → Component）。Primer 和 Carbon 都用 3-4 层；少于 3 层无法处理"同一语义跨主题"，多于 4 层是过度工程。

3. **8px 基础间距单位是默认**。Atlassian 已经替你验证；**不要用 6/10/14**。

4. **主题不只是 light/dark，要包括 a11y 变体**。Primer 提供 9 个主题（4 浅 + 5 深，含 tritanopia / high_contrast / colorblind）——**这是"真支持色盲"而不是嘴上说说**。

5. **字体分角色而不是分字重**。Atlassian 3 套字体对应 3 种场景（品牌 / App / 代码），比"同一字体的 9 个 weight"更有决策力。

6. **AI Patterns 应该作为 Foundation 单列**。Atlassian 把 Rovo 单独成类是 2024 年后的新标准——**自建系统也该给 AI 留位**（如 `prompt` / `streaming` / `confirmation` 三种交互 token）。

## 6 条反面教材

1. **从 Dribbble 抄组件**——5 家中没有任何一家靠"美"赢，它们都靠"决策"赢
2. **token 命名用"primary/secondary"**——一年后没人记得哪个是哪个；用 `text-primary` / `bg-primary` / `border-primary` 区分作用面
3. **"一份 token 走天下"**——浅深主题用同一组 hex，会被设计师/工程师反复打补丁；必须主题层
4. **忽略 elevation 的 shadow token**——多数自建系统只有 surface 没有 shadow，结果 modal 浮起来像"贴了白边"。Atlassian 的 `elevation.surface.raised` + `elevation.shadow.raised` 配对是模板
5. **组件库当设计系统**——没有 token、没有原则文档、没有"何时不用"指南，那只是 MUI 副本
6. **没有 deprecated 通道**——Polaris 67 个组件有 24 个 deprecated，且 2026 宣布 React 库整体 deprecated 转向 Web Components。**没有"下架"机制的设计系统会越积越重**

## 5 条"如果你的产品是 X 场景，参考 Y 系统"

- **开发者工具 / SaaS 平台 / 多人协作编辑器** → **GitHub Primer**（utility-first 思路 + 暗黑色盲全主题 + 工程师文化）
- **企业后台 / 金融 / 医疗 / 强合规产品** → **IBM Carbon**（4 层 token + 可访问性 + IBM Plex 字体资产化）
- **电商 SaaS / 商家管理后台 / 订单库存系统** → **Shopify Polaris**（merchant-first 原则 + 400+ 商业图标 + "anticipate what will happen" 文案原则）
- **团队协作 / 工单 / 项目管理 / Wiki 类** → **Atlassian DS**（token 命名规范 + elevation 5 级 + AI Patterns 提前布局）
- **高密度 CRM / 销售管道 / 大量表单 + 多客户品牌定制** → **Salesforce SLDS**（数据表密度 + 主题可换 + 闭源部分慎学）

## 资源 URL
- primer.style/（components/ + foundations/icons + github.com/primer/css）
- carbondesignsystem.com/（elements/colors/library + elements/typography + components + github.com/carbon-design-system/carbon）
- polaris.shopify.com/（foundations/colors + foundations/typography + components + github.com/Shopify/polaris）
- atlassian.design/（foundations/color-new + foundations/typography + foundations/elevation + foundations/spacing + components）
- lightningdesignsystem.com/（design-tokens + components + utilities）
