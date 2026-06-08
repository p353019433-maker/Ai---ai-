---
name: design-accessibility
description: 可访问性深度 - WCAG 2.2 9 条新规 / ARIA 完整 / 键盘导航 / 屏幕阅读器实战 / 表单 a11y / axe-core CI
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 可访问性深度（a11y Engineering Manual）

## 一句话总结
**WCAG 2.2 已是 W3C Recommendation（2023-10-05），9 条新规 + 4 原则（POUR）+ 3 等级（A/AA/AAA）；a11y 是工程问题，必须用 ARIA、键盘焦点、屏幕阅读器实测验证**。

## 1. WCAG 2.2 核心框架

WCAG 2.2 在 2023 年 10 月正式成为 W3C Recommendation。2.0→2.1→2.2 是累积关系（向后兼容），不替代。

**4 原则 POUR**：Perceivable（信息可被感知）/ Operable（界面可操作）/ Understandable（信息可理解）/ Robust（兼容辅助技术）。

**3 等级 A / AA / AAA**：
- A 解决最严重障碍
- AA 是法律和商业事实标准（Section 508、欧洲 EAA 2025、美国 ADA 诉讼引用）
- AAA 不是为整站设计，是为高优先级内容

**关键 SC 结构**：4 原则 → 13 条 Guideline（1.1~4.1）→ 80+ Success Criteria

| Principle | Guideline 范围 | 关键 SC（AA） |
|---|---|---|
| Perceivable | 1.1~1.4 | 1.4.3 Contrast 4.5:1 / 1.4.11 Non-text Contrast 3:1 |
| Operable | 2.1~2.5 | 2.1.1 Keyboard / 2.4.7 Focus Visible / 2.5.8 Target Size 24×24 |
| Understandable | 3.1~3.3 | 3.3.1 Error ID / 3.3.3 Error Suggestion |
| Robust | 4.1 | 4.1.2 Name Role Value |

**目标**：产品对齐 AA，按钮/链接/表单控件全部满足；AAA 仅对关键任务（认证、付款）做局部提升。

## 2. WCAG 2.2 九条新规详解

| SC | 名称 | 等级 | 含义 |
|---|---|---|---|
| 2.4.11 | Focus Not Obscured (Min) | AA | 焦点元素至少部分可见，不能被 sticky header/cookie 横幅完全遮住 |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | 焦点元素完全可见 |
| 2.4.13 | Focus Appearance | AAA | 焦点指示器面积 ≥ 2px CSS 边界 + 对比度 ≥ 3:1 |
| 2.5.7 | Dragging Movements | AA | 拖拽操作必须有单指替代方案（点击/键盘） |
| 2.5.8 | Target Size (Minimum) | AA | 点击目标 ≥ 24×24 CSS 像素（间距豁免） |
| 3.2.6 | Consistent Help | A | 帮助入口（contact/FAQ/chat）在多页位置一致 |
| 3.3.7 | Redundant Entry | A | 同一流程不重复输入已提供信息 |
| 3.3.8 | Accessible Authentication (Min) | AA | 不能强制记忆/抄写/拼图；支持密码管理器、passkey、邮件链接 |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | 不能用图片识别/对象识别做唯一认证 |

**实操**：
- 2.5.7 拖拽替代 → 拖拽排序的列表必须再提供"上移/下移"按钮
- 2.5.8 24×24 → Tailwind 的 `h-6 w-6`（24px）刚好达标
- 3.3.8 → 登录页别再加 CAPTCHA 二次校验

## 3. ARIA 完整指南

**第一原则**：**能用语义 HTML 就不用 ARIA**。`<button>` 比 `<div role="button">` 强 100 倍。

