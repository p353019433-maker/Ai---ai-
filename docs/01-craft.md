# 01 · 工艺规则 — 字体、色彩、布局、组件、文案、动效、数据

> 蒸馏自：design-typography-practice/craft、design-color-contrast、design-layout-grid、design-component-patterns、design-microcopy、design-motion-microinteractions、design-ui-decisions、design-data-visualization、design-web-aesthetics（原文见 git 历史）

## 一、排版

**字号 scale**：1.125 文档/密信息 UI（Notion、Linear）；**1.25 (Major Third) 是 80% 项目默认**（Vercel、Stripe、GitHub）；1.333 营销页；1.5 编辑出版；1.618 仅杂志封面级 Hero。1.25 具体值（@1rem）：0.64 / 0.8 / 1 / 1.25 / 1.563 / 1.953 / 2.441 / 3.052 / 3.815rem。一页最多 4 个字号。

**三个魔法单位**：字号用 rem、**行高用 unitless**、字距用 em。`line-height: 24px` 会被子元素继承绝对值（48px 标题行高变 0.5）——MDN 明确建议 unitless。

**行高**随字号反比：24px→1.5，48px→1.2，96px→1.0。正文 1.5–1.7（WCAG 要求 ≥1.5，>1.8 会"散"）；标题 1.2（≤1.2 配 `text-wrap: balance`）；按钮 `line-height: 1` + padding 控高。

**字距决策树**：≥48px 必加负字距 -0.02～-0.05em；16–32px 恒为 0；≤12px 可加 +0.01～0.02em；uppercase 必加 +0.05～0.1em。警告：**非零 letter-spacing 会禁用 OpenType 连字**。

**行长**：45–75 字符/行，理想 66（Bringhurst）；用 `max-width: 65ch`。新手最常犯：整页文本无 max-width，桌面端一行 200 字符。**80% 网页的正确答案一行**：`font-size: 1rem; line-height: 1.6; max-width: 65ch;`

**OpenType 铁律**：`kern` 永远开；数字场景（表格/价格/计时器）**必开 `tabular-nums`**——产品里 90% 的"歪"来自数字不等宽。发票序列号加 `'zero' 1`（斜杠零）。

**可变字体**：注册轴小写（wght/wdth/slnt/ital/opsz）、自定义轴大写（GRAD），大小写敏感。**GRAD 轴是 hover 动效理想载体**——改字重不改字宽，不触发 reflow（用 weight 会抖动）。实战 bundle 减 60-80%。

**响应式与加载**：h1 `clamp(2rem, 1rem + 4vw, 4rem)`；**WCAG 1.4.4：clamp 的 max ≤ min 的 2 倍**（否则阻碍 200% 缩放）。加载 2026 标准：WOFF2 唯一格式 + preload + `font-display: swap`（body 绝不用 block）+ 尽量 1 个 weight；防 CLS 用 `size-adjust`/`ascent-override` 调 fallback metrics；`unicode-range` 子集化（拉丁 ~50KB、中文 ~200KB，永不全字符集）。

**选型**：≤12px UI → Inter / IBM Plex / Söhne（高 x-height + text 光学尺寸）；大标题 → Söhne Breit / Tiempos Headline；长正文 → Tiempos Text / Charter / Source Serif；多语言 → Noto；上限 3 套（display/text/mono）。光学尺寸 Adobe 6 档（Caption 4-8pt 到 Poster >72pt）；小字号需要加粗 stroke + ink trap。字体即声纹：Stripe=Söhne、Linear=Inter Display、Notion=IBM Plex。

**工艺背景**：合格正文字体含 5000+ 手调字距对 ≈ 1000+ 工时——字体 70% 成本在 kern 表。反面教材：10px 用 Helvetica Neue Light（stroke 消失）；人文（Gill Sans）与几何（Futura）不混排；不用 CSS 模拟 italic；Helvetica 小字号 aperture 太窄、I/l 无法区分（Spiekermann）。Licko："You read best what you read most."

## 二、色彩

**2024 起新项目用 oklch**：HSL 的 darken 让蓝变脏，oklch 调 L 保持鲜艳（Tailwind v4 已全迁移）。派生状态色：`oklch(from var(--brand) calc(l + 0.1) c h)`；hover = L+5~10%，active = L−5~10%。

**WCAG 对比度**：正文 4.5:1（AA）；大字（18pt+ / 14pt+bold）3:1；UI 组件/图标/焦点环 3:1；**不准四舍五入**（4.47:1 = 不通过）。**状态 5 态（rest/hover/active/focus/disabled）独立测**。focus 环 `outline: 2px solid + offset 2px`；`outline: none` 不补 ring = 违规。disabled 不用 `opacity: 0.5`（破坏一切对比），改 muted token。

