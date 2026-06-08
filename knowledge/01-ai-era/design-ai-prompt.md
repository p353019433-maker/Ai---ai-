---
name: design-ai-prompt
description: AI 设计提示词工程 - 提示词三件套/5 种产品 brief/3 工具差异/20+ 提示词模板/10 条反 slop/迭代策略
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# AI 设计提示词工程：执行手册

## 一句话总结
**好的 AI 设计提示词 = 角色 × 约束 × 反例 × 资产 + 迭代纪律**。它不是 prompt 理论，而是结构化的需求文档：写清楚"你是谁、要做什么、不要做成什么样、参考谁"。

## 1. 提示词三件套：角色 / 约束 / 反例

**Anthropic 官方反复强调的核心结构**：每个高质量提示词必须包含三件套——**Persona（角色）、Constraints（约束）、Anti-patterns（反例）**。

**角色（Persona）**——告诉 AI 它是谁：
- "你是一位有 10 年 SaaS 仪表盘经验的产品设计师，专注 Linear / Vercel / Stripe 风格。"
- "你是一位编辑设计师，熟悉 The New York Times Magazine 与 Bloomberg Businessweek 排版传统。"

**约束（Constraints）**——用具体数值、可验证规则代替形容词：
- 反例："用好看的字体和现代感"
- 正例："标题用 Fraunces 700 / 64px，正文用 Inter 400 / 16px，行高 1.5，色板 #F4F1EA / #11171B / #C2410C 三色"

**反例（Anti-patterns）**——必须显式列出 AI 默认会犯的错：
- "禁止用 Inter / Roboto / Arial / system-ui 作标题"
- "禁止紫色渐变 + 白色背景（'AI slop' 标志）"
- "禁止所有 emoji 充当图标"
- "禁止居中对齐 + 大量留白 + 灰色文字 = 假'极简'"

**核心心法**：把"避免 X"翻译成"做 Y"。Anthropic 明确建议："Tell Claude what to do instead of what not to do."

## 2. 设计 brief 提示词模板：从模糊到 2000 字精确 brief

**80% 失败提示词的问题不是短，是空**。"做一个 SaaS 仪表盘"有 14 个字符，AI 必须猜测 14 个维度。

**精确 brief 模板**（复制即可用）：
```
<role>
你是一位 [行业] 的资深产品设计师，参考 [3 个真实产品] 的视觉语言。
</role>

<project>
[产品名] 是 [一句话产品定位]，目标用户是 [谁]，核心动作是 [什么]。
</project>

<screen>
当前任务：设计 [具体页面，如：Web 端定价页 / 移动端注册流 / 后台数据看板]。
分辨率：1440×900（桌面）/ 390×844（移动）。
</screen>

<tokens>
- 主色：[HEX]
- 中性色阶：#______, #______, #______
- 强调色：[HEX]（仅用于 CTA 与状态）
- 标题字体：[字体名] [字重] [尺寸]
- 正文字体：[字体名] [字重] [尺寸] / 行高 [X]
- 圆角：[X]px
- 间距网格：4 / 8 / 16 / 24 / 32 / 48 / 64
- 阴影：[具体 box-shadow]
</tokens>

<components>
明确列出需要的组件：导航 / 卡片 / 表格 / 表单 / Modal / Toast / Empty State / Loading / Error。
</components>

<layout>
- 12 列网格，gutter 24px
- 容器最大宽 1200px 居中
- 顶部 sticky 导航 64px
- 关键区域：Hero / Features / CTA
</layout>

<do>
- 用 [具体风格描述，如：90 年代瑞士极简 + 编辑设计网格]
- 强调信息层级，主标题占视觉重量 60%
- 真实文案，禁止 "Lorem ipsum"
</do>

<dont>
- 不用 Inter / Roboto 作标题
- 不用紫色渐变
- 不用 emoji 充当图标
- 不用居中对齐所有内容
- 不用"幽灵按钮"——CTA 必须实色
</dont>

<reference>
附 2-3 张参考图 URL 或截图说明。
</reference>
```

**关键原则**：**写好 brief 用了 30 分钟，AI 跑 30 秒，避免 4 轮迭代**。

## 3. Figma Make / v0 / Cursor 提示词工程：三个工具的差异

