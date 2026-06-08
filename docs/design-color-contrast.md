---
name: design-color-contrast
description: 色彩与对比度实操 - oklch 取代 HSL / WCAG AA 4.5:1 / 14 语义 token / 暗色模式 / 状态色 / 调色板工具
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 色彩与对比度：可立即上手的实操手册

## 一句话总结
**现代产品色彩系统用 `oklch()` 替代 HSL/RGB 以获得感知均匀的色板，按 WCAG AA 4.5:1 / AAA 7:1 验证对比度，用"语义令牌"而非"颜色名"组织 token，暗色模式用 8% off-black + 调饱和（而非简单反转）**。

## 1. HSL vs RGB vs oklch：感知均匀才是现代标准

HSL 和 RGB 都不是为"人眼看起来一样"设计的。HSL 的 `lightness 50%` 在黄色和蓝色上看起来亮度差很多，HSL 的 `darken(10%)` 经常让蓝色变"脏"。**oklch 是 2024 起 W3C 推荐的现代色彩空间**（2023.5 起 Chrome/Firefox/Safari 全面支持，CSS 规范 Baseline Widely Available）。

oklch 三个通道独立且符合人眼：
- **L**（Lightness）：0~1，0 是纯黑，1 是纯白
- **C**（Chroma）：0~0.4（实际），饱和度
- **H**（Hue）：0~360，色相角

Tailwind v4 已把全部默认色板从 HSL 改为 oklch：
```css
--color-sky-500: oklch(68.5% 0.169 237.323);
--color-red-500: oklch(63.7% 0.237 25.331);
```

**实战对比**：
```css
/* HSL 调亮蓝色 - 经常变灰 */
hsl(220, 80%, 50%);  /* 蓝 */
hsl(220, 80%, 70%);  /* 看起来是淡紫灰 */

/* oklch 调亮蓝色 - 保持鲜艳 */
oklch(50% 0.2 250);  /* 蓝 */
oklch(70% 0.2 250);  /* 一致的亮蓝 */
```

**相对颜色语法**（2024 起，所有现代浏览器）：
```css
:root { --brand: oklch(60% 0.2 250); }
.btn:hover { background: oklch(from var(--brand) calc(l + 0.1) c h); }
```

## 2. WCAG 对比度算法

**WCAG 2.1 标准**（AA 为合规线，AAA 为推荐线）：
- 普通正文：AA 4.5:1 / AAA 7:1
- 大字（18pt+ 或 14pt+ bold）：AA 3:1 / AAA 4.5:1
- UI 组件 / 图标 / 边框：3:1（WCAG 1.4.11）

**对比度公式**（W3C 官方）：
1. 把 RGB 归一化到 0~1，除以 255
2. 转 sRGB 线性：若 ≤ 0.04045 则 `c/12.92`，否则 `((c+0.055)/1.055)^2.4`
3. 相对亮度：`L = 0.2126·R + 0.7152·G + 0.0722·B`
4. 对比度 = `(L1 + 0.05) / (L2 + 0.05)`，L1 较亮
5. 比值范围 1:1（白对白）到 21:1（黑对白）

**关键规则**：不要四舍五入——**4.499:1 仍不通过 4.5:1**。

**JavaScript 计算函数**（直接复制）：
```js
function srgbToLin(c) {
  c /= 255;
  return c <= 0.04045 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4);
}
function luminance(r,g,b) {
  return 0.2126*srgbToLin(r) + 0.7152*srgbToLin(g) + 0.0722*srgbToLin(b);
}
function contrast(rgb1, rgb2) {
  const L1 = luminance(...rgb1), L2 = luminance(...rgb2);
  const [hi, lo] = L1 > L2 ? [L1, L2] : [L2, L1];
  return (hi + 0.05) / (lo + 0.05);
}
// contrast([0,0,0],[255,255,255]) === 21
```

**状态色也要测**：hover / focus / active / disabled **独立**通过对比度，alpha 透明度会降低对比（背景透出），边框算前景。

**工具**：WebAIM Contrast Checker、Stark、Figma Contrast Checker、Chrome DevTools 强制颜色模式。

## 3. 灰阶系统：zinc / slate / neutral / gray 怎么选

Tailwind v4 提供 4 个中性色，每个 L 值都接近 0.55，但**色相角不同**：
- **slate**（hue ≈ 257）：冷调，略蓝（科技、金融）
- **gray**（hue ≈ 264）：最通用，略蓝灰
- **zinc**（hue ≈ 285）：最冷，略紫灰（GitHub/Linear 风格）
- **neutral**（hue = 0）：纯灰无调，最"安全"