**灰阶**：4 个中性色相——slate(257 冷/金融)、gray(264 通用)、zinc(285 偏紫/GitHub-Linear 风)、neutral(纯灰)；**选一个走到底**；人文产品用 warm gray（hue 30-60）。禁纯黑 #000——用 #0F0F0F/#1A1A1A 或带温度的灰。

**11 阶品牌色 L 锚点**（oklch）：50→97%，500→64%（主色），600→56%（hover），700→48%（active），950→22%。档位用途：50-200 背景 / 300-400 禁用 / 500-600 按钮 / 700-800 链接 / 900-950 标题。状态色 hue 锚点：success 145 / warning 80 / danger 25 / info 220。

**语义 token**：组件禁止 `bg-red-500` 写死，必须 `bg-destructive`；14 个 token 覆盖 90% 场景（bg/bg-elevated/text/text-muted/primary/secondary/accent/success/warning/danger/info/muted/border/ring），每个语义色配 `*-foreground`。**1 个主色且用量 ≤5%**（Radix 12 阶分工：1-2 背景/3-5 组件底/6-8 边框/9-10 实色/11-12 文字）。

**暗色模式三动作**：不反转、要重画——降饱和 10-20% + 提亮主色 + **反转 elevation 逻辑**（浮起=更亮：8%/11%/14%/17%，不是加阴影）。背景用 off-black `oklch(8% 0 0)`（≈GitHub #0d1117）；纯黑+白字产生 halation 光晕。纯白纯黑 21:1 过度，推荐 ≈16:1。

## 三、布局

**8pt 体系**：2/4/8/16/24/32/40/48/64/80 覆盖 95% 场景；4 用于组件内、8 用于模块间；例外仅 1px 边框、2px focus 环。看到 `padding: 17px` 立即改。section 间距 ≥ 内部 2×；页边 ≥32px。

**栅格**：12 列默认（因数全）；16 列仅密集仪表盘。断点用 Tailwind 640/768/1024/1280/1536；简单项目 3 个，**别超 5 个**。**永远移动优先 `min-width`**；容器 max-width ≤1280px。

**Grid 管二维，Flex 管一维**；无媒体查询自适应卡片一行解：`repeat(auto-fit, minmax(280px, 1fr))`。**`gap` 永远优先于 `margin`**。流体 padding：`clamp(2rem, 6vw, 6rem)`。Container queries 用于组件内自适应（`container-type: inline-size` + `@container`）。

**骨架速查**：Article `max-width: 65ch`；Settings `720px + 200px 1fr`；Dashboard `240px 1fr`；404 `display: grid; place-items: center`。

**反 AI 感布局三则**：左对齐是 Swiss 黄金法则、禁全文居中；**不对称优于对称**（对称=模板感）；减少 1px border，用间距+色差代替。圆角全产品统一（8px 卡片/4px 按钮/999px 头像）。**层级 5 工具优先级：Size > Weight > Color > Position > Whitespace**；de-emphasize to emphasize；眯眼测试。

## 四、组件

**组件公式：状态机 × token × ARIA。每个交互组件穷举 8 态**（default/hover/active/focus/disabled/loading/error/empty），漏一个=半成品。不要从 0 设计 Button——shadcn/Radix（结构）+ Tailwind（token）+ Lucide（图标），把时间花在产品独有的 20%。