**Figma Make**——生成 Figma frame + 可点击原型
- 重点：**视觉层级 + 真实文案 + 组件库一致性**
- 必加："使用 Figma Auto Layout、12 列网格、8px 间距系统"
- 必加：`<empty_state>` 和 `<error_state>` 描述

**v0.dev**——生成 React + Tailwind + shadcn/ui 代码
- 必加：`<component_library>` 标签（"用 shadcn/ui 默认组件，扩展自 Radix"）
- 必加：`<data_shape>` 标签——AI 写 mock 数据比写代码更常出错

**Cursor**——Agent 模式写完整应用
- 必加：`<tech_stack>` 明确版本号（"Next.js 15 App Router + React 19 + Zustand 5"）
- 必加：`<folder_structure>`（"app/、components/、lib/、hooks/、types/"）
- 核心技巧：先让 Cursor 生成 design system 文件（tokens.ts + 基础组件），再生成页面

**三工具共通铁律**：
1. 第一稿永远不写"完美"——只写"骨架 + 关键约束"
2. 第二稿："把这版复制，做暗色模式" / "改成移动端" / "把 X 组件替换为 Y"
3. 第三稿："现在填充真实内容：用户 Alice, 30 天数据，$1234 MRR"

## 4. 多模态提示词：截图 / Figma frame / 设计参考作为输入

**截图输入的三种姿势**（按效果排序）：

**姿势 A：截图 + 反向 brief**
- 附一张参考图 + 文字："这个图是反面教材。请用同样的内容做出 Aesop 旗舰店网站的视觉层级。"

**姿势 B：截图 + 结构提取**
- "附图是我的草图。请识别每个区块的意图（左上：hero，左下：features，底部：CTA），按 12 列网格重画。"

**姿势 C：Figma frame 直接输入**
- 把已存在的 Figma frame 当上下文传给 AI 工具
- "基于这个 frame 的视觉风格，生成 3 个变体：极简 / 编辑 / 数据密集。"

**多模态黄金法则**：
- 截图分辨率**优先 1080p**
- 单次多图：3-5 张最佳，超过 5 张会分散注意力
- 文字说明图片位置："图 1 = 参考风格，图 2 = 必备组件清单，图 3 = 反例"

## 5. 迭代提示词策略：第一稿 vs 第五稿的差异

**Anthropic 明确指出**：Claude 4.6+ 是 literal follower，第一稿不要 over-specify 留迭代空间。

**第一稿的提示词哲学**："骨架 + 三件套 + 1 个明确锚点"
- 不要列 50 个组件
- 锚点 = 一个具体的可模仿产品："风格锚定 Linear，密度锚定 Stripe，编辑感锚定 Pentagram 年报"

**第五稿的提示词哲学**："手术刀式修改 + diff 思维"
- "仅修改 hero 区域，保持其余不变"
- "把 X 字号从 64 改为 48，行高保持 1.1 不变"
- "增加 mobile breakpoint 下的 stacking，但桌面布局完全保留"

**三种典型迭代 prompt**（复制即用）：

```
[太复杂] "现在做减法：
- 删除所有 emoji 图标，换成线性 SVG
- 主色从 3 种减为 1 种强调色
- 卡片阴影从 3 层减为 1 层
- 间距从 8 档减为 4 档（16/24/32/64）
保持信息架构不变。"
```

```
[太简单] "现在加细节：
- hero 增加 1 行产品价值主张副标题
- 卡片增加 hover 态：边框 +1px 强调色
- 关键数字增加 tabular-nums 与单位
- footer 增加 3 列站点地图"
```

```
[配色错了] "替换主色板。
目标：从 [冷蓝 #1E3A8A] 改为 [暖琥珀 #B45309]
规则：
- 中性色不变（#F4F1EA 背景 + #11171B 文字）
- 强调色仅用于：CTA / 链接 / 数据高亮
- 不要重新做视觉层级，只换颜色"
```

**迭代铁律**：
1. 每轮迭代只改 1-2 个变量
2. 每轮迭代附"保留什么"清单，避免 AI 改过头
3. 第 5 稿还在改第 1 稿的架构 = 失败，回到第 1 稿重新做

## 6. 设计 token 提示词：把 token 写进提示词

