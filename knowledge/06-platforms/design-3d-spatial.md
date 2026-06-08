---
name: design-3d-spatial
description: 3D / 空间设计 - visionOS / Apple Vision Pro / 注视捏合拖动手势 / 玻璃材质 / 深度层级 / 空间音频 / 5 真实 visionOS 应用拆解
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
  addedDate: 2026-06-06
---

# 3D / 空间设计（visionOS / Apple Vision Pro）· 执行手册

## 一句话总结
**空间设计不是 3D 化的 2D，而是"用户在物理空间里用眼睛+手和内容交互"**。visionOS 把 iOS 的触控换成"注视+捏合"，把窗口从边框释放到空气中，把"系统控件"变成"周围存在"。做对的人让 6 米宽的虚拟屏不挡你的客厅；做错的人把 2D 卡片浮起来当 3D 用，结果用户晕、累、找不到按钮。

## 1. visionOS 范式：3 种窗口模式

Apple 官方反复强调"3 种窗口，每种有专属场景"，不是随便用：

| 模式 | 沉浸度 | 用例 | 实际感受 |
|---|---|---|---|
| **Window** | 0% | 文档/编辑/工具 | 边长固定（如 60cm×45cm），固定方向，可重定位 |
| **Volume** | 30% | 3D 模型浏览/小游戏/预览 | 3D 内容在立方体里，可旋转，用户绕着看 |
| **Space (Immersive)** | 100% | 沉浸式娱乐/创作 | 全场景 3D 环境，背景是环境音 + 360° 内容 |

**铁律**：
- 不要把 2D 网页塞进 Window 模式当"visionOS 应用"——那只是 2D 屏幕换位置
- Volume 适合"看一个物体"（产品预览、3D 模型、地图），不适合"操作多个列表"
- Space 是终极沉浸，错了 100% 失败（晕动症 + 用户不知道怎么退出）

## 2. 三种基础手势

visionOS 没有触控。所有交互都是**注视 + 手势**：

### 注视（Gaze）
- 眼睛看哪里 = 鼠标悬停
- 注视停留 ~0.3-0.5s = 触发悬停态
- **必须有悬停态反馈**（如按钮高亮、scale 1.05），否则用户不知道在看什么
- 辅助功能：Voice Control 用户可"用嘴注视"（"Look at..." → 切换到眼动）

### 捏合（Pinch）
- 拇指+食指捏合 = 点击
- 区分：单击（捏一下）/ 双击 / 长按
- 距离 30-60cm 时识别最准，过远识别不到
- **永远给"按下"反馈**：scale 0.95 + haptic（Apple Watch 那种短促振动）
- **永远给"完成"反馈**：scale 1.0 + 动画

### 拖动（Drag）
- 捏住不松 + 移动 = 拖
- 必须有"被抓住"反馈：opacity 0.7 + 高亮边框
- 拖动时窗口/物体有"惯性"（松手后继续移动 ~200ms）

**反模式**：
- 用"注视 1 秒"代替"捏合"——> 用户累（眼肌肉疲劳 = 真实数据）
- 没有悬停态——> 用户不知道系统在响应
- 没有"完成"反馈——> 用户重复捏合，触发多次操作

## 3. 深度层级（Z 轴 5 层）

visionOS 有 5 个 Z 轴距离，从远到近：

| 层级 | 距离用户 | 用例 | 视觉处理 |
|---|---|---|---|
| **Background** | 5m+ | 环境（天空、远景） | 无阴影，无聚焦 |
| **Midground** | 2-3m | 第二窗口、辅助信息 | 轻阴影（opacity 0.3） |
| **Primary Window** | 1.2-1.5m | 主工作窗口 | 软阴影 + 玻璃背景 |
| **Float UI** | 0.6-0.8m | 工具栏、菜单、弹窗 | 重阴影（opacity 0.5）+ 玻璃 |
| **Foreground** | <0.5m | 警示/确认/手部 UI | 不透明背景，禁用 backdrop blur |

**核心原则**：
- Z 越近 = 视觉权重越大 + 越不可逆
- 浮窗（Float UI）覆盖主窗口时，**主窗口必须 dim 30%**——否则用户迷失
- Z 距离必须物理合理：把 5m 远的内容拖到 0.5m，会触发晕动症

## 4. 玻璃材质（GlassMaterial）

visionOS 的标志性视觉：透明磨砂玻璃。

```swift
// SwiftUI 代码
.glassBackgroundEffect()
.glassBackgroundEffect(displayMode: .always)  // 永远显示
.glassBackgroundEffect(displayMode: .implicit)  // 内容越深越透明
```