- **按钮**：5 变体（primary/secondary/tertiary/ghost/destructive）；**primary 一屏只 1 个**；尺寸 32/40/48px；触控 ≥44×44pt(iOS)/48dp(Android)；loading 时**宽度不变防抖动**；图标按钮必须 `aria-label`；>3 个按钮 = 重新设计流程。表单 primary 永远右下，cancel 在左。
- **卡片**：内边距 16/24/32；**阴影 vs 边框二选一不叠加**；hover 抬升的卡片内禁止第二个独立按钮（hit-area 冲突），≥2 个 CTA 改"整卡可点 + overflow menu"。
- **表单**：**Label 永远在外，placeholder 不能替代 label**；label 顶部对齐（比左对齐快 2 倍，NN/g）；**校验 onBlur 触发，绝不 onChange**；错误 inline 红+icon+文字三通道（8% 男性色盲）；input 高度=按钮高度 40px；**iOS 防自动放大字号 ≥16px**。
- **选择控件**（LukeW "Dropdowns are the UI of Last Resort"）：2 项→toggle；2-7 项→radio/segmented；>7 才下拉；>15→search-select；switch 即时生效 / checkbox 提交后生效。
- **Modal 三件套缺一不可**：focus trap + Esc 关闭 + 焦点回触发钮。confirmation 400px / form 560px；内容 >1 屏=不是 modal 是页面；移动端自动变 bottom sheet；modal 套 modal 绝对禁忌；**永不用 modal 拦 newsletter/cookie/登录**。触发前问 5W（NN/g）。
- **导航**：3-5 高频同级→Top Tab；>5 多层级→Sidebar；移动端 bottom tab 最多 5 个；Breadcrumb ≥3 层才用、当前页不可点；tabs 用下划线+加重表示当前（不用底色块）。
- **表格**：数字右对齐+`tabular-nums`+千分位、文字左对齐；行高 ≥44px；表头 sticky；>1000 行虚拟滚动；**排序 icon 未激活也占位防抖动**；每行操作 >3 折叠到 `⋯`；移动端折叠成卡片。趋势色西方绿涨红跌、**中国相反——按地区切**。
- **Toast**：成功 3s / 信息 5s / **错误不自动消失**（toast 报错是反模式，字段错误用 inline，系统故障用 banner）；关键操作带 Undo（Gmail 模式）。选型：提示+免操作→Toast；重要+持久→Banner；关键+需操作→Modal；上下文→Inline。
- **加载**（NN/g）：<1s 不显示任何 loading；1-9s skeleton（结构可知）或 spinner；≥10s progress + 文案 + 取消。**skeleton 比 spinner 感知快 20-30%**；贴合最终内容、第三行宽 60-80%。**进度条数字来回跳比没进度更糟**——删掉换 indeterminate。
- **空态 4 件套**：插画 / 用户视角标题（"还没有项目"，≤6 字）/ 为什么空+下一步 / 1 个 CTA。**禁止只写"暂无数据"**；过滤后空突出"清空筛选"而非"创建"。
- **错误**：**说"我们"出错不说"你"**；三段式=发生了什么+为什么+怎么办；不暴露 stack trace；表单错误滚动到第一个错误字段并 focus；部分成功写明"10 中 8 成功"。404 放搜索框+主导航。
- **分页**：infinite scroll **必须保存滚动位置 + 底部出口"已加载全部"**；显示总数"21–40 / 共 1,234"。

## 五、微文案

- **按钮首词必须动词**，1-3 词，禁 OK/Cancel/Submit/Yes/No——Cancel→`Keep editing`/`Discard`，Submit→`Sign up`/`Place order`。动词+宾语使误操作率降 30%+（NN/g）。
- 近义词：Delete=永久；Remove=移出列表；Archive=隐藏可恢复。危险操作加对象：`Delete "Q4 report.pdf"` 比裸 `Delete` 安全 10 倍；**可撤销（5s Undo）> 二次确认**；高危才输入 `DELETE` 确认。**不要让 Enter 默认落在危险键**。
- CTA 模板 `[动词]+[收益]+[去风险]`：`Start free trial — 14 days, no card`。禁空动词 Learn more/Click here。
- 错误三段式带示例：`Password needs 8+ characters and 1 number. Try Sun4rise!`；报错不清空用户输入；禁 Invalid/Illegal；不写 `Error 503`，写 `We can't reach our servers. Try again in a minute.`
- 成功 = `[过去式动词]+[具体对象]`：`3 files uploaded to "Q4 reports"`，不是 `Success!`。
- Label 用名词 + Sentence case（`Sign up` 比 `Sign Up` 高级）。
- **AI 文案改稿 5 必做**：删感叹号；删 Please/Kindly/We are sorry；删 `Welcome to.../Let's...`；Click here 换动作本身；Submit/OK 换动词+对象。标志性 AI 套话：`Oops! Something went wrong.`、`Thank you for your submission!`（→ `We'll review and reply within 24 hours.`）。文案动词开头、≤8 字。

## 六、动效

**四件套覆盖 80% 微交互**：`transform` + `opacity` + `cubic-bezier(0.4, 0, 0.2, 1)` + 240ms。**绝不动 width/height/left/top/margin**（触发 layout 必掉帧）。

