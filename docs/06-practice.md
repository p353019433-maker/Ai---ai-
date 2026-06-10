# 06 · 实操 — 反 slop 清单、配方、Prompt 模板、验证协议

> 蒸馏自：APPLIED-DESIGN-JUDGMENT、design-philosophy-master、design-ai-prompt、DESIGN-LAB-PROTOCOL、method-autonomous-overnight-learning（原文见 git 历史）

## 一、反 AI-slop 审查清单（13 项）

接受任何 AI 生成的 UI/网页/品牌设计前逐项检查。**只过视觉关、但在结构/状态/文案/可访问性/出处任一项失败的，仍然是 slop。**

1. **问题框架**——设计是否说出用户目标、机构目标、约束？
2. **信息结构**——不看样式能否画出 IA？
3. **主操作**——每个状态是否恰好一个主导下一步动作？
4. **状态覆盖**——loading/empty/error/partial/success/disabled/undo 是否都被设计？
5. **字体**——选择是否被阅读条件、层级、语言、语气证成？
6. **色彩**——是否有意编码层级/状态/品牌，还是装饰性情绪？
7. **间距网格**——对齐是否系统化？
8. **文案诚实**——标签与消息是否平实说出动作与后果？
9. **动效**——解释连续性/状态，还是表演精致感？
10. **可访问性**——标题、标签、对比度、键盘、读屏、移动行为能否存活？
11. **生产模型**——token、组件、响应规则、归属是否明显？
12. **文化/机构契合**——风格属于这个主体，还是进口的时尚？
13. **出处**——参考能否被命名（超出 "modern/minimal/clean"）？

**AI 出活感速查**（出现即处理）：sparkles 泛滥；"Powered by AI" 当价值主张；紫粉渐变 + 玻璃拟态 + 3D blob 三件套；emoji 图标；全部居中对称；5 并列 feature 卡片；假友好文案；thumbs up/down 当唯一反馈；隐藏"人类可随时停"。

## 二、去 AI 化数值配方（速查）

AI 廉价感 = 训练自最大公约数审美。三大原型问题：表层光鲜内核空洞 / 对称工整没性格 / 装饰代替思考。**解法 = 做减法 + 建立层级 + 给一个主见。**

- **色**：8-10 阶灰；禁纯黑 #000（用 #0F0F0F）；带温度的灰（slate/sage/sand）；**1 个主色用量 ≤5%**；禁紫粉渐变。锚点：Linear（#F4F5F8+#222326+蓝）、Stripe（slate+紫青）。
- **字**：2-3 family（正文 Inter/Geist/Söhne + 标题 GT Sectra/Fraunces）；标题/正文比 ≥1.5×；一页 ≤4 个字号；行宽 45-75ch；display 负字距；数据 tabular figures；Sentence case。
- **层级**：Size > Weight > Color > Position > Whitespace；de-emphasize to emphasize；一页只 1 个显著元素、1 个 CTA（Von Restorff）。
- **布局**：4/8 倍数间距；section 间距 ≥ 内部 2×；**左对齐、不对称**（对称=模板感）；少用 1px border；圆角统一。
- **六条心法**：先限制再创造（1 主色+1 字体+1 圆角）；做减法的勇气（80% 的"加一笔"是错觉）；有一个主见；模仿具体对象不混搭；网格先于元素；真实 > 完美。

**分媒介一眼假清单**：通用=渐变文字/emoji 装饰/AI 人脸/玻璃拟态组合；PPT=居中标题+握手 stock 图+彩虹配色+SmartArt；网页=hero 渐变 overlay+等大等距卡片+Vercel 主页克隆；App=5 tab+emoji 按钮+千篇 FAB；海报=渐变光晕+居中大段文字。

## 三、Prompt 模板

### 失忆 prompt vs 记忆 prompt

普通 prompt 要外观："Make a modern, clean, beautiful SaaS dashboard."（必出 slop）

**Less-amnesiac prompt 要记忆**——每条约束把形式系到一个被记住的条件上：

```text
Design a SaaS dashboard for finance operations teams.
The design must remember:
- medium: desktop web, dense tables, keyboard use, slow network states;
- institution: finance users need auditability, not playful ambiguity;
- production: React components, tokenized color/status system, localizable copy;
- reading: tabular numerals, right-aligned amounts, compact but scannable rows;
- use: loading, empty, error, partial sync, undo, export, permission-denied states;
- labor: support burden reduced by clear logs and recovery paths;
- history: borrow Swiss information clarity, not Helvetica-and-whitespace styling.
Avoid generic AI gradient/card aesthetics. Explain which tradeoffs you made.
```

### 结构化 brief 骨架（生成前写 30 分钟，省 4 轮迭代）