| 属性 | 用途 | 取值 | 关键陷阱 |
|---|---|---|---|
| `role` | 显式声明元素角色 | dialog / alert / status / menu / tab / tooltip | 不要给 `<nav>` 加 `role="navigation"`（冗余） |
| `aria-label` | 覆盖或提供无障碍名 | 字符串 | 视觉不可见，会被读出；别重复显示文本 |
| `aria-labelledby` | 引用其他元素 id 作为名字 | id 列表 | 优先于 aria-label（多语言/可读） |
| `aria-describedby` | 引用描述/帮助/错误文本 | id 列表 | 比 label 朗读晚，常用于 hint |
| `aria-hidden` | 对 AT 隐藏（视觉可见） | true/false | 不可用于聚焦元素；不要挂在 `<html>` 上 |
| `aria-expanded` | 折叠状态 | true/false/undefined | 必须联动实际 DOM 状态 |
| `aria-current` | 当前项 | page/step/location/date/time/true | **tab 用 aria-selected，不要用 aria-current** |
| `aria-live` | 动态内容广播 | off/polite/assertive | polite 不打断，assertive 立即读 |
| `aria-atomic` | 整区域还是子节点广播 | true/false | 配合 aria-live 用 |
| `aria-controls` | 引用被控元素 | id 列表 | 折叠/手风琴常用 |
| `aria-haspopup` | 触发弹层类型 | true/menu/listbox/dialog/tree/grid | 别再写 `aria-haspopup="true"` 而不区分 |
| `aria-invalid` | 校验失败 | true/false/grammar/spelling | 必须配合 aria-describedby 指向错误说明 |
| `aria-required` | 必填 | true/false | 配合 native `required` 一起用 |

## 4. 键盘导航

**键位分配（必须记住）**：

| 按键 | 作用 |
|---|---|
| Tab / Shift+Tab | 下一/上一可聚焦元素 |
| Enter | 激活链接、按钮、menuitem |
| Space | 激活按钮、勾选 checkbox、翻页 |
| Arrow Keys | 单选/菜单/tab/列表项内导航 |
| Escape | 关闭 dialog/popover/menu，回到触发元素 |
| Home / End | 跳到首/末项 |
| Page Up / Page Down | 翻页/列表滚动 |

**Skip Link 完整代码**（必放）：
```html
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header>...</header>
  <main id="main" tabindex="-1">...</main>
</body>

<style>
.skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
  background: #000;
  color: #fff;
  padding: 8px 16px;
  z-index: 999;
}
.skip-link:focus { left: 8px; top: 8px; }
</style>
```

`tabindex="-1"` 关键：让 `<main>` 接受程序化焦点（按 skip link 后落地），但不进入 Tab 序列。

**focus-visible CSS（推荐写法）**：
```css
button:focus { outline: none; }
button:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
  border-radius: 4px;
}
```

`:focus-visible` 浏览器支持自 2022-03 起 BaseLine 全部 OK。`outline-offset` 让 ring 不贴边。

## 5. 焦点管理（Modal / popover / Drawer）

**核心三步**：
1. 打开前记录 `document.activeElement`
2. 打开时把焦点移到容器
3. 关闭时还原焦点
4. 中间加 Tab 循环 trap

**Modal 完整代码**（用原生 `<dialog>`）：
```html
<button id="open">Open modal</button>

<dialog id="dlg" aria-labelledby="t">
  <h2 id="t">Confirm delete</h2>
  <p>This cannot be undone.</p>
  <button id="cancel">Cancel</button>
  <button id="ok">Delete</button>
</dialog>

<script>
const dlg = document.getElementById('dlg');
const open = document.getElementById('open');
let lastFocus;

open.onclick = () => {
  lastFocus = document.activeElement;
  dlg.showModal();
  dlg.querySelector('#cancel').focus();
};

dlg.addEventListener('close', () => {
  lastFocus?.focus();
});

dlg.addEventListener('keydown', e => {
  if (e.key === 'Escape') dlg.close();
  if (e.key === 'Tab') {
    const f = [...dlg.querySelectorAll(
      'a,button,input,textarea,select,[tabindex]:not([tabindex="-1"])'
    )];
    const first = f[0], last = f.at(-1);
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault(); last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault(); first.focus();
    }
  }
});
</script>
```

**注意**：原生 `<dialog>` + `showModal()` 已自动实现 `inert` 背景、`aria-modal`、`Esc` 关闭，**比手写 div 强**。优先用它；非用 div 不可时加 `inert` 属性到背景：
```js
document.querySelectorAll('main, header, footer')
  .forEach(el => el.inert = true);
```

## 6. 屏幕阅读器实战

**市场份额（2024）**：NVDA（Windows 免费 ~40%）/ JAWS（Windows 商业 ~30%）/ VoiceOver（macOS/iOS 内置 ~20%）/ TalkBack（Android 内置）/ Narrator（Windows 内置）

**测试 4 件套**：