**8-12 档灰阶 token**（推荐档位，复制即可）：
```css
:root {
  --gray-1:  oklch(99% 0 0);
  --gray-2:  oklch(98% 0 0);
  --gray-3:  oklch(95% 0.005 264);
  --gray-4:  oklch(92% 0.005 264);
  --gray-5:  oklch(85% 0.01 264);
  --gray-6:  oklch(70% 0.015 264);
  --gray-7:  oklch(55% 0.02 264);   /* 次要文字 AA 4.5+ 必过 */
  --gray-8:  oklch(40% 0.025 264);  /* 正文文字 */
  --gray-9:  oklch(25% 0.025 264);  /* 标题 */
  --gray-10: oklch(15% 0.02 264);   /* 最强文字 - 实测 #18181b */
  --gray-11: oklch(8%  0.01 264);   /* off-black 暗模式背景 */
}
```

**选中性色判断**：产品偏科技/数据 → zinc 或 slate；偏人文/编辑 → warm gray（hue ≈ 30-60）；**不要混用**（zinc 配 slate 看起来脏）。

**档案**（Linear / Vercel / GitHub Prime → zinc；Notion / Apple HIG → neutral；Stripe / Linear 旧版 → slate）。

## 4. 主色生成：1 个色 → 10 阶色板

现代色板不再是手调 50~950，而是**算法从 1 个种子色派生**。Tailwind v4 / Radix / shadcn / Material 3 都用这个思路。

**算法**：固定 hue 和 chroma，按 oklch 的 L 步长生成 11 阶：
```js
function generateScale(hue, chroma) {
  const steps = [95, 90, 80, 70, 60, 55, 50, 45, 40, 30, 20];
  return steps.map((L, i) => {
    const c = i < 4 ? chroma * 0.4 + i * 0.02 : chroma;
    return oklch(`${L}% ${c.toFixed(3)} ${hue}`);
  });
}
```

**Tailwind v4 风格 token**（直接用）：
```css
@theme {
  --color-brand-50:  oklch(97% 0.02  250);
  --color-brand-100: oklch(94% 0.04  250);
  --color-brand-200: oklch(88% 0.08  250);
  --color-brand-300: oklch(80% 0.12  250);
  --color-brand-400: oklch(72% 0.15  250);
  --color-brand-500: oklch(64% 0.18  250);  /* 主色 */
  --color-brand-600: oklch(56% 0.18  250);  /* hover */
  --color-brand-700: oklch(48% 0.16  250);  /* active */
  --color-brand-800: oklch(40% 0.13  250);
  --color-brand-900: oklch(32% 0.10  250);
  --color-brand-950: oklch(22% 0.06  250);
}
```

**色板逻辑一致性**：
- **Tailwind / shadcn**：500 是 brand base，600/700 用于按钮 hover/active
- **Radix**：1-12 步，gray 与 accent 共享 L 比例
- **Material 3**：tone 0-100 映射
- **iOS HIG**：anyAppearance 4 档

**对比度对照**：
- 50-200 → 背景、subtle hover
- 300-400 → 禁用 / 占位
- 500-600 → 按钮默认
- 700-800 → 文字链接 / active
- 900-950 → 标题 / 高对比文字

## 5. 语义颜色命名：不要叫 red/blue/green

**原则**：组件代码用语义 token，不用具体颜色。理由：换主题、暗色模式、品牌迁移只需改 token 映射，组件零修改。

**标准 8 类语义色**：

| Token | 用途 | 示例 |
|---|---|---|
| `primary` | 主色，CTA、关键链接 | "立即购买"按钮 |
| `secondary` | 次要操作 | "查看详情"按钮 |
| `accent` | 装饰、强调 | 标签、徽章 |
| `success` | 成功、完成 | "已支付" |
| `warning` | 警示、注意 | "库存不足" |
| `danger` | 错误、删除 | "确认删除" |
| `info` | 信息提示 | "新功能"提示 |
| `neutral` | 默认、次要 | 标签、辅助文字 |

