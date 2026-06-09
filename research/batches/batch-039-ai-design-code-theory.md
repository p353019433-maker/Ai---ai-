# Batch 039 · AI 设计的代码层面理论基础

**研究问题：** 从设计系统架构、生成艺术算法、字体排版、感知心理学、美学 lint 四个垂直方向，深入研究「让 AI 设计不像 AI」的代码层面理论基础。

**综合来源：**
- research-notes-01（design-system-architecture, 5,510 词）——五层设计系统架构、语义 Token 约束、禁止模式
- research-notes-02（generative-algorithms, 7,559 词）——生成艺术算法系统、种子随机性、Alexander 模式语言
- research-notes-03（typography-deep, 5,756 词）——字体选择逻辑、Variable Font axes、排版层级
- research-notes-04（aesthetic-linting, 8,468 词）——代码级检测系统、ESLint 规则、可视化 CI 流程
- research-notes-05（psychology-perception, 6,449 词）——感知心理学、Gestalt 原理、AI 设计为何"感觉不对"

---

## 一、设计系统作为约束语言

### 1.1 三层 Token 模型的实际运作

大多数设计系统的 Token 讨论停留在「颜色 Token 命名」，没有说清楚约束层之间的代数关系。实质是：

```
primitive tokens → semantic tokens → component tokens
（原始值）         （语义角色）        （实例绑定）
```

Primitive 层回答「什么值」；Semantic 层回答「这个值是给谁用的」；Component 层回答「这个角色在这个组件里怎么表现」。每往上一层，约束力变强，但灵活性降低。AI 之所以在 primitive 层产生大量同质化输出，正是因为它在这个层有太多的「合法路径」可选。

**Material Design 3 的 Reference / System / Component 三层分类** 是目前最清晰的实践参考。Reference 存裸色值；System 定义跨组件语义角色（如 `color.surface.container`）；Component 把 System 角色绑定到具体组件的具体部分（如 `md.comp.fab.primary.container.color`）。关键是「名字描述用法而非值」，值可以变，名字不变——这个名字不变性才是约束的本质。

### 1.2 语义 Token 是「策略句柄」

语义 Token 不是「别名」，而是「策略句柄」——每个 Token 名字编码了产品意图，使得任何基于 Token 的操作可以被 lint、review、theming 和 AI 理解。

```json
{
  "color.text.danger": {
    "value": "{color.red.700}",
    "allowedOn": ["surface.canvas", "surface.panel"],
    "requiresContrast": 4.5,
    "forbiddenIn": ["marketing.hero", "decorative.icon"],
    "intendedUse": "Destructive state, validation error, or irreversible action"
  }
}
```

当 AI 写 `color: token('color.text.danger')` 时，它在做一个产品决策。当它写 `color: red-600` 时，它在做一个美学采样。前者可以被 review 追问「为什么这里危险」，后者无法被 challenge。

### 1.3 Governance 层：让错误选项不编译

真正的约束来自「错误选项变成错误」：

- **包边界隔离：** App 代码只能 import semantic tokens，不能 import reference tokens
- **ESLint 规则：** Atlassian 的 design-system ESLint plugin 已经在生产级别实现了 `no-raw-color`、`no-reference-token-in-app`
- **TypeScript 类型系统：** component props 只接受语义值而非视觉枚举
- **Stylelint token 验证：** 禁止在 app 代码中写 hex/rgb/hsl 值
- **Tailwind arbitrary value 规则：** `no-arbitrary-value` 堵住 `bg-[#7c3aed]` 这类 escape hatch

**核心洞察：** 设计系统必须让正确路径比错误路径短。如果 semantic component 比 raw utility classes 更难写，AI 会选后者。

### 1.4 组件 API 的「意图强制」设计

组件 API 是最关键的 anti-slop 表面，因为 AI 写组件比理解视觉层级更快。

