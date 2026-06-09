# Batch 038 · AI 反设计：代码层面的系统抗 AI 同质化策略

**研究问题：** 如何让 AI 生成的代码/设计不像 AI？抛开提示词技巧，从设计系统、代码架构、Token 体系、检测/纠正流程层面有哪些系统性解决方案？

**综合来源：**
- Paul Bakaus LinkedIn / Impeccable「Slop 检测目录」—— 46 个确定性 AI UI 特征
- MindStudio / Braingrid / Managed Code——设计系统方法论 + AI 生成代码的 token 约束实践
- Nielsen Norman Group（NN/g）——视觉设计五原则、颜色理论、Gestalt 原则
- The Crit「Vibe Coding 设计指南」—— AI App 默认配方与纠正路径
- Pimp My Type——字体选择与 AI 训练数据平均化问题
- TypeType / Figma Kerning 文档——字体间距/字偶距/行高的技术细节
- Schloss & Palmer 色彩研究（PMC）——偏好与和谐的认知机制
- IxDF / NN/g——对称性作为 UX 信号
- Christopher Alexander《模式语言》—— 生成性约束系统的理论原型
- NN/g「Brutalism 与反设计」——粗暴主义作为同质化的解药
- Utopia / Every Layout / W3C Design Tokens 社区组——流体布局与 Token 格式标准
- MIT Media Lab 身份系统 / Pentagram——规则驱动的生成式身份系统案例
- Smashing Magazine SVG 技术——feTurbulence / feDisplacementMap 材质纹理
- Amy Goodchild 等生成艺术文献——规则+随机性+约束的创作方法论
- 各大设计系统（IBM Carbon、Material Design 3）——七层设计系统架构参考

**子代理研究成果：**
- research-notes-01（5,219 词）——反模式视觉特征清单 + 代码级修复方案
- research-notes-02（6,627 词）——约束系统、七层设计系统架构、Alexander 模式语言
- research-notes-03（5,185 词）——字体/颜色/间距/对称性/视觉层级
- research-notes-04（5,777 词）——Token 体系、代码实现、CI 检测流程
- research-notes-05（5,754 词）——历史运动、瑞士风格、AI 同质化理论
- research-notes-06（5,981 词）——微观细节清单、紫蓝渐变、Cardocalyps、glassmorphism

---

## 一、核心命题：AI 设计同质化不是风格问题，是约束缺失

AI 生成设计收敛于同质化，不是因为 AI 没有审美，而是因为模型在做**统计优化**而非**设计决策**。

当 prompt 缺乏约束时，模型采样训练数据中最高概率的组合：Tailwind 教学示例中的 indigo/purple、组件库中的 rounded cards 和 shadow 体系、Hero 模板中的居中大标题 + 两个 CTA 按钮 + 渐变 Dashboard 示意、Lucide 图标库的随手可得和视觉中立性。AI 选 purple 不是因为喜欢紫色，是因为 prompt 没能指定更强的设计逻辑；AI 产生五层嵌套 card 不是因为觉得那样最好，是因为 card 是未知内容最安全的结构答案。

**反 AI 同质化设计的本质是约束工程（Constraint Engineering）。** 不是问 AI「做一个漂亮的 UI」，而是把设计领地定义得足够窄，让「互联网平均设计」不再是合法答案。

---

## 二、视觉特征解剖：哪些信号让 AI 设计暴露身份

以下特征并非单独存在，而是以组合形式出现。检测时关注**聚类**而非单项。

### 2.1 紫蓝色渐变综合征

**典型组合：** 深海军蓝背景 + 居中白色标题（渐变色词如「AI」「未来」「工作流」）+ 紫色 CTA 按钮 + 毛玻璃浮动卡片 + 左上角紫色光晕 + 右下角青色光晕。

**代码气味：**
```css
bg-gradient-to-r from-purple-500 to-blue-500
bg-gradient-to-br from-indigo-600 via-purple-500 to-pink-400
filter: blur(80px) /* 背景散景 */
backdrop-blur-xl bg-white/10
shadow-purple-500/20
```

**根源：** 这些 utility class 在 Tailwind 生态里随手可得，模型从大量 SaaS 模板和 AI 产品营销页中学到了 purple = 「科技/AI/未来」。