**完整 token 结构**（shadcn/Radix 风格）：
```css
:root {
  --background: oklch(99% 0 0);
  --foreground: oklch(15% 0.01 264);
  --muted: oklch(96% 0.005 264);
  --muted-foreground: oklch(45% 0.01 264);
  --primary: oklch(50% 0.2 250);
  --primary-foreground: oklch(98% 0 0);
  --secondary: oklch(96% 0.01 264);
  --secondary-foreground: oklch(20% 0.01 264);
  --accent: oklch(96% 0.02 250);
  --accent-foreground: oklch(20% 0.05 250);
  --destructive: oklch(55% 0.22 25);
  --destructive-foreground: oklch(98% 0 0);
  --success: oklch(60% 0.15 145);
  --warning: oklch(75% 0.15 80);
  --border: oklch(90% 0.005 264);
  --input: oklch(90% 0.005 264);
  --ring: oklch(50% 0.2 250);
}
```

**强制规则**：
- 禁止组件用 `bg-red-500` 写死颜色，**必须用 `bg-destructive`**
- 每个语义色配 `*-foreground`（在主色上的文字色）
- GitHub Primer / Radix / shadcn / Linear / Vercel 都用这套语义命名

## 6. 暗色模式：不要反转，要重画

**陷阱一**：直接反转 HSL 的 L（`lightness: 100% - L`）会让色相"翻转"——蓝色变深黄、绿色变粉。
**陷阱二**：纯黑 `#000` 背景是错的。**纯黑 + 高对比文字 = 眼睛刺痛**（"halation"光晕），OLED 屏还会出"黑块感"。

**正确做法**（GitHub Primer / Linear / Vercel 标准）：
- 背景用 **off-black**：`oklch(8% 0 0)` ≈ `#0d1117`（GitHub）/ `#0a0a0a`（shadcn）
- 暗色模式**降低饱和度 10-20%**：`oklch(50% 0.2 250)` → `oklch(55% 0.15 250)`
- 暗色模式**反转 elevation 逻辑**：亮的更亮（card 浮起 = 颜色更亮）而非加阴影

**双向 token 定义**（复制即用）：
```css
:root {
  --bg: oklch(99% 0 0);
  --bg-elevated: oklch(100% 0 0);
  --text: oklch(15% 0.01 264);
  --text-muted: oklch(45% 0.01 264);
  --border: oklch(90% 0.005 264);
  --primary: oklch(50% 0.2 250);
  --primary-hover: oklch(45% 0.2 250);
  --success: oklch(55% 0.15 145);
  --danger: oklch(55% 0.22 25);
}
[data-theme="dark"] {
  --bg: oklch(8% 0 0);             /* off-black，不用 #000 */
  --bg-elevated: oklch(13% 0 0);
  --text: oklch(95% 0 0);
  --text-muted: oklch(65% 0.01 264);
  --border: oklch(22% 0.005 264);
  --primary: oklch(68% 0.16 250);   /* 提亮 + 降饱和 */
  --primary-hover: oklch(72% 0.16 250);
  --success: oklch(70% 0.15 145);
  --danger: oklch(65% 0.20 25);
}
```

**禁止**：
- ❌ `filter: invert(1)`（会反转图片、emoji）
- ❌ 暗色模式用 `bg-black` 配 `text-white`（对比度过高 21:1）
- ❌ 主色 HSL 反转（hue 漂移）
- ✅ 暗色模式目标对比度：正文 7:1+（用户已习惯亮环境，反向更宽容）

## 7. 状态颜色

| 状态 | 规则 | 数值 |
|---|---|---|
| `rest` | 默认 | base |
| `hover` | 提亮或加饱和 | L +5~10% / 透明度 8% |
| `active` | 压暗 | L -5~10% |
| `focus` | 显示 2px ring | ring = primary @ 50% alpha |
| `disabled` | 降低对比 + 去饱和 | 文字对比 4.5:1 是硬底线 |
| `selected` | 背景 tint + 边框强调 | primary @ 10% 背景 |
| `error` | 边框 + 文字双提示 | danger 色 + icon |

**CSS 完整状态实现**：
```css
.btn {
  background: var(--primary);
  color: var(--primary-foreground);
  transition: background 120ms;
}
.btn:hover { background: var(--primary-hover); }
.btn:active { background: var(--primary-active); }
.btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
.btn[aria-pressed="true"] {
  background: var(--primary-active);
  box-shadow: inset 0 0 0 1px var(--primary);
}
```

**不要用 opacity 处理 disabled**（会让所有颜色都失效）。改用 muted token：`color: var(--muted-foreground); background: var(--muted);`。