```tsx
// Bad: 一个 variant prop 承载过多语义
<Button variant="primary" />

// Good: 分离 intent / emphasis / density / context
<Button intent="submit" emphasis="primary" density="standard" context="form" />
```

discriminated union 强制 AI 必须提供 intent 特定的必填字段：

```ts
type CalloutProps =
  | { intent: 'warning'; title: string; body: string; mitigationAction: Action }
  | { intent: 'success'; title: string; body?: string; nextStep?: Action }
```

现在 AI 不能实例化一个 warning callout 而不提供 mitigation action——这在结构层面阻止 slop，而非只在视觉层面。

---

## 二、生成艺术系统 vs AI 合成：作者权在哪里

### 2.1 本质区别：创作机制 vs 创作请求

**生成艺术** 作者创作的是**决策结构**——规则、约束、变量范围、组合语法、失败守卫、种子处理、材质词汇表、输出评估标准。最终图像有部分自主性，但自主性被作者严格限定在设计的边界内。

**AI 合成** 在 prompt-only 模式下，人类创作的是一个**请求**，而非生成机制本身。模型执行的是基于训练数据中图像-文本相关性的潜在统计合成。

这意味着：生成艺术系统作者定义了一个「可能宇宙」；prompt-only AI 是在请求「从训练数据的平均宇宙里采样一个解」。

### 2.2 种子随机性：可重现的多样性

种子是「独特性」和「可重现性」之间的桥梁。伪随机数生成器是确定性算法——给定相同种子，每次产生相同的随机序列。这使得生成系统可以产生可变的输出，同时保持可重复性。

**Mulberry32 种子 RNG（最小实现）：**

```js
function mulberry32(seed) {
  return function rng() {
    let t = seed += 0x6D2B79F5;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function hashStringToSeed(str) {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}
```

**稳定 keyed 随机性**（避免插入一个随机调用就改变下游所有随机值）：

```js
function randFor(seed, key) {
  return mulberry32(hashStringToSeed(`${seed}:${key}`))();
}
const cardAWidth = randFor(globalSeed, "card:A:width");
const cardAColor = randFor(globalSeed, "card:A:color");
```

**多层级种子派生：**

```js
const seeds = {
  layout: hashStringToSeed(`${base}:layout`),
  texture: hashStringToSeed(`${base}:texture`),
  type: hashStringToSeed(`${base}:type`),
};
```

### 2.3 约束随机性 > 无约束随机性

好的随机性不是「任何事情都可能发生」。好的随机性是「很多事可能发生，但只发生在属于这个系统的范围内」。

**权重选择（而非均匀采样）：**

```js
function weightedChoice(items, weights, rng) {
  const total = weights.reduce((a, b) => a + b, 0);
  let r = rng() * total;
  for (let i = 0; i < items.length; i++) {
    r -= weights[i];
    if (r <= 0) return items[i];
  }
  return items[items.length - 1];
}

const motif = weightedChoice(
  ["line", "dot", "cutout", "glyph", "void"],
  [45, 20, 15, 12, 8],  // 主导行为 + 稀有时刻
  rng
);
```

**噪声场（Perlin/Simplex）** 提供空间相关的有机变化，而非白噪声的每个点独立随机：

```js
function fractalNoise2D(noise2D, x, y, octaves = 4) {
  let value = 0, amplitude = 1, frequency = 1, norm = 0;
  for (let i = 0; i < octaves; i++) {
    value += amplitude * noise2D(x * frequency, y * frequency);
    norm += amplitude;
    amplitude *= 0.5;  // persistence
    frequency *= 2.0; // lacunarity
  }
  return value / norm;
}

function organicRadius(base, x, y, noise2D) {
  const n = fractalNoise2D(noise2D, x * 0.004, y * 0.004, 5);
  return base * (1 + 0.18 * n); // 有界 18% 变化
}
```

### 2.4 拒绝条件：生成器要会说「不」

生成系统应该知道什么状态是无效的：

