---
name: design-motion-microinteractions
description: 动效与微交互实操 - Easing/时长/微交互 4 阶段/loading 4 种/视图转场 6 范式/scroll-driven animations/View Transitions API/Framer Motion
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 动效与微交互：可立即上手的执行手册

## 一句话总结
**动效做对 = 用 `transform` / `opacity`、200–300ms 区间、`cubic-bezier(0.4, 0, 0.2, 1)` 或等价曲线、尊重 `prefers-reduced-motion`**。

## 1. Easing 函数：6 种足够覆盖 95% 场景

| 关键字 | cubic-bezier 等价 | 用途 |
|---|---|---|
| `linear` | `cubic-bezier(0,0,1,1)` | 旋转、color-cycle、避免用 |
| `ease` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | 浏览器默认，**几乎不要用** |
| `ease-in` | `cubic-bezier(0.42, 0, 1, 1)` | 元素**离场**（加速离开） |
| `ease-out` | `cubic-bezier(0, 0, 0.58, 1)` | 元素**入场**（减速停下） |
| `ease-in-out` | `cubic-bezier(0.42, 0, 0.58, 1)` | 状态**切换**（淡入淡出对位） |
| `ease-in-out` Material | `cubic-bezier(0.4, 0, 0.2, 1)` | **MD 标准，几乎所有 UI 动画的默认值** |

**经验法则**：
- **入场用 `ease-out`**
- **离场用 `ease-in`**
- **状态切换用 `cubic-bezier(0.4, 0, 0.2, 1)`**
- **`linear` 看上去机械**，只用于纯装饰（spinner 旋转、shimmer 扫光）

**MDN 明确** `ease` 是默认但少用——`ease` 在中段有奇怪的"先慢后快再慢"曲线，体感上不如 Material 曲线稳定。

**弹簧（spring）**用 JS 库（Framer Motion / Motion）：`transition: { type: "spring", stiffness: 260, damping: 20 }`。UI 拖拽、卡片展开、可中断动画才用 spring。

## 2. 时长（Duration）：5 档 Token 系统

**NN/g 研究**：100–400ms 是甜区，超过 500ms 烦人，进入 < 100ms 像没动。

```css
:root {
  --dur-instant: 80ms;   /* 颜色、opacity 微变 */
  --dur-fast:    150ms;  /* hover、focus ring、tooltip */
  --dur-base:    240ms;  /* 按钮按下、checkbox 翻转、chip */
  --dur-slow:    360ms;  /* 模态框、抽屉、菜单展开 */
  --dur-page:    500ms;  /* 页面转场、shared element */
}
```

**入场比离场慢 50–100ms**（NN/g 建议）：用户先感受到"东西到了"，再"东西走了"，心智模型更顺。Material 3 的补充：**大元素用更短时长**（大的卡片反而比小的 chip 动得更快，否则显得拖沓）。

## 3. 微交互 4 阶段（Dan Saffer）

**Trigger → Rule → Feedback → Loop**。每个微交互必须能回答这 4 个问题：

- **Trigger**：用户/系统什么动作触发？（hover、click、scroll、3s 无操作）
- **Rule**：规则是什么？（"点击 → 数量 +1"）
- **Feedback**：用户感受到什么？（按钮 scale 0.98 + 100ms 反弹 + 数字 +1 颜色闪一下）
- **Loop**：重复模式（每按一次累加，无上限？加满抖动？）

**反例**：点赞按钮只触发 `count++`，没 scale、没颜色、没 haptic → 用户怀疑没点上。**反馈缺失 = 信任缺失**。

## 4. Loading：4 种选型

| 类型 | 何时用 | 不要用 |
|---|---|---|
| **Spinner** | 等待时间不可预测、< 2s | 长任务（>3s 用户焦虑） |
| **Skeleton** | 内容结构可预测、> 1s | 一次性的小加载 |
| **Progress bar** | 任务有明确进度 | 进度不可知时（会撒谎） |
| **Shimmer** | skeleton 上加扫光效果 | 静态骨架（容易让用户以为是内容） |

**Nielsen Norman 关键结论**：skeleton 屏比 spinner **感知快 20–30%**，因为给用户"东西正在来"的预期。**进度条如果跳来跳去**（异步分片）**就删掉**——比没进度还糟。

```css
/* Shimmer skeleton */
.skeleton {
  background: linear-gradient(90deg, #eee 0%, #f5f5f5 50%, #eee 100%);
  background-size: 200% 100%;
  animation: shimmer 1.4s linear infinite;
}
@keyframes shimmer { to { background-position: -200% 0; } }
```

## 5. 视图/页面转场：6 种范式

| 范式 | 适用 |
|---|---|
| **fade** | 内容结构相同、仅数据更新（列表刷新） |
| **slide** | 层级关系（推入下一级 = 向左滑） |
| **push** | 移动端页面间最常用 |
| **zoom** | 模态框（背景缩小 + 自身放大） |
| **morph** | FAB 变全屏编辑器 |
| **shared element** | 列表项 → 详情页 hero 图 |

