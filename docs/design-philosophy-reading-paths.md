---
name: design-philosophy-reading-paths
description: 视觉层级/阅读路径/色彩相互作用/错觉 - 循环3 深度补充
metadata: 
  node_type: memory
  type: project
  originSessionId: 3f38aac3-2f3d-4319-970a-92f048d2d27d
---

# 视觉层级 / 阅读路径 / 色彩相互作用（循环3深度补充）

## F-Pattern 扫描研究（NN/g）
- 第一行水平扫读（content area 顶部）
- 第二行较短水平扫
- 沿左侧垂直扫
- **首行比后续行获得更多注视**
- **每行首几个词获得更多注视**

## 其他扫描模式
- **Layer-cake**：只扫标题/子标题，跳过正文
- **Spotted**：找特定项（链接、数字）
- **Marking**：滚动时固定（移动端常见）
- **Bypassing**：跳过重复的起始词
- **Commitment**：全文阅读（少见，深度参与时）

## F-Pattern 出现条件
- 文本无格式
- 用户追求效率
- 用户参与度不高

## 80/20 关键发现
- **80% 注视在页面左半**
- 20% 在右半
- 搜索结果页：94% 在左半
- **设计含义**：
  - 关键内容放左半
  - 最左留导航
  - 次要内容放右
  - 左导航已被用户学会——可不注视即识别

## 视觉层级五元素（综合）
- **Color 颜色**（hue / saturation / value / texture）
- **Size 大小**
- **Alignment 对齐**
- **Character 形状复杂度 / pattern 对比**
- **Isolation 孤立**

## 视觉权重 (visual weight)
- 大元素吸引注意
- 孤立元素（Von Restorff）吸引注意
- 高对比吸引注意
- 色彩鲜艳吸引注意
- "Small, high contrast elements have as much impact as larger, duller elements"

## 焦点 (focal point)
- 通过 isolation 创造
- 控制要素：color / size / alignment / character
- 设计师"指挥眼睛按特定顺序移动"

## 视觉平衡
- 对齐 + 负空间 = 平衡
- 孤立元素在大白空间中比在一群元素中更突出
- **眯眼测试**：脱焦看 gestalt 模式

## Bezold Effect
- 命名自 Wilhelm von Bezold（1837-1907）
- 一处小色块变化 → 影响周围颜色感知
- 小而散布的颜色 → 混合/扩散效果
- 大而相邻的颜色 → 强化对比
- 含义：**色彩感知是相对的，context matters**

## 色彩恒常性 (color constancy) 现象
- 同色卡片在不同背景下"看似不同"
- **Checker shadow illusion**：A 看似比 B 暗，实际同灰度
- **Land effect**：从黑白透明片叠加彩色滤镜可感知全色
- **Double-opponent cells**：初级视皮层计算局部锥体活动比
- **Metamerism**：两个不同光谱刺激看起来同色

## Müller-Lyer 错觉
- 大脑依赖过去视觉经验
- 构造 3D 模型解释 2D 图像
- "size constancy" 把物体投影到预期距离
- 视觉系统快速评估深度线索 → 误判
- 关键：周围上下文剧烈影响主体感知
- "spatial pooling of positional signals evoked by neighboring object parts"
- 整体先于部分（"the whole figure is the primary determinant"）

## 视觉注意力（神经科学）
- **Spotlight 聚光灯模型**：可移动的光束
  - Focus：高分辨率处理区
  - Fringe：粗处理
  - Margin：外边界
- 额叶眼动区 + 背外侧前额叶皮层
- 顶叶皮层（侧顶内区）含 saliency maps
- **外源性注意**：自下而上的 saliency map
- 注意力网络：alerting / orienting / executive

## Stroop 效应
- 颜色词与墨水颜色冲突 → 反应变慢
- 注意力选择与自动加工的冲突
- 含义：UI 标签颜色与文字含义不符会拖慢用户

## 鸡尾酒会问题
- Colin Cherry dichotic listening studies
- 注意能在多通道中选择
- 含义：UI 可用声音、视觉、触觉多通道

## 色彩跨文化
- **红**：西方=爱情/危险；中国=好运/婚礼；古中国/埃及=死亡
- **白**：西方=纯洁（婚礼）；亚洲=死亡/哀悼
- **绿**：全球=自然/治愈/健康
- **黑羊**：多数文化=被排斥；意大利=自信
- **警告色**：马来西亚=绿；美国=红
- **股市颜色**：东亚与西方相反
- **嫉妒色**：比利时/美国=绿；德国/俄国=黄
- **设计含义**：国际化产品必查目标文化

## 对 AI 去 AI 化的启示
1. **左半优先**：AI 默认居中/对称 = 违反 80/20 规律
2. **F-pattern 出现条件**：AI 给"无格式大段文字"= 触发 F = 难看
3. **大段首词最被注意**：标题/CTA 前几个字最重要
4. **Bezold 效应**：AI 给"和谐配色"未必好，context 决定
5. **Checker shadow 错觉**：永远要看实际应用，不要信色卡
6. **Müller-Lyer**：箭头/装饰的"角度"会改变对长度的感知
7. **Spotlight 模型**：动画应引导 spotlight，而不是平铺
8. **多通道**：色彩 + 形状 + 文字 + 位置 = 色盲友好
9. **跨文化**：全球化产品必查每个市场
10. **AI 不懂"孤立"**：AI 喜欢对称 = 没有孤立 = 没有焦点 = 没有层级

## 来源
2026-06-03；NN Group F-pattern / NN Group 80/20 水平注意 / Wikipedia (Color constancy / Bezold effect / Müller-Lyer / Visual attention / Color symbolism / Visual hierarchy)