### 2.2 字体平权主义：Inter 统治一切

**典型组合：** 全页面同一个 sans-serif，hero 用 600 weight 大标题，body 用 400 weight gray-600，14–16px 正文，48–64px hero 标题，1.5 行高，全部权重集中在 400/600/700 三档。

**代码气味：**
```tsx
font-family: Inter, sans-serif
text-4xl md:text-6xl font-bold tracking-tight
text-gray-600
```

**根源：** Inter 是训练数据中最常见的开源字体，模型把它当作「无立场」的默认选项，而非一个需要设计理由的决策。

### 2.3 Cardocalyps（卡片末日）：万物皆卡片，嵌套无止境

**典型组合：** Hero 卡片 → Dashboard 卡片 → Stat 卡片 → Mini Chart 卡片 → Badge，每个层级都有独立 padding、radius、shadow。

**代码气味：**
```tsx
// 每个 feature 都是相同结构
<div className="rounded-2xl border bg-white shadow-sm p-6">
  <div className="w-12 h-12 rounded-xl bg-primary/10"><Icon /></div>
  <h3>Feature</h3><p>Description</p>
</div>
```

**根源：** 卡片是最容易生成的包含结构，AI 用它解决所有内容分组问题，而不判断内容是否真的需要独立容器。

### 2.4 图标拜物教：每个 heading 上面一个 Lucide

**典型组合：** 48–64px 圆角图标色块（通常带 `bg-primary/10`）+ 标题 + 描述，等间距三列网格。

**代码气味：**
```tsx
import { Sparkles, Shield, Users } from 'lucide-react'
<div className="w-12 h-12 rounded-xl bg-indigo-500/10"><Sparkles /></div>
```

**根源：** Lucide 图标随手可得，图标 = 「精致感」已是模板思维，AI 用它填充每个 feature 槽位而不问该槽位是否真的需要图标。

### 2.5 柔焦恐惧：glass + glow + shadow 的装饰性堆叠

**典型组合：** 半透明卡片 + backdrop-blur + 柔和 shadow-xl + 边缘霓虹光晕 + 渐变文字。

**代码气味：**
```css
backdrop-blur-xl bg-white/10 shadow-xl
shadow-purple-500/20 ring-white/10
```

**根源：** 效果层是「高级感」的最快注脚，AI 用它们掩盖设计意图的缺失而不提供真实的交互深度逻辑。

### 2.6 SaaS Hero 模板：居中宇宙中心

**典型组合：** `text-center max-w-3xl mx-auto` 的 hero → 三个等宽 feature 卡片 → 指标行（假数据「10x更快」「99.9% 正常运行」「50k 用户」）→ testimonials → pricing → FAQ。

**代码气味：**
```tsx
<section className="text-center max-w-4xl mx-auto py-24">
  <h1>Transform Your Workflow</h1>
  <p className="text-gray-600">Unlock powerful insights effortlessly...</p>
  <div className="flex gap-4 justify-center mt-8">
    <button className="rounded-full bg-indigo-600">Get Started</button>
    <button className="rounded-full border">Learn More</button>
  </div>
</section>
```

### 2.7 对称执念与均匀节奏

AI 追求「平衡感」时几乎总会产生：**所有 section 等高等宽等间距，所有卡片等大小等 padding，所有图标等尺寸，所有边框圆角相同**。

**感知机制：** 心理对称是安静的、静态的；不对称是动态的、吸引注意力的（NN/g）。AI 不懂得何时用对称传达稳定（银行/医疗），何时用不对称传达张力（品牌/编辑/创意产品）。

---

## 三、代码层面的系统性修复

### 3.1 Token 体系：从命名值到语义决策

**问题：** AI 发明视觉决策时是因为它只能看到原始值，不能理解角色。

**修复：建立语义 Token 层级。**

```
primitive tokens（原始值）→ semantic tokens（角色）→ component tokens（实例）
```

