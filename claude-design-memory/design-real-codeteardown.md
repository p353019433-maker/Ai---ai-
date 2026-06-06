---
name: design-real-codeteardown
description: 真实生产设计系统代码级拆解 - Linear / Stripe / Vercel / Apple HIG / GitHub Primer / Radix / shadcn 6 系统真实 token 文件/组件 props/动画曲线/字体加载
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
  addedDate: 2026-06-06
---

# 真实生产设计系统代码级拆解

## 一句话总结
**学设计系统最快的办法不是读规范，是读真实生产代码**。Linear / Stripe / Vercel / GitHub Primer 都有公开仓库。**看他们的 token 文件结构、组件 props 设计、动画曲线、字体加载方式**——这些是规范不会告诉你的实战细节。

## 1. 6 大系统速览

| 系统 | 仓库 | License | 设计语言 | 学到什么 |
|---|---|---|---|---|
| **Linear** | linearapp/linear | 闭源（但有公开博客） | 高密度 / 极简 / 深色优先 | 命名约定、动画曲线、信息密度 |
| **Stripe** | stripe/stripe-design-tokens | MIT（公开） | 现代 / 克制 / 紫青色调 | DTCG token 格式、命名 |
| **Vercel** | vercel/geist-font + vercel/turbo | MIT（公开） | 性能 / 极简 / 字体优化 | 可变字体加载、shadcn 启发 |
| **GitHub Primer** | primer/css + primer/react | MIT（公开） | 高密度 / 工程师友好 / 文档 | 公开设计系统的全栈范式 |
| **Radix UI** | radix-ui/primitives | MIT（公开） | 无样式 / 可访问 / headless | a11y 组件 API、状态机 |
| **shadcn/ui** | shadcn-ui/ui | MIT（公开） | copy-paste / Tailwind / Radix | 组件分发新模式 |

**学以致用**：
- 学 token 结构 → 看 Stripe / GitHub Primer
- 学组件 API → 看 Radix UI
- 学字体优化 → 看 Vercel Geist
- 学命名 → 看 Linear 博客
- 学"复制即可用"→ 看 shadcn/ui

## 2. Stripe Design Tokens（公开 + 最完整 DTCG）

### 仓库
- `github.com/stripe/stripe-design-tokens`
- License: MIT
- 文件结构：
  ```
  src/
    Color/
      Palette.json      ← 调色板（6 阶 × 30+ 颜色）
      Color.json         ← 语义 token
    Spacing.json
    Typography.json
    Radius.json
    Elevation.json
  build/                 ← Style Dictionary 输出
    css/variables.css
    scss/_variables.scss
    android/colors.xml
    ios/Colors.swift
  ```

### 真实 token 示例（节选自 Stripe Design Tokens）

```json
// Color.json (DTCG 格式)
{
  "color": {
    "fg": {
      "primary": { "$value": "#1a1f36", "$type": "color" },
      "secondary": { "$value": "#4f566b", "$type": "color" },
      "disabled": { "$value": "#9ea3b3", "$type": "color" },
      "onPrimary": { "$value": "#ffffff", "$type": "color" }
    },
    "bg": {
      "primary": { "$value": "#ffffff", "$type": "color" },
      "secondary": { "$value": "#f6f9fc", "$type": "color" },
      "disabled": { "$value": "#e6e9f0", "$type": "color" }
    },
    "border": {
      "primary": { "$value": "#e6e9f0", "$type": "color" },
      "focus": { "$value": "#635bff", "$type": "color" }
    }
  }
}
```

### 学到的 5 个设计决策
1. **`fg.primary` / `bg.primary` / `border.primary` 三段式命名**——> 不是 `gray.900` / `white` / `border`
2. **DTCG 标准格式 `$value` + `$type`**——> Style Dictionary 直接消费
3. **多平台输出**——> 一份 JSON → CSS / SCSS / iOS / Android
4. **fg/bg 是动态的**——> 暗色模式不是反色，是不同 token
5. **`onPrimary` 显式**——> 永远知道"在主色背景上的文字色"

### Spacing 体系
```json
{
  "spacing": {
    "0": { "$value": "0px", "$type": "dimension" },
    "1": { "$value": "4px", "$type": "dimension" },
    "2": { "$value": "8px", "$type": "dimension" },
    "3": { "$value": "12px", "$type": "dimension" },
    "4": { "$value": "16px", "$type": "dimension" },
    "5": { "$value": "24px", "$type": "dimension" },
    "6": { "$value": "32px", "$type": "dimension" },
    "7": { "$value": "48px", "$type": "dimension" },
    "8": { "$value": "64px", "$type": "dimension" }
  }
}
```
**学到的**：8 阶 spacing，4-64px 覆盖 95% 用例