**Token 必须显式**——AI 不会自己发明 token。注入格式有三种：

**格式 A：CSS variables 块**（用于 v0 / Cursor）
```css
<design_tokens>
:root {
  --color-bg: #F4F1EA;
  --color-fg: #11171B;
  --color-accent: #C2410C;
  --color-muted: #6B7280;
  --font-display: 'Fraunces', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 4px;
  --space-1: 4px; --space-2: 8px; --space-3: 16px;
  --space-4: 24px; --space-5: 32px; --space-6: 48px; --space-7: 64px;
  --shadow-1: 0 1px 2px rgba(17,23,27,0.06);
}
</design_tokens>
```

**格式 B：Figma Variables 描述**（用于 Figma Make）
```
使用以下 Figma Variables：
- color/background/page = #F4F1EA
- color/text/primary = #11171B
- color/text/muted = #6B7280
- color/accent/default = #C2410C
- spacing/xs/sm/md/lg/xl = 4/8/16/24/32
- radius/default = 4
- typography/display = Fraunces 64/1.1
- typography/body = Inter 16/1.5
```

**格式 C：Tailwind config 片段**（用于 v0 / Cursor）
```javascript
<tokens>
theme: {
  colors: { bg: '#F4F1EA', fg: '#11171B', accent: '#C2410C' },
  fontFamily: { display: ['Fraunces','serif'], sans: ['Inter','sans-serif'] },
  borderRadius: { DEFAULT: '4px' },
  spacing: { 1: '4px', 2: '8px', 3: '16px', 4: '24px', 5: '32px', 6: '48px', 7: '64px' }
}
</tokens>
```

**Token 注入铁律**：
1. **必须用 hex，不用色名**
2. **必须给具体值，不用相对值**
3. **必须在首轮就给出**，后续迭代不要改 token
4. **缺失 token = 100% 出 AI slop**——这是"去 AI 化"的核心抓手

## 7. 设计模式提示词库：20+ 复制即用模板

**通用三件套（每个项目都用）**：
```
<role>你是有 10 年 [领域] 经验的资深设计师，参考 [产品 1] [产品 2] [产品 3] 的视觉语言。</role>
<constraints>只用 [字体] + [字体]；色板严格限制 [X] 色；圆角 [X]px；最大宽度 [X]px。</constraints>
<anti-patterns>禁止 Inter / Roboto 作标题；禁止紫色渐变；禁止 emoji 图标；禁止居中堆叠；禁止占位文案 "Lorem ipsum"。</anti-patterns>
```

**5 种产品类型完整 brief 模板**：

**(1) 登录页**
```
<role>SaaS 产品设计师，参考 Linear / Vercel / Stripe 落地页的克制编辑感。</role>
<page>桌面 1440×900 移动 390×844 响应式。/ 顶部 sticky nav 64px / Hero 50vh / Features 3 列 / Social proof / Pricing teaser / Final CTA / Footer。</page>
<hero>主标题 <h1> 用 Fraunces 64px，仅一句话价值主张。副标题 Inter 16px 一行。CTA 实色按钮 #C2410C 文字 "Start free"。右上角小标志。</hero>
<density>每屏文字 < 30% 覆盖率；间距慷慨；左右边距 80px 桌面 / 24px 移动。</density>
```

**(2) 仪表盘**
```
<role>B2B SaaS 仪表盘设计师，参考 Stripe Sigma / Linear Insights / Plausible 信息密度。</role>
<layout>左侧 240px 导航（图标+文字），主区 12 列网格，顶部 64px 工具栏（搜索 + 用户菜单），主区分 4-6 个数据卡片，底部时间序列图表。</layout>
<data>卡片用真实 mock 数据：4 位数数字 + 单位 + 同比 + sparkline；图表用淡灰填充 + 强调色描边；空状态用插画 + 一行说明 + 主 CTA。</layout>
<states>必须包含：loading skeleton / empty state / error state / success toast。</states>
```