| 平台 | 屏幕阅读器 + 浏览器 |
|---|---|
| Windows | NVDA + Firefox（最准）/ JAWS + Chrome |
| macOS | VoiceOver + Safari（Cmd+F5 启动） |
| iOS | VoiceOver + Safari（设置→辅助→VoiceOver） |
| Android | TalkBack + Chrome（设置→辅助→TalkBack） |
| 任何 | ChromeVox（Chrome 扩展，最快上手） |

**NVDA 必会快捷键**（搭配 Firefox）：
- `H` / `Shift+H` 跳下/上一标题
- `K` 跳链接
- `F` 跳表单字段
- `D` 跳 landmark（`<header>/<nav>/<main>/<footer>`）
- `T` 跳表格
- `1` `2` `3` 跳 1/2/3 级标题
- `NVDA+F7` 打开元素列表
- `NVDA+Space` 切换 Browse/Focus 模式
- `Insert+F7` 列出全部快捷键

**VoiceOver 必会快捷键**（搭配 Safari）：
- `VO+U` 打开 Rotor（headings/links/landmarks/forms 全览）
- `VO+→/←` 读下/上一项
- `VO+Shift+↓` 进入元素；`VO+Shift+↑` 跳出
- `VO+Space` 激活
- `VO+Cmd+H` 跳下一标题

**测试 Checklist**：开屏幕阅读器后只听不摸——
1. 是否有 skip link 提示？
2. H 跳转顺序是否合理？
3. 表单字段是否报"edit text, required, blank"？
4. 按钮是否说"button"？
5. 图标是否被读成"graphic"还是被 aria-label 替换？

## 7. 对比度与色盲

**WCAG 对比度公式**：
1. sRGB→线性化（≤0.03928 → /12.92；否则 ((c+0.055)/1.055)^2.4）
2. L = 0.2126·R + 0.7152·G + 0.0722·B
3. (L1+0.05)/(L2+0.05) ≥ 4.5（AA 文本）/ 3（AA 大字 18pt+ 或 14pt+ bold）/ 3（非文本 UI/焦点指示）

**不准四舍五入**：4.47:1 < 4.5:1 不通过。

**色盲类型**（影响 ~8% 男性）：红绿色盲（deuteranopia/protanopia）最常见，全色盲 0.003%。

**色盲对策**：
- 不只用颜色区分：加图标/文字/下划线
- 错误状态用红色 + 图标 ❌ + 文字提示
- 状态用绿色 ✓ + 文字"Success"

**工具**：WebAIM Contrast Checker、Stark（Figma 插件）、Colour Contrast Analyser（TPGi）、Sim Daltonism（macOS）、Chrome DevTools Rendering 面板有 4 种色盲模拟

```css
:focus-visible { outline: 3px solid #1d4ed8; }   /* blue-700 vs 白 8.6:1 */
```

## 8. 表单 a11y 完整示例

```html
<form>
  <div>
    <label for="email">Email <span aria-hidden="true">*</span></label>
    <input id="email" name="email" type="email"
           required autocomplete="email"
           aria-required="true"
           aria-describedby="email-hint email-err"
           aria-invalid="true">
    <p id="email-hint">We'll never share your email.</p>
    <p id="email-err">Please enter a valid email address.</p>
  </div>

  <div>
    <label for="pwd">Password</label>
    <input id="pwd" name="password" type="password"
           required minlength="8"
           autocomplete="current-password"
           aria-describedby="pwd-req">
    <p id="pwd-req">Minimum 8 characters, 1 number.</p>
  </div>

  <button type="submit">Sign up</button>

  <div role="status" aria-live="polite" class="sr-only"></div>
</form>

<style>
.sr-only {
  position:absolute; width:1px; height:1px;
  padding:0; margin:-1px; overflow:hidden;
  clip:rect(0,0,0,0); white-space:nowrap; border:0;
}
</style>
```

**铁律**：
1. `<label for>` 永远显示，**不要**用 placeholder 代替
2. 错误用 `aria-invalid="true"` + `aria-describedby` 指向 inline 错误段落（红 + 图标 + 文字）
3. 必填用 `required` + `aria-required="true"` 双保险
4. `autocomplete="email"` 让密码管理器/自动填充能工作（3.3.8 友好）
5. 提交结果在 `role="status"` live region 里播报

## 9. 图像 / 图标 / 媒体 a11y

