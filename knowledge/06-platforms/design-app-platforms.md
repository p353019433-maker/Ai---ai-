---
name: design-app-platforms
description: App 平台设计语言 - iOS HIG / Material You / visionOS / watchOS 的真实约定 + native vs custom 决策 + 跨平台策略
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# App 平台设计语言

## 一句话总结
每个平台都有几十年的隐式约定、显式规范、动效方言和系统字体；"不 native"的根本原因是把这些约定当可选项，而不是把"属于这个平台"当作产品的入门门槛。

## 一、iOS HIG 三大核心原则
来源：1987 Mac 时代奠基至今（[en.wikipedia.org/wiki/Human_Interface_Guidelines](https://en.wikipedia.org/wiki/Human_Interface_Guidelines)）
1. **Clarity（清晰）**——内容主导，装饰退后
2. **Deference（顺从）**——UI 不抢内容风头
3. **Depth（深度）**——用层次、动效、视差表达内容关系

**iOS 历史三次大转向**：
- iOS 7（2013）Jony Ive 去拟物化 → 扁平+半透明+视差
- iPhone X（2017）全面屏手势
- iPhone 14 Pro（2022）Dynamic Island 把硬件开孔演化为软件控件

**2025+ 做 iOS app 意味着**：
- 使用 **SF Pro**（iOS 9 取代 Helvetica Neue）
- 尊重安全区 + Home Indicator
- 不把内容塞进状态栏
- 用 NavigationStack push/pop（从右向左滑入）
- 用 **Tab Bar**（3-5 个）而非顶部 tab
- 用 **SF Symbols** 不用自定义图标栅格
- 按钮圆角 10pt（iOS 11+ 默认）
- **Dynamic Type** 让用户字号偏好穿透全应用

| 元素 | iOS 约定 |
|---|---|
| 顶部栏 | NavigationBar（push/pop 层级） |
| 底部导航 | TabBar 49pt |
| 模态 | Sheet 从底部上滑 |
| 列表行 | 圆角矩形 56-60pt 高，17pt 文本 |
| 主色 | systemBlue 等系统色，**不硬编码 hex** |
| 字体 | SF Pro 17pt body / 13pt caption |

## 二、Material You（Material 3）—— 把品牌色权力交回用户
2021 Google I/O 公布，2021.10 随 Android 12 首发。

**核心转变**：通过 "monet" 系统从用户壁纸自动提取主色，生成 Tonal Palette 应用于系统+应用（[Material Design wiki](https://en.wikipedia.org/wiki/Material_Design)）。

**规则**：
- 颜色用 **Key Color + Tones 0-100** 表达，主色 40、辅色 40 默认
- 排版用 **Roboto Flex**（12 个可变轴：weight/width/optical size/slant/grade/ascender/descender/italic 等）
- 形状 7 档圆角（None / Extra Small / Small / Medium / Large / Extra Large / Full）
- 50+ 组件（按钮、卡片、FAB、NavigationBar、NavigationRail、NavigationDrawer）
- **Material 3 Expressive**（2025.5 Android Show）：more colorful and fun，改进动效（[Material 3 Expressive](https://en.wikipedia.org/wiki/Material_3_Expressive)）

| 元素 | Material 3 约定 |
|---|---|
| 顶部栏 | TopAppBar（小/中/大） |
| 底部导航 | NavigationBar 80dp（3-5 项） |
| 侧边导航 | NavigationRail 80dp（折叠屏/平板） |
| 主操作 | **FAB** 浮动按钮 |
| 列表行 | 56dp 网格，左图标+文本+尾 |
| 字体 | Roboto Flex（可调轴） |
| 圆角 | Medium 12dp 默认 |
| 主题色 | Tonal Palette 从壁纸生成 |

## 三、visionOS 空间设计
基于 iPadOS 框架派生的 3D UI OS（[visionOS wiki](https://en.wikipedia.org/wiki/visionOS)）。

**三大输入范式**：
- **眼动 + 捏合**（看哪儿+捏手指）
- **手部追踪**（直接戳空中 UI）
- **语音**（Siri 与听写）

**核心设计语言 = 玻璃（Glass）**：
- 5 档透明度 `.ultraThinMaterial` → `.thickMaterial`
- 深度用 z 轴分层（远 = 更大模糊 + 更低不透明）
- **焦点（Focus）**：眼睛注视自动显示柔和辉光焦点环
- 主内容约 1 米远的舒适焦点区
- 空间音频定位
- 4 档沉浸：Windowed / Mixed（带透视）/ Progressive / Full

**真正属于 visionOS**：
- 不把 iOS app 直接打包移植
- 用 **Volumes 和 3D 实体**（RealityKit）
- 不用 2D alert 弹窗，用悬浮玻璃面板
- 内容有深度梯度，不要全贴 z=0 平面

## 四、watchOS 极简约束
**核心 = "瞥一眼"**——抬腕 1-2 秒拿到信息。

**核心交互硬件**：
- **Digital Crown**（旋转滚动、按下返回）
- **Side Button**（App Dock / Friends）
- **Force Touch**（watchOS 7 移除）
- **Complications**（表盘小信息块）

字体是 **SF Compact**——比 SF Pro 更扁、字间距更大，专为小屏。

**真正属于 watchOS**：
- 一次只做一件事（不要 iOS 多层级）
- 列表行高 ≥ 44pt
- 文本**永远不要滚出屏幕**
- 通知"短到抬腕读完"
- 颜色高对比（深色背景 + 高饱和前景）
- 动效要轻（< 200ms cross-fade）

## 五、4 平台对比表

| 功能 | iOS | Android (Material 3) | visionOS | watchOS |
|---|---|---|---|---|
| 顶部导航 | NavBar + back | TopAppBar + up | 浮动玻璃面板 | 不可用 |
| 底部导航 | TabBar 49pt | NavBar 80dp | Orbit / glass TabView | TabView in List |
| 侧边导航 | 不可用 | NavRail（折叠/平板） | 空间环绕 | 不可用 |
| 模态 | Sheet（卡片/全屏） | BottomSheet / Dialog | Floating glass | Modal full |
| 滑动手势 | 边缘右滑=返回 | 系统返回（手势/虚拟键） | 捏合+推 | Digital Crown |
| 长按 | context menu | contextual action | 不可用 | 不可用 |
| 主操作 | NavBar 右上 | FAB | 浮动按钮 | 主屏大圆图标 |
| 删除/危险 | 左滑 Delete | 长按弹菜单 | glass 内嵌 | Force Press（弃） |
| 字体 | SF Pro 17pt | Roboto Flex 16sp | SF Pro Rounded | SF Compact 16pt |
| 系统色 | systemRed/Blue | Material Color Scheme | systemBackground glass | 单一 accentColor |
| 刷新 | 下拉刷新 | 下拉 + SwipeRefresh | 不可用 | 不可用 |
| 振动 | Taptic Engine | Vibrator API（粗粒度） | 不可用 | Haptic（数字表冠） |

## 六、Native vs Custom 决策卡

**优先系统控件**：
- 平台核心控件（iOS TabBar/Switch/Slider；Android FAB/Snackbar/TextField）
- 需要平台能力（Dynamic Type、Switch 物理感）
- 承担无障碍职责（VoiceOver、TalkBack、Switch Control）

**可自定义**：
- 平台无等价物（3D 地图、画布工具、复杂数据可视化）
- 全新交互范式（绘图 app 笔刷面板）
- 强品牌诉求（但仍要遵守基础规范）

**判断（评分卡）**：
- 80%+ 顶级 app 用同样方式实现？→ native
- 自定义后用户能更少步骤？→ 否则用 native
- 自定义后承担平台无障碍/状态变化责任？→ native
- 设计师能写出所有状态 spec？→ 否则 native

**反例**：用 div+CSS 模拟 iOS Switch → touch target 偏小、VoiceOver 不会说"switch, on"、长按不触发平台菜单。

## 七、动效方言
**iOS = Spring**：
- dampingRatio / response / initialVelocity 三参数
- 可中断、可反转、有质量感
- SFSymbols 自带 bounce，按钮按下 scale 0.97
- 性格：**弹性、惯性、跟手**

**Material = Easing Curves**：
- 4 档 cubic-bezier（标准/加速/减速/线性）
- Container Transform（FAB→App Bar）、Shared Axis（X/Y/Z）、Fade Through、Fade
- 性格：**弧线、明确方向、"从这里到那里"**

**watchOS**：< 200ms cross-fade，不用 spring
**visionOS**：spring 适用但避免大尺度移动（防晕动症）

| 维度 | iOS | Material 3 |
|---|---|---|
| 核心数学 | Spring physics | Easing curves |
| 标准时长 | 250-350ms | 200-500ms |
| 列表删除 | 左侧滑出 | 滑出 + undo snackbar |
| 打开详情 | Push 从右 | Shared Axis Z |
| 错误反馈 | Shake + Haptic | Shake + Snackbar |
| 物理特性 | 有质量、可中断 | 不可中断、确定性 |

## 八、7 条"属于这个平台"规则
1. **遵守系统隐喻层级**：iOS 卡片从边缘滑入，Material 共享元素从中心放大
2. **用系统字体**：不引外部字体，至少不引超过两款
3. **遵守安全区与留白**：iOS 顶 44pt 底 34pt；Android 状态栏透明 padding 16dp；visionOS 主内容离用户 1 米
4. **用系统导航隐喻**：iOS push/pop、TabBar；Android up + NavBar/Rail；watchOS Crown；visionOS 浮窗
5. **接系统动效方言**：iOS spring、Material 共享元素，**不照抄 CSS cubic-bezier**
6. **让用户系统偏好穿透**：Dynamic Type、字号、深色模式、Reduce Motion、对比度增强
7. **用系统能力而不是绕开**：Live Activities、Widgets、App Intents、App Clip；Android Glance、Quick Settings、Material You Monet

## 7 条"不 native"反例
1. **全宽按钮 + 系统色背景**：Material 3 FAB 应是浮动圆形 56dp，不是 iOS 风格胶囊
2. **顶部横向 tab 切换**：iOS 肌肉记忆是底部 TabBar
3. **"汉堡菜单"独占主导航**：HIG 明确反对；Material 早用 NavBar/Rail/Drawer 替代
4. **左上"返回"按钮**：iOS 返回跟随 push 层级；Android Up 跟随父级；混用让用户跨级
5. **CSS box-shadow + 1px 边框 + 6px 圆角**：iOS 11 起转大圆角+半透明；Material 用 elevation 1-5
6. **下拉刷新用"整页淡出"**：iOS indicator 在 NavBar 下；Material 顶部进度条
7. **Toast 长期停留 5+ 秒**：Material Snackbar 默认 4-10s；iOS 没用 Toast 只有 Banner

## 跨平台策略（RN / Flutter / KMP）
1. **抽象只到 30%**：业务逻辑抽到共享代码，UI 永远写两份
2. **平台无关 token + 平台相关渲染**：颜色间距 token 共享，按钮列表 tab 渲染平台相关
3. **避免"全屏自定义画布"**：Flutter Skia / RN Skia 自绘"伪 native"
4. **设计 system 分两套"皮肤"**：Material skin + Cupertino skin
5. **用户系统设置穿透**：字号/Reduce Motion/深色模式必须接 native API
6. **KMP 走"业务共享 UI native"**：Compose Multiplatform 适合 Android 重度
7. **关键交互用 native 库**：导航/相机/地图/支付用 platform SDK

## 系统字体历史速记
- **SF Pro**（2014.11）：Apple 20 年来第一个新字体（[SF Pro wiki](https://en.wikipedia.org/wiki/SF_Pro)），基于 Helvetica/FF DIN/Roboto/Arial；20pt+ 用 Display（紧），20pt- 用 Text（松）
- **SF Compact**：watchOS 专用，更扁、字间距更大
- **Roboto Flex**：12 个可变轴（[Roboto wiki](https://en.wikipedia.org/wiki/Roboto_(typeface))），强调"扩展"（区别于 Roboto VF 的 1:1 复刻）
- **不要把 Inter 当 native 字体**：是 web 字体，会让 native app 有 web 感
- **永不在 Android 用 SF Pro**（违反 Apple EULA + metric 不对）