**设计原则**：
- 玻璃背景 = 浅色（dark mode 下黑灰）+ 高斯模糊（radius ~40px）+ 1px 内描边（白色 10% opacity）
- **不要把玻璃当 UI 装饰滥用**——> Apple 在 visionOS 2 之前就批评过"glass everything"是 slop
- 玻璃在 5m 远处几乎透明，<1m 才有明显效果——> 强制用 Z 距离分层
- 玻璃 + 高对比文字（#FFFFFF on dark glass）= 4.5:1 ✓ / 低对比（#888 on glass）= 失败

## 5. 空间音频（Spatial Audio）

visionOS 默认有空间音频。声音从 3D 空间里"那个位置"传来。

**5 条铁律**：
1. **重要反馈必须有声**——> 用户眼睛可能看别处（多窗口、房间另一人）
2. **错误/成功用不同音调**——> 错误低频（200-400Hz），成功高频（800-1200Hz）
3. **3D 定位要准**——> 按钮在右侧 = 声音从右侧来（HRTF 算法）
4. **不要同时 >3 个声源**——> 用户分不清，烦躁
5. **永远给"静音"开关**——> 公共场合用、录音时用

**反模式**：
- 默认开 7.1 环绕声——> 别人（不戴 Vision Pro 的人）会反感
- 用铃声当通知音——> 像手机响；用柔和的"叮"声
- 沉浸式场景里 360° 不断变化的背景音——> 5 分钟就开始累

## 6. 5 个真实 visionOS 应用拆解

### (1) Apple Vision Pro 原生 "Photos"
- **窗口**：Window 模式 + 居中 + 1.2m
- **3D Photos**：双击照片 → 立体展开，1.5m 距离
- **Spatial Audio**：照片里的人"在你面前"说话（用 iPhone 15 Pro 拍的空间视频）
- **学到的**：3D 内容必须**主动触发**（双击），不能默认展开——> 默认展开用户就晕

### (2) Disney+ on Vision Pro
- **模式选择**：先在 2D 选电影，然后可选 2D 窗口或全沉浸（泰山、曼达洛人场景）
- **环境音**：环境主题（Endor 森林、银河系天空）持续播放，可调音量
- **学到的**：内容**渐进沉浸**，不要一进去就全屏 360°

### (3) JigSpace（3D 模型浏览）
- **Volume 模式**：3D 物体在 60cm³ 立方体里
- **双手缩放**：双捏合 = 等比缩放（区别于 2D 的 pinch-zoom）
- **标注系统**：3D 钉子 = 部件名称，"用眼睛看 + 单击"= 弹出说明
- **学到的**：3D 模型必须**可旋转**（不锁死角度），否则用户迷失方位

### (4) MindNode（思维导图）
- **无限画布**：可扩展到整个房间
- **节点捏合拖动**：3D 中拖动节点，眼动会跟丢，所以节点拖动时**显示轨迹线**（200ms 残影）
- **缩略图导航**：右下角永远有 minimap（Window 模式不沉浸）
- **学到的**：3D 大画布必须有"导航锚点"（minimap / 鸟瞰模式）

### (5) Pocket Yoga（瑜伽教学）
- **半沉浸**：教练 3D 化身在 2m 距离，跟随练习
- **空间音频**：教练声音从正前方
- **错误检测**：Vision Framework 检测你的姿态（用 ML 模型）
- **学到的**：实时反馈用 Vision Framework = 用户**自我纠正**比教练口头说更有效

## 7. 与 2D 设计的 6 大差异

| 维度 | 2D 屏幕 | visionOS 空间 |
|---|---|---|
| **视场** | 100% 屏幕 | 周围 360°，主视场 ~100° |
| **焦距** | 固定 50-60cm | 动态 0.5m-5m |
| **交互** | 手指触控 | 注视+捏合+语音 |
| **持续时间** | 8 小时工作 | 30 分钟开始累（眼/颈） |
| **背景** | 不存在 | 物理房间 |
| **多任务** | 多个窗口分屏 | 多个窗口在 3D 空间散开 |

**设计含义**：
- **30 分钟原则**：3D 沉浸任务设计不要超过 30 分钟，超过必须给"返回"提示
- **物理房间优先**：UI 永远不应该把用户"困在"虚拟空间里——> 永远显示"退出到房间"按钮
- **多次退出机会**：沉浸应用至少 3 个退出路径（按钮、语音、手势）

## 8. 9 条反模式（看到 X 必改）

1. **3D 化的 2D**——> 把卡片浮起来当 3D 用，没有 Z 轴逻辑
2. **永远全沉浸**——> 一进去就 360°，用户晕 + 不知道怎么退
3. **注视 1 秒触发**——> 眼肌肉疲劳，10 分钟用户就累
4. **玻璃滥用**——> 任何 UI 都用 glassBackgroundEffect = 视觉噪声
5. **悬停态缺失**——> 用户不知道系统在响应他的注视
6. **强光颜色**——> 纯红/纯蓝/纯紫在 3D 空间里很刺眼
7. **小字号**——> < 14pt 在 1.2m 距离几乎看不清
8. **平面贴图**——> 用 2D JPEG 假装 3D 模型（"3D" 按钮 + 静态图片）
9. **没有退出**——> 沉浸应用只有 1 个退出按钮 = 用户怕进去

