---
name: design-typography-practice
description: 排版实操手册 - 字号 scale/行高/字距/行长/字体特性/可变字体/响应式 clamp/字体加载性能
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 排版实操手册

## 一句话总结
**排版是密度 50% 由字号/行高/行长决定、30% 由字距决定、20% 由字体特性决定的工程问题**。下面每条规则都来自 MDN、web.dev、Material 3、Primer、Bringhurst 的可执行结论，全部可复制粘贴。

## 1. 字号 Scale 系统：6 个比例该用哪个

字号 scale = 上一级 × ratio。以 1rem (16px) 为基准。

| 比例 | 名称 | 用在哪 |
|---|---|---|
| 1.125 (Minor Second) | 微调 | 文档型、密信息型 UI（Notion、Linear） |
| 1.2 (Minor Third) | 轻量 | 大部分 SaaS 后台 |
| 1.25 (Major Third) | **默认推荐** | Web 产品主力（Vercel、Stripe、GitHub） |
| 1.333 (Perfect Fourth) | 标准 | 营销页、文章站 |
| 1.5 (Perfect Fifth) | 强调 | 编辑出版、品牌站 |
| 1.618 (Golden) | 戏剧 | 杂志封面、Hero（不要全站用） |

**1.25 (Major Third) 是 80% 项目最优解**——h1 不会太大压死 hero，h6 又能保持可读性。1.618 在 Web 上属"过头"。

```css
/* CSS Variables - 1.25 scale @ 1rem */
:root {
  --text-xs:  0.64rem;   --text-sm:  0.8rem;
  --text-base:1rem;      --text-lg:  1.25rem;
  --text-xl:  1.563rem;  --text-2xl: 1.953rem;
  --text-3xl: 2.441rem;  --text-4xl: 3.052rem;
  --text-5xl: 3.815rem;
}
```

```js
// tailwind.config.js
fontSize: {
  'base': ['1rem',     { lineHeight: '1.6' }],
  'lg':   ['1.25rem',  { lineHeight: '1.5' }],
  'xl':   ['1.563rem', { lineHeight: '1.35' }],
  '2xl':  ['1.953rem', { lineHeight: '1.25' }],
  '3xl':  ['2.441rem', { lineHeight: '1.2' }],
  '4xl':  ['3.052rem', { lineHeight: '1.1' }],
}
```

**判断方法**：画 360px 宽卡片，6 个 h1 放进去——哪个既"看得见差异"又"不撑爆卡片"，用哪个。

## 2. 行高 (line-height)：永远 unitless

**MDN 明确建议 unitless（1.5）**——子元素按自己 font-size 重算；`1.5em` 继承父元素绝对值，嵌套后行高被压扁。

```css
body, p   { line-height: 1.6; }   /* 正文 (16px → 25.6px) */
h1, h2, h3{ line-height: 1.2; }   /* 标题 */
.btn      { line-height: 1; padding: 0.75rem 1.25rem; }
.ui-label { line-height: 1.3; }   /* UI 标签 */
```

**核心规则**：
- 字号越大 → 行高越小（24px 用 1.5，48px 用 1.2，96px 用 1.0）
- 行高 ≤ 1.2 需 `text-wrap: balance`（Chrome 114+）让标题不"撞尾"
- WCAG 2.2 要求 body ≥ 1.5

**避坑**：**绝对不要**写 `line-height: 24px`——子元素继承 24px 不管自己字号，标题行高会变 24/48 = 0.5。

## 3. 字距 (letter-spacing)：负给大字，正给小字和 caps

字距基于 em（不是 px）—— 随字号缩放。**MDN 关键发现：非零 letter-spacing 会禁用 OpenType 可选连字 (liga, clig)**——只在需要的字重/位置打开。

```css
.display-96{ letter-spacing: -0.04em; }   /* 96px+ hero */
.h1-48     { letter-spacing: -0.02em; }   /* 48px 标题 */
.h2-32     { letter-spacing: -0.015em; }  /* 32px 标题 */
.body      { letter-spacing: 0; }          /* 正文恒 0 */
.caps-sm   { letter-spacing: 0.05em; text-transform: uppercase; }
.caps-lg   { letter-spacing: 0.1em;  text-transform: uppercase; }
.small-caps{ font-feature-settings: 'smcp' 1, 'c2sc' 1; letter-spacing: 0.05em; }
```

