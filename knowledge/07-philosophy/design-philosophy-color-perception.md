---
name: design-philosophy-color-perception
description: 色彩学与视觉感知 - 色彩心理学/Gestalt完形/UX定律/眼动/认知负荷 - 循环3研究
metadata: 
  node_type: memory
  type: project
  originSessionId: 3f38aac3-2f3d-4319-970a-92f048d2d27d
---

# 色彩学与视觉感知（循环3）

## 色彩心理学
- 红：唤起 + 紧迫感（冲动消费）
- 蓝：信任 + 放松（理性决策）
- 黄：快乐 + 温暖
- 绿：环保 + 可靠
- 紫：复杂感
- **关键数据**：90 秒内 62-90% 的判断来自颜色
- **文化差异**：中英审美差异大；红色"愤怒"跨文化；紫色"嫉妒"只在波兰文化中
- 暖色=冲动购买；冷色=理性决策

## 视觉感知
- 眼睛先看**高对比区**
- 注意力是"attentional selection"——选择部分视觉输入做深处理
- 脸是"peripheral 视野里最吸引人的搜索图标"
- 眼动类型：fixation (静态) / saccade (扫视) / pursuit (追踪) / vergence (聚散)
- **Gesalt 原则**自动组织视觉：proximity/similarity/closure/symmetry/common fate/continuity/good Gestalt/past experience

## Gestalt 完形原则（设计黄金法则）
1. **Proximity 接近**：相近 = 一组
2. **Similarity 相似**：形状/颜色/大小相似 = 一组
3. **Closure 闭合**：不完整 = 大脑补完
4. **Symmetry 对称**：围绕中心点组织
5. **Continuity 连续**：沿最光滑路径
6. **Common fate 共同命运**：同向运动 = 一组
7. **Figure-Ground 图形-背景**：前景/后景分离

## Von Restorff Effect 隔离效应（1933, Hedwig von Restorff）
- 同质元素中**不同**的最被记住
- 例：购物清单中**绿色高亮**的那项
- **设计应用**：
  - 教育：色彩/粗体/对比格式强调关键信息
  - 品牌：从竞品中视觉跳出
  - **设计层级的基础**：唯一不同的元素 = 最重要

## 黄金比例
- 真实自然界存在（叶序、贝壳）
- Le Corbusier、Salvador Dalí 都用
- 但！**数据拟合有时"可疑"**——帕特农神庙/金字塔的拟合是有争议的
- **设计原则**：信眼不信公式；context 比数学更重要

## 三大 UX 定律
### Hick's Law (1952)
- **T = b × log₂(n+1)**
- 选项越多决策越久（对数级）
- 例外：熟悉刺激、扫视、结构化序列
- 设计：分步决策，每步 ≤ half（二分搜索）

### Fitts's Law (1954)
- **MT = a + b · log₂(2D/W)**
- 移动时间 = 距离/宽度比
- **设计应用**：
  - 按钮越大越好
  - 关键按钮放屏幕**边缘**（边缘"无限长"）
  - "Magic corners" 边角 = 理论上无限大按钮
  - macOS 顶栏 / Windows 左下角都是此原则
  - 上下文菜单在光标位（prime pixel）

### Miller's Law (1956)
- 工作记忆 7±2 块（后续研究 ≈4）
- **Chunking 切块**：把信息归组
- 设计：导航 ≤ 7 项、流程 ≤ 7 步、表单字段分组

## 序列位置效应
- 头尾记得最牢（primacy/recency）
- 设计：重要项放菜单首/末

## 色彩对比
- 视觉对**相对差异**比**绝对亮度**更敏感
- "周边抑制"：中心蓝 + 白底 = 周边黄
- 视网膜节细胞：中心+外周双向反应
- 含义：**不要相信色卡，要看实际应用效果**

## 色彩盲
- 红绿色盲最常见：男性 8% / 女性 0.5%
- 类型：Monochromacy（完全）/ Dichromacy（二色：protanopia/deuteranopia/tritanopia）/ Anomalous trichromacy
- **设计铁律**：永远用 **色彩 + 形状/图案/大小/位置** 多通道传达
- 同时用**亮度对比**（明度差异）和**色相对比**（色相差异）

## 认知负荷
- **Intrinsic 内禀**：材料本身难度（不可消除）
- **Extraneous 外在**：呈现方式（设计师可控）
- **Germane 相关**：图式构建（应增加）
- **设计目标**：消除 split-attention、用视觉代替文字、worked examples 优于 problem solving

## 色彩理论
- **RYB 模型**（传统）：红黄蓝为原色
- **RGB 模型**（加法）：红绿蓝
- **CMYK**（减法，用于印刷）
- **次色 = 两原色等量混合**
- **三原色等量 = 灰**（饱和度递减）
- **三次色 = 原色 + 次色**

## 对 AI 去 AI 化的启示
1. **不要全用所有对比**：一页最多 1-2 个对比（Itten 七对比里挑 1）
2. **重视唯一性**：Von Restorff 告诉你——让 1 个元素显著不同比所有元素都"差不多好看"更高级
3. **利用 Miller 限制**：导航 7 项、菜单 5-7 项，AI 喜欢全展开
4. **Hick 反例**：分步代替一次性给所有选项
5. **Fitts 应用**：主 CTA 一定要大、要在视觉动线终点
6. **色彩心理反 AI 套路**：紫粉渐变不是"科技感"——AI 错把"鲜艳=未来"
7. **眼睛先看对比**：title/CTA 必须有强对比
8. **F/Z 模式**：Web hero 左对齐，左上放关键信息
9. **色彩盲友好**：加图标/形状，不要只靠颜色
10. **信眼不信公式**：黄金比例是参考，AI 给你的"黄金分割"可能毫无意义

## 来源
2026-06-03；参考：Wikipedia (Color Psychology / Visual Perception / Gestalt / Golden Ratio / Hick's law / Fitts's law / Miller's law / Serial position / Color blindness / Cognitive Load / Contrast / Primary color / Tertiary color / Von Restorff)
