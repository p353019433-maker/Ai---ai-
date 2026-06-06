---
name: design-i18n-rtl
description: 国际化 / i18n / RTL / 多语言设计 - Unicode bidi 算法 / 8 个 RTL 反转点 / 字体回退栈 / 翻译工作流 / LTR↔RTL 测试 / 数字日期货币本地化 / Stripe Notion Linear 真实 RTL 模式 / 4 常见陷阱
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
  addedDate: 2026-06-06
---

# 国际化 / i18n / RTL 设计：执行手册

## 一句话总结
**国际化设计的核心不是"翻译"，是"让 UI 不知道该用哪种方向"**。做对的人 RTL 是 LTR 的镜像（左/右对调即可），内容自动双向排版；做错的人硬编码 `padding-left`、不测 RTL、忘记 emoji 在阿拉伯语里会从左到右渲染——结果阿拉伯用户看你的产品像 bug 一样。

## 1. 全球设计语言分布（2026）

| 语言族 | 占比 | 文字方向 | 代表语言 |
|---|---|---|---|
| **拉丁（LTR）** | 35% | 从左到右 | 英语、西班牙语、葡萄牙语、法语、德语 |
| **中文 / 日文 / 韩文（CJK）** | 25% | 从左到右 | 简体中文、繁体中文、日文、韩文 |
| **阿拉伯文（RTL）** | 4% | 从右到左 | 阿拉伯语、希伯来语、波斯语、乌尔都语 |
| **印度（部分 RTL）** | 5% | 多数 LTR | 印地语、泰米尔语、孟加拉语 |
| **其他 RTL** | <1% | 从右到左 | 库尔德语、意第绪语 |

**关键数字**：
- 阿拉伯国家人口 4.5 亿 + 伊朗 8800 万 + 以色列 950 万 = **5 亿+ RTL 用户**
- 阿拉伯国家 GDP 总和 2.5 万亿+ 美元
- 不做 RTL = 损失 5 亿用户 / 万亿市场
- **iOS / Android / Windows / macOS 全部原生支持 RTL**——> 不是技术难，是习惯问题

## 2. 8 个 RTL 反转点（设计师必查）

做 RTL 不是"全部反"——> 是这 8 个维度单独看：

### (1) 文本对齐
- LTR: `text-align: left`
- RTL: `text-align: right`
- **CSS 解决**：`text-align: start` / `text-align: end`（逻辑属性）

### (2) padding / margin
- LTR: `padding-left: 16px`
- RTL: `padding-right: 16px`
- **CSS 解决**：`padding-inline-start: 16px`（逻辑属性）
- **永远不用 `padding-left`**——> 用 `padding-inline-start`

### (3) border-radius
- LTR: `border-top-left-radius: 8px`
- RTL: `border-top-right-radius: 8px`
- **CSS 解决**：`border-start-start-radius: 8px`

### (4) 图标方向
- 不对称图标要镜像：箭头、面包屑、播放/暂停、列表缩进
- 对称图标不镜像：搜索、用户、设置、关闭
- **CSS 解决**：`transform: scaleX(-1)` 或 `<svg dir="auto">`

### (5) 数字
- **阿拉伯数字在阿拉伯文本里仍是 LTR 方向**（从左到右）
- 例：`123` 在阿拉伯语里是 `123`（不是 `321`），但整段文本 RTL
- **陷阱**：英文数字 + 阿拉伯单位（如 `د.إ. 123`）要测试

### (6) 日期 / 时间
- 美国：`MM/DD/YYYY`（12/05/2026 = 12 月 5 日）
- 欧洲：`DD/MM/YYYY`（05/12/2026 = 5 月 12 日）
- 中国：`YYYY-MM-DD`（2026-12-05）
- 阿拉伯：`DD/MM/YYYY`（多数）
- 希伯来：`DD.MM.YYYY` 或 `DD/MM/YYYY`
- **库**：用 `Intl.DateTimeFormat` 而非手写 format

### (7) 货币
- 美国：`$100.00`
- 欧洲：`100,00 €`（逗号小数、符号后置）
- 阿拉伯：`100.00 د.إ.`（符号后置）
- 印度：`₹1,00,000`（千位用 `,`，十万位用独立分隔）
- **库**：用 `Intl.NumberFormat`