**决策树**：
- 字号 ≥ 48px → 必加负字距（-0.02 到 -0.05em）
- 字号 = 16–32px → 0
- 字号 ≤ 12px → 可加 +0.01 到 +0.02em 提升可读性
- `text-transform: uppercase` → 必加 +0.05 到 +0.1em
- `small-caps` → 必加 +0.05em

**警告**：Inter/Helvetica 几何无衬线，负字距要"克制"——超过 -0.05em 字会"挤"。

## 4. 行长 (line-length / measure)：66ch 是黄金

Bringhurst《The Elements of Typographic Style》：**45–75 字符/行，理想 66**。低于 45 无法预读节奏，高于 75 视线回扫丢失。

```css
.prose-narrow { max-width: 45ch; }
.prose        { max-width: 65ch; }   /* 默认 */
.prose-wide   { max-width: 75ch; }
.container    { max-width: 80ch; }
```

`ch` 单位 = "0" 字符宽度，比 px 更稳。

**响应式微调**：
```css
.prose { max-width: clamp(45ch, 60%, 75ch); }
```

**新手最常犯**：把整页内容放进 `max-width: 100%`——桌面端一行 200 字符。**任何文本块都必须设 max-width**。

## 5. 字体特性 (font-feature-settings)：3 行 CSS 改 50% 体验

现代字体（Inter、IBM Plex、Source Sans）有几十种 OpenType 特性：

```css
:root {
  font-feature-settings: 'kern' 1, 'liga' 1, 'calt' 1, 'ss01' 1;
  font-variant-ligatures: common-ligatures contextual;
  font-variant-numeric: lining-nums proportional-nums;
}

.data, table, .price { font-variant-numeric: tabular-nums lining-nums; }
.code, .invoice, .serial { font-feature-settings: 'tnum' 1, 'zero' 1; }
.recipe { font-variant-numeric: diagonal-fractions; }
.rank, .badge { font-feature-settings: 'ordn' 1; }
```

**两条铁律**：
1. **`kern` 永远打开**——字距自动调整
2. **数字相关场景**（表格、价格、计时器、ID）**必开 `tnum`**——否则 111/111/111 三列对不齐

## 6. 可变字体：一个文件替代 12 个

**Monotype 实验**：48 个静态字体打包进一个 variable font，**文件大小减少 88%**。Inter、InterVariable、IBM Plex、Source Sans、Recoleta 全部支持。

```css
@font-face {
  font-family: 'InterVariable';
  src: url('/fonts/InterVariable.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-stretch: 75% 125%;
  font-style: normal;
  font-display: swap;
}

.light   { font-weight: 250; }   /* 之前不存在这个 weight */
.medium  { font-weight: 500; }
.heavy   { font-weight: 800; }
.condensed { font-stretch: 90%; }

.hero {
  font-size: 80px;
  font-variation-settings: 'opsz' 96, 'GRAD' 200;
  /* opsz 让大字用 display 切形，GRAD 调粗细不变宽 */
}

/* GRAD 实战：hover 不抖动地加粗 */
.btn { font-variation-settings: 'GRAD' 0; transition: all .2s; }
.btn:hover { font-variation-settings: 'GRAD' 150; }
/* 用 weight 会改 layout，用 GRAD 不会 */
```

**5 个注册轴**：
- `font-weight: 100-1000` → `wght`
- `font-stretch: 75%-125%` → `wdth`
- `font-style: oblique 14deg` → `slnt`
- `font-optical-sizing: auto` → `opsz`
- `font-variation-settings: 'GRAD' 88` → grade（自定义轴）

**降级**：
```css
@supports not (font-variation-settings: normal) {
  @font-face {
    font-family: 'Inter';
    src: url('/fonts/Inter-Regular.woff2') format('woff2');
  }
}
```

