---
name: design-philosophy-dataviz
description: 数据可视化与信息设计 - Tufte/Few/McCandless/Playfair/误导图 - 循环8研究
metadata: 
  node_type: memory
  type: project
  originSessionId: 3f38aac3-2f3d-4319-970a-92f048d2d27d
---

# 数据可视化与信息设计（循环8）

## Edward Tufte 数据可视化圣经
- **Data-ink ratio 数据墨水比**：墨水分数据相关 vs 非相关
- **Chartjunk 图表垃圾**：无用/分散/遮挡信息的元素
- **Small multiples 小型复数**：同尺度/同轴系列图 → 直接对比
- 关键书：
  - *The Visual Display of Quantitative Information* (1983)
  - *Envisioning Information* (1990)
- 哲学："graphical integrity" + "graphics reveal data"
- "Compared to what?" 量化推理的核心问题

## Stephen Few Dashboard 原则
- 好 dashboard：Simple, communicates easily, minimum distractions
- **Z pattern 布局**：左上最重要（左到右语言）
- 用图 > 表格
- 元素：bar/line/sparkline/scorecards
- 色彩：一致 + 必要 + 色盲友好
- 避免 "data graveyard" 数据坟墓
- 几个关键数字 > 全部

## David McCandless Information is Beautiful
- 探索 data visualization + 记者工作的协同
- 视觉风格：Visual Miscellaneum
- 展出：MoMA / Wellcome / Tate Britain
- 书：*Information Is Beautiful* (2009) / *Knowledge Is Beautiful* (2014) / *Beautiful News* (2023)

## Fernanda Viégas & Martin Wattenberg
- **Social Visualization**：揭示社交动态
- **Democratizing Data**：通过 Many Eyes 让大众可访问
- **Visualization as Art**：把数据视为艺术媒介
- **Storytelling Through Data**：邮件可视化等揭示人类经验
- **Collaborative Intelligence**：研究群体如何创造/修改/修复信息
- 维基百科"vandalism 修复"的首次科学研究

## Hans Rosling
- Gapminder 创始人
- 关键贡献：让统计数据动起来（animated bubble chart）
- 数据讲故事的开创者
- 演讲述说技巧影响深远

## William Playfair（统计图之父）
- 发明条形图 / 线形图 / 饼图 / 面积图
- 18-19c 商业图表之父
- **数据表示的奠基**

## 视觉编码（pre-attentive attributes）
- **Length 长度**：最有效（bar chart）
- **Position 位置**：第二有效
- **Angle 角度**：中
- **Area 面积**：较弱
- **Color hue 色相**：弱（分类）
- **Color saturation 饱和度**：弱（量化）
- **Shape 形状**：最弱（仅分类）
- **结论**：用长度比较 > 表面/角度

## 8 种定量信息
1. Time-series → line chart
2. Ranking → bar chart
3. Part-to-whole → pie/bar
4. Correlation → scatter
5. Frequency distribution → histogram
6. Geographic → cartogram
7. Deviation → bar
8. Distribution → box plot

## Chartjunk 具体清单
- 重/暗的网格线
- 不必要文字 + 复杂字体
- 装饰性坐标轴 / 框
- 数据图中的图/背景/icon
- 装饰性阴影
- 元素不成比例
- 噪声背景
- **3D 折线/柱状**（典型 AI 套路）

## 误导图（避免）
- **Truncated graphs 截断图**：Y 轴不从 0 起 → 放大变化
- **Pictogram scaling 缩放**：面积 ≠ 高度（看起来差被平方）
- **Log 标度混淆**：让大差看似小
- **3D effects**：扭曲饼图切块大小
- **Axis manipulation**：Y 轴最大值影响感知
- **Biased labeling 偏标签**：用引导词
- **Fabricated trends**：把无关数据画趋势线
- **Omitting data**：删除关键点
- **Excessive complexity**：需要解释的图不该存在

## 测量失真工具
- **Lie factor 撒谎因子**：视觉变化 / 实际数据 = 1 才正常
- **Graph discrepancy index**：失真百分比
- **Data-ink ratio**：越高越好
- **Data density**：每面积数据点，越高越好

## Tufte 名言
"A table is nearly always better than a dumb pie chart"

## Simplicity 五步
1. Tell the truth
2. Get to the point
3. Pick the right tool for the job
4. Highlight what is important
5. Keep it simple

## 对 AI 去 AI 化的启示
1. **删 chartjunk**：AI 默认给 3D 饼图、阴影、装饰 — 全部要删
2. **截断 Y 轴**：AI 经常用截断让数据"看着更厉害" — 必须从 0 开始
3. **小复数**：用 small multiples 展示变化 > 单个复杂图
4. **Z 模式布局**：dashboard 关键元素左上
5. **数据墨水比**：每加一个元素问"它传达数据吗？"
6. **编码选择**：bar > pie 比较；用 length > area
7. **色盲友好**：永远不要只靠颜色区分
8. **Tufte "table > dumb pie"**：复杂信息用表
9. **讲故事**：数据可视化 + 叙事 = 影响力
10. **不要 3D**：3D 数据图 = 100% AI 套路，立刻删除

## 来源
2026-06-03；参考：Wikipedia (Edward Tufte / Data visualization / Small multiple / Chartjunk / Information design / Misleading graph / Data storytelling / Dashboard / Fernanda Viégas / Hans Rosling / William Playfair)