```js
function scoreComposition(comp) {
  let score = 1;
  if (comp.textContrast < 4.5) score -= 0.5;
  if (comp.visualDensity > 0.75) score -= 0.3;
  if (comp.accentArea > 0.14) score -= 0.2;
  if (!comp.hasHeroAnchor) score -= 0.4;
  return score;
}
```

这定义了「生成艺术系统」和「prompt-only AI」之间最大的差异：设计师可以用代码定义成功条件。

---

## 三、排版：为什么 AI 排版感觉平淡

### 3.1 AI 默认到 Inter 的根本原因

Inter 本身不是问题——它是优秀的字体。问题在于它成为了**统计吸引子**。原因：

1. **可用性和许可**：开源字体在公开示例中随手可得，AI 生成代码没有许可风险
2. **训练频率**：大量「现代 SaaS 着陆页」示例中都是 neo-grotesque 或 geometric sans
3. **Prompt 词汇**：「clean、modern、minimal、SaaS」这些词强烈关联中性 sans-serif 系统
4. **组件库继承**：大量生成的 UI 基于默认视觉文化为中性 sans 的组件生态

### 3.2 字体选择：按声音选，而非按流行度选

避开泛泛的「clean, modern, premium」。用更精确的对立项：

- **judicial vs conversational**
- **editorial vs operational**
- **warm vs clinical**
- **archival vs futuristic**
- **handmade vs engineered**
- **literary vs transactional**

然后选择**字体的构造本身**支持那个声音的 typeface。Humanist sans-serif 有书法影响；Old-style serif 暗示阅读、传统和文学肌理；Slab serif 传达 utility、信心或工业风味；Condensed grotesque 给出编辑紧迫感或数据密度。

### 3.3 Variable Font Axes：上下文相关的排版深度

Variable Font 是 anti-AI 排版的主要机会——它允许字体根据上下文调整，而不需要切换文件。

**注册轴（Registered Axes）：**

| 轴 | CSS 属性 | 用途 |
|---|---|---|
| `wght` | `font-weight` | 粗细 |
| `wdth` | `font-stretch` | 宽窄 |
| `opsz` | `font-optical-sizing` | 光学尺寸 |
| `slnt` | `font-style: oblique` | 倾斜 |
| `ital` | `font-style` | 斜体 |

**自定义轴：**

| 字体 | 自定义轴 | 用途 |
|---|---|---|
| Roboto Flex | `GRAD`, `XTRA`, `XOPQ`, `YOPQ` 等 | 精细调优 |
| Recursive | `MONO`, `CASL`, `CRSV` | 单一家族跨 mono/proportional 和 strict/casual |
| Fraunces | `SOFT`, `WONK` | 表达性 display 效果 |

**`GRAD`（字重不改变字宽）：** 在暗模式下增加文字深度而不改变布局：

```css
.dark body { font-variation-settings: "GRAD" -20; }
.small-label { font-variation-settings: "GRAD" 30; } /* 小字加粗 */
```

### 3.4 光学尺寸（Optical Sizing）：最清晰的专业排版标记之一

`opsz` 轴恢复尺寸特定设计。小字号需要更粗的笔画、更开放的间距、更大的 x-height、更简单的细节；大字号可以更紧凑、更高的对比度、更精致的细节。

AI-shallow typography 对所有尺寸使用同一个设计——64px 标题和 14px 标题用的是同一个 neutral sans 字体，只改变 size 和 weight。Human-intentional typography 问：**这个字在这个尺寸需要什么？**

```css
.caption {
  font-size: 12px;
  font-variation-settings: "opsz" 10, "GRAD" 25;
  letter-spacing: 0.012em;
}
.display {
  font-size: clamp(48px, 8vw, 112px);
  font-variation-settings: "opsz" 96, "GRAD" -5;
  letter-spacing: -0.055em;
}
```

### 3.5 AI 排版感觉平淡的真正原因

AI 排版感觉平淡不是因为度量错误，而是因为：