- Easing 语义：入场 ease-out、离场 ease-in；**浏览器默认 `ease` 几乎不用**；`linear` 只用于 spinner/shimmer。
- 时长 5 档 token：80ms（颜色微变）/150ms（hover、tooltip）/240ms（按钮）/360ms（modal、抽屉）/500ms（页面转场）。甜区 100-400ms；**200ms 是跨系统共识甜点**（<100ms 像 bug，>300ms 像卡）；入场比离场慢 50-100ms。
- 按钮：hover `scale(1.02)`（不要 1.05）；active `scale(0.98)` + 80ms。
- 微交互 4 阶段（Saffer）：Trigger → Rule → Feedback → Loop；**反馈缺失 = 信任缺失**。
- 转场 6 范式：fade（仅数据更新）/slide/push（移动端默认）/zoom（modal）/morph/shared element（列表→详情）。iOS=Spring（可中断），Material=easing 曲线（不可中断）——别混用方言。spring 仅用于拖拽/可中断动画。
- Scroll-driven：纯 CSS `animation-timeline: view()` + `animation-range: entry 0% cover 30%`（避开 AI 默认 0-100% 线性触发）；**`prefers-reduced-motion` 必查**。
- 工具：纯 CSS 微交互→CSS；SPA 路由→View Transitions API；AE 动效→Lottie/Rive；React layout→Framer Motion。
- Disney 12 原则对 UI 最关键：Anticipation（hover 预告）、Staging、Slow in/out（永不 linear）、Exaggeration（反馈要大到能被感知）。

## 七、数据可视化

- **Tufte**：data-ink ratio 最大化；chartjunk 清单（3D、粗网格、阴影、图案填充、pictogram 柱子）；**Excel/AI 默认图永远先重做**；"A table is nearly always better than a dumb pie chart"；Lie factor=视觉变化/数据变化=1 才诚实；核心问题 "Compared to what?"
- **Cleveland & McGill 感知精度排序（圣经）**：共同刻度位置 > 非对齐位置 > 长度 > 角度/斜率 > 面积 > 颜色——bar 永远比 pie 准的实验依据。
- 图表选择：比较→bar；趋势→line（stacked area 几乎总该换 small multiples）；分布→histogram/box；关系→scatter；构成→饼仅 ≤5 类；heatmap **必用 Viridis 等感知均匀色板，永不 rainbow/jet**。
- 颜色只承载一种含义：类别（Tableau 10）/顺序（Viridis）/发散（RdBu，中点=0）三选一。
- **Y 轴：bar 永远从 0；line 可例外但必须标注**。标题写结论（"收入 Q3 增长 23%"）不写描述。每图必有：数据源/轴标签/单位/样本量。
- 10 类欺骗识别：截断 Y 轴、双 Y 轴伪相关、3D 饼、pictogram 面积失真、rainbow、缺刻度、截取范围、伪趋势线、多层饼、aspect ratio 操纵。怀疑数据图 6 问：Y 轴起点？图例？n=？第二根 Y 轴？rainbow？散点硬画趋势线？
- Few dashboard：从"用户每天第一个问题"倒推；bullet graph 替代仪表盘；sparkline 嵌表格；direct labelling 替代图例；必有 "as of [时间戳]"。反模式：一屏 20 个 KPI、交通灯三色代替数字。

## 八、2026 网页美学

- **Editorial**：hero 1 行 150-240pt 衬线大标 + 60-80 字 lead；单色背景 + 1 个 accent；display 专属字体 + body 双轨制（Inter/Geist）。
- **Brutalist 的本义**是"拒绝装作精致"非"丑"：system font、default 链接蓝、可见边框、`border-radius: 0`。
- **性能即美学（也是道德）**：首屏 <100KB、零 layout shift 写进 lint；一个 YouTube embed ≈1.2MB；反面 = 800KB React bundle 跑 20px 位移。
- 现代 CSS 替代依赖：`@scope` 替 BEM、Popover API 替 tooltip 库、`contrast-color()` 自动主题——以前三个依赖的效果现在 50 行 CSS。
- **"像 2015"反例清单**（出现即重做）：全屏背景视频+居中 logo+3 icon；渐变阴影等距卡片；滚动 50% 弹 newsletter modal；3MB JS 跑 200 字 reveal；毛玻璃导航 + 4 列 60 链接 mega footer。
- Awwwards 风向：2026 不再奖励"好看"，开始奖励"有意思"。

## 九、生成式算法（增量并入）

> 蒸馏自 research-notes-02（generative algorithms）。约束三原则：**有种子（可重现）、有界（可用）、有意义（内容/品牌驱动）**——生成器要会说"不"。

