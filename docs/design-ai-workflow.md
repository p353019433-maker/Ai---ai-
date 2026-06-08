---
name: design-ai-workflow
description: "AI 设计工作流实操 - 11 工具地图/3 工具对比/10 prompt 模板/4 步流水线/反 slop 清单/角色转变 - 让你\"做\"AI 设计"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# AI 设计工作流实操（2025-2026）

## 一句话总结
**AI 不会取代设计师，但会用 AI 的设计师会取代不会用 AI 的设计师**——关键不是"用哪个工具"，而是建立 **brief → wireframe → polish → code → 审查** 的流水线，并掌握"反 slop"改稿能力。

## 一、AI 设计工具地图（11 个）

| 工具 | 何时用 | 何时不用 | 输出质量 |
|---|---|---|---|
| **Figma Make** | 已有 Figma 设计稿，要加交互/动画/响应式 | 从零做产品、需复杂后端 | 7/10（交互好，代码封闭） |
| **v0**（Vercel） | Next.js/React 前端 + shadcn/ui，1 天要 demo | 需要精细品牌、复杂状态机 | 7/10（代码可读、可 ship） |
| **Galileo → Google Stitch** | 快速出多屏 Figma 稿，给非设计师改 | 要写代码、复杂业务流 | 6/10（稿子漂亮，落地差） |
| **Cursor** | 把 v0/Figma 出的代码接入真实项目、补组件 | 设计还没定型 | 9/10（AI 写代码天花板） |
| **Lovable**（前 GPT Engineer） | 创业 idea → 完整可点 prototype + 部署 | 要精细交互/品牌 | 6/10（出活快，深度弱） |
| **Bolt.new** | 全栈 + 数据库 + 认证 + 部署一条龙 | 设计系统要严格统一 | 6/10（栈锁死在 StackBlitz） |
| **Relume** | 用 wireframe + 文案生成 Figma 结构 + sitemap | 要像素级精修 | 7/10（信息架构好） |
| **Uizard** | 截图/手绘转 Figma 稿 | 要响应式、要代码 | 5/10（原型够用） |
| **Visily** | 截图/线框转可编辑设计稿 | 严肃产品设计 | 5/10（适合 PM/BA） |
| **Magi** | 设计师个人 sketch 转生产稿 | 团队协作 | 4/10（新工具，慎用） |
| **FigJam AI** | 用户旅程图、亲和图、头脑风暴 | 出 UI | 6/10 |
| **Figma Buzz** | 营销素材批量出图 | UI 设计 | 7/10 |

**核心规律**：**写代码越深（Figma Make &gt; v0 &gt; Lovable/Bolt &gt; Galileo &gt; Relume &gt; Uizard），设计自由度越低**；出稿越快，设计精度越差。**没有银弹，只有组合**。

## 二、同一 brief 的 3 工具实战对比

**Brief**：SaaS 控制台侧边栏——Logo + 搜索 + 6 个一级菜单（带图标 + 角标）+ 底部用户卡片 + 折叠按钮。深色模式，240px 宽，圆角 8px。

### Figma Make 输出
- 优点：保留 Figma 已有设计系统（自动读 token），折叠/展开动画丝滑，深色模式色彩准确
- 缺点：代码是"包装过的 Figma 节点"，导到代码仓库里全是 magic number，命名混乱
- 能 ship 吗：能，但需要重写 60% 命名和结构

### v0 输出
- 优点：输出标准 shadcn/ui `Sidebar` 组件结构，Tailwind class 干净，TypeScript 类型完整，移动端响应式自带
- 缺点：图标库猜错（用 lucide 还是 heroicons 看你提示），间距 14px 不是你设计系统的 16px
- 能 ship 吗：**能直接 git push**，进 Storybook 几乎不用改

### Galileo / Google Stitch 输出
- 优点：1 秒钟出 4 个方向的稿子，颜色、字体、icon 选择最"现代"
- 缺点：不能出代码；细节不耐久看（hover 状态、focus ring、键盘导航全没有）
- 能 ship 吗：稿子能 ship，代码不能从这里出