```css
/* 原始值（危险区） */
--blue-500: #3b82f6;
--gray-600: #4b5563;

/* 语义 Token（设计意图） */
--color-ground: #f4efe6;       /* 纸张/背景 */
--color-ink: #16130f;         /* 主文本 */
--color-accent-warm: #b84a28; /* 行动/强调 */
--color-accent-cool: #2f6f73; /* 数据/信息 */
--color-paper: #f7f2ea;       /* 次级表面 */
--color-line: color-mix(in srgb, var(--ink) 14%, var(--ground));

/* 组件 Token（具体实例） */
--button-primary-bg: var(--color-ink);
--button-primary-text: var(--color-ground);
--card-surface: var(--color-paper);
--form-label-color: var(--color-ink);
```

```tsx
/* 字体角色 Token */
--font-display: "Fraunces", Georgia, serif;
--font-text: "IBM Plex Sans", Arial, sans-serif;
--font-mono: "CommitMono", ui-monospace, monospace;

--type-hero-size: clamp(3.2rem, 9vw, 8.5rem);
--type-hero-line: .86;
--type-body-size: 1.0625rem;
--type-body-line: 1.58;
--type-label-tracking: .14em;
```

**关键原则：** Token 名称描述**用途**，不描述值。`--color-action-primary` 比 `--blue-500` 给模型的约束力强得多。

### 3.2 抗 AI 的 CSS 组件抽象

**问题：** AI 直接用 utility class 组装，绕过设计系统。

**修复：把 easy path 变成 semantic component。**

```tsx
/* 禁止 AI 自由组合 utility */
/* ✗ AI 可能写出：className="rounded-2xl bg-white/80 backdrop-blur-xl shadow-xl" */

/* 正确的组件层级 */
<Surface variant="ruled" density="compact">
  <Card padding="compact" radius="media">
    <FeatureRow icon={<MetricIcon />} label="活跃用户" value="12,847" />
  </Card>
</Surface>

/* Surface 变体 */
.surface--ruled { border: 1px solid var(--color-line); background: var(--color-ground); }
.surface--tinted { background: var(--color-paper); }
.surface--elevated { box-shadow: var(--shadow-popover); }

/* Card 变体 */
.card--compact { padding: var(--space-3) var(--space-4); }
.card--media { border-radius: var(--radius-media); overflow: hidden; }
.card--note { padding: var(--space-6); box-shadow: var(--shadow-paper); }
```

### 3.3 布局语法库（Layout Grammar）

**问题：** AI 只知道少数几个页面模板，无法根据内容选择布局。

**修复：提供基于内容类型的布局模式选择器。**

```tsx
const layoutPatterns = {
  // 编辑部分割：图像/制品在一侧，文案在另一侧，底部基准线偏移
  editorialSplit: {
    grid: "grid-cols-12 items-end",
    copySpan: "col-span-5",
    artifactSpan: "col-span-6",
    offset: "translateY(2rem)"
  },
  // 海报网格：大标题占 7/12 列，边距注释放小字
  posterGrid: {
    headlineSpan: "col-span-7",
    marginNotes: true
  },
  // 数据主导：关键数字作为字体对象，图表次之
  dataLed: {
    metricTypographic: true,
    chartSecondary: true
  },
  // 账本列表：紧凑行，左标签右数据，严格基线对齐
  ledger: {
    grid: "grid-cols-[12ch_1fr]",
    density: "compact"
  },
  // 工具界面：真实 UI 截图 + 注解，不用装饰性 Dashboard 示意
  toolInterface: {
    screenshotFirst: true,
    annotationOverlay: true
  }
};

// AI 的 layout 选择逻辑
function chooseLayoutPattern(content: ContentType): LayoutKey {
  if (content.type === "workflow") return "annotatedProcess";
  if (content.type === "data") return "dataLed";
  if (content.type === "comparison") return "ledger";
  if (content.type === "brand") return "editorialSplit";
  return "posterGrid";
}
```

### 3.4 密度模式系统（Density Modes）

**问题：** AI 倾向于在所有 surface 使用相同的宽松 SaaS 间距。

**修复：密度是设计系统的顶层变量。**

