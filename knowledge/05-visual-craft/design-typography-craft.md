---
name: design-typography-craft
description: 字体作为工艺 - Klim/Frutiger/Gill/Licko + 可变字体 + 字距/光学尺寸 + 字体版权史
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 字体作为工艺（Typography as craft）

## 一句话总结
字体不是"字符表"，是工程师在像素格栅、视觉光学、版权法之间用手与算法反复打孔的物理造物；理解这层工艺，才能解释为什么 Inter 比 Helvetica 在屏幕上更对、为什么 Frutiger 在数字时代越活越年轻。

## 一、当代 Foundry 工艺（5 家代表）

**Klim Type Foundry**（Kris Sowersby，新西兰）：Söhne 一个字体就拆 Mono / Schmal（窄）/ Breit（宽）三个变体 + 完整字重；Tiempos 分 Fine / Headline / Text 三个尺寸优化。Söhne 主页写"careful observations, decisive updates"——**每个 glyph 都被当作独立草图打磨**。

**Commercial Type**（Schwartzco 旗下）：Canela / Dahsar / Successor 等，强调"editorial, cultural, and retail projects"；提供 "one-time fee for perpetual usage" 一次买断。

**Type Network**：分销 Adobe Originals / LucasFonts / Original Type 等 100+ foundry 字体，强调"industry-leading technical review process"——**每份发布前都有外部审稿人检查 hinting / 垂直 metrics / OpenType 特性**。

**Frere-Jones Type**（Tobias Frere-Jones，2014 后独立）：代表作 Gotham（奥巴马 2008 竞选字体）从 Port Authority Bus Terminal 招牌的"建筑式抄写"——**先实景摄影取字，再回 Glyphs 描轮廓，最后手工调 hinting**。

**Production Type + Optimoz**：主营欧洲拉丁字体复刻与混排。

**共同工艺**（2-5 年项目）：草图 → 数字化 → 字距表 → OpenType 特性 → 多语言扩展 → 真人测试 → 发布。

## 二、Adrian Frutiger 的字距哲学
1928-2015，唯一跨越热金属/照排/数字三大时代的瑞士设计师。

**OCR-B**（1968，Monotype）：ECMA 国际标准字体，必须同时满足"机器扫描能识"与"人眼能读"——stroke 末端圆头但字怀开放。**ISO 1073-2 接受，写入现代护照机读区**。

**Univers**（1957）：字体史上第一个真正完整的"家族编号系统"：
- 第一位 1-9 表字重（1=超细、5=常规、9=超粗）
- 第二位表字宽+斜体方向（56=常规斜体）
- Walter Tracy："比 Helvetica 更适合正文"

**Avenir**（1988，晚 30 年）：Frutiger 自述"几何风格的有机诠释"——保留 Futura 圆形骨架（O 几乎完美圆），但 S 中段调粗、e 开口收窄、双层 a/g 改回传统形式，让正文更"色彩均匀"。

**Avenir Next**（2004-2007，Frutiger + 小林章）：3 字重扩 6+，新增 condensed 字宽、希腊与西里尔。

**Frutiger**（1975，戴高乐机场）：**字距哲学集大成**——字距不是度量（metric），是光学（optical）；远距识别场景（铁路、机场）要松，10pt 正文要紧。

## 三、Eric Gill 的"永恒几何" + 道德丑闻
1928 年 Gill Sans 脱胎于 Edward Johnston 1916 的 London Underground 字母，但大写改 Trajan 罗马石刻、小写改自传统衬线字形——**双层 a、双层 g、真正 italic** 是它与 Futura 几何至上派最大区别。

1935 年 Penguin Books 把它印经典企鹅平装封面，一用 30 年。

**争议无法跳过**：1989 Fiona MacCarthy 传记披露 Gill **对自己女儿的性虐待、与姐妹的乱伦、与动物的兽交**。2017 BBC 把 Gill Sans 换成定制字体，2020s 多家机构下架。

**当代设计师两难**：作品能脱离作者吗？默认答案是"可研究可讨论，**但默认不在新品牌项目采用**"。