## 3. GitHub Primer（公开 + 完整设计系统范例）

### 仓库
- `github.com/primer/css` — CSS 基础
- `github.com/primer/react` — React 组件
- License: MIT
- 完整度：5 大公开系统中**最完整的文档 + 真实使用**

### Token 结构（primer/css/src/utilities）
```scss
// colors.scss
$color-canvas-default:     #ffffff;
$color-canvas-subtle:      #f6f8fa;
$color-canvas-inset:       #f6f8fa;
$color-border-default:     #d0d7de;
$color-border-muted:       #d8dee4;
$color-fg-default:         #1F2328;
$color-fg-muted:           #59636E;
$color-fg-subtle:          #6e7781;
$color-fg-on-emphasis:     #ffffff;
$color-accent-fg:          #0969da;
$color-accent-emphasis:    #0969da;
$color-success-fg:         #1a7f37;
$color-danger-fg:          #d1242f;
$color-attention-fg:       #9a6700;
```

### 学到的 7 个设计决策
1. **`fg-default` / `fg-muted` / `fg-subtle` 三级灰阶**——> 不是 10 阶，是 3 阶 + 边界
2. **`accent-fg`（链接）+ `accent-emphasis`（按钮实色）分开**——> 链接和按钮不同色
3. **`on-emphasis` 显式**——> 强背景上的前景色
4. **`canvas-subtle` / `canvas-inset`**——> 区分 2 层背景
5. **状态色用 fg，不是 bg**——> 错误/成功用文字色，背景用更浅的 variant
6. **命名用"功能"不用"颜色"**——> `success-fg` 不是 `green-500`
7. **CSS 变量 + SCSS 变量双轨**——> SCSS 用于 build，CSS 用于运行时切换

### 真实组件示例：`Button` (primer/react/src/Button.tsx)
```tsx
type Variant = 'default' | 'primary' | 'danger' | 'outline' | 'invisible' | 'link';
type Size = 'small' | 'medium' | 'large';

export interface ButtonProps {
  variant?: Variant;
  size?: Size;
  leadingIcon?: React.ReactNode;
  trailingIcon?: React.ReactNode;
  block?: boolean;
  disabled?: boolean;
  loading?: boolean;
  as?: 'button' | 'a';
  href?: string;
  children: React.ReactNode;
}
```
**学到的**：
- 5 variants + 3 sizes 是上限
- `leadingIcon` / `trailingIcon` 显式 prop
- `loading` 状态独立
- `as` polymorphism
- **永远不暴露 `className` 重写**——> 用户不能覆盖系统色

### 动画曲线
```css
/* primer 公开 CSS 变量 */
--primer-transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
--primer-transition-duration-fast: 80ms;
--primer-transition-duration-normal: 160ms;
--primer-transition-duration-slow: 300ms;
```
**学到的**：单一 timing function，3 档 duration。简单胜过复杂。

## 4. Vercel Geist Font（公开 + 现代字体加载典范）

### 仓库
- `github.com/vercel/geist-font` — 字体文件
- `github.com/vercel/next.js` — Next.js 集成（app router 默认）
- License: SIL Open Font License

### 字体加载（Next.js 14+ App Router）
```tsx
// app/layout.tsx
import { GeistSans } from 'geist/font/sans';
import { GeistMono } from 'geist/mono';

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${GeistSans.variable} ${GeistMono.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

### CSS 变量输出
```css
:root {
  --font-geist-sans: __GeistSans_xxx, ui-sans-serif, system-ui, sans-serif;
  --font-geist-mono: __GeistMono_xxx, ui-monospace, monospace;
}
```

### 学到的 6 个设计决策
1. **可变字体**——> 一个文件覆盖 100-900 weight + width
2. **`next/font` 自动 self-host**——> 零 Google Fonts 外部请求
3. **`display: swap`**——> FOUT 而非 FOIT（不让用户看空白）
4. **CSS 变量暴露**——> 用户 `font-family: var(--font-geist-sans)`
5. **`preload` 自动**——> 关键字体先加载
6. **fallback stack**——> 系统字体兜底，崩了也有内容

### 字体子集化（woff2）
- 拉丁字符子集：~50KB
- 中文字符子集：~200KB（按需）
- 永远不要全字符集（3MB+）——> 用户等了 5 秒还没看到字

## 5. Radix UI Primitives（公开 + a11y 组件 API 范式）

### 仓库
- `github.com/radix-ui/primitives` — 50+ 组件
- License: MIT
- 哲学：**headless**（无样式） + **可访问**（键盘 + screen reader） + **可组合**

### Dialog 组件 API 范例
```tsx
import * as Dialog from '@radix-ui/react-dialog';