```json
{
  "density": {
    "productive": {
      "controlGap": "6px",
      "panelPadding": "12px",
      "sectionGap": "32px",
      "typeRole": "body.compact"
    },
    "standard": {
      "controlGap": "8px",
      "panelPadding": "16px",
      "sectionGap": "56px",
      "typeRole": "body.default"
    },
    "editorial": {
      "controlGap": "12px",
      "panelPadding": "24px",
      "sectionGap": "clamp(64px, 10vw, 144px)",
      "typeRole": "body.editorial"
    },
    "immersive": {
      "controlGap": "16px",
      "panelPadding": "32px",
      "sectionGap": "clamp(80px, 15vw, 200px)",
      "typeRole": "display"
    }
  }
}
```

### 3.5 间距关系 Token（替代纯数值 Token）

```css
/* 纯数值 Token（可用，但不够） */
--space-1: .25rem;
--space-2: .5rem;
--space-4: 1rem;
--space-6: 1.5rem;

/* 关系 Token（约束力更强） */
--gap-inline-icon-label: .35em;     /* 图标与标签的关系 */
--gap-caption-to-media: .5rem;       /* 说明文字贴近图像 */
--gap-heading-to-body: .6em;         /* 标题到正文的间距 */
--gap-paragraph: 1.4em;               /* 段落之间 */
--gap-group: 1.75rem;                /* 内容组之间 */
--gap-section: 4rem;                /* narrative 段落之间 */
--gap-scene: clamp(5rem, 12vw, 10rem); /* 大段节奏转折 */
--gap-annotation-offset: 6rem;        /* 边缘标注与正文 */

/* AI 选用 --gap-scene 比 py-24 更容易被约束 */
```

### 3.6 _elevation Token（海拔/阴影体系）

**问题：** AI 对所有卡片使用同一个 `shadow-lg`，或者用 `shadow-xl shadow-purple-500/20` 制造虚假深度。

**修复：物理隐喻明确的 Elevation 系统。**

```css
:root {
  --elevation-flat: none;                                  /* 静止内容 */
  --elevation-ruled: 0 1px 0 rgba(22,19,15,.08);          /* 分割线等价物 */
  --elevation-lifted: 0 4px 16px rgba(22,19,15,.10);      /* 可移动卡片 */
  --elevation-popover: 0 18px 40px rgba(22,19,15,.14);   /* 浮层 */
  --elevation-dialog: 0 32px 80px rgba(22,19,15,.22);    /* 对话框 */
  --elevation-glow: 0 0 24px rgba(184,74,40,.25);        /* 强调光晕（仅用于 active/focus） */
}

/* 使用规则：静态内容不得使用 popover 以上的 elevation */
```

### 3.7 抗 Slop 的类型系统

```css
:root {
  /* 五层类型角色，而非 size+weight 组合 */
  --type-display: {
    font-family: var(--font-display);
    font-size: var(--type-hero-size);
    line-height: var(--type-hero-line);
    letter-spacing: -0.055em;
    font-weight: 620;  /* 非 bold，默认用 medium */
  };
  
  --type-title: {
    font-family: var(--font-text);
    font-size: clamp(1.75rem, 3.5vw, 3rem);
    line-height: 1.1;
    font-weight: 500;
  };
  
  --type-body: {
    font-family: var(--font-text);
    font-size: var(--type-body-size);
    line-height: var(--type-body-line);
    max-width: 65ch;  /* 阅读最佳行长 */
  };
  
  --type-caption: {
    font-family: var(--font-mono);
    font-size: .72rem;
    letter-spacing: .06em;
    text-transform: uppercase;
    font-weight: 500;
  };
  
  --type-annotation: {
    font-family: var(--font-display);
    font-style: italic;
    font-size: 1.05rem;
    opacity: .75;
  };
}
```

---

## 四、字体、颜色、间距、层级、对称性：五大检测通道

### 4.1 字体决策链

**AI 的失败模式：**
- 全页面单一 neutral sans，无角色区分
- 过度依赖 Inter/Montserrat/Poppins/Roboto，无设计理由
- 大标题不手动调整字偶距（AV/WA/VA/LY/To 等问题配）
- 字号无意义跳跃（15px/17px/19px 而非角色定义）
- 行高与内容长度/字号不匹配
- 全大写 label 无依据地加宽字间距

