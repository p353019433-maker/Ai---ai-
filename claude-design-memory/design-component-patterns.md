---
name: design-component-patterns
description: 12 核心组件设计模式 - 按钮/卡片/表单/弹窗/导航/列表/数据/反馈/状态/空态/错误/分页 - 全部 if-then 规则 + 真实 Tailwind 代码
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 组件设计模式（实操手册）

## 一句话总结
**组件设计 = "状态机 × 视觉 token × 可访问性"**——每个组件先列穷状态（default/hover/active/focus/disabled/loading/error/empty），再上 token（spacing/color/radius/shadow），最后接 ARIA，**缺一个就塌**。

## 1. Button（按钮）

**变体**（参考 shadcn/ui + Carbon + Material 3）：
- `primary` 主操作（**每屏只 1 个**）
- `secondary` 次操作（边框/底色弱）
- `tertiary` 文字按钮（链接感）
- `ghost` 透明，仅 hover 出底色（工具栏）
- `destructive` 删除/不可逆（红）

**Size**：`sm` 32px / `md` 40px / `lg` 48px（Carbon 还有 xl 64px、2xl 80px 用于落地页）。**触控目标 ≥ 44×44px（iOS）/ 48×48dp（Material）**。

**状态**：default / hover（亮度 ±8%）/ active（按下 ±12%）/ focus（2px ring + 2px offset）/ disabled（**38% opacity，Material 3 规范**）/ loading（spinner 替代图标，**按钮宽度不变防止抖动**）。

**If-Then**：
- 如果操作不可逆 → `destructive` + 二次确认弹窗
- 如果一屏出现 2 个 primary → 错，降级一个为 secondary
- 如果按钮在表单底部 → primary 永远在最右（西方阅读流），左边是 cancel
- 如果是图标按钮 → 必须有 `aria-label` 或 tooltip
- 如果加载 > 1s → 必须 loading 态；> 10s → 用 progress bar 不用 spinner（NN/g 阈值）

```html
<button class="inline-flex items-center justify-center gap-2 h-10 px-4 rounded-md
  bg-neutral-900 text-white text-sm font-medium
  hover:bg-neutral-800 active:bg-neutral-950
  focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-neutral-900 focus-visible:ring-offset-2
  disabled:opacity-40 disabled:pointer-events-none
  transition-colors">
  Save
</button>
```

## 2. Card（卡片）

**4 种变体**：
- **基础**：仅 border + padding，无内容结构
- **媒体**：封面图（16:9 / 4:3）+ 标题 + 副文 + 操作区
- **交互**：整张可点击，hover 抬高
- **数据**：KPI 数字 + 标签 + 趋势小箭头

**关键规则**：
- 内边距：紧凑 16px / 标准 24px / 宽松 32px——**永远整数倍 4 或 8**
- 圆角：4–16px，**整套产品统一一个值，不要每个卡片不同**
- **阴影 vs 边框选一个**，不要叠加（Refactoring UI 原则）
- 标题 16–20px / semibold，副文 14px / regular / 60% opacity
- 交互卡片 hover shadow + translate-y-0.5，**禁止再放第二个独立按钮**（hit-area 冲突）

**If-Then**：
- 如果卡片里有 2 个以上 CTA → 改成"整卡可点 + 顶部 overflow menu"
- 如果是图片卡片 → 图片永远顶部全宽，**不要图片留白边**
- 如果是数据卡片 → 数字 28–48px >> 标签 12–14px

## 3. Form Field（表单字段）

**类型**：input / textarea / select / checkbox / radio / switch / date / file。

**关键规则**：
- **Label 永远在外，不要用 placeholder 替代 label**（Smashing 经典反模式，盲屏读不出来，输入后消失）
- Label 顶部对齐 > 左对齐 > 浮动。**移动端必须顶部对齐**
- Placeholder 仅放"示例值"，不放说明。说明用 `helper text`
- 必填星号 `*` 紧贴 label 右侧，颜色与 destructive 一致
- 错误信息：**inline 内联在字段下方**，红色 + icon，**不要靠 toast 报错**
- 错误时机：**onBlur 触发，不是 onChange**（每打一个字就报红是噪音）
- Input 高度 = button 高度（40px），padding 12px，font 14–16px（iOS 防自动放大用 ≥16px）