1. **均匀的 type color**——所有内容使用相同 weight 和 line-height
2. **只按 size/weight 建立层级**——没有 measure、case、spacing、figure style 等角色区分
3. **无内容特定 features**——表格里没有 tabular numeral；代码里没有 slashed zero
4. **默认行长**——AI 让文本块跟随容器，而非控制 measure
5. **过度的居中对齐**——所有 hero、feature card、testimonial 都居中

---

## 四、美学 Lint：代码层面的检测系统

### 4.1 美学 Lint 的定义

**美学 Lint = UI 源代码和渲染制品的视觉模式风险自动化审查。** 目标不是「美」，而是「可检测的审美风险」：

- 硬编码视觉值而非语义 tokens
- 值或组合的重复（如相同 radius/shadow/card 结构跨不相关 surface）
- 已知陈词滥调组合（如 gradient text + pill badge + centered hero + bento grid）
- 低 palette entropy（调色板缺乏丰富性）
- 间距直方图崩塌到一组窄的 Tailwind 值
- 与 generic AI 模板匹配的 component silhouettes

### 4.2 四层检测架构

```
Layer 1: Static JSX/TSX linting（AST 级别）
  → 解析 JSX 属性，检测 className 中的可疑 utility 组合

Layer 2: CSS/Token linting（Stylelint）
  → token 验证，禁止 raw colors/shadows/radii

Layer 3: Rendered DOM + Accessibility（Playwright）
  → 检查 computed styles，验证视觉抛光未替代语义

Layer 4: Screenshot analysis（Playwright + 图像处理）
  → 从截图计算视觉指标：radius 分布、shadow 分布、间距直方图、调色板 entropy
```

### 4.3 ESLint 规则：AST 级别的 AI 模式检测

**核心挑战：** 从 JSX 中提取 className 字符串，解析出 tailwind class token。

```js
// 从 CallExpression（cn/clsx/classnames）提取静态 class 字符串
function extractClassChunksFromExpression(expr, chunks = []) {
  if (!expr) return chunks;
  if (expr.type === "Literal" && typeof expr.value === "string") {
    chunks.push({ text: expr.value, node: expr });
  }
  if (expr.type === "CallExpression") {
    for (const arg of expr.arguments) extractClassChunksFromExpression(arg, chunks);
  }
  if (expr.type === "LogicalExpression") {
    extractClassChunksFromExpression(expr.left, chunks);
    extractClassChunksFromExpression(expr.right, chunks);
  }
  return chunks;
}
```

**Radius 单调性检测（示例）：**

```js
const largeRadiusTokens = new Set(["rounded-xl", "rounded-2xl", "rounded-3xl"]);
const MAX_PER_COMPONENT = 4;
const MAX_PER_FILE = 8;

// 对每个 radius token 计数，超过阈值则 warn
// 应该区分 container radius（高风险）和 badge/avatar radius（低风险）
```

**Gradient 陈词滥调检测（示例）：**

```js
// 检测 gradient text = bg-clip-text + text-transparent + bg-gradient
// 检测被禁止的颜色对：from-blue-600 + to-purple-600
// 检测 decorative blur blob：absolute + rounded-full + blur-* + opacity-*
```

**Card 骨架评分系统：**

```js
function scoreCard(tokens, jsxNode) {
  let score = 0;
  if (isRawElement(jsxNode, ["div", "article"])) score += 1;
  if (tokens.some(t => /^rounded-(xl|2xl|3xl)/)) score += 2;
  if (tokens.some(t => /^shadow-(lg|xl|2xl)/)) score += 2;
  if (tokens.includes("border")) score += 1;
  if (tokens.some(t => /^(p|px|py)-([678]|10|12)$/)) score += 1;
  if (hasIconBadgeChild(jsxNode)) score += 2;
  if (score >= 6) warn("generic card pattern");
}
```

### 4.4 Screenshot 分析：渲染结果层