**(3) 电商商品页**
```
<role>高端电商产品页设计师，参考 Aesop / Mr Porter / Apple Store 的编辑感与克制。</role>
<structure>2 列布局：左 60% 商品图轮播（5 图 + 缩略图），右 40% 信息（标题 / 价格 / 容量 / 数量 / 加入购物车 / 详情 tab：描述 / 成分 / 配送）。</layout>
<typography>商品名 Fraunces 32px 500；价格 Inter 24px 600 tabular-nums；详情 Inter 14px 1.6 行高。</typography>
<micro>hover 态图片切换 200ms 缓动；CTA 实色无阴影；移动端 1 列 sticky 底部 CTA。</micro>
```

**(4) 博客 / 长文**
```
<role>编辑设计师，参考 NYT Magazine / The Verge / Stratechery 的网格与排版传统。</role>
<layout>顶部 nav 64px / 文章 hero（主图 + 标题区 80vh）/ 正文 680px 居中 / 中间穿插 pull quote / 作者 bio / 推荐阅读 3 卡 / 评论区 / footer。</layout>
<type>正文 Inter 18px / 行高 1.7 / 段距 24px；小标题 24px 600；pull quote Fraunces italic 32px 左右各缩进 80px。</typography>
<rules>首字下沉；图片说明 italic 14px；链接下划线 hover 变粗。</rules>
```

**(5) 落地页（Marketing）**
```
<role>增长设计师，参考 Notion / Figma / Framer 落地页的对话感与转化优化。</role>
<structure>Hero（动画 1 个产品场景）→ 价值主张 3 点 → 客户 logos 灰度 → 大图特性展示 → 用户证言（头像 + 名字 + 公司）→ 集成展示 → 定价 → FAQ accordion → 最终 CTA。</structure>
<cta>贯穿全页 sticky 底部 CTA 移动端；桌面每屏 1 个 CTA；按钮文字具体动作（"Get my free workspace" 而非 "Sign up"）。</cta>
```

**3 种工具版本**：

**Figma Make 版**：在每个模板末尾加 `<figma_specific>`：使用 Figma Auto Layout 4 / 8 / 16 / 24 / 32 间距 / 12 列网格 / Variables 引用 token / 包含 sticky nav 与 responsive frame。

**v0 版**：在每个模板末尾加 `<v0_specific>`：使用 Next.js 14 App Router + TypeScript + Tailwind + shadcn/ui + Lucide 图标（不用 emoji）/ 响应式 md: lg: 断点 / 暗色模式通过 CSS 变量切换。

**Cursor 版**：在每个模板末尾加 `<cursor_specific>`：先把 token 写入 lib/tokens.ts / 用 cn() 合并 className / 每个组件独立文件 / 写 prop interface / 加 Storybook story（可选）。

## 8. AI 反 slop 检查清单（10 条）

**Anthropic 官方"AI slop"清单 + 设计师补充**——交付前逐条 grep：

1. **Inter / Roboto / Arial / system-ui 作标题** → 换成 Fraunces / GT Sectra / Suisse / Editorial New
2. **紫色渐变 + 白色背景** → 换成单色强调 + 大色块对比
3. **居中对齐所有内容** → 改左对齐 + 网格约束
4. **emoji 充当图标** → 换成 Lucide / Phosphor / Tabler
5. **Lorem ipsum 占位** → 换成真实文案或方框标记 "TITLE GOES HERE"
6. **3+ 阴影层级堆叠** → 减为 1 层或 0 层
7. **"Ghost button" 滥用** → 主 CTA 必须是实色
8. **过度圆角（16px+）** → 改 4-8px
9. **过度动画（页面入场 5+ 元素飞入）** → 减为 1 个主动画 + 2-3 微交互
10. **过度留白 + 灰色文字 = 假极简** → 用 1-2 个大色块 + 高对比文字（#111 on #F4F1EA）打破"性冷淡"

**额外红线**：
- 看到 "1000+ integrations" / "Built for scale" / "Empower your workflow" → 立刻删
- 看到 3D 抽象渐变球 / 抽象插画小人 → 删
- 看到 "🚀 Get started" → 改成 "Start free"

## 9. AI 设计师的新工作流：brief → AI 出稿 → 人类审稿 → 合并 → ship

**5 步标准化流程**（每个项目 4-8 小时）：

**Step 1: Brief（30-60 分钟）**
- 用第 2 节模板写 1500-2000 字 brief
- 收集 3-5 张参考图（Pin / Are.na / Figma Community）
- 写完 brief 自我检查：能否把这个 brief 给一个新同事，他能直接动手？