**修复路径：**
1. 角色选择 > 字号选择（`heading.section` 而非 `text-4xl`）
2. Display 字体配 Text 字体（ editorial 对比 + trustworthy）
3. 光学调整：display 的 tracking 收紧，caption 的 tracking 放宽
4. 行高按内容密度设置（长正文 1.5–1.6，短居中标题 1.0–1.1）
5. Variable Font axes：使用 `opsz`（光学尺寸）、`GRAD`（粗细而不改宽）、`wdth`（宽窄）赋予排版深度

**实用组合参考（The Crit）：**
- Instrument Serif + Inter → 编辑部/信任感
- Satoshi/Geist Sans → SaaS
- IBM Plex Sans + JetBrains Mono → 金融科技/技术工具
- Manrope/DM Sans/Lexend → 消费/生活方式
- Fraunces（display）+ 基础 sans → 创意/品牌

### 4.2 颜色系统：超越色轮的故事

**AI 颜色综合征：** 高饱和蓝紫渐变无处不在，所有 badge 颜色亮度相同，地面和文本之间对比不足或过强，色彩选择无品牌理由。

**人类感色彩系统的特征：**
- **来源故事**：从材质、地点、文化、季节、实物中提取色彩，而非从「现代配色」网站复制
- **饱和度稀缺**：饱和度是注意力货币，只在关键行动点花费；背景保持低饱和
- **明度对比独立于色相**：独特性不一定靠色相差异实现；暗橄榄文本配暖白背景（窄色相范围 + 宽明度对比）比彩虹渐变更有个性
- **中性色有温度**：不是 #fff 和 #000，而是 off-white、warm gray、ink brown、paper cream——引入氛围感
- **对比度是审美约束**：WCAG 对比度要求不是体验折扣，而是可读性设计的一部分

**色板作为故事（NN/g）：**
```
「界面应该感觉像档案纸和黑墨水，加上一个紧急红戳。
背景：暖纸色；文本：墨黑；次级表面：稍深的 Manila；CTA：盖章红；数据高亮：铅笔蓝」
```

### 4.3 间距：关系的编码

间距是最清晰的 AI 检测器之一，因为它编码分组、强调、节奏和工艺感。

**AI 的间距失败：**
- 所有 section 使用相同 py-24 padding，不管内容复杂度
- 标题正文间距 == 卡片间距 == 区域间距（无节奏感）
- Hero 垂直居中所有元素，等间距排列
- 卡片内部图标/标题/文本/标签/按钮全部等间距

**间距修复核心：**
- 使用关系 Token 编码意图，不只用数值
- 基线网格 + 铅直节奏系统对齐行高、元素高度和垂直间距
- 编辑设计允许意外的暂停或压缩来创造层级
- 通过眯眼测试（squint test）：模糊页面，主要焦点仍然可辨则为通过

### 4.4 视觉层级：引导注意力而非均匀抛光

**AI 的两种极端失败：**
1. **过度抛光**：每个元素同等精致，卡片、标题、图标、按钮、徽章、阴影、插图全部同等强调 → 用户不知道往哪看
2. **过度主导**：大 Hero 标题和渐变 CTA 统治页面，不管页面实际任务是什么

**NN/g 层级工具：**
- Scale：相对尺寸传达重要性
- Value/Color：亮度/色相区分优先级
- Spacing：proximity = 关联性
- Placement：扫描顺序决定阅读顺序

**实际检验：** 去掉颜色，层级还成立吗？如果不成立，颜色在承担过多的装饰性工作。

### 4.5 对称性：何时安静，何时动态

**AI 对称执念的信号：**
- 所有 major block 居中，所有 margin 相等，所有元素坐落在明显轴线上
- 卡片 icon 位置相同、标题长度相同、段落长度相同、按钮相同、阴影相同
- 六张 feature 卡片轮换六种颜色只为网格视觉平衡，但颜色不编码类别

**反对称策略：**
- 使用 12 列网格但允许内容跨越非常规列（如 2/8、8/13）
- 至少一个主要 section 使用左对齐或偏移
- 避免三个连续 section 具有相同 max-width 和居中对齐
- 在用户任务有方向的地方打破对称：before/after、input/output、时间线、进度