## 7. 响应式字号 (clamp)：2 行写好流式排版

`clamp(min, ideal, max)`——ideal 通常 `vw` 配合 rem。

```css
h1 { font-size: clamp(2rem, 1rem + 4vw, 4rem); }
/* 320px → 32px
   768px → 31.7px（理想）
   1440px → 58.6px
   1600px+ → 64px（封顶） */

p  { font-size: clamp(1rem, 0.9rem + 0.5vw, 1.125rem); }
h2 { font-size: clamp(1.5rem, 1rem + 2vw, 2.5rem); }
h3 { font-size: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
```

**5 步算出 clamp 值**：
1. 决定移动端 min
2. 决定桌面端 max（min 的 1.5–2 倍）
3. 算 `RATIO = (max - min) / (理想断点 - 320px) × 100`
4. 算 `BASE = min - RATIO × 320 / 100`
5. 套公式 `clamp(min, BASE + RATIO * vw, max)`

**WCAG 1.4.4 警告**：clamp max 可能阻碍浏览器缩放到 200%。**解决方法**——max ≤ 基准 2 倍。

## 8. 字体加载性能：4 个决定 CLS 的关键

**WOFF2 是唯一需要支持的格式**（Brotli 压缩比 WOFF 小 30%）。EOT/TTF/SVG 全可弃。

```html
<!-- 1. 提前握手 -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- 2. preload 关键字体 -->
<link rel="preload" href="/fonts/InterVariable.woff2"
      as="font" type="font/woff2" crossorigin>
```

```css
/* 3. font-display 决策：
   - body → swap（先 fallback，加载完切换）
   - 装饰 → optional（没缓存好直接 fallback）
   - 绝不用 block（FOIT 空白 3s）
*/
@font-face {
  font-family: 'InterVariable';
  src: url('/fonts/InterVariable.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
}

/* 4. 防 CLS：把 fallback 的 metrics 改到接近 web font */
@font-face {
  font-family: 'InterFallback';
  src: local('Arial');
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

body { font-family: 'InterVariable', 'InterFallback', sans-serif; }

/* 5. unicode-range subset（大幅减小文件）*/
@font-face {
  font-family: 'InterVariable';
  src: url('/fonts/InterVariable.woff2') format('woff2-variations');
  unicode-range: U+0000-00FF, U+2000-206F, U+4E00-9FFF;
  /* Latin + 标点 + CJK 基本区 */
}
```

## 可复用代码片段

### 5 套字号 scale
```css
/* A. 紧凑 (1.125) - 文档 */
--t1: 0.875rem; --t2: 1rem; --t3: 1.125rem; --t4: 1.266rem;
--t5: 1.424rem; --t6: 1.602rem; --t7: 1.802rem; --t8: 2.027rem;

/* B. 默认 (1.25) - 主力 */
--t1: 0.64rem; --t2: 0.8rem; --t3: 1rem; --t4: 1.25rem;
--t5: 1.563rem; --t6: 1.953rem; --t7: 2.441rem; --t8: 3.052rem;

/* C. 1.333 - 文章 */
--t1: 0.75rem; --t2: 1rem; --t3: 1.333rem; --t4: 1.777rem;
--t5: 2.369rem; --t6: 3.157rem; --t7: 4.209rem;

/* D. 1.5 - 品牌 */
--t1: 0.667rem; --t2: 1rem; --t3: 1.5rem; --t4: 2.25rem;
--t5: 3.375rem; --t6: 5.063rem;

/* E. 1.618 - Hero */
--t1: 0.618rem; --t2: 1rem; --t3: 1.618rem; --t4: 2.618rem;
--t5: 4.236rem; --t6: 6.854rem;
```

### 4 种场景行高
```css
body   { line-height: 1.6; }   /* 长文 */
h1-h6  { line-height: 1.2; }   /* 标题 */
.btn   { line-height: 1; padding: 0.75rem 1.25rem; }
.label { line-height: 1.3; }   /* UI */
```

### 3 种字距规则
```css
display   { letter-spacing: -0.03em; }
caps      { letter-spacing: 0.08em; text-transform: uppercase; }
small-caps{ letter-spacing: 0.05em; font-feature-settings: 'smcp' 1; }
```