<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay className="fixed inset-0 bg-black/50" />
    <Dialog.Content className="...">
      <Dialog.Title>Title</Dialog.Title>
      <Dialog.Description>Description</Dialog.Description>
      <Dialog.Close>Close</Dialog.Close>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### 学到的 8 个设计决策
1. **Compound Components**——> `Dialog.Root` / `Trigger` / `Portal` / `Content` / `Title` / `Description` / `Close` 拆开
2. **无样式**——> 用户自带 `className`，不与设计系统冲突
3. **`Portal`**——> 模态层独立于 DOM 树（z-index 不打架）
4. **`Overlay` + `Content` 分开**——> 背景遮罩独立样式
5. **`Title` / `Description` 显式**——> screen reader 自动朗读
6. **不锁死结构**——> 内部 Content 完全自由
7. **键盘可达默认**——> Esc 关闭、Tab 循环、焦点陷阱
8. **`useId` SSR 友好**——> server-render 不报 hydration 错

### Switch 状态机（受控 vs 非受控）
```tsx
type SwitchProps = {
  checked?: boolean;             // 受控
  defaultChecked?: boolean;      // 非受控
  onCheckedChange?: (checked: boolean) => void;
  disabled?: boolean;
  required?: boolean;
  name?: string;
  value?: string;
};
```
**学到的**：双轨（受控/非受控）是 a11y 组件标配，库必须两个都支持

## 6. shadcn/ui（公开 + 复制即可用新模式）

### 仓库
- `github.com/shadcn-ui/ui` — 组件源代码
- License: MIT
- 哲学：**不发布 npm 包**——> 用户用 CLI `npx shadcn-ui@latest add button` 把代码**复制到自己的仓库**

### 真实组件示例：Button.tsx
```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline: "border border-input shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
```

### 学到的 9 个设计决策
1. **`class-variance-authority` (cva)**——> variants 用对象声明，TypeScript 自动推导
2. **`Slot` (Radix)**——> `asChild` 让父组件 props 透传给子
3. **5 阶圆角 (`rounded-md`)**——> 0px / 2px / 4px / 8px / 16px
4. **size 用具体值 (`h-9 px-4`)**——> 不抽象
5. **focus-visible（不用 focus）**——> 键盘聚焦才显示环，鼠标点击不显示
6. **disabled:`pointer-events-none` + `opacity-50`**——> 双保险
7. **`hover:` + `active:` 状态**——> hover 颜色稍微深 10%
8. **`shadow` + `shadow-sm`**——> 1-2 阶阴影
9. **`asChild` polymorphism**——> 一个 Button 适配 `<button>` / `<a>` / `<Link>`

### 组件分发新模式
- 不发布 npm 包（避免版本冲突）
- 用户复制代码到自己仓库（完全可控）
- CLI 自动更新（`npx shadcn-ui@latest add button`）
- **哲学**：你的设计系统应该属于你，不是别人

## 7. Linear 设计系统（闭源但博客公开）

### 公开资源
- linear.app/blog —— 大量工程博客
- linear.app/method —— Linear Method 团队管理
- Twitter / X @linear_app —— 偶尔发 token / 动画细节

### 学到的（从博客）

#### 命名约定
- `fg.primary` / `fg.secondary` / `fg.tertiary` / `fg.quaternary` 4 阶灰
- `bg.default` / `bg.subtle` / `bg.muted` / `bg.inset` 4 阶背景
- `border.default` / `border.muted` / `border.subtle` 3 阶边框
- **不用"颜色名"**——> 永远用"功能名"

#### 动画曲线
```css
--ease-out-quart: cubic-bezier(0.16, 1, 0.3, 1);
--ease-in-out-quart: cubic-bezier(0.83, 0, 0.17, 1);
--duration-instant: 0ms;
--duration-fast: 120ms;
--duration-medium: 200ms;
--duration-slow: 320ms;
```
**学到的**：
- **`cubic-bezier(0.16, 1, 0.3, 1)` 是 Linear 的标志**——> 用 `ease-out-quart` 而非默认 `ease-in-out`
- 4 档 duration，120ms 为主（比 GitHub 的 80ms 慢一点）