## 四、Zuzana Licko + Emigre（屏幕像素当设计材料）
1984 Rudy VanderLans 在伯克利办 Emigre 杂志，1985 Licko 扩成 Emigre Graphics——**世界第一个把 bitmap 字体当合法设计语言的 foundry**。

Licko 在布拉迪斯拉发长大、左撇子被强迫用右手写字的经历，让她对"传统书法规范"本身就不信任。**Matrix / Modula / Oakland（后改名 Lo-Res）**直接用 Mac 72dpi 屏幕像素作画，**不试图"骗"屏幕呈现金属字模的圆润**——她说"I started my venture with bitmap type designs, created for the coarse resolutions of the computer screen"。

1990s 与 Neville Brody / David Carson 一起推动**孟菲斯版式语言**（错位网格、装饰无衬线、俗丽彩色）。**Mrs Eaves**（1996）致敬 Baskerville 1750s 衬线——字号做大、字怀打开、加入 small caps，名字来自 Baskerville 助手/妻子 Sarah Eaves。

**Licko "Legibility Wars" 那句 "You read best what you read most"**——字体"好不好"不再只是度量学问题，**是文化熟悉度问题**。

## 五、可变字体的工艺（5 注册轴 + 自定义）
2016 Adobe/Apple/Google/微软联合发布，OpenType 1.8 的一部分，根植于 Apple TrueType GX。

**原理**：一份字体文件存"两端 master glyph + 中间插值算法"，渲染时按 `font-variation-settings` 实时算任意位置轮廓。

**5 注册轴**：
- **wght**（weight）：1-1000
- **wdth**（width）：75%-125%
- **slnt**（slant）：-90° 到 90°
- **ital**（italic）：0/1 切换
- **opsz**（optical size）

**MDN 代码**：`font-variation-settings: "wght" 625, "wdth" 85, "opsz" 36, "GRAD" 88;`

**grade（GRAD）自定义轴**最值得 UI 设计师注意——**改变字重但不改变字宽**，所以动效从 GRAD 80 到 130 不触发 layout reflow，**是悬停/聚焦动效的理想载体**。

**工程陷阱**：注册轴必须小写（`wght`），自定义轴必须大写（`GRAD`），**轴名大小写敏感**。

## 六、光学尺寸（optical sizing）

Adobe 6 档：Poster（>72pt）/ Display（19-72）/ Subhead（14-18）/ Text（10-13）/ Small Text（8-10）/ Caption（4-8）。

**核心差异**：
- 大字号：stroke 更细、字怀更大、衬线更长更细
- 小字号：stroke 加粗、字怀收紧、加入 **ink trap**（笔画交汇处故意开小三角防油墨糊成团）、**x-height 抬高**

**Inter 在这点最聪明**：rsms.me 把 text 和 display 做成**两套独立设计**——text 模式 x-height 极高，display 模式笔画曲线干净。**同一份文件能在 9px UI 标签和 96px 落地页大标题下都站得住**。

## 七、字距与间距（手工表 vs 视觉算法）

**Kerning**（局部，调两个特定字符距离如 A-V）vs **tracking/letter-spacing**（整体，整段字符）。

**两类字距**：
- **metric kerning** 读字体文件 `kern` 表（设计师手填，主流含 1,000-10,000 对）
- **optical kerning** 跑算法看 glyph 轮廓"光学边缘距离"

**工艺成本**：一份合格正文级字体（如 Tiempos Text）含 **5,000+ 字距对**，**手工调一对平均 3-5 分钟，整份字体 1,000+ 工时**。**字体工艺 70% 成本藏在 kerning 表里**。

## 八、字体版权历史

**Helvetica** 1957 Max Miedinger 设计、Eduard Hoffmann 监制，原名 Neue Haas Grotesk，1960 改名 Helvetica（拉丁语"瑞士"）。版权在 Haas → Stempel → Linotype → Monotype 之间多次转手，2019 Monotype 推 "Helvetica Now" 大改版。

**争议**：Erik Spiekermann 公开说"Helvetica Sucks"、Martin Majoor 评"rather cheap"——核心论点：Helvetica 在小字号 aperture 太窄、大写 I 与小写 l 几乎无法区分、字怀设计压制可读性。