### (8) Layout 方向
- LTR: 侧边栏在左 → 主内容在右
- RTL: 侧边栏在右 → 主内容在左
- **CSS 解决**：`dir="rtl"` 自动反转 flex 方向
- **永远不要 `flex-direction: row`**——> 用 `row`（自动跟 dir 走）

## 3. 5 个 CSS 逻辑属性（必学）

```css
/* ❌ 物理属性（硬编码方向） */
.element {
  margin-left: 16px;
  padding-right: 8px;
  border-top-left-radius: 4px;
  left: 0;
  text-align: left;
}

/* ✅ 逻辑属性（跟 dir 走） */
.element {
  margin-inline-start: 16px;  /* LTR: left, RTL: right */
  padding-inline-end: 8px;     /* LTR: right, RTL: left */
  border-start-start-radius: 4px;  /* LTR: top-left, RTL: top-right */
  inset-inline-start: 0;       /* LTR: left, RTL: right */
  text-align: start;           /* LTR: left, RTL: right */
}
```

**浏览器支持**：98%+（Chrome 89+ / Firefox 66+ / Safari 14.1+）

**4 个常见物理属性**：
- `margin-left` / `margin-right` → `margin-inline-start` / `margin-inline-end`
- `padding-left` / `padding-right` → `padding-inline-start` / `padding-inline-end`
- `border-top-left-radius` / `border-top-right-radius` → `border-start-start-radius` / `border-start-end-radius`
- `left` / `right` → `inset-inline-start` / `inset-inline-end`

## 4. 字体回退栈（多语言）

```css
/* 阿拉伯文优先 */
:root[lang="ar"] {
  --font-sans: 'IBM Plex Sans Arabic', 'Noto Sans Arabic', 'Tajawal', 
               'Cairo', system-ui, sans-serif;
  --font-display: 'Reem Kufi', 'Amiri', serif;
}

/* 希伯来文优先 */
:root[lang="he"] {
  --font-sans: 'Heebo', 'Noto Sans Hebrew', 'Assistant', 
               system-ui, sans-serif;
  --font-display: 'Frank Ruhl Libre', serif;
}

/* 中文优先 */
:root[lang="zh-CN"] {
  --font-sans: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 
               'Source Han Sans', system-ui, sans-serif;
}

/* 日文优先 */
:root[lang="ja"] {
  --font-sans: 'Hiragino Sans', 'Yu Gothic', 'Noto Sans JP', 
               system-ui, sans-serif;
}

/* 多语言混合（最高复杂度） */
:root[lang="ar"] .mixed-content {
  font-family: 'IBM Plex Sans Arabic', 'Inter', 
               'Noto Sans', 'Noto Sans Arabic', system-ui, sans-serif;
  unicode-bidi: plaintext;  /* 让浏览器自动决定每段方向 */
}
```

**学到的 4 个原则**：
1. 优先用本地设计字体（如 `IBM Plex Sans Arabic`）
2. fallback 到 Noto 系列（Google 维护，覆盖 150+ 语言）
3. 最后 fallback 到 `system-ui`（用系统字体，崩溃兜底）
4. **永远不用单字体覆盖所有语言**——> 中文字体显示阿拉伯文丑

## 5. 翻译工作流（3 步）

### Step 1: 抽出所有硬编码字符串
```ts
// ❌ 硬编码
<button>Submit</button>
<label>Email address</label>

// ✅ i18n key
<button>{t('form.submit')}</button>
<label>{t('form.email')}</label>
```

### Step 2: 准备翻译文件
```json
// locales/en.json
{
  "form": {
    "submit": "Submit",
    "email": "Email address"
  }
}

// locales/ar.json
{
  "form": {
    "submit": "إرسال",
    "email": "عنوان البريد الإلكتروني"
  }
}

// locales/zh-CN.json
{
  "form": {
    "submit": "提交",
    "email": "邮箱地址"
  }
}
```

### Step 3: 翻译者工作流
- **Lokalise / Crowdin / Phrase**（SaaS 平台）
- 翻译者用 Web UI 改 key，不动代码
- 自动 push 到仓库，触发 CI
- **质量门**：
  - 100% key 翻译完成
  - 关键术语一致（用 glossary）
  - 截图对比（机器翻译 / 真人翻译差异巨大）

**关键指标**：
- **翻译覆盖率** = 已翻译 key / 总 key
- **i18n 完整性** = 硬编码字符串数（越少越好，目标 0）
- **伪本地化测试** = 把英文改成 "ẞüßmîţ" 测试 UI 是否能容纳长字符串

