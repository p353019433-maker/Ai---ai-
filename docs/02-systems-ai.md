# 02 · 设计系统与 AI 工作流 — Token、代码拆解、交付、提示词

> 蒸馏自：design-system-build、design-systems-comparison、design-real-codeteardown、github-design-aesthetics、design-handoff、design-cursor-figma-loop、design-ai-prompt、design-ai-workflow、design-ai-products（原文见 git 历史）

## 一、设计系统：建不建、怎么建

**建/不建**：≤5 人直接 Tailwind + Radix；5-15 人 shadcn 起步；15+ 才配专职 DesignOps。该建的 3 信号：同一按钮样式 ≥3 种；改主题色要改 ≥50 处；新人 ≥2 周才能上手。

**Token 三层**：Primitive（`blue.500=#0969DA`，数量 <50）→ Semantic（`color.text.danger`、`elevation.surface.hovered`）→ Component（`button.bg.primary` 引用 semantic）。命名：semantic 层 `{css-property}.{role}.{state}`。少于 3 层无法处理跨主题语义，多于 4 层过度工程。

**6 步时间线（3-4 个月到 v1.0）**：决策签字 1-2 周（要 VP mandate）→ 审计 2-3 周（抓 30-50 个真实页面，量化目标：复用率 ≥60%、硬编码 ≤5%、同类样式 ≤3 种、字号 ≤5 档）→ token 3-4 周 → 核心组件 4-8 周（P0：Button/Input/Select/Modal/Toast/Tabs/Card/Icon）→ 文档 2-4 周（上线前 3 个外部开发者盲测"5 分钟能否上手"）→ 治理持续。

**治理**：入库判定=被 ≥3 处使用；僵尸组件（<3 调用方）半年清一次；deprecated 流程=标注+console warning+迁移示例+维护 ≥6 个月，breaking change 必须有 codemod。**同步铁律：Figma 是 source of truth，code 是 consumer，不允许反向写**。管线：Figma Variables → Tokens Studio → DTCG JSON → Style Dictionary → 多端。反面教材："87 个组件"90% 是僵尸；文档放 Notion（不能跑代码）立刻迁 Storybook。

**5 大系统对比与选型**：
- **Primer**（GitHub）："system, not library"；**9 个主题**覆盖色盲/高对比全谱。开发者工具学它。
- **Carbon**（IBM）：**4 层 token 是行业标杆**；自研 IBM Plex 以 token 形式暴露=企业字体资产化；16 列网格。强合规企业学它。
- **Polaris**（Shopify）："Merchant first" 写进每条原则（"Never mislead someone by mislabeling a button"）。**2026.1 官方弃 React 转 Web Components**——技术选型警示。电商后台学它。
- **Atlassian**：token 命名行业最优雅（`color.text.accent.red`）；间距阶梯最规范（`space.100=8`…`space.1000=80`，无零碎值）；3 套字体分角色（品牌/产品/代码）；**5 家中唯一把 AI Patterns 列为 Foundation**。协作工具学它。
- **SLDS**（Salesforce）：BEM、Datatable 之王、多客户主题。高密度 CRM 学它。

自建 6 原则：从"为谁服务"写 token 而非从色卡；token 命名要 `text-primary/bg-primary` 区分作用面（只写 "primary" 一年后没人记得）；8px 基础间距；主题含 a11y 变体；字体分角色不分字重；AI Patterns 单列 Foundation。

## 二、真实生产代码拆解