**WCAG 强制要求**：focus 环对比度 ≥ 3:1（WCAG 1.4.11）。禁用 `outline: none` 不补 ring 是合规失败。

## 8. 调色板工具：6 个工具的角色分工

| 工具 | 角色 | 输出 | 适合 |
|---|---|---|---|
| **uicolors.app** | Tailwind 色板生成器 | 50-950 token，可导入 config | 快速生成可用 Tailwind 色板 |
| **Realtime Colors** | 视觉化预览 + 实时切换 | CSS / Tailwind / shadcn / DaisyUI | 客户演示、新手快速起步 |
| **Coolors** | 随机色 + 调色板构建 | HEX 导出 | 灵感探索、品牌色起点 |
| **Huemint** | ML 生成品牌/插画/网站色 | 协调色板 | 品牌色、插画、渐变 |
| **Khroma** | AI 学习你的偏好 | 个性化推荐 | 设计师寻找灵感 |
| **Figma Variables** | 设计稿 token 化 | 直接同步代码 | 设计-工程协同 |
| **Stark** | 对比度 / 色盲模拟 | 检查器 | 验收 |

**工作流**：
1. **Coolors** 选 5 个候选色（用空格翻页）
2. **uicolors.app** 把候选主色变 50-950 阶梯
3. **Realtime Colors** 验证组件外观
4. **Stark** 测所有状态对比度
5. **Figma Variables** 同步给工程

## 15 个可复用代码片段

### 1. 8 阶 zinc 灰
```css
:root {
  --zinc-50:  oklch(98.5% 0 0);
  --zinc-100: oklch(96.7% 0.001 286.375);
  --zinc-200: oklch(92% 0.004 286.32);
  --zinc-300: oklch(87% 0.006 286.286);
  --zinc-400: oklch(70% 0.01 286.149);
  --zinc-500: oklch(55.2% 0.016 285.938);
  --zinc-600: oklch(44.2% 0.017 285.786);
  --zinc-700: oklch(37% 0.013 285.805);
  --zinc-800: oklch(27.4% 0.006 286.033);
  --zinc-900: oklch(21% 0.006 285.885);
  --zinc-950: oklch(14.1% 0.005 285.823);
}
```

### 2. 主色 10 阶（JS）
```js
function brand(h, c) {
  const map = {50:97,100:94,200:88,300:80,400:72,500:64,
               600:56,700:48,800:40,900:32,950:22};
  return Object.fromEntries(
    Object.entries(map).map(([k,L]) =>
      [k, `oklch(${L}% ${(c*0.6 + (L<70?L/300:c)).toFixed(3)} ${h})`])
  );
}
```

### 4. 暗色模式双向 token
```css
:root {
  --bg: oklch(99% 0 0);
  --bg-elevated: oklch(100% 0 0);
  --text: oklch(15% 0.01 264);
  --text-muted: oklch(45% 0.01 264);
  --border: oklch(90% 0.005 264);
  --primary: oklch(50% 0.2 250);
}
[data-theme="dark"] {
  --bg: oklch(8% 0 0);
  --bg-elevated: oklch(13% 0 0);
  --text: oklch(95% 0 0);
  --text-muted: oklch(65% 0.01 264);
  --border: oklch(22% 0.005 264);
  --primary: oklch(68% 0.16 250);
}
```

### 5. 状态色 token
```css
--state-hover:  oklch(from var(--primary) calc(l + 0.05) c h);
--state-active: oklch(from var(--primary) calc(l - 0.05) c h);
--state-disabled: oklch(from var(--primary) l 0 c);
```

### 6. 8% off-black 暗色背景
```css
--bg: oklch(8% 0 0);
--bg-elevated: oklch(13% 0 0);
--bg-overlay: oklch(16% 0 0);
```

### 7. Focus ring 3:1
```css
:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
--ring: oklch(from var(--primary) l c h / 100%);
```

### 8. 11 阶品牌色
```css
@theme {
  --color-brand-50:  oklch(97% 0.02  250);
  --color-brand-100: oklch(94% 0.04  250);
  --color-brand-200: oklch(88% 0.08  250);
  --color-brand-300: oklch(80% 0.12  250);
  --color-brand-400: oklch(72% 0.15  250);
  --color-brand-500: oklch(64% 0.18  250);
  --color-brand-600: oklch(56% 0.18  250);
  --color-brand-700: oklch(48% 0.16  250);
  --color-brand-800: oklch(40% 0.13  250);
  --color-brand-900: oklch(32% 0.10  250);
  --color-brand-950: oklch(22% 0.06  250);
}
```