## 6. 4 个常见陷阱

### 陷阱 1: 硬编码方向
```css
/* ❌ 失败 */
.arrow { margin-left: 8px; }

/* ✅ 解决 */
.arrow { margin-inline-start: 8px; }
```
**测试**：`dir="rtl"` 时这个 icon 应该自动到右边

### 陷阱 2: 不测 RTL
**症状**：开发完"看着对"，RTL 一塌糊涂
**修正**：
- Storybook 里加 `dir="rtl"` 切换
- Playwright 跑 RTL 截图对比
- CI 必跑 RTL 视觉回归

### 陷阱 3: 翻译后长度爆
**症状**：英文 "Submit" 翻译成德文 "Einreichen"（多 50% 长度），按钮崩
**修正**：
- `min-width` 或 `flex-shrink: 0` 防止按钮塌
- `text-overflow: ellipsis` 截断但保留可读
- 提前用伪本地化测试

### 陷阱 4: 数字方向错误
**症状**：阿拉伯文里嵌入英文数字，方向错乱
**修正**：
```html
<!-- 强制 LTR 数字段 -->
<span dir="ltr">123</span>
```

## 7. Stripe / Notion / Linear 真实 RTL 模式

### Stripe Dashboard
- **完全镜像**：左侧导航 → 右侧，主内容方向反
- **数字保持 LTR**：`$100.00` 在阿拉伯语里仍是 `$100.00`（不变成 `100.00 $`）
- **图标镜像**：左箭头 → 右箭头（`> → <`）

### Notion
- **块结构镜像**：嵌套列表缩进方向反
- **emoji 不镜像**：😊 在阿拉伯语里不变（emoji 设计为方向无关）
- **斜体 + RTL 复杂**：Notion 文档里经常出问题（用 `unicode-bidi: isolate`）

### Linear
- **极致信息密度 RTL**：
  - 表格列反：Actions | Status | Title | ID 变成 ID | Title | Status | Actions
  - 头像位置反：左侧 → 右侧
  - 工具栏：所有图标按 RTL 镜像
- **暗色模式 RTL 一致**：颜色、阴影保持，仅方向反

## 8. 翻译成本（4 档）

| 档 | 服务 | 成本 / 字 | 适用 |
|---|---|---|---|
| **机器翻译** | Google Translate / DeepL | $0 | 草稿 / 内部 |
| **众包** | Crowdin / Lokalise | $0.05-0.15 | 小项目 / 早期 |
| **专业翻译** | Gengo / TransPerfect | $0.15-0.30 | 商业 / 关键文案 |
| **本地化母语** | 自由译者 | $0.30-0.50 | 营销 / 法律 / 品牌 |

**铁律**：
- **机器翻译 + 母语校对** = 95% 商业项目最佳性价比
- **法律 / 医疗** = 必须母语
- **营销文案** = 必须母语 + 文化适配（不是翻译，是本地化）

## 9. 5 大本地化测试

### 测试 1: 镜像测试
把整页 `dir="rtl"`，看是否镜像正确。

### 测试 2: 长度测试
伪本地化（pseudo-localization）：把所有字符串改成 `[[[Tëšt ïñpût]]]`（比原文长 30-50%），看 UI 撑不撑得住。

### 测试 3: 数字 / 日期测试
```html
<p>Today is 12/05/2026 and price is $1,000.50</p>
<!-- 在阿拉伯语里：今天是 12/05/2026，价格是 $1,000.50 -->
<!-- 数字仍 LTR，但整段 RTL -->
```

### 测试 4: 双向文本测试
阿拉伯文 + 英文混排（最常见 bug 源）：
```html
<p>مرحبا Hello world</p>
<!-- 期望：两段都正确 -->
```

### 测试 5: 截断测试
长语言（德文、俄文）UI 是否截断 / 换行正确。

## 10. 5 个 i18n 库对比

| 库 | 框架 | 体积 | 性能 | 易用性 |
|---|---|---|---|---|
| **react-i18next** | React | 18KB | 快 | ★★★★★ |
| **next-intl** | Next.js | 5KB | 极快 | ★★★★ |
| **react-intl** | React | 35KB | 中 | ★★★ |
| **vue-i18n** | Vue | 15KB | 快 | ★★★★★ |
| **svelte-i18n** | Svelte | 5KB | 极快 | ★★★★ |