**Step 2: AI 出稿（5-15 分钟/工具）**
- v0：生成主页面 + 关键组件
- Figma Make：生成高保真 frame
- Cursor：生成 component library + 主页面
- 不要合并 3 个工具的输出，**先各自跑 3 轮**

**Step 3: 人类审稿（30-60 分钟）**
- 打开反 slop 检查清单（10 条）逐条过
- 在 Figma / 代码里直接标 comment
- 区分"硬错"（错位、错色、断链）vs"软错"（风格不一致、密度不对）

**Step 4: 合并（60-120 分钟）**
- 选一个工具作"主"（通常是 Figma Make 出视觉，Cursor 出代码）
- 把 v0 的代码资产 / Cursor 的 design tokens / Figma 的 frame 互相打通
- 用 Figma MCP 把 Figma 直接喂给 Cursor（design-to-code）

**Step 5: Ship（2-4 小时）**
- 在 Cursor 里把 AI 生成的 mock 替换为真实数据
- 用 Playwright 截图对比 Figma 与实现
- 跑 Lighthouse + a11y + 响应式三件套
- 提交 PR，附 AI 提示词作为 PR description 的一部分

**新工作流的本质**：**设计师不再是"做图的人"，而是"定 brief 的人 + 审稿的人 + 把关的人"**。三件套各 30 分钟 = 1.5 小时，比纯手做 8 小时快 5 倍，质量还更好。

## 10 条"如果你在写 AI 提示词，记住这些"

1. **具体 > 形容词**——"64px Fraunces" > "大标题"
2. **反例 > 正例**——必须列"禁止 X"清单
3. **首轮做骨架，不做完美**——给 1 个锚点，留迭代空间
4. **Token 写在最前**——缺失 token = 100% AI slop
5. **迭代只改 1-2 个变量**——同时改 5 个 = 失控
6. **每轮附"保留清单"**——避免 AI 改过头
7. **写完 brief 自我测试**——给陌生同事能直接动手吗
8. **不要合并 3 工具首稿**——先各自跑 3 轮
9. **真实文案 > Lorem**——"Alice's dashboard" > "Lorem ipsum"
10. **风格锚定 3 个真实产品**——比形容词描述强 10 倍

## 5 条反面教材

1. **"做一个 SaaS 仪表盘，要好看"**——零信息量
2. **"用现代极简风，配色随意"**——"随意"= 紫色渐变
3. **"参考 Apple 但要更高级"**——AI 不知道"更高级"是什么
4. **第一稿就列 50 个组件 + 完整 design system**——过拟合，迭代困难
5. **5 轮迭代都在改同一个错**——说明第一稿的 brief 本身就错了

## 5 条"如果你只能记一条"

1. **写好 brief 用了 30 分钟，AI 跑 30 秒，避免 4 轮迭代。** 投入预算到 brief，不是到迭代
2. **三件套 = 角色 + 约束 + 反例。** 缺一不可
3. **Token 写进 prompt。** 缺 token = 100% AI slop
4. **风格锚定 3 个真实产品。** 比任何形容词描述有效 10 倍
5. **反 slop 检查清单 10 条交付前过一遍。** 这 10 条是"AI 设计"的最低验收标准

## 资源 URL
- v0.dev/docs / v0.dev/docs/text-prompting / v0.dev/docs/prompting
- figma.com/blog/prompt-engineering-for-designers/ / figma.com/blog/writing-prompts-for-figma-ai/
- help.figma.com/hc/en-us/sections/1500008802581-Figma-AI / figma.com/ai/
- cursor.com/blog/agent-design / cursor.com/docs / docs.cursor.com/chat/overview
- docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview / use-xml-tags / prompt-templates / chain-prompts / long-context-tips
- platform.openai.com/docs/guides/prompt-engineering
- smashingmagazine.com/2023/12/ai-prompts-designers/ / 2024/04/figma-ai-prompts/ / 2024/09/prompt-engineering/
- uxdesigninstitute.com/blog/prompt-engineering-designers/ / nngroup.com/articles/ai-design-prompts/ / prompt-design/
- lovart.ai/blog/prompt-guide / relume.com/blog/prompt-engineering