### Cursor 接力（接 v0 输出）
**prompt**：`把 Sidebar 接到真实的 design-system 项目里。读取 src/design-tokens.ts，把硬编码的 bg-zinc-950 换成 bg-surface，把 lucide 换成我们项目用的 @phosphor-icons/react，加 ARIA 标签。`
- 30 秒搞定。原本要 40 分钟。

**结论**：**v0 出代码、Figma Make 出交互、Galileo 出稿子、Cursor 改代码**。一个项目 4 个工具配合用，而不是 1 个工具打天下。

## 三、10 个可直接复制的 prompt 模板

> **prompt 黄金三件套**：① 角色（"你是给 30-40 岁设计师做工具的产品经理"）② 约束（颜色 hex、间距 px、技术栈）③ 反例（"不要用紫色渐变"）。

### 1. 登录页（v0）
```
生成 Next.js + shadcn/ui 登录页。左侧 50% 是产品截图占位（用渐变蒙版 + 标签 "Acme Studio"），右侧 50% 是居中登录卡片：邮箱 input、密码 input（带眼睛图标 toggle）、"Sign in" 主按钮（bg-zinc-900 圆角 8px）、分割线、Google 按钮。
卡片宽度 400px，max-width。深色模式 bg-zinc-950。文字 zin-50。间距统一 16px 网格。
不要：紫色渐变、3D 插画、emoji、社交登录多余图标。
```

### 2. 仪表盘（v0 / Figma Make）
```
生成 SaaS 仪表盘：顶部 64px 导航（logo / 全局搜索 / 通知 / 头像），左侧 240px 侧边栏，主区是 4 列 KPI 卡（数字 32px / tabular-nums / 上箭头带 +12%），下方 12 列网格里放 8 列折线图 + 4 列最近活动列表。
图用 recharts，列表用虚拟滚动。Tailwind 间距 4 的倍数。
不要：饼图、彩虹色、阴影、3D 图表。
```

### 3. 表单（Figma Make）
```
生成 3 步注册表单。步骤指示器在顶部（数字 1/2/3，当前步骤 bg-blue-600，其他 zinc-200）。每步一个 section 标题 + 4 个 field + 下一步按钮。
所有 input 高度 40px、border-zinc-200、focus:ring-2 focus:ring-zinc-900。错误状态 border-red-500 + 下方 12px 红字。
第 3 步完成后展示成功状态：勾号 + "Account created" + "Go to dashboard" 按钮。
```

### 4. 卡片（v0）
```
生成项目卡片网格：3 列响应式（移动 1 列、平板 2 列、桌面 3 列）。卡片高度 320px，包含 16:9 封面图（用 placeholder）、标题 18px medium、描述 14px 锌色、底部作者头像 + 名称 + 发布时间 + 右上角更多按钮。
hover 时整卡上移 2px + shadow-lg。点击封面图进入详情。
```

### 5. 弹窗（v0 / Cursor）
```
生成 shadcn Dialog 二次确认弹窗：标题 "Delete project?" 18px semibold、描述 14px 锌色、底部右对齐两按钮（Cancel 描边 / Delete 红色实心）。Delete 按钮按回车键触发。
背景遮罩 bg-black/40 + backdrop-blur-sm。Dialog 内容 max-w-md。打开时锁滚、自动 focus 到 Cancel 按钮。
```

### 6. 错误页（v0）
```
生成 404 页面：极简单色背景 bg-zinc-50，中间 200px 见方插画占位（一只迷路的猫 SVG 线条稿，1.5px stroke）、下方 H1 48px "Page not found"、副文 16px "The link you followed may be broken"、主按钮 "Back to home" 圆角 8px。
不要用 emoji、插画库、彩色。整页垂直水平居中。
```

### 7. 空状态（Relume / Figma Make）
```
生成 SaaS 项目的空状态：240px 见方插画占位（用一个简单的、灰色的、线稿 SVG：文件夹 + 虚线框表示 "空"）、标题 "No projects yet" 20px、描述 14px "Create your first project to get started"、CTA 按钮 "New project" bg-zinc-900。
居中显示，垂直内边距 80px。
```