**选择**：
- Next.js 项目 → **next-intl**（轻量 + App Router 原生）
- React 其他 → **react-i18next**（生态最完整）
- Vue → **vue-i18n**
- Svelte → **svelte-i18n**

## 11. 8 个 SwiftUI / React 反例（看到 X 必改）

1. **硬编码 `padding-left`**——> 用 `padding-inline-start`
2. **图标不镜像**——> 箭头、面包屑必须镜像
3. **不测 RTL**——> CI 必跑 RTL 视觉回归
4. **不写 `dir="ltr"` 保护数字**——> 数字在 RTL 段里仍 LTR
5. **单字体覆盖所有语言**——> 中文渲染阿拉伯文崩溃
6. **不测长度**——> 德文/俄文 30-50% 长于英文，UI 必崩
7. **手写日期格式**——> 用 `Intl.DateTimeFormat`
8. **emoji 镜像**——> emoji 设计为方向无关，不要 `transform: scaleX(-1)`

## 12. 10 条"如果你在做国际化设计，记住这些"

1. **`dir="rtl"` 一个属性，全页反转**——> 但只对 8 个维度有效
2. **用逻辑属性不用物理属性**——> `padding-inline-start` 不用 `padding-left`
3. **图标分两类**——> 不对称镜像、对称不镜像
4. **数字保持 LTR**——> 即使在 RTL 段里也用 `dir="ltr"`
5. **字体按语言切**——> 不要一字体覆盖
6. **CI 必跑 RTL 视觉回归**——> 不然阿拉伯用户看 bug
7. **伪本地化测试**——> 提前发现长度问题
8. **机器翻译 + 母语校对**——> 95% 商业项目最佳
9. **用 `Intl.DateTimeFormat` / `Intl.NumberFormat`**——> 不要手写
10. **本地化 ≠ 翻译**——> 营销 / 法律 / 文化适配

## 5 条反面教材

1. **Twitter 2014 RTL 切换**：整整花 6 个月重构，因为硬编码 `padding-left`
2. **Apple.com 早期阿拉伯文版**：很多布局还是 LTR
3. **WhatsApp Web**：RTL 段里数字不强制 LTR，混排乱
4. **银行 App**：日期格式不本地化（美国格式硬塞给欧洲用户）
5. **电商网站**：价格符号不本地化（`$100.00` 给欧洲用户看，逗号不对）

## 5 条"如果你只能记一条"

1. **i18n 不是翻译，是让 UI 不知道该用哪种方向**——> `dir="rtl"` + 逻辑属性
2. **8 个 RTL 反转点**——> 文本 / padding / border-radius / 图标 / 数字 / 日期 / 货币 / layout
3. **数字保持 LTR**——> `dir="ltr"` 保护数字段
4. **用 Intl API**——> `Intl.DateTimeFormat` / `Intl.NumberFormat` / `Intl.Collator`
5. **CI 必跑 RTL 视觉回归**——> 不然永远是 bug

## 资源 URL
- w3.org/International/articles/rtl-stylesheets/ — W3C RTL 样式指南
- material.io/design/communication/writing.html — Material i18n
- developer.apple.com/design/human-interface-guidelines/right-to-left — Apple HIG RTL
- developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties — MDN 逻辑属性
- developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl — Intl API
- lokalise.com / crowdin.com / phrase.com — 翻译平台
- notistack.com / react.i18next.com / kazupon.github.io/vue-i18n — 库文档
- r12a.github.io/scripts/tutorial — Unicode bidi 算法教程
- unicode.org/reports/tr9/ — Unicode BiDi 算法规范
- caniuse.com/css-logical — 浏览器支持
- smashingmagazine.com/2020/09/internationalization-design/ — 实战指南
- web.dev/i18n-css-logical-properties/ — 逻辑属性

## 跨引用
- [design-typography-practice.md](design-typography-practice.md) — 字体加载 + 多语言
- [design-color-contrast.md](design-color-contrast.md) — 跨文化色彩
- [design-philosophy-color-perception.md](design-philosophy-color-perception.md) — 色彩跨文化
- [design-component-patterns.md](design-component-patterns.md) — 组件 props 设计
- [design-system-build.md](design-system-build.md) — 设计系统 token + 多语言
- [design-handoff.md](design-handoff.md) — Figma → 代码 + 多语言
- [design-ai-workflow.md](design-ai-workflow.md) — AI 翻译工具