**iOS HIG 原则**：转场必须传达**空间关系**——push 暗示层级前进，modal 暗示临时覆盖。**slide-in 必带 spring 反弹**，否则像 PPT 翻页。

## 6. 按钮反馈：完整可复制 CSS

```css
.btn {
  --bg: #111;
  --shadow: 0 1px 2px rgba(0,0,0,.12);
  --shadow-hover: 0 6px 16px rgba(0,0,0,.18);
  background: var(--bg);
  color: #fff;
  padding: 12px 20px;
  border: 0;
  border-radius: 8px;
  box-shadow: var(--shadow);
  transition:
    transform 200ms cubic-bezier(0.4, 0, 0.2, 1),
    box-shadow 200ms cubic-bezier(0.4, 0, 0.2, 1),
    background-color 150ms ease-out;
}
.btn:hover  { transform: translateY(-1px) scale(1.02); box-shadow: var(--shadow-hover); }
.btn:active { transform: translateY(0)    scale(0.98); transition-duration: 80ms; }
.btn:focus-visible { outline: 2px solid #4f8cff; outline-offset: 2px; }

/* Material ripple */
.btn { position: relative; overflow: hidden; }
.ripple {
  position: absolute; border-radius: 50%;
  transform: scale(0);
  background: rgba(255,255,255,.5);
  animation: ripple 600ms cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
}
@keyframes ripple { to { transform: scale(4); opacity: 0; } }
```

**关键**：
- hover 用 `scale(1.02)` 而非 `1.05`（5% 太跳）
- active 用 `0.98` + 短时长（80ms，按下要"实"）
- **只动 transform 和 box-shadow**
- **绝不动 width/height/margin**（触发 layout，重排 60fps 必死）

## 7. 滚动驱动动画（Scroll-Driven Animations）

**无需 JS**，纯 CSS 2024 已稳定（Chrome/Edge 115+，Safari 26+）：

```css
@keyframes reveal {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}

.reveal-on-scroll {
  animation: reveal linear both;
  animation-timeline: view();        /* 元素自身进入视口时驱动 */
  animation-range: entry 0% cover 40%;  /* 进入 0%~40% 完成动画 */
}

/* 视差背景 */
.hero {
  animation: parallax linear both;
  animation-timeline: scroll(root block);
}
@keyframes parallax { to { transform: translateY(-30%); } }
```

**`animation-range` 5 个值**：`cover`（全程）、`entry`（进入）、`exit`（离开）、`entry-crossing`/`exit-crossing`（仅过线）、`contain`（完全在内）。**实用配方**：`entry 0% cover 30%` = 元素进入视口后 30% 内完成 fade-in，最自然。

**降级**：用 `@supports (animation-timeline: view())` 包裹，旧浏览器拿到静态状态。**一定要尊重 `prefers-reduced-motion`**。

## 8. 现代工具栈

| 工具 | 用在 |
|---|---|
| **CSS `transition`** | 状态切换（hover、focus、disabled） |
| **CSS `@keyframes` + `animation`** | 进入/离场、装饰性循环（spinner、shimmer） |
| **View Transitions API** | SPA 路由转场、`document.startViewTransition(cb)` |
| **Lottie** | 设计师给的 After Effects 复杂矢量动画（JSON，~50KB 起） |
| **Rive** | 交互式矢量动画 + 状态机（按钮状态、人物表情） |
| **Framer Motion / Motion** | React 项目、layout 动画、AnimatePresence 退场、spring、gesture |
| **Motion One** | 框架无关的小型库（`animate(el, {x:100})`） |

**选型**：
- 纯 CSS 微交互 → CSS 即可
- SPA 路由转场 → View Transitions API
- 设计师 AE 出动效 → Lottie/Rive
- React 项目要 layout 动画 + 退场 → Framer Motion
- 非 React 轻量需求 → Motion One

## 15 个可复用片段

### 4 种标准 easing
```css
--ease-out:  cubic-bezier(0, 0, 0.2, 1);    /* 入场 */
--ease-in:   cubic-bezier(0.4, 0, 1, 1);    /* 离场 */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);/* Material 标准 */
--linear:    linear;                        /* 旋转/扫光 */
```

### 时长 token（5 档）
```css
--d1: 80ms;  --d2: 150ms; --d3: 240ms; --d4: 360ms; --d5: 500ms;
```

### Spinner（用 transform）
```css
.spinner {
  width: 24px; height: 24px;
  border: 2px solid #eee; border-top-color: #111;
  border-radius: 50%;
  animation: spin 800ms linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
```

### 进度条
```css
.bar { height: 4px; background: #eee; overflow: hidden; }
.bar::after {
  content: ""; display: block; height: 100%;
  background: #111;
  transform-origin: left;
  animation: fill 1.2s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
@keyframes fill { from { transform: scaleX(0); } to { transform: scaleX(1); } }
```