---

## 五、Christopher Alexander 模式语言：约束系统的理论原型

Alexander 的模式语言是**最有价值的 AI 面设计系统理论模型**，不是因为它的形而上学，而是因为它精确描述了如何用条件生成规则替代模糊形容词。

### 5.1 模式的精确结构

```
Pattern: [模式名称]
Context：模式适用的场景
Problem：重复出现的冲突或人类需求
Forces：使问题复杂的竞争压力
Solution：解决力量的不变空间关系
Links：上层的包含模式 + 下层的细化模式
```

### 5.2 AI 面设计系统的具体模式示例

**模式：可信 AI 结果面板（Trustworthy AI Result Panel）**
- **Context：** 展示可能影响用户决策的机器生成答案
- **Forces：** 用户需要快速理解，但也需要来源、不确定性和可逆操作
- **Solution：** 答案放在安静地面上，标注 AI 参与，包含置信度/来源元数据的渐进披露，区分主要用户行动和系统建议行动，提供更正或反馈
- **Larger：** Assisted Decision、Explainable Workflow
- **Smaller：** Source Chip、Confidence Language、Reversible CTA、Human Override

这远比「做一个 AI 答案卡片」有力。它把形式绑定到人类力量。

**模式：密度区段（Density Zone）**
- **Context：** 不同内容类型需要不同的空间密度
- **Forces：** 仪表板需要信息密度，着陆页需要戏剧感，表单需要聚焦感
- **Solution：** 定义密度模式：compact/standard/spacious/editorial/immersive；每个映射到 spacing/type/width/imagery
- **AI 规则：** AI 不得为 section 发明密度；密度由 zone 模式决定

### 5.3 Alexander「十五个基本性质」的抗 AI 约束

Alexander 后期的「活的结构」性质列表是实用的反通用约束：

| 性质 | AI 通常的问题 | 抗 AI 效果 |
|------|--------------|-----------|
| Levels of scale | 只有 hero 大 + 卡片同样大，两档 | 多档层级：页面→区域→组件→文本→微细节 |
| Strong centers | 所有元素音量相同 | 每个构图有主次焦点 |
| Boundaries | 任意边框和阴影 | section/card/control 需要有意义的边界 |
| Alternating repetition | feature card 机械重复 | 重复有节律变化 |
| Positive space | 均匀 padding | 空白有形状，不是剩余 |
| Roughness | 过度平滑 | 局部适应，不追求全局一致 |
| Echoes | 视觉纹理无深度互锁 | 子元素与整体系统共振 |

---

## 六、历史系统作为反 AI 工具

### 6.1 瑞士国际主义风格（Swiss Grid System）

瑞士风格不是「极简」，而是**基于规则的生成系统**：模块化网格、不对称布局、无衬线字体、清晰层级、内容驱动的构图。不是说内容一样，而是网格逻辑产生精确的组合。

**对 AI 的教训：** 强大的布局逻辑可以产生多种组合，而不依赖当前的 SaaS 模板。用不对称网格替代居中 Hero，用严格的类型层级替代「看起来不错」的标题。

### 6.2 Bauhaus 几何系统

Bauhaus 用功能网格、几何形式、原色和「形式追随功能」原则——设计从材质和目的出发，而非从审美模板出发。

**对 AI 的教训：** 组件的视觉处理应该遵循其功能角色，不应该每个组件看起来同样「精致」。

### 6.3 生成式身份系统（MIT Media Lab / Pentagram）

MIT Media Lab 身份系统展示：**规则驱动的系统可以生成多种相关但不同的输出**。七乘七网格为 Lab 及其研究组生成数千种标志变体，保持可识别性。

**对 AI 的教训：** 设计系统不是 Figma 组件库，而是一个生成引擎。AI 应该从种子值组装，而不是每次重新发明视觉语言。

---

## 七、代码实现：实用技术栈

### 7.1 美学 Lint（超出 Style Lint）

普通 linter 检查语法和可访问性。**美学 linter** 检查高概率通用 UI 组合。

