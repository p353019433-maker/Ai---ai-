# Claude Design Memory

这是一套整理后的设计知识库，不是原始爬取语料。它的目标是让 agent 在做 UI、网页、产品、PPT、视觉系统、AI 设计提示词时，有可引用的判断框架，而不是只凭“好看/不好看”。

## 最重要的入口

- [`HANDOVER.md`](HANDOVER.md)：接手说明，解释这套知识库怎么用。
- [`MEMORY.md`](MEMORY.md)：完整索引。
- [`design-decision-handbook.md`](design-decision-handbook.md)：按具体设计问题路由到对应文件。
- [`design-ultimate-handbook.md`](design-ultimate-handbook.md)：跨主题总纲。
- [`design-philosophy-master.md`](design-philosophy-master.md)：去 AI 化设计哲学总纲。

## 核心判断

这套知识库反复围绕一个主题展开：

> AI 感来自平均、安全、对称、装饰代替结构；真实设计来自减法、层级、约束、材料诚实、具体传统和明确主见。

## 文件分组

### 1. AI 时代设计

- [`design-ai-prompt.md`](design-ai-prompt.md)：AI 设计提示词、反 slop 清单、设计 brief。
- [`design-ai-workflow.md`](design-ai-workflow.md)：AI 设计工具地图、prompt 模板、工作流。
- [`design-ai-products.md`](design-ai-products.md)：LLM UI、Agent UX、生成式界面、不确定性设计。
- [`design-handoff.md`](design-handoff.md)：Figma 到代码交付、Dev Mode、Storybook、Chromatic。
- [`design-ab-testing.md`](design-ab-testing.md)：设计验证、样本量、Feature Flag、A/B 测试。

### 2. Figma、代码与设计系统

- [`design-cursor-figma-loop.md`](design-cursor-figma-loop.md)：Cursor + Figma MCP 端到端工作流。
- [`design-real-codeteardown.md`](design-real-codeteardown.md)：Linear、Stripe、Vercel、Primer、Radix、shadcn 真实代码拆解。
- [`design-system-build.md`](design-system-build.md)：从 0 到 1 搭建设计系统。
- [`design-systems-comparison.md`](design-systems-comparison.md)：Primer、Carbon、Polaris、Atlassian、SLDS 对比。

### 3. UI 工艺

- [`design-typography-practice.md`](design-typography-practice.md)：字号、行高、字距、行长、可变字体、性能。
- [`design-typography-craft.md`](design-typography-craft.md)：字体作为工艺，foundry、光学尺寸、版权史。
- [`design-color-contrast.md`](design-color-contrast.md)：oklch、WCAG、语义 token、暗色模式。
- [`design-layout-grid.md`](design-layout-grid.md)：8pt、12 列、CSS Grid、Flexbox、container queries。
- [`design-component-patterns.md`](design-component-patterns.md)：按钮、卡片、表单、弹窗、导航、空态、错误态。
- [`design-microcopy.md`](design-microcopy.md)：按钮、错误、空状态、确认对话框、AI 文案改稿。
- [`design-motion-microinteractions.md`](design-motion-microinteractions.md)：easing、duration、loading、转场、scroll animation。
- [`design-ui-decisions.md`](design-ui-decisions.md)：UI 微决策的 if-then 规则。

### 4. 平台与场景

- [`design-app-platforms.md`](design-app-platforms.md)：iOS、Material You、visionOS、watchOS。
- [`design-web-aesthetics.md`](design-web-aesthetics.md)：editorial web、brutalist、scrollytelling、现代 CSS。
- [`design-3d-spatial.md`](design-3d-spatial.md)：visionOS、空间窗口、注视捏合、玻璃材质。
- [`design-game-ux.md`](design-game-ux.md)：游戏 UI、心流、HUD、战斗 UI、F2P。
- [`design-service-design.md`](design-service-design.md)：Journey Map、Service Blueprint、Double Diamond。
- [`design-information-architecture.md`](design-information-architecture.md)：IA、导航、搜索、Card Sort、Tree Test。
- [`design-i18n-rtl.md`](design-i18n-rtl.md)：国际化、RTL、bidi、逻辑属性、本地化。
- [`design-verticals-b2b.md`](design-verticals-b2b.md)：医疗、金融、工业、车载等垂直行业设计。
- [`design-chinese-circle.md`](design-chinese-circle.md)：中文设计圈、中文排版、国产工具、中文 UI 特殊处理。

### 5. 研究、伦理与包容

- [`design-accessibility.md`](design-accessibility.md)：WCAG 2.2、ARIA、键盘、屏幕阅读器。
- [`design-inclusivity.md`](design-inclusivity.md)：通用设计、Curb Cut、色盲、神经多样性。
- [`design-ethics.md`](design-ethics.md)：dark patterns、隐私、AI 训练数据伦理。
- [`design-user-research.md`](design-user-research.md)：用户访谈、可用性测试、Card Sort、Tree Test。

### 6. 批评、工作流、职业与商业