AST 检测不到 CSS cascade、component library variants、runtime theme 后的真实视觉。Screenshot 分析观察渲染结果：

**可计算的视觉指标：**

- **Radius 分布：** 收集 computed `border-radius`，计算最大 radius 共享率（单一 radius 占总面积的比例）
- **Shadow 分布：** 解析 `box-shadow` 字符串，统计不同 shadow recipe 数量和强度分布
- **Spacing 直方图：** 从 DOM box model 计算 sibling gaps 和 section padding 的分布
- **调色板 entropy：** 像素级采样 + k-means 提取主色，计算 hue/staturation/luminance 分布
- **边缘密度：** Canny/Sobel 边缘检测，区分 text/icon/decorative 边缘
- **Component 重复度：** 感知哈希或 DOM 结构相似度计算 card 相似度
- **对齐与对称性：** center-aligned 文本块占比，对称 section 数量

### 4.5 CI 流程

```yaml
Stage 1: eslint --format json > eslint-aesthetic.json
Stage 2: stylelint + token lint
Stage 3: build Storybook + playwright screenshot capture
Stage 4: visual metrics computation
Stage 5: risk aggregation
Stage 6: SARIF/PR comment/HTML report
```

**风险公式示例：**

```
risk = min(100,
  0.30 * staticPatternScore +
  0.20 * tokenDriftScore +
  0.25 * visualMetricScore +
  0.15 * repetitionDeltaScore +
  0.10 * accessibilityOverlapScore
)
```

---

## 五、感知心理学：为什么 AI 设计「感觉不对」

### 5.1 核心机制：流畅性高但意图性低

Processing Fluency 理论（Reber, Schwarz, Winkielman）提出：美感的愉悦部分来源于感知者处理刺激的容易程度。AI 设计往往有非常高的感知流畅性——清晰的轮廓、居中的构图、平衡的间距、顺畅的渐变、熟悉的视觉 tropes。

但设计不仅仅是感知处理。人类观众也在推断**选择**——这个元素为什么在这里？为什么这个颜色？为什么这个节奏？为什么这个网格中断？

当一个设计流畅但其微观决策不服务于内容、约束、材质、品牌或使用时，结果感觉「不对劲」。观众可以处理它，但无法为其找到令人信服的理由。

### 5.2 AI 设计中「不对」感知的具体机制

1. **预测误差：** 视觉系统预测边缘、阴影、间距、材质应该如何表现。AI 设计往往在局部期望上违反直觉，在全局上满足直觉。
2. **感知不匹配：** 写实眼睛配不写实皮肤。在设计中：高级照明配无意义的图标；贵的颜色配通用文案；抛光的卡片配无任务逻辑。
3. **类别模糊：** 观众无法判断这个对象是产品、概念 mockup、品牌系统、插图还是装饰样本。
4. **原型过拟合：** AI 系统擅长产生一个风格的中央样本。人类对原型敏感，但也注意到一个设计从不偏离原型而没有任何理由。
5. **约束痕迹缺失：** 人类制品往往带有约束的痕迹：内容长度、生产方法、可访问性、遗留系统、文化引用。AI 视觉通常缺乏这些痕迹。
6. **过度均匀：** 当每个角、发光、渐变和间距间隔都同样平滑时，设计失去了努力的层级。它感觉像是在各处优化过，但在任何地方都没有真正决定什么。

### 5.3 Schloss & Palmer 的色彩偏好理论

**Ecological Valence Theory：** 人们对颜色的偏好源于对与这些颜色相关物体的平均情感反应的关联。WAVE（加权情感 valence 估计）可以解释大部分颜色偏好方差。

**AI 调色板感觉「AI」的真正原因：** AI 设计收敛到蓝色、紫色、蓝紫色渐变、霓虹亮色，不是因为它们是随机选择的，而是因为：