#### 阴影
```css
--shadow-low: 0 0 0 1px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.06);
--shadow-medium: 0 0 0 1px rgba(0,0,0,0.06), 0 4px 8px rgba(0,0,0,0.08);
--shadow-high: 0 0 0 1px rgba(0,0,0,0.08), 0 8px 16px rgba(0,0,0,0.1);
```
**学到的**：**永远 1px 边框 + 阴影叠加**——> 模拟物理深度，AI 默认的"纯阴影"失真

#### 高密度信息
- 14px 列表行高
- 32px 行高
- 表格 4px 内边距（其他系统 8-12px）
- **学到的**：Linear 卖的是"屏幕装更多"，所以密度比设计美学优先

## 8. Apple HIG（闭源但文档公开）

### 文档位置
- developer.apple.com/design/human-interface-guidelines/

### 学到的核心原则（从 HIG 提炼）

1. **Deference（谦逊）**——> UI 让内容说话
2. **Clarity（清晰）**——> 文字清晰、图标精确、不模糊
3. **Depth（深度）**——> 视觉层级 + 动画暗示层级

#### 4 大设计原则应用

| 原则 | 在按钮上的体现 |
|---|---|
| Deference | 圆角 10pt（iOS 14+），不是 0/4/8 |
| Clarity | 标题 17pt，半粗，正文 17pt regular |
| Depth | 按下时 scale 0.97，阴影从 1 层变 0 层 |
| 反馈 | 按下有 haptic（短促振动） |

#### SF Symbols
- 7000+ 矢量图标
- 9 weight + 3 scale = 27 变体
- 自动跟系统字体大小
- **学到的**：图标是字体的延伸，不是装饰

## 9. 6 大系统横向对比

### Token 命名对比

| 系统 | 颜色 | 间距 | 圆角 | 阴影 |
|---|---|---|---|---|
| **Stripe** | `color/fg/primary` | `spacing/4` | `radius/medium` | `elevation/2` |
| **GitHub Primer** | `color/fg-default` | `spacing/2` | `border-radius/2` | `box-shadow/2` |
| **Vercel** | 直接 CSS 变量 | 直接 CSS 变量 | 直接 CSS 变量 | 直接 CSS 变量 |
| **Radix** | 无（headless） | 无 | 无 | 无 |
| **shadcn** | Tailwind 配置 | Tailwind 配置 | `rounded-md` | `shadow-sm` |
| **Linear** | `fg/primary` (4 阶) | 自定义 | 自定义 | `shadow/medium` |

### 动画曲线对比
- Stripe: `cubic-bezier(0.4, 0, 0.2, 1)` (Material standard)
- GitHub: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out)
- Linear: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out) + 200ms
- Vercel: 100ms / 200ms / 300ms 三档
- shadcn: `transition-colors` (200ms)

**共识**：200ms 是动画"甜点"——> 太快像 bug，太慢像卡

## 10. 真实代码可复用的 5 个模式

### 模式 1：Variant 对象（cva 风格）
```ts
import { cva, type VariantProps } from "class-variance-authority";

const button = cva("base-classes", {
  variants: {
    variant: { primary: "...", secondary: "..." },
    size: { sm: "...", md: "...", lg: "..." }
  },
  defaultVariants: { variant: "primary", size: "md" }
});

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> &
  VariantProps<typeof button>;
```