```text
Role: senior product/visual designer with experience in [domain].
Subject: [product] exists to [goal] for [users].
Behavior: the screen must help users [task], including [edge cases].
Structure: IA sections are [list]. Primary action is [one action].
Style reason: use [visual language] because [domain-specific reason].
Type: [fonts] because [reading condition / language / tone].
Color: [palette + hex] with roles [bg/text/action/status/data].
States: loading, empty, error, partial, success, disabled, undo.
Constraints: [grid, spacing scale, breakpoints, a11y, component library].
Anti-patterns: purple gradient, generic cards, fake friendly copy, emoji icons,
  centered everything, decorative motion, hidden uncertainty.
Validation: explain tradeoffs and what should be user-tested.
```

要点：**用数值替代形容词**（"Fraunces 700/64px，#F4F1EA"，不是"优雅的衬线"）；锚定 1-2 个具体参考（"风格锚定 Linear，密度锚定 Stripe"）；显式列反模式；附 2-3 张参考图并标注用途（图 1=风格，图 3=反例）。迭代时手术刀式 diff（"仅改 hero，其余不变"），每轮只动 1-2 个变量。

### 失忆批评 vs 记忆批评

普通批评："层级弱、按钮太响、字体平庸、要呼吸感。"
记忆批评把形式系回被遗忘的语境："这个层级不匹配用户失败后的恢复路径"；"这个按钮颜色把破坏性操作当营销 CTA 处理"；"这个字体没有产品实际数据需要的数字与字重"；"这块留白在隐藏缺失的系统状态，不是在澄清关系"；"这个 AI 披露放在保护公司的位置，不是告知用户的位置"。

## 四、四种设计模式（按信任契约选，不按"好看"选）

| 模式 | 用于 | 特征 | 参考 |
|---|---|---|---|
| 公共清晰 | 多样人群在压力/移动中定向 | 高可读、克制色、明显层级、低时尚依赖 | London Transport、Vignelli、GOV.UK |
| 编辑声音 | 身份、批评、文化立场 | 表现型字体、不对称节奏、有意摩擦、稳定 DNA 下的季节变化 | Eye on Design、Public Theater |
| 产品信任 | 重复任务的准确完成 | 清晰 IA、状态纪律、强微文案、token 一致性 | Linear、Stripe、设计系统治理 |
| 实验批判 | 质疑规范、文化立场 | 带论点的破规、故意"坏品味"、可见约束 | Memphis、brutalism、anti-design |

## 五、验证协议（防止档案假装成操作系统）

**四级验证，不准混淆**：
- **L0 档案声明**——原则出现在语料/综合里（"字体是基础设施"）。有用，但未在自己的工作上测过。
- **L1 产出应用**——原则被用于产出具体制品（before/after、prompt、取舍记录）。已应用，未验证。
- **L2 专家批评**——人类设计师/开发/可访问性审查者批评了制品（批评记录、矛盾笔记、修订 diff）。被外部挑战过。
- **L3 用户/效果证据**——任务成功率、错误率、理解度、转化、支持工单、可访问性测试。被验证或证伪。

**原则没到 L3 不许叫"被证明"。本仓库绝大多数主张是 L0。**

**实验模板**（每个实验小到能完成，真到会疼）：项目语境 / 基线与已知问题 / 应用的原则与预期冲突（**预测哪条原则会输**）/ 设计干预 / 审查（反 slop 清单+可访问性+实现摩擦）/ 效果证据（包括**什么变差了**）/ 教义修订（确认/削弱/新例外）。

**三个必做对抗性检查**：
1. **反方来源**——找至少一个会反对所选原则的可信传统（"结构先行"被表现型编辑设计挑战；"少即是多"被密集专家工具挑战）。
2. **失败模式预测**——设计前预测原则如何让结果更糟（极简可能藏状态；诚实文案在高压流程里可能显得冷）。
3. **什么会改变我的想法**——命名能证伪这个设计选择的证据（任务时间变长=新层级失败；读屏输出更差=视觉简化无效）。

**教义更新规则**：只有当①原则在批评下产出更好制品、②原则失败或需要边界条件、③两原则相撞且输家不显然、④用户证据反驳档案、⑤实现暴露隐藏生产成本——才更新教义，且写回对应文档。

> 在重复做到"选原则 → 预测冲突 → 产出制品 → 接受批评 → 修订制品 → 修订教义"之前，诚实标签是：**可审计的设计研究档案 + 应用综合层，不是经验证的设计操作系统。**

## 六、附：自主学习方法（产出本仓库的机制）

不让 agent 当主角，让脚本当主角——agent 只写脚本、启动、睡、醒来读结果。5 步：真实抓取（curl 存带元数据 Markdown，不靠模型回忆）→ 自我发现（只从质量分 q≥0.6 的文章提取新链接，防坏种子污染）→ 质量过滤（壳子信号+句子密度，<0.4 跳过）→ 优雅退出（SIGTERM 触发最终综合；PID 文件供跨会话 kill）→ 综合按主题而非计数。参数：并发 4、同域冷却 1.5s、失败 30 分钟重试。可换种子池迁移到任何领域。