- 蓝色被信任/科技/水的联想所喜爱
- 紫色被想象力/未来感/奢侈品联想所喜爱
- 青色/电蓝色唤起屏幕/LED/数据/网络
- 深色背景使饱和渐变更亮更高级

**问题：** 随着这些调色板被 AI 初创公司、AI 工具、合成头像和通用 SaaS 着陆页重复使用，它们的生态 valence 改变了。颜色现在意味着「机器生成的未来美学」，而非具体的品牌承诺。

### 5.4 对称性：感觉安全但最终错误

对称性是 AI 最常用的构图策略，因为它**降低风险**。居中 hero 文本、平衡卡片网格、对称抽象形状——这些都是高概率解，当模型缺乏更深的知识时。

但人类设计**选择性地**使用对称性。银行/医疗网站用对称性传达稳定；编辑/品牌/创意产品用不对称传达张力；数据 dashboard 避免对称因为真实用户工作流是不均匀的。

**AI 缺乏这种选择性。** 它在所有 context 默认对称。当内容需要层次感、叙事弧线或任务特定权重时，对称变成了「过于解决」的信号。

### 5.5 Gestalt 原则作为风格先验而非语义结构

AI 系统复制「Gestalt 友好」的排列——proximity、similarity、continuity、closure、figure-ground——因为这些排列在训练数据中很常见，产生流畅的图像。

问题在于：**人类用这些线索来推断关系。** 当推断的关系薄弱时，设计感觉是人工的。

- **Proximity：** AI layouts 往往按节奏而非语义使用间距——相关的和无关的元素收到相似的 gap；分组由时尚留白分隔而非任务边界
- **Similarity：** AI overuses it——每个卡片有相同 radius、shadow、glow、icon container
- **Continuity：** AI decorative continuity（swooshes、blobs、gradient trails）引导眼睛但不代表真实过程
- **Closure：** AI often gives closure too cheaply——形状感觉应该意味着什么，但没有

---

## 六、综合理论框架：Anti-AI 设计的六项原则

### P1. 每个感知线索必须编码意义

如果 proximity grouping 元素，这些元素必须真的相关。如果颜色变化，那个变化必须编码类别、状态、情感或叙事。如果形状重复，它的重复必须定义一个组件类。如果一个元素打破网格，打破必须标记优先级或声音。

**audit 问题：** 这个视觉线索告诉用户什么他们还不知道的？

### P2. 选择 Situated 调色板而非通用和谐

Schloss & Palmer 的生态 valence 理论意味着：颜色从真实物体、地方、仪式、材质、领域经验中提取时更有意义。从「高级蓝色」调色板网站复制来的颜色缺乏这种联系。

**audit 问题：** 这个调色板能属于任何 AI 初创公司吗？如果是，是什么让它属于我们？

### P3. 用不对称来揭示优先级

不要随机打破对称。在内容权重不均匀的地方打破对称。高风险行动不应该在视觉上等同于低风险行动。

**audit 问题：** 系统在哪里假装事情平等而它们并不平等？

### P4. 保留有用的 grain

让系统的不同部分有不同的密度、纹理和抛光，当它们的角色不同时。settings table 可以是朴素的。launch campaign 可以是表达性的。error state 可以是直白的。

**audit 问题：** 我们是否过度调和了应该让用户感觉不同的 zones？

### P5. 定义 variation 语法

Variation 应该遵循用户可以学习的规则：人类生成内容用暖色 accent；系统生成内容用冷色 accent；草稿用粗糙边缘；验证信息用严格网格。

**audit 问题：** 如果用户三次看到这个 variation，他们会理解它的意思吗？

### P6. 区分 polish 和 care

Polish 是表面一致性。Care 是对用户需求的适当性。AI 可以轻松模仿 polish。AI 在 care 方面较弱，因为 care 取决于了解上下文中的什么重要。

**audit 问题：** 这个设计美是因为它服务于情境，还是因为它类似于美丽的东西？

---

## 七、核心结论：反 AI 设计的本质

### 7.1 统计平均 vs 具体选择