### 9. 调饱和相对颜色（暗色模式自动适配）
```css
@media (prefers-color-scheme: dark) {
  --primary: oklch(from var(--primary) calc(l + 0.1) calc(c * 0.8) h);
}
```

### 10. 透明叠加 hover tint
```css
.btn { background: var(--primary); }
.btn:hover { background: oklch(from var(--primary) l c h / 92%); }
```

### 11. 错误状态双重提示
```css
.input[aria-invalid="true"] {
  border-color: var(--danger);
  --ring: var(--danger);
}
```

### 12. 暗色 elevation 规则
```css
--surface-1: oklch(8% 0 0);
--surface-2: oklch(11% 0 0);
--surface-3: oklch(14% 0 0);
--surface-4: oklch(17% 0 0);
```

### 13. 主色 hue 一致性
```css
--success: oklch(60% 0.15 145);
--warning: oklch(75% 0.15 80);
--danger:  oklch(55% 0.22 25);
--info:    oklch(60% 0.13 220);
```

### 14. OKLCH 渐变（感知平滑）
```css
background: linear-gradient(in oklch, oklch(50% 0.2 250), oklch(70% 0.2 50));
```

### 15. 14 token 速查
```css
--bg, --bg-elevated, --text, --text-muted,
--primary, --secondary, --accent, --success, --warning, --danger, --info, --muted,
--border, --ring
```

## 10 条"如果你在做色彩，记住这些"

1. **2024 起新项目用 `oklch()`**，不要新建 HSL 色板
2. **正文文字对比 ≥ 4.5:1**（AA），推荐 7:1（AAA），4.499:1 仍不通过
3. **暗色模式背景用 `oklch(8% 0 0)`** ≈ `#0d1117`，**不是** `#000`
4. **暗色模式降饱和 10-20%**（不要直接反转 L）
5. **状态色 5 态独立测对比度**：rest / hover / active / focus / disabled
6. **focus 环必须有且 ≥ 3:1**，禁止 `outline: none` 不补
7. **禁止用 `bg-red-500` 写死**，必须用 `bg-destructive` 语义 token
8. **灰阶选一个中性色**（zinc / slate / gray / neutral）走到底，不要混
9. **shadcn 风格 14 token** 覆盖 90% 场景
10. **暗色模式每个 token 都要重定义**，不要靠 `filter: invert(1)`

## 5 条反面教材（"看到 X 必改"）

1. **纯黑 `#000` + 纯白 `#fff`**：21:1 对比过度，文字会"晕开"。改：`oklch(99% 0 0)` + `oklch(15% 0.01 264)`，对比 ≈ 16:1 仍超 AAA
2. **`filter: invert(1)` 切暗色模式**：图片、emoji、logo 全反转
3. **HSL 反转做暗色**（`hsl(220, 80%, 50%)` → 反 L）：蓝色变深黄。改：调 C + 微调 L
4. **`opacity: 0.5` 做 disabled**：同时破坏文字对比度。改：用 muted token 替代
5. **组件写死 `bg-red-500`**：换品牌色要全文件搜。改：全部走 `bg-destructive`

## 5 条"如果你只能记一条"

1. `oklch(L C H)` 替代 HSL/RGB
2. 正文对比 ≥ 4.5:1，状态色独立测
3. 暗色模式 off-black `oklch(8% 0 0)` + 降饱和
4. 14 语义 token（bg / text / primary / secondary / accent / success / warning / danger / info / muted / border / ring / +foreground 变体）
5. 状态色 5 态：rest / hover / active / focus / disabled

## 资源 URL
- tailwindcss.com/docs/customizing-colors / uicolors.app / coolors.co / www.realtimecolors.com / huemint.com
- web.dev/articles/building/accessible-color-systems / contrast-and-color-choices / color-picker-for-accessibility
- developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch
- webaim.org/articles/contrast/ / www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
- atlassian.design/foundations/color-new / primer.style/foundations/color / m3.material.io/styles/color / polaris.shopify.com/foundations/colors
- en.wikipedia.org/wiki/Oklab_color_space
- smashingmagazine.com/2022/07/lch-color-space-css/ / 2023/07/oklch-color-space/ / 2021/06/css-color-functions/
- nngroup.com/articles/color-accessibility/ / dark-mode/
