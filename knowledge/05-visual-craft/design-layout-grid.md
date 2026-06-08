---
name: design-layout-grid
description: 布局与栅格实操 - 8pt 节奏/12 列栅格/CSS Grid+Flexbox/container queries/响应式断点/clamp 流式排版
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 布局与栅格（产品级实操手册）

## 一句话总结
**用 8pt 节奏控制尺寸、用 12 列栅格控制水平、用 CSS Grid 搭二维结构、用 Flexbox 处理一维流、用 container query 处理组件内自适应、用 5 个断点做视图切换、用 clamp() 做流式排版——这七件事做好，80% 的布局问题消失**。

## 一、8pt 栅格系统

**为什么是 8 而不是 4 或 12？**
- 4 太碎：1/2/3/4 像素在 1x/2x/3x DPR 下都不够清晰边缘
- 12 太疏：间距粒度太大，组件内部无法做微调
- **8 是甜点**：2/4/8/16/24/32/40/48/64/80 覆盖 95% 场景，在 2x/3x 屏都是整数像素

**强制规则**：
- 任何 `padding`、`margin`、`gap`、`width`、`height`、`border-radius` 必须是 4 或 8 的倍数
- 4 用于密集组件内（按钮内边距、icon 间距），8 用于模块间
- 例外：1px 边框、2px 焦点环、`0.5px` 分割线

**CSS 变量模板**（复制即用）：
```css
:root {
  --space-1: 4px;   --space-2: 8px;   --space-3: 12px;
  --space-4: 16px;  --space-5: 24px;  --space-6: 32px;
  --space-7: 48px;  --space-8: 64px;  --space-9: 96px;
  --radius-sm: 4px; --radius-md: 8px; --radius-lg: 16px;
  --size-icon-sm: 16px; --size-icon-md: 24px; --size-icon-lg: 32px;
}
```

## 二、12 列 vs 16 列栅格

- **12 列是默认**：12 有 6 个因数（1/2/3/4/6/12），可拆出 6+6、4+8、3+9、4+4+4 等所有常用组合
- **16 列用于密集仪表盘**：Atlassian、IBM Carbon 用 16 列，组件更小更精密

**选择规则**：
- 营销页/文章/落地页 → **12 列**
- 仪表盘/SaaS 后台/数据密集界面 → **16 列或 12 列细分**（每列占 1/12）

**Bootstrap 5.3 12 列参数**：
| 断点 | 类前缀 | 容器 max-width | gutter |
|---|---|---|---|
| xs | `.col-` | 100% | 1.5rem |
| sm | `.col-sm-` | 540px | 1.5rem |
| md | `.col-md-` | 720px | 1.5rem |
| lg | `.col-lg-` | 960px | 1.5rem |
| xl | `.col-xl-` | 1140px | 1.5rem |
| xxl | `.col-xxl-` | 1320px | 1.5rem |

## 三、CSS Grid 实战

**核心三件套**：`grid-template-columns`、`grid-template-areas`、`grid-auto-flow`。

**12 列响应式模板**：
```css
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
  padding-inline: var(--space-4);
}
.span-6 { grid-column: span 6; }
.span-4 { grid-column: span 4; }
.span-3 { grid-column: span 3; }

@media (max-width: 768px) {
  .grid-12 { grid-template-columns: 1fr; }
  [class*="span-"] { grid-column: 1 / -1; }
}
```

**命名区域**（适合布局固定的页面）：
```css
.page {
  display: grid;
  grid-template-areas:
    "header header header"
    "side   main   main"
    "footer footer footer";
  grid-template-columns: 240px 1fr 1fr;
  gap: var(--space-4);
  min-height: 100vh;
}
.page > header { grid-area: header; }
.page > aside  { grid-area: side; }
.page > main   { grid-area: main; }
.page > footer { grid-area: footer; }
```

**`auto-fit` + `minmax` 是无媒体查询的自适应**：
```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-4);
}
```