**Alt 决策树**：

| 图像类型 | 处理 |
|---|---|
| 信息图 | `alt="完整描述"` |
| 装饰图 | `alt=""`（空 alt，不是无 alt） |
| 链接/按钮图 | `alt="动作"`（看链接去哪） |
| 文本图 | `alt="图中文字"` |
| 复杂图（图表） | `alt="简短说明"` + `aria-describedby` 指向详细文本 或 `<figcaption>` |
| 头像（重复信息） | `alt=""`（旁边已有名字） |

**SVG 图标按钮**（必背模板）：
```html
<button aria-label="Close">
  <svg aria-hidden="true" focusable="false" width="20" height="20">
    <path d="..."/>
  </svg>
</button>
```

`aria-hidden="true"` + `focusable="false"` 双保险。

**视频**：
1. `<video controls>` 必须有字幕轨 `<track kind="captions" srclang="en" src="..." default>`
2. 自动播放要 `muted`（WCAG 1.4.2）
3. 音频必须有 `.vtt` 字幕或文字稿
4. `<video>` 避免背景自动播放

## 15 个可复用代码片段

### 1. Dialog (Modal) 完整
```html
<button id="open1">Open</button>
<dialog id="d1" aria-labelledby="t1">
  <h2 id="t1">Title</h2>
  <p>Body</p>
  <form method="dialog"><button>OK</button></form>
</dialog>
<script>document.getElementById('open1').onclick = () => d1.showModal();</script>
```

### 2. Tabs 完整
参考 WAI-ARIA Authoring Practices Guide（role=tablist/tab/tabpanel，roving tabindex，Arrow 键切换）

### 3. Listbox（aria-activedescendant 模式）
```html
<div role="combobox" aria-expanded="true" aria-haspopup="listbox"
     aria-owns="lb1" tabindex="0">Choose fruit</div>
<ul id="lb1" role="listbox">
  <li id="o1" role="option" aria-selected="true">Apple</li>
  <li id="o2" role="option">Banana</li>
  <li id="o3" role="option">Cherry</li>
</ul>
```

### 4. Tooltip 完整
```html
<button aria-describedby="tt1">?</button>
<div id="tt1" role="tooltip">Need help? Email us.</div>
```

### 9. 屏幕阅读器 live region 模板
```html
<div id="status" role="status" aria-live="polite" aria-atomic="true" class="sr-only"></div>
<div id="alert" role="alert"></div>
<script>
document.getElementById('save').onclick = () => {
  document.getElementById('status').textContent = 'Saved at ' + new Date().toLocaleTimeString();
};
</script>
```

`aria-atomic="true"` 让整段被读；polite 等当前朗读完；assertive 立刻打断（**慎用**：成功提示用 polite，错误用 alert/assertive）。

### 11. axe-core + Playwright CI
```js
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage a11y', async ({ page }) => {
  await page.goto('/');
  const r = await new AxeBuilder({ page })
    .withTags(['wcag2a','wcag2aa','wcag22aa']).analyze();
  expect(r.violations).toEqual([]);
});
```

### 12. 颜色对比度自检函数
```js
function contrast(a, b) {
  const L = c => {
    c = c / 255;
    return c <= 0.03928 ? c/12.92 : ((c+0.055)/1.055)**2.4;
  };
  const lum = ([r,g,bb]) => 0.2126*L(r)+0.7152*L(g)+0.0722*L(bb);
  const la = lum(a) + 0.05, lb = lum(b) + 0.05;
  return la > lb ? la/lb : lb/la;
}
console.log(contrast([29,78,216],[255,255,255])); // 8.59 → AAA
```

### 13. Roving Tabindex（用于工具栏/菜单）
```js
const items = [...document.querySelectorAll('[role="tab"]')];
items.forEach((el,i) => el.tabIndex = i === 0 ? 0 : -1);
items.forEach((el,i) => el.addEventListener('keydown', e => {
  let n = i;
  if (e.key === 'ArrowRight') n = (i+1) % items.length;
  if (e.key === 'ArrowLeft')  n = (i-1+items.length) % items.length;
  if (e.key === 'Home') n = 0;
  if (e.key === 'End')  n = items.length-1;
  if (n !== i) {
    e.preventDefault();
    items.forEach(x => x.tabIndex = -1);
    items[n].tabIndex = 0;
    items[n].focus();
  }
}));
```