### 行长 CSS
```css
.prose     { max-width: 65ch; margin-inline: auto; }
.prose p   { max-width: 65ch; }
.prose h2  { max-width: 30ch; }   /* 标题可以更短 */
```

### clamp 字号函数（5 套）
```css
h1 { font-size: clamp(2rem, 1rem + 4vw, 4rem); }
h2 { font-size: clamp(1.5rem, 1rem + 2vw, 2.5rem); }
h3 { font-size: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
body { font-size: clamp(1rem, 0.9rem + 0.4vw, 1.125rem); }
small { font-size: clamp(0.8rem, 0.7rem + 0.4vw, 0.875rem); }
```

### 字体特性最优组合
```css
:root {
  font-feature-settings: 'kern' 1, 'liga' 1, 'calt' 1;
  font-variant-ligatures: common-ligatures contextual;
  font-variant-numeric: lining-nums proportional-nums;
}
.num, table { font-variant-numeric: tabular-nums lining-nums; }
```

### font-display + preload 完整 link 标签
```html
<link rel="preconnect" href="https://your-cdn.com" crossorigin>
<link rel="preload" href="/fonts/InterVariable.woff2"
      as="font" type="font/woff2" crossorigin>
<style>
@font-face {
  font-family: 'InterVariable';
  src: url('/fonts/InterVariable.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
  unicode-range: U+0000-00FF;
}
</style>
```

## 10 条"如果你在做排版，记住这些"

1. **永远用 rem 写 font-size**——避免 em 嵌套复合
2. **永远用 unitless 写 line-height**——子元素按自己 font-size 重算
3. **body 行高 1.5–1.7**——低于 1.5 失访达，高于 1.8 文字"散"
4. **body 字号 1rem (16px)**——浏览器默认，WCAG 推荐基线
5. **正文 max-width: 65ch**——Bringhurst 黄金数字
6. **大字（≥48px）必加负字距**——默认 -0.02 到 -0.04em
7. **数字表格必开 tabular-nums**——三列数字对齐是基本功
8. **kern 永远开，liga 永远开**——开了没坏处
9. **font-display: swap**——body 文字永远不要 block
10. **WOFF2 是唯一格式**——EOT/TTF/WOFF 全可弃，文件小 30%

## 5 条反面教材

1. **"h1 用了 56px 但行高 1.5"** → 56px 用 1.05–1.1
2. **"正文容器 100% 宽"** → max-width: 65ch
3. **"button 写 line-height: 1.5em"** → line-height: 1 + padding 控高度
4. **"自定义字体的 letter-spacing: 1px"** → 改 em，px 不随字号缩
5. **"font-feature-settings: 'liga' 0"** → 默认都开，禁掉只让"fi"分家

## 5 条"如果你只能记一条"

1. **body = `font-size: 1rem; line-height: 1.6; max-width: 65ch;`**——80% 网页的正确答案
2. **行高跟着字号走**：24px→1.5，48px→1.2，96px→1.0
3. **字号用 rem，行高用 unitless，字距用 em**——三个"魔法单位"
4. **数字场景开 tabular-nums**——产品里 90% 的"歪"都是数字不等宽
5. **WOFF2 + font-display: swap + preload + 1 个 weight**——2026 字体加载标准答案

## 资源 URL
- rsms.me/inter/ / developer.mozilla.org/en-US/docs/Web/CSS/font-size / line-height / letter-spacing
- developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_fonts_guide
- web.dev/articles/font-best-practices / variable-fonts / clamp / font-display
- smashingmagazine.com/2011/10/16-pixels-body-copy-anything-isnt-ideal/ / 2023/03/css-fallback-fonts/
- smashingmagazine.com/2014/09/css-font-rendering/ / 2020/06/css-font-loading/
- typescale.com/ / m3.material.io/styles/typography/applying-type-scale / primer.style/foundations/typography
- en.wikipedia.org/wiki/Measure_(typography) / Robert_Bringhurst / The_Elements_of_Typographic_Style