**`dense` 自动填坑**：
```css
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-flow: dense;
  gap: var(--space-4);
}
```
警告：dense 会让 tab 顺序乱，**慎用于有阅读顺序的内容**。

## 四、Flexbox 实战

**6 个核心属性**：`display: flex`、`flex-direction`、`flex-wrap`、`justify-content`、`align-items`、`gap`。

**垂直居中（最常用）**：
```css
.center { display: flex; align-items: center; justify-content: center; }
```

**Sticky footer**（页脚永远在底）：
```css
body { display: flex; flex-direction: column; min-height: 100vh; }
main { flex: 1; }
```

**等宽卡片**（一行 N 张，N 自动算）：
```css
.row { display: flex; flex-wrap: wrap; gap: var(--space-4); }
.row > * { flex: 1 1 280px; }  /* 最小 280px，剩余均分 */
```

**导航平均分布**：
```css
.nav { display: flex; justify-content: space-between; gap: var(--space-4); }
```

**关键经验**：**Grid 用于"页面骨架 + 卡片阵列"，Flex 用于"组件内部排列 + 一行分布"**。两者混用而不是二选一。

## 五、Container Queries（2023 稳定）

**为什么需要**：媒体查询跟着视口走，组件在不同视口位置应有不同表现——**只有 container query 解决这个**。

**最小可用模板**：
```css
.card { container-type: inline-size; }

.card .title { font-size: 1rem; }
.card .meta  { display: none; }

@container (min-width: 400px) {
  .card { display: grid; grid-template-columns: 120px 1fr; gap: 16px; }
  .card .title { font-size: 1.25rem; }
  .card .meta  { display: block; }
}
```

**容器查询单位**（cqw/cqi）：1% 容器宽度。
```css
.card .title { font-size: clamp(1rem, 5cqi, 1.75rem); }
```

**命名容器**（避免嵌套冲突）：
```css
.sidebar { container: sidebar / inline-size; }
@container sidebar (min-width: 600px) { .item { flex-direction: row; } }
```

**降级方案**（无 container query 支持）：
```css
.card { display: grid; grid-template-columns: 1fr; }
@supports (container-type: inline-size) {
  .card { container-type: inline-size; }
  @container (min-width: 400px) { .card { grid-template-columns: 1fr 2fr; } }
}
```

## 六、响应式断点（移动优先）

**Tailwind 默认断点**（行业事实标准）：
| 前缀 | 像素 | rem |
|---|---|---|
| (base) | 0 | 0 |
| sm | 640px | 40rem |
| md | 768px | 48rem |
| lg | 1024px | 64rem |
| xl | 1280px | 80rem |
| 2xl | 1536px | 96rem |

**Bootstrap 5.3 断点**（次常用）：576 / 768 / 992 / 1200 / 1400px

**移动优先写法**：
```css
/* 默认：手机样式 */
.card { flex-direction: column; }

/* 平板及以上：水平排列 */
@media (min-width: 768px) {
  .card { flex-direction: row; }
}
```

**永远不要写 `max-width` 媒体查询**（除了要排除某个范围的少见场景）。原因：`max-width` 难以扩展，`min-width` 增量叠加。

**3 个断点 vs 5 个断点**：
- 个人项目/简单落地页：3 个（768 / 1024 / 1280）
- 商业产品：5 个（640 / 768 / 1024 / 1280 / 1536）
- **别超过 5 个**：每多一个断点，维护成本翻倍

## 七、`clamp()` 流式排版

**核心公式**：`clamp(最小, 视口相关, 最大)`

**容器宽度**：
```css
.container { width: clamp(320px, 90vw, 1200px); margin-inline: auto; }
```

**标题字号**：
```css
h1 { font-size: clamp(1.75rem, 4vw + 0.5rem, 3.5rem); }
```

**流体 padding**：
```css
.section { padding: clamp(2rem, 6vw, 6rem) clamp(1rem, 4vw, 3rem); }
```

**无障碍检查**：`max ≥ 2 × min`（保证 200% 缩放可用）。

## 八、五种页面的实际栅格