```tsx
// ESLint 规则伪代码：检测 radius 单调性
function detectRadiusMonoculture(ast) {
  const radiusClasses = collectTailwindClasses(ast, /^rounded(-[a-z0-9]+)?$/)
  const counts = countBy(radiusClasses)
  const maxShare = Math.max(...Object.values(counts)) / radiusClasses.length
  
  if (maxShare > 0.75 && radiusClasses.length > 8) {
    warn('Radius monoculture: too many elements share the same rounding.')
  }
}

// 检测可预测的着陆页节奏
function detectSectionRhythm(sections) {
  const gaps = sections.map(s => gapBetween(s.prev, s.current))
  
  if (mostlyEqual(gaps) && sections.length >= 5) {
    warn('Section rhythm is too uniform. Add content-shaped pacing.')
  }
}

// 检测渐变滥用
const GRADIENT_CLICHES = [
  /from-(purple|violet|indigo)/gi,
  /to-(blue|cyan|pink)/gi,
  /via-purple/i
]

// 检测 generic hero 模式
const GENERIC_HERO = /text-center[\s\S]{0,80}max-w-(2xl|3xl|4xl)[\s\S]{0,80}mx-auto/
```

### 7.2 SVG 材质纹理技术

```html
<!-- 纸张纹理 filter -->
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="paper-grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" seed="42" result="noise" />
    <feColorMatrix type="saturate" values="0" />
    <feComponentTransfer>
      <feFuncA type="table" tableValues="0 0.05" />
    </feComponentTransfer>
    <feBlend in="SourceGraphic" in2="noise" mode="multiply" />
  </filter>
</html>

<style>
.paper-surface { filter: url(#paper-grain); }
</style>
```

```html
<!-- 边缘粗糙化 filter -->
<filter id="roughen">
  <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="7" result="noise" />
  <feDisplacementMap in="SourceGraphic" in2="noise" scale="6" xChannelSelector="R" yChannelSelector="G" />
</filter>
```

### 7.3 可变字体（Variable Font）的人性化层

```css
/* AI 通常只用 size 和 weight。可变字体让排版响应式且有光学感 */
:root {
  --font-body-var: "Recursive", system-ui;
  --font-caption-var: "Recursive", system-ui;
  --font-display-var: "Fraunces", Georgia, serif;
}

body {
  font-family: var(--font-body-var);
  font-variation-settings: "opsz" 14, "GRAD" 0, "wght" 400;
}

.caption {
  font-variation-settings: "opsz" 10, "GRAD" 25, "wght" 500;
  letter-spacing: .06em;
}

.display {
  font-family: var(--font-display-var);
  font-variation-settings: "opsz" 72, "wdth" 92, "wght" 680;
  letter-spacing: -0.055em;
}
```

### 7.4 种子化的人类化随机性

```ts
import seedrandom from 'seedrandom'

export function humanize(seed: string) {
  const r = seedrandom(seed)
  return {
    // 旋转：-0.6deg 到 +0.6deg
    rotate: (r() - 0.5) * 1.2,
    // 微偏移
    offsetX: Math.round((r() - 0.5) * 6),
    offsetY: Math.round((r() - 0.5) * 6),
    // 噪点种子
    grainSeed: Math.floor(r() * 1000),
    // 手绘下划线（5 个控制点的 Y 偏移）
    underline: Array.from({ length: 5 }, () => (r() - 0.5) * 3)
  }
}
```

```tsx
function NoteCard({ id, children }) {
  const h = humanize(id)
  return (
    <article style={{
      '--rotate': `${h.rotate}deg`,
      '--dx': `${h.offsetX}px`,
      '--dy': `${h.offsetY}px`
    } as React.CSSProperties}
    className="note-card">
      {children}
    </article>
  )
}
```

**关键约束：** 随机性必须有种子（可重现）、有界（可用性）、有意义（内容或品牌驱动）。

### 7.5 内容驱动的布局变体

```tsx
const spanRules = {
  quote: { col: 2, row: 1 },      // 引用跨两列一行
  image: { col: 2, row: 2 },      // 图像跨两列两行
  metric: { col: 1, row: 1 },     // 指标只占一列一行
  note: { col: 1, row: 2 }        // 注释占一列两行
}

// AI 不得随意决定布局；内容类型决定跨度
```