### 模态框进退场
```css
.overlay { background: rgba(0,0,0,0); transition: background 240ms ease-out; }
.overlay.open { background: rgba(0,0,0,0.5); }

.modal {
  opacity: 0; transform: translateY(20px) scale(0.96);
  transition: opacity 240ms ease-out, transform 360ms cubic-bezier(0.4, 0, 0.2, 1);
}
.modal.open { opacity: 1; transform: translateY(0) scale(1); }
```

### 列表 stagger
```css
@starting-style { .item { opacity: 0; transform: translateY(8px); } }
.item { opacity: 1; transform: none; transition: 240ms cubic-bezier(0, 0, 0.2, 1); }
.item:nth-child(1) { transition-delay: 0ms; }
.item:nth-child(2) { transition-delay: 40ms; }
.item:nth-child(3) { transition-delay: 80ms; }
.item:nth-child(4) { transition-delay: 120ms; }
```

### Scroll-driven 完整模板
```css
.reveal {
  animation: reveal-up linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 35%;
}
@keyframes reveal-up {
  from { opacity: 0; transform: translateY(40px) scale(0.98); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}
@media (prefers-reduced-motion: reduce) {
  .reveal { animation: none; }
}
```

### View Transitions API（SPA）
```js
function navigate(url) {
  document.startViewTransition(async () => {
    const html = await fetch(url).then(r => r.text());
    document.querySelector('#app').innerHTML = html;
  });
}
```
```css
::view-transition-old(root) { animation: 200ms ease-in fade-out; }
::view-transition-new(root) { animation: 300ms cubic-bezier(0, 0, 0.2, 1) fade-up; }
@keyframes fade-out { to { opacity: 0; } }
@keyframes fade-up  { from { opacity: 0; transform: translateY(20px); } }

/* 共享元素 */
.card-image { view-transition-name: card-hero; }
.detail-hero { view-transition-name: card-hero; }
```

### Framer Motion 组件
```jsx
import { motion, AnimatePresence } from "framer-motion";

export function Modal({ open, onClose, children }) {
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          className="overlay"
        >
          <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.96 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 20, scale: 0.96 }}
            transition={{ duration: 0.24, ease: [0.4, 0, 0.2, 1] }}
          >
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

## 10 条"如果你在做动效，记住这些"

1. **只动 `transform` 和 `opacity`**，其它属性触发 layout/paint → 掉帧
2. **`cubic-bezier(0.4, 0, 0.2, 1)` 是 Material 标准**，从今往后这就是你的默认
3. **时长 200–300ms 是 90% UI 动画的家**（NN/g），别超过 500ms
4. **入场用 `ease-out`，离场用 `ease-in`**
5. **入场比离场慢 50–100ms**，用户先"感到到达"再"感到离开"
6. **hover 用 `scale(1.02)` 不要 `1.05`**，active 用 `scale(0.98)` + 短时长 80ms
7. **spinner 给 < 2s 任务，skeleton 给 > 1s 且结构可预测的任务**
8. **`prefers-reduced-motion` 必查**，降级方案是 `animation: none`
9. **microinteractions 必有 4 阶段**（trigger/rule/feedback/loop），反馈缺失 = 用户不信
10. **CSS scroll-driven animations 已稳定**，`view()` + `entry 0% cover 30%` 是进场范式

## 5 条反面教材（"看到 X 必改"）

1. **时长 800ms+ 的弹窗入场** → 嫌慢。改 300ms
2. **动 `width/height/left/top` 的动画** → 必掉帧。改 `transform: translate/scale`
3. **`ease`（浏览器默认）做主入场** → 中段奇怪曲线。改 `cubic-bezier(0.4, 0, 0.2, 1)`
4. **进度条数字来回跳（异步 chunk）** → 比没进度还糟。改 indeterminate spinner 或 skeleton
5. **模态框直接 `display: none` ↔ `display: block`** → 没有动画。改 `opacity + transform` + `pointer-events`

## 5 条"如果你只能记一条"

1. **`transform` + `opacity` + `cubic-bezier(0.4, 0, 0.2, 1)` + 240ms**——这 4 个值覆盖 80% 微交互
2. **入场 `ease-out`、离场 `ease-in`、状态切 `ease-in-out`**——曲线对应语义
3. **200–300ms 是 UI 动画的家**，超过 500ms 必有问题
4. **微交互 4 阶段：trigger / rule / feedback / loop**，缺一个就坏
5. **`prefers-reduced-motion` 不是可选项**，是 Web 标准

## 资源 URL
- developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations / CSS_transitions/Using_CSS_transitions
- developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function / cubic-bezier / animation / animation-timeline / animation-range
- developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations / View_Transitions_API
- developer.chrome.com/docs/css-ui/scroll-driven-animations / view-transitions
- web.dev/articles/animations-guide / animating-css-properties / css-animations-vs-transitions
- m3.material.io/styles/motion/overview / easing-and-duration
- atlassian.design/foundations/motion / primer.style/foundations/motion
- developer.apple.com/design/human-interface-guidelines/motion
- nngroup.com/articles/animation-duration/ / skeletial-screens/ / progress-indicators/
- lottiefiles.com / rive.app / motion.dev