### 8. 邮件模板（Cursor / v0）
```
生成交易邮件的 React Email 模板：等宽 600px、bg-white、内边距 32px。顶部品牌 logo、标题 24px H1 锌色 950、正文 16px/24px 锌色 700、CTA 按钮 bg-zinc-900 文字 white 圆角 8px 内边距 12x24、底部版权 12px 锌色 500、unsubscribe 链接。
所有图片 alt 文字齐全。Outlook 兼容（table 布局）。不要用 background-image 关键内容。
```

### 9. 图标（v0 / Uizard）
```
生成 24x24 SVG icon set：home / search / bell / user / settings / chevron-down / plus / x / check / arrow-right / trash / edit。
线条 1.5px，stroke currentColor，24x24 viewBox，圆角端点。每个 icon 一个组件，支持 size / color / className props。
风格：Phosphor Icons regular weight。
```

### 10. 配色（Figma Make / Galileo）
```
为 [品牌：面向开发者的工具] 生成 8 步色板：
- zinc 50-950（中性灰）
- blue 500/600/700（主色 CTA）
- red 500/600（错误/危险）
- green 500/600（成功）
- amber 500（警告）
所有 hex 满足 WCAG AA 对比度（4.5:1 文字、3:1 大文字）。生成对应的 CSS variables、Figma variables、tailwind.config。
```

## 四、4 步流水线（brief → prototype → code）

### Step 1 · Notion brief（30 分钟）
```
# 项目：XXX
## 用户
- 谁：30-40 岁独立设计师
- 痛点：管理项目进度
- 关键任务：建项目 / 跟踪 / 出图

## 成功标准
- 5 分钟内完成首次建项目
- 3 次点击内看到所有项目状态

## 不做什么
- 不做协作（v1 单人）
- 不做时间追踪
- 不做移动端

## 风格参考
- 关键词：克制的、瑞士风、单色 + 一个主色
- 反例：渐变、3D、emoji

## 技术约束
- Next.js 14 + shadcn/ui
- Tailwind 4 的网格
- 部署到 Vercel
```

### Step 2 · v0 wireframe（1-2 小时）
把 brief 末尾加：`基于以上 brief，先生成登录页 + 主仪表盘 + 项目详情 3 屏的 wireframe 代码，每个屏幕有 2 个状态（空/满）。用最低保真度，颜色用 zinc 色阶，间距严格 4 的倍数。`
**v0 输出**后，把 GitHub repo 链接复制。

### Step 3 · Figma polish（2-4 小时）
- 把 v0 截图导进 Figma 当参考
- 用 Figma Make：`把这段 wireframe 加上正确的字体（Inter）、间距 8 的倍数、阴影 zinc-200/40、动效 150ms ease-out`
- 调品牌色、加 1px 边框、加 hover/focus 状态
- **不要在 Figma 里写代码逻辑**——Figma Make 的代码是装饰品

### Step 4 · Cursor code（1-2 天）
- `git clone` v0 的 repo
- 在 Cursor 用 Composer：`读取 docs/brief.md 和 src/，把 v0 出的 wireframe 接到 design system：换 token、加 ARIA、加错误状态、加 Storybook stories、跑通 lighthouse 90+。`
- Cursor 跑测试、改 lint、提 PR

**总时间**：传统流程 2-3 周 → 这套流程 **3-5 天**。前提：brief 写得清楚。

## 五、AI 输出的"反 slop"清单（看到 X 必改）

AI 出的稿子有个致命问题：**全部往"中位数漂亮"靠拢**。你要做的不是接受，是改。