**Landing Page**：
```css
.landing { max-width: 1200px; margin-inline: auto; padding: clamp(2rem, 5vw, 5rem) 1rem; }
.hero { display: grid; grid-template-columns: 1fr; gap: 2rem; }
@media (min-width: 768px) { .hero { grid-template-columns: 1fr 1fr; } }
```

**Dashboard**：
```css
.dash { display: grid; grid-template-columns: 240px 1fr; min-height: 100vh; }
@media (max-width: 768px) { .dash { grid-template-columns: 1fr; } }
.metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; }
```

**Article**：
```css
.article { max-width: 65ch; margin-inline: auto; padding: 2rem 1rem; line-height: 1.7; }
```

**Settings**：
```css
.settings { max-width: 720px; margin-inline: auto; display: grid; gap: 1.5rem; }
@media (min-width: 768px) { .settings { grid-template-columns: 200px 1fr; } }
```

**404**：
```css
.error { min-height: 100vh; display: grid; place-items: center; padding: 2rem; text-align: center; }
```

## 10 条做布局时记住的

1. **8pt 节奏比"看着差不多"重要**：4/8/16/24/32/48 出现得越频繁，整页越稳
2. **12 列是默认，16 列是仪表盘专属**
3. **Grid 管二维、Flex 管一维**——别用 Flex 模拟 12 列
4. **永远移动优先**：用 `min-width` 而非 `max-width`
5. **5 个断点是上限，3 个断点更省心**
6. **`auto-fit` + `minmax(280px, 1fr)`** 一行解决卡片自适应
7. **container query 用于组件内**（卡片、表单字段），媒体查询用于页面级
8. **`gap` 比 `margin` 干净**——永远优先用 `gap`
9. **`clamp()` 替代固定字号和固定宽度**——减少 50% 的媒体查询
10. **容器 max-width 永远 ≤ 1280px**（1200px / 1024px 更安全），超过就开始难读

## 5 条反面教材（看到必改）

1. **看到 `margin-left: 13px` / `padding: 17px`**：不是 4 的倍数，立即改成 12/16/20/24
2. **看到 `@media (max-width: 768px)`**：改写成 `min-width` 移动优先
3. **看到嵌套 4 层 `div` 只为左右布局**：直接用 `display: grid; grid-template-columns: 200px 1fr;`
4. **看到用 Flexbox 模拟网格**（多行 `flex-wrap` + 复杂 `flex-basis`）：换成 `grid-template-columns: repeat(N, 1fr)`
5. **看到 `width: 100%` 直接写到卡片上**：用 `max-width: 1280px; width: calc(100% - 2rem);` 留呼吸空间

## 5 条"如果你只能记一条"

1. **8pt + 12 列 + 移动优先**——这三件事做好，所有布局都不会塌
2. **Grid 搭骨架，Flex 处理流**——不要混
3. **`gap` 替代 `margin` 永远更安全**——子元素之间不会再叠加
4. **`clamp(min, vw, max)` 替代固定值**——少写一半媒体查询
5. **container query 解决"同一个组件在视口不同位置表现不同"**——这是 2023 之后的产品级默认值

## 资源 URL
- css-tricks.com/snippets/css/complete-guide-grid/ / css-tricks.com/snippets/css/a-guide-to-flexbox/
- developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout / CSS_flexible_box_layout / CSS_container_queries
- developer.chrome.com/docs/css-ui/scroll-driven-animations
- web.dev/articles/animations-guide / animating-css-properties / layout-shifts / responsive-web-design-basics
- tailwindcss.com/docs/container / responsive-design / grid-template-columns
- getbootstrap.com/docs/5.3/layout/grid/ / breakpoints/
- atlassian.design/foundations/grid / m3.material.io/foundations/layout/applying-layout
- primer.style/foundations/layout
- smashingmagazine.com/css-grid-definite-indefinite/ / grid-level-2-subgrid/ / css-grid-meet-vertical-rhythm/
- smashingmagazine.com/responsive-design-with-css-containers-and-media-queries/ / approaches-to-container-based-and-element-based-queries/