- **Stripe**（stripe-design-tokens，MIT）：fg/bg/border 三段式命名（不是 `gray.900`）；DTCG 格式直接喂 Style Dictionary；暗色模式不是反色而是另一套 token；`onPrimary` 显式声明。Spacing 8 阶 4-64px 覆盖 95%。
- **Primer**：**灰阶只 3 级**（fg-default/muted/subtle）不是 10 级；`accent-fg`（链接）与 `accent-emphasis`（按钮）分开；状态色用 fg 不用 bg；Button 5 variants + 3 sizes 是上限，**不暴露 className 重写**。动画单一曲线 + 3 档 duration（80/160/300ms）。
- **Vercel Geist**：可变字体一个文件覆盖 100-900；`next/font` self-host 零外部请求。
- **Radix**：Compound Components（`Dialog.Root/Trigger/Portal/...`）；Portal 解 z-index；**受控/非受控双轨（`checked`+`defaultChecked`+`onCheckedChange`）是 a11y 组件标配**；键盘默认全配。
- **shadcn/ui**：cva 声明 variants + TS 自动推导；`Slot` 实现 asChild 多态；**focus-visible 不用 focus**（键盘聚焦才显环）；不发 npm 包，CLI 复制代码——"你的设计系统应该属于你"。它不是组件库是**代码模板**。
- **Linear**：4 阶功能灰 + 4 阶背景 + 3 阶边框；标志性曲线 `cubic-bezier(0.16, 1, 0.3, 1)`；**永远 1px 边框+阴影叠加**（AI 默认纯阴影失真）；高密度=14px 列表字号、表格 4px 内边距。
- **Apple HIG**：按钮圆角 10pt；按下 scale 0.97 + 阴影降级 + haptic；SF Symbols 7000+ × 9 weight × 3 scale 自动跟字号——"图标是字体的延伸"。
- **Monaspace**（GitHub Next）：5 个 metrics-compatible 可变轴 mono 可混排；"Texture Healing"。**5 种声音 = 风格即选择**——AI 缺的是主观声音。
- **design.md 趋势**：DESIGN.md 给 coding agents 持久的设计系统理解（awesome-design-md 86k stars）；design-extract 单命令提取任意网站 token。

## 三、交付（Handoff）

- **Dev Mode 4 件事**：Code Connect（展示仓库真实组件而非猜测代码）、Ready for dev、Variables 显示代码语法、像素 diff。Dev seat 必须给所有前端。
- **Token 管线 CI 化**：`style-dictionary build` 在前端构建前跑；**PR 加 `color-no-hex` lint——一处手抄 token 就死**。
- Storybook CSF 3.0：`satisfies Meta` + play 函数交互断言；**没有 story 的组件不允许 merge**。
- **Handoff 文档 7 节**：背景一句话 / 量化目标 / 用户 ≤50 字 / 技术约束 / **不做清单** / 成功标准（QA 硬条件）/ 设计资源。反模式："让用户感受到温暖"——不能 pass 也不能 fail。
- **4 层验收**：像素 diff <1px → play 全过 → Chromatic 5 viewport → axe 扫描（0 critical）。
- 协作三件事：设计走查在 Chromatic 部署的 Storybook URL 上做（不看 PR 截图）；联合编码 30 分钟（1 次抵 3 轮 PR review）；设计 QA 6 条（间距 token？颜色 token？三态齐？空错载齐？dark mode？i18n key？）。
- 暗黑模式第一版就做；AI 写 60% 样板，人类 review 100% token 映射。

## 四、Cursor + Figma MCP 闭环

- **核心命题：不配 Code Connect = MCP 价值损失 70%**。症状：AI 输出 `<button className="bg-blue-500">` 而不是 `<Button variant="primary" />`。
- 3 工具：`get_design_context`（一次一个 frame，大 frame 拆开防 context 爆）；`get_screenshot`（视觉理解，不可替代 design_context）；`create_frame`（code-to-design 回流做视觉回归）。
- **标准 prompt 结构**：frame URL + 用 Code Connect 真实组件不重写 / 用 token 不写 hex / props 继承原生 HTML 属性 / 带 Storybook story / 带 Playwright 测试。
- **branch 铁律**：永远不让 AI 改 main Figma 文件；设计师建 branch → AI 工作 → review → merge，每 branch 对应一个 PR。
- Linear 式流程跑通后：设计系统变更从 1 周缩到 4 小时。
- 8 个反 slop 卡点（节选）：grep 防重复组件、`color-no-hex`、px 字面值禁用、函数 >200 行拆分、CI 跑 axe。

## 五、AI 设计提示词工程