### 14. `<details>` 替代手写折叠
```html
<details>
  <summary>More info</summary>
  <p>Native HTML, keyboard accessible, screen reader friendly.</p>
</details>
```

### 15. 视频字幕模板
```html
<video controls width="640">
  <source src="movie.mp4" type="video/mp4">
  <track kind="captions" src="captions.en.vtt" srclang="en" default>
  <track kind="subtitles" src="captions.zh.vtt" srclang="zh">
</video>
```

## WCAG 2.2 9 条新规速查 Checklist

```markdown
- [ ] 2.4.11 Focus Not Obscured (AA)  焦点不被 sticky header 完全遮住
- [ ] 2.4.13 Focus Appearance (AAA)  焦点环 ≥ 2px 边界 + 3:1 对比
- [ ] 2.5.7 Dragging Movements (AA)  拖拽必有替代按钮
- [ ] 2.5.8 Target Size (AA)  点击目标 ≥ 24×24 CSS px
- [ ] 3.2.6 Consistent Help (A)  帮助入口跨页同位
- [ ] 3.3.7 Redundant Entry (A)  同流程不重复输入
- [ ] 3.3.8 Accessible Auth (AA)  支持 passkey / 邮件链接 / 密码管理器
- [ ] 2.4.12 Focus Not Obscured Enhanced (AAA)  完全可见
- [ ] 3.3.9 Accessible Auth Enhanced (AAA)  不用图片识别
```

## 10 条"如果你在做 a11y，记住这些"

1. **语义 HTML 第一**。`<button>` 不是 `<div role="button">`，`<nav>` 不是 `<div role="navigation">`
2. **永远保留焦点环**。`:focus { outline: none }` 是 a11y 头号反模式
3. **每个交互元素必须有可访问名**。屏幕阅读器不会自己猜
4. **`<label for>` 必显示**。placeholder 不能当 label
5. **模态框用原生 `<dialog>`**。`showModal()` 自动 inert、focus、Esc
6. **焦点必须可被看见**。对比度 ≥ 3:1，面积 ≥ 2px
7. **点击目标 ≥ 24×24**。2.5.8 是 AA 强制
8. **永远测键盘**。拔鼠标，从地址栏 Tab 一遍
9. **永远测屏幕阅读器**。NVDA+Firefox + VoiceOver+Safari 至少跑一遍
10. **CI 跑 axe-core**。自动化抓 30-40% 的 a11y bug，剩余靠人

## 5 条反面教材

1. `<div onclick="...">` 当按钮 → 键盘不可达、屏幕阅读器不识别，零状态
2. `<img src="x.png">` 不写 alt → 屏幕阅读器读出文件名"x dot png"
3. 模态打开后焦点不进去 / 关闭后焦点不还原 → 用户被丢到 body 顶端
4. 自定义下拉用 `<div>` + click，忽略键盘 → 永远进不去
5. 错误信息用 `color: red` 不用文字 + 图标 → 色盲用户看不到失败

## 3 条"如果你只能记一条"

1. **用语义 HTML 写，按 WAI-ARIA Authoring Practices Guide 写自定义控件，按 WCAG 2.2 AA 测**
2. **键盘 + 屏幕阅读器 + axe-core 三件套实测，缺一不可**
3. **a11y 是工程问题，不是 checkbox**——焦点、名称、状态、动态播报四件必做

## 资源 URL
- w3.org/WAI/standards-guidelines/wcag/new-in-22/ / wcag/ / WAI/ARIA/apg/ / tutorials/ / test-evaluate/
- webaim.org/ / articles/ / techniques/keyboard/ / techniques/screenreader/ / standards/wcag/checklist / articles/contrast/
- dequeuniversity.com/ / accessibility-developer-guide.com/
- scottohara.me/writing/（aria-current / aria-labels / aria-described / aria-hidden 详解）
- developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA / ARIA/Reference / Keyboard-navigable_JavaScript_widgets / Understanding_WCAG
- smashingmagazine.com/category/accessibility/ / 2021/11/accessible-aria-patterns/ / 2022/03/aria-html/ / 2021/12/focus-visible/ / 2020/08/accessible-forms/
- nngroup.com/articles/accessibility/ / keyboard-accessibility/ / screen-readers/ / alt-text/ / keyboard-traps/ / wcag-2-2/