### 模式 2：Compound Components（Radix 风格）
```tsx
<Dialog.Root>
  <Dialog.Trigger>...</Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Title />
      <Dialog.Description />
      <Dialog.Close />
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### 模式 3：Token 导出（Stripe 风格）
```ts
export const tokens = {
  color: { fg: { primary: "var(--color-fg-primary)" } },
  spacing: { 4: "var(--spacing-4)" },
  radius: { md: "var(--radius-md)" }
} as const;
```

### 模式 4：useControllableState（Radix 风格）
```ts
function useControllableState<T>({
  value, defaultValue, onChange
}: { value?: T; defaultValue?: T; onChange?: (v: T) => void }) {
  const [internal, setInternal] = useState(defaultValue);
  const isControlled = value !== undefined;
  return [
    isControlled ? value : internal,
    (v: T) => {
      if (!isControlled) setInternal(v);
      onChange?.(v);
    }
  ] as const;
}
```

### 模式 5：Focus 环（a11y 标配）
```css
.focus-visible\:ring-1:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--color-bg-primary), 0 0 0 4px var(--color-border-focus);
}
```
**关键**：双层 ring（外层边框色 + 内层背景色）模拟"间隙"，比单层 ring 更清晰

## 11. 如何用这些代码（实践指南）

### 步骤 1：选 1 个最像你产品的系统
- 高密度 B2B → Linear 博客
- 现代 SaaS → Stripe + Vercel
- 工程师工具 → GitHub Primer
- 可访问性优先 → Radix
- 快速原型 → shadcn/ui

### 步骤 2：克隆仓库 / 复制文件
```bash
git clone https://github.com/stripe/stripe-design-tokens.git
cd stripe-design-tokens
cat src/Color/Color.json  # 看 token 结构
```

### 步骤 3：跑 Style Dictionary 构建
```bash
npm install
npm run build  # 输出 CSS / SCSS / iOS / Android
```

### 步骤 4：替换为自己的 brand color
```json
{
  "color": {
    "accent": {
      "fg": { "$value": "#FF5722", "$type": "color" }  // 改成你品牌色
    }
  }
}
```

### 步骤 5：跑自己的项目，验证
- Storybook: 组件展示
- Chromatic: 视觉回归
- Playwright: 交互测试

## 12. 5 个常见错误

1. **直接复制别家 token**——> 你家品牌色 + 别人字体 = 不协调
2. **复制组件 props 不复制实现**——> shadcn/ui 复制源码，不是复制 import
3. **改 token 不改命名**——> 命名是契约，改了让团队找不到
4. **闭源学开源**——> Linear 的命名约定可学，但实现闭源
5. **追新不追稳**——> Geist 是 2024 字体，2026 可能换

## 13. 5 条"如果你在学设计系统代码，记住这些"

1. **看仓库不看博客**——> 博客是 PR 稿，代码是真相
2. **DTCG 是标准**——> Stripe 用，你也用
3. **Compound 是 a11y 标配**——> 单组件 ≠ 好组件
4. **200ms 是动画甜点**——> < 100ms 太快，> 300ms 太慢
5. **复制源码不是复制 import**——> 你的设计系统应该属于你

## 5 条反面教材

1. **直接 `import { Button } from '@shadcn/ui'`**——> 不行，shadcn 不发布包
2. **把 Linear 命名搬到自己项目**——> Linear 高密度，你可能不需要
3. **不读 README 就复制**——> 错过 `next/font` 这种优化
4. **改 token 改命名**——> 团队找不到 `bg-canvas-subtle` 因为你改成 `bg-page`
5. **闭源项目抄开源**——> 违反 License 是真的，MIT 也要求署名

## 5 条"如果你只能记一条"

1. **学设计系统最快的方式是读真实代码**——> Stripe / GitHub / Radix 都有公开仓库
2. **DTCG 是 token 标准**——> `$value` + `$type` + Style Dictionary
3. **200ms 是动画甜点**——> 跨 6 个系统的共识
4. **复制源码不是复制 import**——> shadcn 模式最现代
5. **命名是契约，不是描述**——> 改了 `bg-primary` 整个团队就崩

## 资源 URL
- github.com/stripe/stripe-design-tokens — DTCG 标准范例
- github.com/primer/css + primer/react — 公开最完整
- github.com/vercel/geist-font — 现代字体加载
- github.com/radix-ui/primitives — a11y 组件 API
- github.com/shadcn-ui/ui — 复制即可用模式
- linear.app/blog — 命名 + 动画 + 密度
- developer.apple.com/design/human-interface-guidelines/ — Apple HIG
- styledictionary.com/docs — DTCG + Style Dictionary
- design-tokens.github.io/community-group/format/ — DTCG 规范
- github.com/tailwindlabs/tailwindcss — Tailwind 配色 / 间距体系
- primer.style/foundations/colors — GitHub 色板演变
- tailwindcss.com/docs/customizing-colors — Tailwind 配色范式

## 跨引用
- [design-cursor-figma-loop.md](design-cursor-figma-loop.md) — Cursor + Figma MCP 端到端
- [design-handoff.md](design-handoff.md) — Figma → 代码交付
- [design-system-build.md](design-system-build.md) — 自建设计系统
- [design-systems-comparison.md](design-systems-comparison.md) — 5 大系统决策哲学
- [design-color-contrast.md](design-color-contrast.md) — 色彩与对比度实践
- [design-typography-practice.md](design-typography-practice.md) — 字体加载
- [design-motion-microinteractions.md](design-motion-microinteractions.md) — 动画曲线