## 9. SwiftUI 实战代码模板

### 基本窗口
```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .windowResizability(.contentSize)  // 边长固定
    }
}
```

### Volume 模式（3D 物体）
```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultSize(width: 0.6, height: 0.6, depth: 0.6)  // 60cm³
        .windowResizability(.contentSize)
    }
}
```

### Immersive Space（沉浸式）
```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
        ImmersiveSpace(id: "Space") {
            SpaceView()
        }
        .immersionStyle(selection: .constant(.full), in: .full)
    }
}

// 切换
await openImmersiveSpace(id: "Space")
await dismissImmersiveSpace()
```

### RealityKit 3D 实体
```swift
import RealityKit
import RealityKitContent

let modelEntity = try await Entity(named: "Robot")
modelEntity.position = [0, 0.5, -1.0]  // 0.5m 高，1m 远
modelEntity.components.set(InputTargetComponent())  // 可交互
modelEntity.generateCollisionShapes(recursive: true)
content.add(modelEntity)
```

### 注视 + 高亮
```swift
.modelEntity(modelEntity) { event in
    switch event {
    case .focusChanged(let isFocused):
        if isFocused {
            modelEntity.scale = SIMD3<Float>(repeating: 1.05)
        } else {
            modelEntity.scale = SIMD3<Float>(repeating: 1.0)
        }
    }
}
```

## 10. 10 条"如果你在做空间设计，记住这些"

1. **3 种模式有专属场景**——> Window/Volume/Space 别混用
2. **注视 + 捏合 = iOS 触控的演化，不是替代**——> 思维模型要 iOS 化
3. **30 分钟原则**——> 沉浸任务不要超过 30 分钟
4. **物理房间永远存在**——> UI 不能让用户感觉被困
5. **多次退出机会**——> 至少 3 个退出路径
6. **Z 距离要物理合理**——> 5m 远到 0.5m 触发晕动症
7. **悬停态是必做**——> 没有悬停 = 没有反馈 = 失败
8. **空间音频是默认**——> 重要反馈必须有声
9. **小字号 < 14pt 失败**——> 在 1.2m 距离几乎看不清
10. **永远不要 100% 沉浸起手**——> 让用户选择进 360° 模式

## 5 条反面教材

1. **一个 2D 仪表盘浮起来当 visionOS 应用**——> 这是 AR 化的 2D，不是空间设计
2. **用眼动代替点击**——> 10 分钟用户眼肌肉就累
3. **一进去就全屏 360°**——> 用户不知道是按了什么进、退不出
4. **玻璃背景 + 玻璃文字**——> 完全看不清
5. **3D 物体没有阴影**——> 漂浮感太强，用户不知道距离

## 5 条"如果你只能记一条"

1. **空间设计 = 用户在物理空间里和内容共存**——> 不是"屏幕变立体"
2. **注视 + 捏合 + 拖动**——> 这就是新"触控"
3. **30 分钟原则**——> 超过 30 分钟必须给"返回现实"提示
4. **5 个 Z 层级**——> 5m / 2-3m / 1.2-1.5m / 0.6-0.8m / <0.5m
5. **永远给退出路径**——> 至少 3 个，让用户不害怕进去

## 资源 URL
- developer.apple.com/visionos/ — visionOS 官方文档
- developer.apple.com/wwdc/sessions/?q=vision — WWDC visionOS sessions（2023-2025 全部）
- developer.apple.com/documentation/realitykit — RealityKit API
- developer.apple.com/design/human-interface-guidelines/visionos — HIG for visionOS
- realitykit.dev/ — 社区资源
- sketchfab.com/vision-pro — Vision Pro 3D 模型库
- polyhaven.com/ — 3D 资产 + HDR 环境
- arkit.apple.com/documentation — ARKit 互补
- visionprodeveloper.com/ — 第三方开发者博客
- github.com/topics/visionos — 真实开源 visionOS 应用

## 跨引用
- [design-app-platforms.md](design-app-platforms.md) — iOS HIG / visionOS / watchOS 平台约定
- [design-motion-microinteractions.md](design-motion-microinteractions.md) — 3D 动画曲线
- [design-accessibility.md](design-accessibility.md) — 空间辅助功能
- [design-ai-products.md](design-ai-products.md) — 空间 AI 代理
- [design-philosophy-photography.md](design-philosophy-photography.md) — 空间构图 / 景深
