---
name: design-philosophy-master
description: 设计师级去AI化设计哲学最终手册 - 色彩/字体/层级/布局/AI反套路 + 东方+西方美学融合
metadata: 
  node_type: memory
  type: project
  originSessionId: 3f38aac3-2f3d-4319-970a-92f048d2d27d
---

# 去 AI 化设计哲学总纲（最终版）

## 第一性原理
AI 廉价 = 训练自最大公约数审美 → 输出安全、均匀、套路化。三大原型问题：
1. 表层光鲜内核空洞 (superficial competence)
2. 对称工整没有性格
3. 装饰代替思考

**去 AI 化 = 做减法 + 建立层级 + 给一个主见**

## 东方美学（侘寂/静美/Ma）
- shibui 七元素：Simplicity / Implicitness / Modesty / Naturalness / Everydayness / Imperfection / Silence
- 配色：低饱和 + 混灰 + 银感
- Matthew May 总结：Elegant simplicity. Effortless effectiveness. Understated excellence. Beautiful imperfection
- Ma（间）：留白即设计，主动留白是反 AI 第一动作
- Kintsugi：使用痕迹可见，AI "完美"反而不诚实
- Muji 工作法：原型手绘而非电脑，"以免鼓励不必要的细节"

## 西方现代主义（功能/诚实）
- Form follows function (Bauhaus)
- Less is more (Mies)
- Truth to materials（诚实材料）
- Asymmetric balance via opposition (De Stijl)
- Good design is as little design as possible (Rams 第10诫)
- Rams 十诫核心：第 5 条"不显眼"被 AI 严重违反

## 色彩
- 8-10 阶灰，禁纯黑 #000，用 #0F0F0F / #1A1A1A
- 选带温度的灰：mauve / slate / sage / sand / olive
- 严格 1 个主色，用量 ≤5%
- Radix 12 阶：1-2 背景 / 3-5 组件底 / 6-8 边框 / 9-10 实色 / 11-12 文字
- WCAG 4.5:1 正文 / 3:1 大字
- 禁用：紫粉渐变、荧光、饱和 blue-500 满铺
- 参考：Linear (#F4F5F8 + #222326 + 蓝) / Stripe (slate + 紫青) / Apple / Muji

## 字体
- 2-3 family：Inter/Geist/Söhne 正文 + GT Sectra/Newsreader 标题 + 可选等宽
- 正文与标题至少 1.5× 比例差
- 尺度 12/14/16/20/24/32/48/64，一页最多 4 个 size
- 行宽 45-75 字符，理想 66ch
- 行高：正文 1.5-1.7，标题 1.05-1.2
- Display 大字可负字距 -0.02em
- 大写字母字距 +0.05em
- 数据用 tabular figures
- Sentence case 不用 Title Case

## 视觉层级
5 工具优先级：Size > Weight > Color > Position > Whitespace
- De-emphasize to emphasize
- 眯眼测试 (squint test)
- 一页最多 3 个 size
- Gestalt：Proximity / Similarity / Closure / Continuity

## 布局与间距
- 间距 4/8 倍数：4/8/12/16/24/32/48/64/96/128
- section 间距至少内部 2×
- 内容与边缘至少 32px
- 12 列响应式栅格
- **左对齐是 Swiss Style 黄金法则**
- **不对称优于对称**（对称=模板感=AI 感）
- 重要元素偏左或偏上
- 减少 1px border，用间距+背景色差+阴影代替
- 圆角统一：8px 卡片 / 4px 按钮 / 999px 头像

## AI 一眼假清单
通用：紫粉渐变、渐变文字、emoji 装饰、AI 人脸、Times New Roman、透明背景彩色图标、3D 抽象 blob、玻璃拟态+紫粉渐变+3D 末日组合
PPT：居中标题、商务握手 stock、彩虹配色每页、Justify、SmartArt、模板过渡、阴影在图片上
网页：Hero+重渐变 overlay、卡片等大等距、Vercel 主页克隆、5 tab bar、多色霓虹阴影
App：5 tab bar、emoji 按钮、彩虹状态色、千篇一律 FAB
海报：渐变光晕、AI 美图主视觉、字间距过宽过紧、居中大段文字

## 四媒介配方
- 网页：白/近黑+1 主色+12 阶色板+2 字体；Hero 左对齐 64-80px+一句价值主张+1 CTA+真实产品截图；section 间距 96-128px
- PPT：纯白或近黑+1 主色+灰阶 5 档；每页一个 idea；大数字+简短解释；左对齐为主；单色线性图标；图表删 3D/阴影/网格线/图例
- App：白+系统色板；移动端 44pt+ 触控；主操作 FAB/顶部 bar；空状态自设计
- 海报：12 列/Villard 网格先；真实摄影>AI 美图；Display 衬线+小号无衬线副文；大量纯色块

## 6 条心法
1. 先限制再创造（1 主色+1 字体+1 圆角）
2. 做减法的勇气（80% "加一笔"是错觉）
3. 有一个主见（决定气质，通篇贯彻）
4. 模仿具体对象（不要混搭）
5. 网格先于元素
6. 真实 > 完美

## Prompt 套话
```
1. 严格使用 [主色 HEX] + 8 阶灰色（#F...→#1...，选带温度的：mauve/slate/sand）
2. 字体限定 [正文] + [标题]，最多 2 个 family
3. 字号尺度 [12/14/16/20/24/32/48/64]，最多 4 个 size
4. 内容左对齐，禁止居中
5. 间距用 8 的倍数，section 间距 ≥64px
6. 留白慷慨
7. 禁止：渐变文字、emoji 装饰、玻璃拟态、紫粉渐变、3D 元素
8. 重要元素 1 个，次要用减弱的 color/weight
9. 整体气质：[极简/克制/编辑感/科技冷峻/温暖手作/日式禅意]
10. 视觉参考：[1-2 个具体网站/品牌]
11. 不必完美——可材质纹理、轻微不对齐、留白呼吸
```

## 黄金法则
**好的设计 90% 是删除，10% 是摆放。** AI 缺的是"删掉这一笔"的勇气。

## 大师谱系
Muji（手绘原型）→ Rams（十诫第 5：不显眼）→ Aalto（人性化功能）→ Apple（材料诚实）→ Linear（克制表达）

## 与前文关系
- 本文是 design-ai-de-slop.md 的最终综合版
- 包含 design-philosophy-japan-nordic.md 全部要点
- 是面向所有设计任务的统一设计哲学手册