**checkbox vs radio**（NN/g）：
- 单选必有默认值 → radio
- 多选可零可全 → checkbox
- 单个开关 → switch（即时生效）/ checkbox（提交后生效）
- **dropdown 慎用**：2–7 项用 radio/segmented，>15 项用 search-select

## 4. Dialog（弹窗）·5 种浮层对比

| 类型 | 何时用 | 触发 | 关闭 |
|------|--------|--------|------|
| **Modal** | 关键决策，阻断流程 | 用户主动 | esc/btn/overlay |
| **Sheet/Drawer** | 副内容（筛选/导航/详情）| 用户主动 | 同上 + 滑动 |
| **Popover** | 上下文相关的操作组 | 锚点 click | click outside |
| **Tooltip** | 解释性文字（≤ 80 字符）| hover/focus | hover out |
| **Toast** | 操作结果反馈 | 系统触发 | 超时/手动 |

**Modal 必备**（Headless UI + Radix 规范）：
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby`
- **Focus trap**：tab 循环只在 modal 内
- esc 关闭、点击 overlay 关闭、关闭后**焦点回到触发按钮**
- overlay 黑色 50–60% opacity，**不要纯黑**
- 最大宽度：confirmation 400px / form 560px / full-screen 移动端
- 按钮顺序：`[Cancel] [Primary]`，primary 在右

**If-Then**：
- 如果内容 > 1 屏 → 不是 modal 是页面
- 如果是表单 > 3 字段 → 用 sheet 而非 modal
- 如果是确认删除 → modal + destructive + 描述具体影响（"将删除 23 条记录"）
- **移动端任何 modal → 自动变 bottom sheet**

## 5. Navigation（导航）·6 种对比

| 类型 | 用途 | 数量上限 | 移动端 |
|------|------|---------|-------|
| **Top bar** | 全局导航 | 3–7 项 | 折叠为 hamburger |
| **Sidebar** | 多层级（管理后台）| 无上限（分组）| 抽屉式 |
| **Tabs** | 同层级切换内容 | 2–6 项 | 可横向滚动 |
| **Breadcrumb** | 显示当前位置 | ≥ 3 层才用 | 折叠中间 |
| **Stepper** | 多步骤流程 | 3–7 步 | 顶部进度条 |
| **Pagination** | 列表翻页 | 分页 | 改 load more |

**Tabs 规则**：当前 tab 用**下划线 + 文字加重**（不要用底色块，太重）；8 个以上 → 转下拉或左侧 sidebar；必须 `role="tablist"`，键盘 ←→ 切换。

**Breadcrumb 规则**：当前页用 `BreadcrumbPage`（不可点）；分隔符 `/` 或 `›` 颜色 40% opacity；**移动端只显示"← 上一级"**。

## 6. List（列表）·5 种

| 类型 | 何时用 |
|------|--------|
| **Plain list** | 同质化文本（消息/通知）|
| **Card list** | 视觉强（商品/项目）|
| **Table** | 多列对比可排序（数据）|
| **Kanban** | 状态流转（任务/CRM）|
| **Timeline** | 时间顺序（日志/历史）|

**Table 规则**：
- 数字右对齐、文字左对齐、状态居中
- 行高 ≥ 44px，hover 整行底色高亮
- 表头 sticky，分页/虚拟滚动 > 1000 行
- 斑马纹 vs 横线：选一个；**密集表用斑马，稀疏表用横线**
- 排序 icon 始终占位（即使未激活），防止抖动

**If-Then**：
- 如果每行操作 > 3 → 折叠到 overflow `⋯` menu
- 如果列 > 7 → 提供列管理器或冻结首列
- **移动端 → 横向滚动 / 折叠成卡片，不要省略列**

## 7. Data Display（数据展示）

**类型**：KPI 卡 / Stat 卡 / Chart 容器 / Sparkline / Progress bar

**关键规则**：
- 数字字体用 `tabular-nums`（等宽数字），防止 2 和 8 错位
- KPI 数字 28–48px，单位 14–16px 小一号
- 趋势绿涨红跌（西方），**中国/亚洲反过来**——按地区切
- 货币符号紧贴数字：`$2,400.00`，**不要 `$ 2,400.00`**
- 大数字千分位：`1,234,567`；移动端可缩写 `1.23M`

## 8. Feedback（反馈）·4 种

| 类型 | 严重度 | 持续 | 位置 |
|------|--------|------|------|
| **Toast** | 成功/信息 | 3–5s 自动消失 | 右上/底部 |
| **Banner** | 系统级警告 | 持久 | 顶部全宽 |
| **Inline message** | 表单/区块内 | 持久 | 字段下方 |
| **Alert** | 模态级警告 | 持久至关闭 | 内嵌或弹窗 |

**Toast 规则**：
- 成功 3s / 信息 5s / 错误**不自动消失或 10s+**
- 同时最多 3 个堆叠，多余进队列
- `aria-live="polite"` 信息态 / `"assertive"` 错误态
- 必须可手动关闭，带 undo（关键操作）

**If-Then**：
- 如果操作可撤回 → toast + "Undo" 按钮（Gmail 模式）
- 如果是系统故障/限流 → banner，不要 toast
- 如果是字段验证错误 → inline，不要 toast

## 9. State（状态）·加载

**3 种加载态**（NN/g 阈值法则）：
- `< 1s`：**不显示任何 loading**（闪一下反而烦）
- `1–9s`：**spinner**（不知道总长时）/ **skeleton**（知道结构时）
- `≥ 10s`：**progress bar**（有进度）+ 文案"正在处理 23/100..."

**Skeleton 规则**：形状贴合最终内容（圆头像、矩形文字、宽度递减模拟段落）；用 `bg-neutral-200` + `animate-pulse`，**不要彩色 shimmer**（太花）；至少模拟 3 行，第三行宽度 60–80%。

**If-Then**：
- 已知结构（卡片/表格/列表）→ skeleton
- 未知或瞬时（提交按钮）→ inline spinner
- 文件上传/批处理 → progress bar + 百分比

## 10. Empty State（空态）·4 种

| 场景 | 文案重心 | CTA |
|------|---------|-----|
| **首次使用** | 教育"这里会显示什么" | "创建第一个" |
| **无搜索结果** | "试试别的关键词" | 清空筛选 |
| **无权限** | 解释原因 | 联系管理员 |
| **无网络** | 提示原因 + 重试 | 重新加载 |

**必含 4 件**：插画 / 标题 / 描述 / CTA。**不要只有"无数据"三个字**。
- 插画风格匹配品牌，**不要默认 illustration**
- 标题写**用户视角**（"还没有项目"），不是系统视角（"列表为空"）
- 描述说明"为什么是空"+"接下来做什么"
- CTA 只 1 个 primary + 可选 1 个 link

**If-Then**：
- 首次态 → 强引导，CTA 一定 primary
- 过滤后空 → 突出"清空筛选"而非"创建新的"
- 错误导致 → 转 Error 组件，不要伪装成 empty

## 11. Error（错误）·5 种

| 类型 | 出现位置 | 文案 |
|------|---------|------|
| **表单错误** | 字段下方 inline | 具体问题 + 修复 |
| **404** | 整页 | "找不到这页" + 返回 |
| **500** | 整页 | "我们的问题" + 重试/反馈 |
| **网络错误** | toast 或 banner | 自动重试 + 手动 |
| **权限错误** | 整页或 inline | 解释 + 联系/登录 |

**关键规则**：
- **永远说"我们"出错，不说"你"出错**（除非真是用户输入问题）
- 错误文案 3 段：发生了什么 + 为什么 + 怎么办
- 不要展示原始 stack trace、HTTP code（除非给开发者）
- 提供"复制错误 ID"按钮
- 404 页放**搜索框 + 主导航**，不要只放"回首页"

**If-Then**：
- 可恢复 → 显眼"重试"按钮 + 自动重试 3 次
- 需用户行动 → 写清楚下一步
- 表单错误 → 滚动到第一个错误字段并 focus

## 12. Pagination（分页）·4 种

| 类型 | 何时用 | 何时别用 |
|------|--------|--------|
| **页码** | 可定位（电商目录/搜索）| 流式内容 |
| **Load more** | 移动端/列表流 | 需跳到 100 页 |
| **Infinite scroll** | feeds/社交流 | 有 footer / 需跳页 |
| **Virtual scroll** | 列表 > 1000 行 | 短列表 |

**关键规则**：
- 页码组件至少含：← 上一页 / 1 / 2 / 3 / … / 99 / 下一页
- 当前页用强对比（filled 方块），其他 ghost
- **infinite scroll 必须保存滚动位置**（用户返回时回到原位）
- infinite scroll 必须有 footer 出口（"已加载全部"），否则用户永远摸不到底
- 显示总数："显示 21–40 / 共 1,234 条"

## 5 个跨组件通用原则

1. **每个交互组件穷举 6 态**：default / hover / active / focus-visible / disabled / loading。**少一个就是没做完**
2. **Token 化所有数值**：color、spacing（4/8 倍数）、radius、shadow、font-size 全部走变量。**禁止硬编码 `padding: 13px`**
3. **键盘可达**：tab 顺序、enter/space 触发、esc 关闭、↑↓ 导航。每个组件都跑一遍只用键盘的测试
4. **ARIA 默认到位**：button/dialog/alert/tablist 角色必加；图标按钮必须 `aria-label`；动态内容必须 `aria-live`
5. **响应式默认转换**：modal → bottom sheet、sidebar → drawer、horizontal tabs → scroll、table → card list。**移动端不是缩小版桌面端**

## 10 条"做组件必须记住"

1. Primary 按钮**一屏一个**，多了等于没有
2. Placeholder **不是 label**，永远写独立 label
3. 错误信息**永远 inline**，不要全靠 toast
4. Loading **分三段**（< 1s / 1–9s / ≥ 10s），不要一律 spinner
5. Empty state 必须 4 件套（插画/标题/描述/CTA），**禁止"暂无数据"**
6. 触控目标 **≥ 44×44**，hit-area 可超出视觉边界
7. 数字用 `tabular-nums`，**永远千分位**
8. Modal **focus trap + esc 关闭 + 焦点回原位**，三件事一件都不能少
9. Toast 错误态**不自动消失**或 ≥ 10s
10. 销毁性操作 = `destructive` 色 + **二次确认 + 写清后果**（"将删除 23 条记录"）

## 反面教材（绝对不要）

1. **用 placeholder 当 label**（2010 年代的烂梗）
2. **`onChange` 报错**（每打一字红一片 → onBlur 校验）
3. **modal 套 modal**（信息架构垮了，改多步流程或 sheet 堆叠）
4. **`alert("成功")` 或 `confirm()`**（浏览器原生弹窗一坨 → 一律自建 Dialog/Toast）
5. **空态写"暂无数据"**（等同于没写）

## 3 条"如果你只能记一条"

1. **每个组件先列状态机**：穷举 default/hover/active/focus/disabled/loading/error/empty 8 态，画完再写 CSS。**漏一个 = 组件半成品**
2. **永远 inline 校验、永远独立 label、永远 focus-visible**：这三条把 80% 的表单灾难挡在门外
3. **复制现成的设计系统**：shadcn/ui + Radix（结构）+ Tailwind（token）+ Lucide（图标）。**不要从 0 设计 Button**——你 2 周做的不会比 shadcn 三年迭代的好，把时间花在你产品独有的那 20% 组件上

## 资源 URL
- shadcn/ui 完整组件库（buttons/cards/dialog/forms/pagination/breadcrumb/tabs/skeleton/alert/sonner/progress）
- Radix UI Themes / Headless UI（focus trap 规范）
- Material Design 3 按钮规范（40dp/24dp/38% opacity disabled）
- Carbon（5 size 32/40/48/64/80px）
- Refactoring UI（层级/阴影/边框）
- NN/g（loading 1s/9s/10s 阈值、checkbox vs radio、dropdown 慎用）
- Smashing Magazine（placeholder 反模式）