### 7.6 字体排版的 CSS Intrinsic 布局

```css
/* 使用 subgrid 对齐嵌套内容 */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--gap-group);
}

.card {
  /* 继承父 grid 的行列 */
  grid-row: span 1;
  subgrid;
  /* 内部元素与父网格对齐 */
}

/* 使用 :has() 让组件响应内容 */
.card:has(.card__media) {
  grid-template-rows: auto 1fr;  /* 有媒体时顶部放图 */
}

.card:has(.card__kicker) {
  --accent-weight: 720;  /* 有 kicker 时加重 */
}

/* container queries 让模块局部响应 */
.feature-panel {
  container-type: inline-size;
  container-name: feature;
}

@container feature (min-width: 480px) {
  .feature { grid-template-columns: 2fr 1fr; }
}
```

---

## 八、检测与 CI 流程

### 8.1 三层检测架构

```
Figma（设计阶段）
  └─ Sameness audit：radius/shadow/spacing/alignment 分布直方图
  └─ Generic pattern flags：居中 Hero + 渐变 + 三卡片
  └─ Token intent audit：检测原始值 vs Token 使用
  └─ Rhythm map：垂直间距时序可视化

Local dev（编码阶段）
  └─ ESLint custom rules：AST 级别检测 utility 滥用
  └─ Stylelint rules：CSS 值的分布检查
  └─ Tailwind plugin：禁别名化 generic utilities

CI/CD（构建阶段）
  └─ Playwright screenshot：核心页面截图 + 视觉度量
  └─ Visual diff（Chromatic/Percy）：检测回归到默认值
  └─ Aesthetic risk scorecard：spacing 直方图、color 分布、radius 分布、对齐分布
```

### 8.2 美学风险报告模板

```
Aesthetic risk: medium-high

检测到的问题：
- 83% 的卡片使用相同 radius/shadow/padding
- 6/7 个 section 居中且垂直节奏相同
- 字体只用了两个 weight，无光学/上下文变化
- 渐变背景匹配被禁用的 generic aurora 模式

建议：
- 将 feature section 切换为 ledger 布局
- 将原始 radius 替换为 media/control/sheet token
- 添加 caption 和 annotation 字体角色
- 使用内容派生的图标或移除装饰性图标
```

---

## 九、抗 Slop 检查清单

### 生成前
- [ ] 定义受众、工作任务、主要证据、内容清单
- [ ] 加载设计系统和抗 Slop 规则文件
- [ ] 选择非当前 SaaS 的视觉领地
- [ ] 定义 Token 体系

### 生成中
- [ ] 使用语义组件而非自由 utility
- [ ] 根据内容类型选择布局模式
- [ ] 使用真实制品（截图、数据、引言、图表）而非装饰
- [ ] 避免被禁视觉陈词滥调
- [ ] 包含非 happy path 状态

### 生成后（lint）
- [ ] 运行 gradient、shadow、card、icon、generic copy 的代码 lint
- [ ] 检查对比度和响应式状态
- [ ] 移除一层装饰
- [ ] 添加一个内容特定的细节
- [ ] 如果 section 感觉相同则改变节奏
- [ ] **最终测试：** 换个 Logo 这页还能属于任何 AI 创业公司吗？若是，仍是 Slop

---

## 十、核心结论

**AI Slop 不是因为 AI 无能力设计，而是因为在没有设计系统的情况下把创作权委托给模型。** 模型选择了现代网页设计的统计中心。

抗 Slop 设计因此不是一种风格，而是一种**工作流程**：
1. 给 AI 具体 context
2. 严格的 Token
3. 作者约束
4. 布局语法
5. 真实内容
6. 检测通过

让模型在观点内运作。输出停止看起来像 AI 生成的时刻，是它停止看起来像所有人 prompt 平均值的时刻。

**最有力的设计系统不是提供颜色和组件，而是提供：节奏、密度、排版、材质、动机、异常处理和美学 lint。** 代码库应该让通用输出**失败但不静默**。设计工具应该显示分布和同类风险。生成层应该是种子的、语义的、内容派生的。

人的感觉不来自随机的不完美，而来自**情境化的决策**——那些经得起翻译成代码的决策。