AI 生成设计感觉像统计平均，因为每个特征单独看都是 plausible 的，组合起来却缺乏 specificity。设计师的具体选择往往带有机会成本——选择了粗糙的黑白照片，就拒绝了抛光的渐变插图。AI 输出往往避免这种可见的机会成本。它选择的是广泛可接受的选项。这缺乏牺牲感是可以被感知的。

### 7.2 创作的「意图密度」

设计的每个决策——颜色、radius、间距、字体、图标、节奏——都携带「意图密度」。高意图密度意味着每个选择都可以被解释：为什么这个颜色属于这里？为什么这个 radius 而不是另一个？为什么间距这么大？

AI 设计往往在感知流畅性上打高分，在意图密度上打低分。这就是为什么它 pass 缩略图检查但在注意力下变弱。

### 7.3 约束 > 限制

对抗 AI 同质化不是限制 AI，而是**用更具体的约束替换模糊的空间**。当 prompt 说「做一个漂亮的 UI」时，模型在很大的未定义空间中采样。当设计系统说「这是一个决策语言，其中每个选择必须符合语义角色、允许的组合、禁止的模式」，模型在受限的语言中运作。

**好的设计系统不是更好的 Tailwind 配置。好的设计系统是一个受控的生成语言。**

### 7.4 最终命题

AI Slop 不是因为 AI 无能力设计，而是因为创作权被委托给了一个统计优化器而没有足够的语义约束。

抗 Slop 设计因此是一种**语言工程**：将品味、品牌、可访问性、层级关系和产品意义编码成 AI 和人类都必须使用的 API。系统命名决策的意图越清晰，限制 raw 值越多，约束组合越紧，自动执行规则越多，通用 AI 输出能够生存的空间就越少。

Human-sounding 设计不来自随机的不完美，而来自**情境化的决策**——那些经得起翻译成代码的决策。

---

## 附录：实践检查清单

### 设计系统层面
- [ ] Primitive tokens 设为 private；只发布 semantic 和 component tokens
- [ ] Token 名字描述用途，不描述值
- [ ] 组件 API 使用 intent/emphasis/density/context 而非单一 variant prop
- [ ] TypeScript discriminated union 强制 intent-specific 必填字段
- [ ] 包边界隔离：app 代码不能 import reference tokens
- [ ] ESLint 规则禁止 raw colors 和 arbitrary values
- [ ] 维护 forbidden patterns registry 和 exception 过期机制

### 排版层面
- [ ] 字体选择有 voice rationale，不只是「modern」
- [ ] Variable font axes 做语义工作（opsz/GRAD/wdth 有实际映射）
- [ ] 光学尺寸启用或手动映射（caption 用 opsz 低值，display 用高值）
- [ ] Numerals 按上下文选择（prose 用 oldstyle，table 用 tabular）
- [ ] Leading 按内容密度设置（长正文 1.6+，display 0.92-1.05）
- [ ] Uppercase labels 有 tracking（0.04-0.12em）
- [ ] 关键标题有人工检查 kerning pair

### 生成系统层面
- [ ] 使用种子随机性（相同 seed = 相同输出）
- [ ] 变量范围有 authored bounds（不是无界随机）
- [ ] variation 映射到 intent（density/mood/emphasis 而非纯随机）
- [ ] 有 rejection criteria（对比度、密度、碰撞检查）
- [ ] 维护 approved seeds 注册表
- [ ] macro/meso/micro variation 分层（布局/网格/纹理）

### 检测层面
- [ ] ESLint custom rules 检测 radius monoculture、gradient clichés、card 骨架
- [ ] Stylelint 强制 tokenized colors
- [ ] Playwright 截图捕获核心 routes
- [ ] 计算 radius/shadow/spacing 分布直方图
- [ ] 输出 aesthetic risk score + per-finding evidence + suggested fix
- [ ] 允许 scoped exception（需 rational + owner + 过期）