1. **紫色渐变 + 蓝紫光晕** → 换成你设计系统里的主色 + 灰阶阴影。"AI 美" = 紫蓝渐变 + glass morphism + 3D 玻璃球。看到立刻删
2. **emoji 替代图标**（🚀 ⚡ ✨） → 换成 lucide/phosphor/tabler 等正经图标库。emoji 出现在 B 端 = 业余
3. **居中、对称、垂直堆叠** → 这是 AI 最爱的"安全结构"。真实产品是左对齐 + 网格 + 信息密度。**先左对齐，再考虑居中**
4. **到处都是"AI 友好"文案**（"Welcome to your dashboard! Let's get started."） → 改成动词开头、省略号结尾、不超过 8 个字的微文案。`New project` 比 `Welcome to your project creation center` 好 10 倍
5. **"Generate with AI"按钮放在最显眼位置** → AI 不该是产品的主角，是工具。把它放在次要位置（"More"菜单里），别让 AI 自吹自擂
6. **空白 + 大量 padding** → AI 怕出错所以留白多。实际产品 14-16px 间距就够了，桌面 1280+ 屏不要 80px padding
7. **3D 插画 + 渐变背景图 + 抽象几何** → 换成真实产品截图、黑白照片、单一纹理。"抽象 = 高级"是 2023 年的 AI 套路，2025 年是减法
8. **5 种字体混合** → 只用 1-2 种：标题用更紧的 sans（Inter Tight / Söhne），正文用宽松可读 sans（Inter / IBM Plex Sans）
9. **"Hover 才出现的辅助信息"** → AI 默认不做 tooltip、focus ring、键盘导航。生产稿必须有
10. **没有错误状态、没有空状态、没有 loading** → AI 出 happy path。3 个状态 × 5 个主页面 = 15 张图要补。这是 AI 最薄弱的地方，也是设计师最值钱的地方

## 六、设计师角色的 5 个转变

| 旧角色 | 新角色 |
|---|---|
| 画界面 | 写 brief + 审 AI 输出 |
| 选颜色 | 维护 design tokens |
| 拼组件 | 拼 prompt + 审 code |
| 一天画 3 屏 | 一天审 30 屏 AI 输出 + 改 5 屏 |
| 设计稿/开发者交接 | 一个 Cursor 会话里完成 |

**5 个新核心能力**：
1. **写 brief 比画图重要 10 倍**：AI 吃文字不吃草图。Brief 模糊 = 输出烂
2. **系统化 prompt**：把 10 个模板存到 Notion，按场景调参
3. **设计系统维护者**：tokens、组件、变体、状态机。这些 AI 不会自动管理
4. **"AI 改稿师"**：能看出"中位数漂亮"和"有判断力"的区别，10 分钟改完关键 5 处
5. **代码素养**：不需要写，但要能读 Cursor 输出、能用浏览器 DevTools 调试、能看懂 React 错误

## 5 条"如果你只能记一条"

1. **Figma Make 出交互、v0 出代码、Galileo 出稿子、Cursor 改代码**——一个项目 4 个工具，不要找银弹
2. **Brief 写不好，AI 输出一定烂**。"30-40 岁设计师" 比 "modern professional user" 好 100 倍。给 AI 具体的人、具体的数字、具体的反例
3. **AI 最强的是 0→1，最弱的是 1→100**。用它出第一稿，别让它做品牌、状态、错误处理。设计师的核心价值 = 审 AI + 补 AI 漏的状态
4. **看到"紫蓝渐变 + glass morphism + 3D 球"立刻删**。这是 AI 的口头禅，反过来用：克制、单色、留白、真实素材 = 反 AI 套路 = 高级感
5. **设计师不学代码 5 年内必死**。不需要写 React，但要能读 Cursor 输出、能用浏览器 DevTools、能维护 design tokens 和 Storybook。**会用 AI 写代码的设计师 = 设计 + 工程双倍杠杆**

## 资源 URL
- figma.com/ai/ / figma.com/blog/introducing-figma-make/ / figma.com/blog/category/ai/
- v0.dev/ / v0.dev/docs
- usegalileo.ai/ / cursor.com/ / lovable.dev/ / bolt.new/ / uizard.io/
- smashingmagazine.com/2024/02/ai-design-tools/ / smashingmagazine.com/2024/10/figma-ai-review/
- nngroup.com/articles/ai-design-tools/ / uxdesigninstitute.com/blog/ai-design/
- figma.com/blog/prompt-engineering-for-designers/