- [`design-workflow-critique.md`](design-workflow-critique.md)：设计师工作流、critique、AI 工具边界。
- [`design-review-practice.md`](design-review-practice.md)：设计评审实战、反馈分类、评审句式。
- [`design-criticism.md`](design-criticism.md)：设计批评方法论、公开批评、奖项评审。
- [`design-business.md`](design-business.md)：设计商业化、咨询、个人品牌、定价。
- [`design-education-career.md`](design-education-career.md)：设计教育、作品集、职业路径。
- [`design-education-teaching.md`](design-education-teaching.md)：设计教学、课程结构、知识传递。
- [`design-startup-studio.md`](design-startup-studio.md)：设计师创业、微型工作室、SaaS、课程、投资。
- [`design-font-legal.md`](design-font-legal.md)：字体授权、合同、NDA、版权风险。

### 7. 真实案例与审美谱系

- [`design-product-critique.md`](design-product-critique.md)：Stripe、Linear、Apple、Windows 8 等产品批评。
- [`design-studios-cases.md`](design-studios-cases.md)：Frog、IDEO、Pentagram、MetaDesign、Lippincott。
- [`design-history-movements.md`](design-history-movements.md)：Bauhaus、Swiss Style、New Wave、Memphis、AI 时代。
- [`design-data-visualization.md`](design-data-visualization.md)：Tufte、Few、McCandless、Cleveland-McGill。
- [`design-code-craft.md`](design-code-craft.md)：代码作为审美对象，命名、结构、literate programming。
- [`github-design-aesthetics.md`](github-design-aesthetics.md)：GitHub 设计项目漫游。

### 8. 设计哲学专题

- [`design-philosophy-modernism-sources.md`](design-philosophy-modernism-sources.md)
- [`design-philosophy-japan-nordic.md`](design-philosophy-japan-nordic.md)
- [`design-philosophy-color-perception.md`](design-philosophy-color-perception.md)
- [`design-philosophy-typography-history.md`](design-philosophy-typography-history.md)
- [`design-philosophy-architecture.md`](design-philosophy-architecture.md)
- [`design-philosophy-brand-graphics.md`](design-philosophy-brand-graphics.md)
- [`design-philosophy-photography.md`](design-philosophy-photography.md)
- [`design-philosophy-dataviz.md`](design-philosophy-dataviz.md)
- [`design-philosophy-experience-ux.md`](design-philosophy-experience-ux.md)
- [`design-philosophy-italian-modern.md`](design-philosophy-italian-modern.md)
- [`design-philosophy-movements-depth.md`](design-philosophy-movements-depth.md)
- [`design-philosophy-iconic-brands.md`](design-philosophy-iconic-brands.md)
- [`design-philosophy-reading-paths.md`](design-philosophy-reading-paths.md)

### 9. 方法论

- [`method-autonomous-overnight-learning.md`](method-autonomous-overnight-learning.md)：自主学习一晚的方法论，说明如何让脚本负责采集，让 agent 负责读结果。

### 10. 深读综合（从 memory 系统同步）

这一组来自 `/Users/nothingfear/.claude/projects/-Users-nothingfear/memory/` 的持久化学习成果，是旧 `/tmp/design-study/digest/` 中间产物被清理后留下的可用总结层。它们不是原始语料，而是主题化深读综合。

- [`design-corpus-deep-digest.md`](design-corpus-deep-digest.md)：corpus 深读总摘要。
- [`design-notes-pre-digest-synthesis.md`](design-notes-pre-digest-synthesis.md)：digest 前置笔记综合。
- [`design-pentagram-synthesis.md`](design-pentagram-synthesis.md)：Pentagram 主题综合。
- [`design-pentagram-extended-synthesis.md`](design-pentagram-extended-synthesis.md)：Pentagram 扩展综合。
- [`design-paula-scher-synthesis.md`](design-paula-scher-synthesis.md)：Paula Scher 综合。
- [`design-emigre-synthesis.md`](design-emigre-synthesis.md)：Emigre / 字体与编辑文化综合。
- [`design-type-platform-synthesis.md`](design-type-platform-synthesis.md)：字体平台与生产生态综合。
- [`design-typefaces-2026-synthesis.md`](design-typefaces-2026-synthesis.md)：2026 字体资料综合。
- [`design-web-ux-tech-synthesis.md`](design-web-ux-tech-synthesis.md)：Web / UX / 技术综合。
- [`design-apple-aalto-history-synthesis.md`](design-apple-aalto-history-synthesis.md)：Apple / Aalto / 设计史综合。
- [`design-vitra-eames-synthesis.md`](design-vitra-eames-synthesis.md)：Vitra / Eames 综合。
- [`design-japan-azumi-synthesis.md`](design-japan-azumi-synthesis.md)：日本设计 / Azumi 综合。
- [`design-kauffer-poster-synthesis.md`](design-kauffer-poster-synthesis.md)：Kauffer / poster 综合。
- [`design-french-type-research-synthesis.md`](design-french-type-research-synthesis.md)：法国字体研究综合。
- [`design-designers-wikipedia-synthesis.md`](design-designers-wikipedia-synthesis.md)：设计师 Wikipedia 资料综合。
- [`design-modern-designers-synthesis.md`](design-modern-designers-synthesis.md)：现代设计师综合。
- [`design-pugh-wilson-synthesis.md`](design-pugh-wilson-synthesis.md)：Pugh / Wilson 综合。
- [`design-final-remaining-synthesis.md`](design-final-remaining-synthesis.md)：最终剩余材料综合。
- [`design-uncategorized-synthesis.md`](design-uncategorized-synthesis.md)：未分类材料综合。