**Inter**（Rasmus Andersson，2017，SIL OFL 1.1 协议开源）——**对 Monotype 订阅制与 Helvetica 闭源历史最系统的反叛**。覆盖 147 语言、2000+ glyph、专门 text/display 双套轮廓。

**版权三条路**：
1. 商业字体（一次性或订阅）
2. OFL 开源（Inter / IBM Plex / Noto / Source Sans / Atkinson Hyperlegible）
3. 独立 foundry 买断（Commercial Type / Klim / Production Type 的"perpetual usage"模式）

**成本差距**：Söhne 企业版 $400-$800/字重，Inter 完全免费——**100x 级**。

## 9 条可复用原则（"在 X 场景用 Y"）
1. **≤12px UI 标签与密集表格** → Inter / IBM Plex Sans / Söhne（text 光学尺寸 + 高 x-height）
2. **大字号品牌标题** → Söhne Breit / Founders Grotesk Condensed / Tiempos Headline（display 优化 stroke 更细、字怀更大）
3. **悬停/聚焦动效** → GRAD 自定义轴（Inter / Recoleta）——改字重不改字宽
4. **长篇正文** → Tiempos Text / Charter / Source Serif（5000+ 手调字距对、ink trap 完整）
5. **多语言项目** → Noto Sans/Serif（Google 覆盖所有 Unicode 字符）
6. **数字 UI 永远开** `font-feature-settings: "kern" 1, "liga" 1, "calt" 1`（字距、连字、上下文替换）
7. **品牌系统** → Commercial Type / Klim 的一次性买断许可（避免 Monotype 订阅涨价）
8. **设计走查** → 同时打印 A4 黑白 + 13" Retina 屏幕测试（金属感、ink trap、stroke contrast 媒介不同）
9. **版权合规** → 把授权范围（web/app/print/broadcast）+ 到期日 + 备份路径当采购合同管理

## 8 条反面教材
1. **不要在 10px 标签用 Helvetica Neue Light**（stroke 几乎消失、aperture 闭合）
2. **不要把 Frutiger 与 Univers 混排**（两套字距哲学打架）
3. **不要用 5 种以上字体**（3 套上限：display / text / mono）
4. **不要用 CSS 模拟 italic**（`font-style: italic` + 系统无 italic 变体时浏览器几何斜切）
5. **不要在屏幕上用 Times New Roman 做正文**（金属活字时代"够用就好"，未为 sub-pixel hinting）
6. **不要混用 Gill Sans 与 Futura**（人文主义 vs 几何主义哲学相反）
7. **不要在登录/支付等关键流程用商业字体的免费 demo 版**（合规风险）
8. **不要忽视 hinting**（Windows + 非 Retina 屏幕用户占比仍高）

## 5 条与软件/UI 的连接
1. **字体选择 = 产品"声纹"**：Stripe Söhne、Linear Inter Display、Notion IBM Plex——换字体 = 换声纹
2. **可变性 = 界面响应式新维度**：Inter Variable 替代 5 个静态文件，bundle size 减 60-80%
3. **光学尺寸 = 自适应排版物理基础**：`font-optical-sizing: auto` 让同一份字体自动调 stroke
4. **字距 = 数字产品可读性隐藏 80%**：设计系统把 `letter-spacing` 当 token 管理（`--letter-spacing-tight: -0.01em`）
5. **版权合规 = 工程化采购**：把字体决策从"设计师个人喜好"提升到"采购合同级别"

## 资源 URL
- klim.co.nz / commercialtype.com / typenetwork.com / frerejones.com
- en.wikipedia.org/wiki/Adrian_Frutiger / wiki/Univers / wiki/Avenir / wiki/OCR-B
- en.wikipedia.org/wiki/Eric_Gill / wiki/Gill_Sans
- en.wikipedia.org/wiki/Emigre_(magazine) / wiki/Zuzana_Licko / wiki/Mrs_Eaves
- en.wikipedia.org/wiki/Variable_font / wiki/Optical_size / wiki/Kerning
- developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_fonts_guide
- rsms.me/inter / smashingmagazine.com/category/typography