- **三件套**：Persona（"10 年 SaaS 仪表盘经验，专注 Linear/Stripe 风格"）× Constraints（**用数值替代形容词**："Fraunces 700/64px，Inter 400/16px，色板 #F4F1EA/#11171B/#C2410C"）× Anti-patterns（显式列 AI 默认错误）。心法：把"避免 X"翻译成"做 Y"。
- **Brief 模板骨架**（XML 标签）：`<role>` `<project>` `<screen>`（分辨率）`<tokens>`（hex+字体+圆角+间距网格+阴影）`<components>` `<layout>`（12 列、容器 1200px）`<do>` `<dont>` `<reference>`（2-3 张参考图，标注"图 1=风格，图 2=组件清单，图 3=反例"）。**写 brief 30 分钟，省 4 轮迭代。缺 token = 100% AI slop。**
- **工具分工**：v0 出代码（能直接 push，但图标库会猜错）、Figma Make 出交互（代码全是 magic number，是装饰品）、Galileo/Stitch 出稿子（无 hover/focus/键盘）、Cursor 改代码（先生成 tokens.ts 再生成页面）。规律：写代码越深设计自由度越低。
- **迭代策略**：第一稿"骨架+三件套+1 个锚点"（"风格锚定 Linear，密度锚定 Stripe"）；之后"手术刀式 diff"（"仅改 hero，其余不变"）；每轮只改 1-2 个变量+附保留清单；**第 5 稿还在改架构 = 回去重写 brief**。
- **反 slop 10 替换**：Inter 作标题→Fraunces/GT Sectra；紫渐变→单色强调+大色块；居中堆叠→左对齐网格；emoji 图标→Lucide/Phosphor；Lorem ipsum→真实文案；3 层阴影→1 层；ghost 主 CTA→实色；圆角 16px+→4-8px；5+ 入场动画→1 个；假极简→1-2 大色块高对比。红线词："Empower your workflow"、"🚀 Get started"、3D 渐变球。
- **AI 只出 happy path**：3 状态 × 5 主页面 = 15 张图要人补——这是设计师最值钱的地方。角色转变：画界面→写 brief+审输出；一天画 3 屏→一天审 30 屏改 5 屏。"AI 最强 0→1，最弱 1→100"。
- Cursor 接力 prompt 范例："读取 src/design-tokens.ts，把硬编码 bg-zinc-950 换成 bg-surface，lucide 换 phosphor，加 ARIA"——30 秒替代 40 分钟。

## 六、AI 产品设计模式

- **对话 UI 5 模式**：Streaming + Stop 随时打断；Regenerate 放每条回答下；Edit 直接改消息；Branch = 可恢复检查点；Feedback 升级为数据源。
- **关键数据**（NN/g）：**86% 智能助手任务是单步操作**——用户面对低可预测系统会自我收敛，UI 必须主动暴露"我能做什么"脚手架。最大痛点是 articulation barrier，解法：结构化输入、3 个具体场景示范、`@file`/`/command` 式 Prompt Controls。
- **Agent UX**：Plan Mode 四阶段把不确定性在执行前拦截；Autonomy Slider 显式表达"走多远"；Anthropic 三铁律——保持简单、显式透明、poka-yoke 工具（参数本身防错）。
- **反馈层级**（反直觉：thumbs 是最弱反馈）：行内接受/拒绝（Tab/Esc，生成瞬间）→ 区块 regenerate → 结构化理由（用自动化测试代替评分）→ 状态反转（rewind）。**反馈分布到整个交互链，不堆结尾。**
- **不确定性 UI**：置信度可见（句末来源）；草稿/假设标签；Effort Control（快而浅/慢而深）。
- **5 个 AI 时代新差异**：可逆性 > 一致性（checkpoint/rewind 取代 undo）；能力边界本身是产品；反馈是训练数据；诚实 > 能力；思考可见性是新型 affordance。
- 反面：每个按钮加 sparkles（"AI 视觉符号通胀"）；"Powered by AI"当价值主张；默认全自主 agent；隐藏工具调用；省略"随时停"。