- **种子化随机**：Mulberry32 PRNG（`seed += 0x6D2B79F5`）+ FNV-1a `hashStringToSeed`。**keyed 随机**：`randFor(seed, "card:A:width")` 用 `seed:key` 派生，避免插入一个随机调用打乱下游全部；layout/texture/type/motion 独立派生种子。
- **weighted categorical**（避免均匀采样的同质化）：motif 权重如 `[line 45, dot 20, cutout 15, glyph 12, void 8]`——主导行为 + 稀有时刻。
- **分布选择**：Gaussian（笔画粗细聚集，`softRandom=(r+r+r)/3`）、power-law（多小少大）、`randomRange` mode center/low(`pow(r,2)`)/high。
- **fractal noise**：octaves 4–5，persistence（amplitude×0.5），lacunarity（frequency×2.0）；`organicRadius` 有界 18% 变化（`1 + 0.18*n`）；domain warping（warpStrength≈80）。
- **flow field**：grid 存角度，可 quantize 到 45°；离开 bounds / 进入 protectedZone / 超 maxSteps 时停。**jittered grid**：jitter 必须 < 半个 cell（`min(jitterRatio, 0.5)`）。**recursive subdivision**：split 35–65% 避免 sliver，min 边长 80px。还有 Poisson disk、L-systems（`F→F[+F]F[-F]F`）、cellular automata（B3/S23）。
- **rejection / scoring**：`scoreComposition`——textContrast<4.5 扣 0.5、density>0.75 扣 0.3、accentArea>0.14 扣 0.2、无 heroAnchor 扣 0.4；`generateUntilGood(maxTries=50)`。
- **生成 token 层**：design token 里加 `generative.grid.jitterRatio {min,max,distribution}`、`composition.maxDensity:0.68`、`minTextContrast:4.5`、`protectedZones`。**named modes 而非 random soup**：archive/signal/field 各定 density 区间、palette、angleQuantization、typeWeight；macro/meso/micro 分层；维护 approved/rejected seeds 注册表。
- 人性化随机：rotate ±0.6°、offset ±6px、手绘下划线 5 控制点 ±3px。

## 十、Typography deep：可变轴与 OpenType 数值规则（增量并入）

> 蒸馏自 research-notes-03。这些是 AI 几乎不用、但决定"专业 vs 模板"的具体杠杆。

- **`opsz` 是不同 drawing 不是缩放**：caption `opsz 10 + GRAD 25 + letter-spacing .012em`；body `opsz 17`；display `opsz 96 + GRAD -5 + letter-spacing -.055em`。
- **`GRAD` 轴（改粗细不改字宽、不 reflow）**：dark mode `GRAD -20`（防 bloom）；small-label `GRAD 30`（防变细）。AI 只用 400/600/700 三档，从不用 GRAD——这是廉价的差异化。
- 自定义轴速查：Roboto Flex（GRAD/XTRA/XOPQ/YOPQ/YTAS/YTDE/YTLC/YTUC）；Recursive（MONO/CASL/CRSV，单家族跨 mono↔proportional、strict↔casual，可替代 Inter+JetBrains Mono）；Fraunces（opsz 9–144 + SOFT + WONK）。
- **CSS 属性映射**：注册轴优先用高级属性（`font-optical-sizing:auto`、`font-stretch`、`font-style:oblique`），自定义轴才用 `font-variation-settings`。
- **OpenType 按上下文（AI 常忽略）**：prose 用 `oldstyle-nums proportional-nums`；table/price/time 用 `lining-nums tabular-nums`；code/serial 用 `slashed-zero tabular-nums`；真 small caps 用 `font-variant-caps: all-small-caps`+tracking .045em（不是缩放大写）；`ss01`–`ss20` 必须在设计系统文档化含义。
- tracking 量化：全大写 label `letter-spacing: 0.04–0.12em`（必须正）；大号 display 响应式负 tracking `clamp(-0.065em, -0.5vw, -0.025em)`；body 维持 0。leading 角色化：长正文 1.6+、大标题 0.92–1.05、serif 正文 ≠ 高 x-height sans。
- **用 role token 不用 size/weight**：`--type-display-hero/-section/-title-card/-body-long/-body-compact/-label-ui/-caption-data/-code-inline/-quote`，每个角色回答"读者在做什么 / 文本多长 / 需要何种 numeral / 是否 opsz/GRAD"。
- rationale 字体配对（任务分工非装饰）：Fraunces+Atkinson Hyperlegible（公益/可访问）；Source Serif 4+IBM Plex Sans（研究报告）；Recursive 单家族（开发者工具）；Newsreader+Bricolage Grotesque（文化出版）；Instrument Serif+Inter（编辑/信任）。
- SVG 材质纹理：纸纹 `feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3"`；边缘粗糙 `feTurbulence baseFrequency="0.02"` + `feDisplacementMap scale="6"`。
