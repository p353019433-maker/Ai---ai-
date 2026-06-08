---
name: design-workflow-critique
description: 设计师工作流与批评 - 评审三级 / Action-Persuade-Clarify / AI 工具何时用 / 职业路径 5 阶段
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计师工作流与批评

## 一句话总结
真实的设计是"团队 + 批评 + 迭代"，AI 把执行变得廉价之后，剩下最值钱的反而是 brief 里的"为什么"、critique 里的"判断"、以及把决策沉淀成团队资产（tokens / principles / history）的能力。

## 一、设计师一天：研究 / 草图 / 协作 / 实现 / 评审

专业设计师的"一天"和"个人创作模式"最不一样的地方，是**几乎没有"做图时间"**。Figma《State of the Designer 2026》调查：**89% 设计师表示自己"用 AI 后做得更快了"，80% 表示"协作更好了"**——这背后是工作流的重新洗牌：执行时间被压扁，判断和沟通时间被拉长。

**典型一天**：早上 30 分钟站对齐 + 上午 critique + 中午和 PM/工程师同步 + 下午推动一个具体"决策点"往前推一格。Niko Klein 在《Hard problems are still hard》："It's not just about getting an idea out. It's about getting it right." 工具在变，但"把 idea 推向对的位置"没变——**设计师一天真正稀缺的不是"画"，是"定调"**。

Wikipedia Design Thinking 词条：设计是"iterative, non-linear process"，包含"context analysis, user testing, problem finding and framing, ideation and solution generating, sketching, prototyping, evaluating"。**设计师的一天是被多个循环（不是单一顺序）切割的**。

Wikipedia Interaction Design 词条：交互设计师"informed through iterative cycles of user research"，"work on problems that have many possible users, in many possible contexts, to create software with many possible states"——**设计"不会做完"，它本身就是循环**。

## 二、Critique Session：怎么开、规则、常见错误

NN/g 核心法则：

1. **会前先对齐"我要哪种反馈"**："set the stage with stakeholders before presenting the work. Provide context and deliberately ask for the types of feedback that will be most helpful to you." 不然会上 70% 时间浪费在无关意见上。

2. **三分类框架**：每个反馈必须落到 **Action**（必须改）/ **Persuade**（要说服我改）/ **Clarify**（我没看懂，需要你解释）之一。比让所有人"自由发言"高效十倍。

3. **24 小时 action items 关闭**："Most designers invest in running critiques but skip the followup. That missing step is often why feedback culture breaks down." 会开完没跟进 = critique 变"发泄会"。**会上写的 action item 必须 24 小时内被认领 / 排期 / 关闭**，否则下次开会没人再认真提意见。

4. **避免 hypothetical scenarios 和 pseudoevidence**："young designers feel overwhelmed" 是因为没信心顶回去。**会后的"防御训练"也是 critique 文化的一部分**：教初级设计师怎么用证据而不是个人偏好回应。

5. **远程 vs 现场**：
   - 远程最大风险："沉默的多数"——一半人不开麦，最后只剩两三个发声的人
   - 现场最大风险："权力不平等"——资深声音盖过新人
   - **Linear 的解法是"Quality Wednesdays"**：每周三团队会议里，每人必须"find and fix some defect that's decreasing the overall quality of the app"——**把 critique 变成"肌肉训练"**

## 三、设计评审的三级：critique vs stakeholder review vs ship review

Wikipedia《Design review》："evaluate designs against requirements to identify issues before committing to further work"，引用工程铁律"the cost of correcting a fault increases as it progresses through the development process"——**越往后越贵，所以评审不是一次性事件，是分级的**。

| 级别 | 频率 | 人数 | 目的 | 关键规则 |
|---|---|---|---|---|
| **Critique**（设计内部） | 每周 1 | 3-6 人 纯设计 | 打掉设计里的"傻逼决定" | **不问"老板喜不喜欢"** |
| **Stakeholder review**（跨职能） | 每 2 周/关键节点 | PM + 工程师 + 利益相关方（可达 10 人） | 对齐方向 + 暴露业务约束 | 不是细节抠图 |
| **Ship review**（上线前） | 1 次/项目结尾 | 不超过 5 人 | 最后的可发布性检查 | 无障碍 / 性能 / 边界 case / 品牌一致性 |

**最常被混在一起搞的灾难场景**："stakeholder 在 critique 会上大改交互"或者"critique 会上要求对齐 OKR"。

## 四、从 Brief 到 Final：真实案例

**Linear（Karri Saarinen 领导）**：
- 公开信条"**Output isn't design**"和"Design is more than code"——明确反对把设计等同于"产出界面"
- brief 阶段强迫团队先写一篇文章讲清楚"为什么这是值得做的"，再做界面
- 《Quality Wednesdays》文章：VP Engineering 2023 offsite 放了一段三按钮的录屏，全组没人看出问题，**于是把"找缺陷"制度化为每周肌肉训练**——两年完成 1000+ 个小修复

**Figma（Config 2026）**：
- 反复讲"**go broad and deep at the same time**"——同时用 AI 生成多个方向，再分别推进
- 强调"direction"和"craft"是两件事：AI 让"有什么可能"廉价化，**但"选择哪个 + 把它打磨到有人味"反而变贵**

**Stripe**："design as documentation" 闻名，UI 既是产品也是 API 文档。设计师相当一部分时间花在"把决定变成可被工程师直接用的系统"——颜色/间距/字号都进 design tokens，组件有 strict usage rules，**brief 出来后设计师先动 design system 再画具体界面**。

**Notion / Airbnb / Atlassian**：共同点是"**design system 优先于 feature 页面**"——任何一个新功能进来，设计师先问"这个能不能用现有 token + 现有 component 组合出来"，只有不能的时候才允许新发明。**这一步把 brief 推到了 60% 完成度**。

## 五、设计师 vs 工程师 vs PM：角色边界与决策权

NN/g《What Designers Actually Struggle with on Product Teams》："**Designers' top struggles aren't about design skills. They're about alignment, influence, and navigating org complexity — the work no one taught them to do.**" 跨职能协作才是设计师的主战场，不是画图。

**经典三角色分工**：
- PM 决定"做什么 + 为什么"（problem space + business outcome）
- 设计师决定"用什么形态 + 为什么这种形态"（solution shape）
- 工程师决定"怎么实现 + 哪些 trade-off"（implementation path）

实际工作里这三条线是重叠的——PM 提"加个导出按钮"，设计师可以挑战"也许该加个模板系统"，工程师可以挑战"导出会导致 5s 延迟"。**健康的团队把"挑战"当作默认；不健康的团队把"越界"当作冒犯**。

Figma《The design-to-code loop》新趋势：Figma MCP（Model Context Protocol）让 design decisions 直接进 Cursor / Codex / Claude Code 等编码工具，**design system 变成 coding agent 的"上下文"**——这把设计师角色从"画界面给工程师看"推到了"维护 AI 共同依赖的真相源"。

## 六、设计决策的文档化：原则 / Tokens / History

成熟的团队把决策沉淀成三种资产：

**1. 设计原则**（Principles）：3-7 条
- Stripe "Be consistent, not uniform"
- Atlassian "由内而外的克制"
- Linear "Output isn't design"
- 原则不是口号，是**在 trade-off 时用的——当两个方向都对，原则就是天平**

**2. Design tokens**：颜色/字号/间距/阴影/动效曲线全部进 token（Figma / Material Design 3 / Atlassian DS）。好处：design-to-code 自动化 + 改一处全站生效 + brand 一致性

**3. Design history / ADRs**：Figma 文件 + Loom + 决策记录。Linear Quality Wednesdays 把每个修复沉淀成可搜索的"决策史"，**下次遇到类似问题不用重新发明**。

Wikipedia Design thinking："non-verbal, graphic/spatial modelling media"——**文档不是写出来的，是画出来 + 论证出来 + 沉淀进系统的**。

## 七、AI 工具如何改变工作流

| 工具 | 路线 | 强项 | 弱项 / 何时不用 |
|---|---|---|---|
| **Figma AI / Figma Make / Figma Design Agent** | AI 放进 canvas | "your creative collaborator"：批量改名 / 改间距 / 应用 design system / 生成图像 / 调 copy tone / 翻译 | 不用于 final 界面（缺 brand 味） |
| **v0 by Vercel** | prompt → full-stack app | repository sync / agentic planning / one-click deploy | 不用于生产级 UI（一致性和 a11y 都不够） |
| **Uizard** | 手绘草图转数字 | Wireframe Scanner / Autodesigner 2.0 | 不替代设计师做 final 视觉 |
| **Magnific AI** | 图像升级 + 风格化放大 | moodboard 素材 / 终稿高清化 | 不用于"造一个不存在的素材"（伦理 + 版权） |

**注**：Galileo AI 实际是 AI observability 平台，不是设计工具——搜资料时容易踩坑。

Figma《State of the Designer 2026》关键数字：91% 设计师说 AI 改善了他们的设计，**AI 用户比非 AI 用户高出 25% 的工作满意度**。

Yuhki Yamashita Figma 博客："**If AI can make anyone a product builder, the real edge is knowing what's worth shipping.**" AI 让"能造"变廉价，让"该造什么"变昂贵。

## 八、职业路径：Junior → Senior → Staff

NN/g《Return of the UX Generalist》提了一个反直觉趋势：**AI 让 specialist 价值下降、generalist 价值上升，"expertise T"在变平**——深度仍在，但需要更宽。

**NN/g 5 stages of UX career progression**（核心不是工具熟练度，是**判断半径**）：
- **Junior**：管一个 screen
- **Mid**：管一个 flow
- **Senior**：管一个 product surface
- **Staff**：管一个 product line + 影响其他设计师方向
- **Principal**：管整个公司的 design org + 行业影响力

Linear Karri Saarinen 反复强调"**design is understanding, not execution**"。Figma "What matters when anyone can build"："方向（direction）+ 工艺（craft）是 AI 时代设计师的两根脊柱——Craft is what separates the memorable from the merely functional. **It's active: choosing, not accepting.**"

Frank Chimero《Why vs How》："教育过度教了'how'，而'why'是越来越稀缺的技能"。

## 9 条做好 critique 的可复用规则

1. **会前定调**：会前 24 小时发"我要哪种反馈"（视觉？交互？信息架构？），否则会上 70% 是噪音
2. **Action / Persuade / Clarify 三分类**：每个反馈必须落到其中一类
3. **24 小时内关闭 action items**：会开完没跟进，下次没人再认真提
4. **主持人（facilitator）必须存在**：固定 1 个人做时间管理 + 控场 + 防止"老板一言堂"
5. **先看作品，再看 brief**：避免"我先听你解释再来评判"的偏见
6. **用"我观察到 X，因为 Y，建议 Z"句式**，而非"我觉得 X 不好"
7. **限制人数**：critique 4-6 人 / stakeholder review 到 10 人 / ship review 不超过 5 人
8. **远程 + 沉默症**：强制"每人一分钟开口"，否则只剩 3 个人发声
9. **教初级设计师"顶回去"**：用证据而不是个人偏好回应 challenge

## 9 条反面教材

1. "我觉得蓝色不好"——没有 Action/Persuade/Clarify 分类的纯个人偏好
2. "我表妹可能看不懂"——基于 hypothetical scenarios 的伪证据
3. Stakeholder 在 critique 会上大改交互方向——把三个级别评审混着开
4. 主持人在做"评论家"而不是"时间管理员"——主持人一开口，全场闭嘴
5. 会议写满墙，会后无 action——critique 变发泄会
6. "老板说改就改"——权力不平等下的 critique，结果是设计被高资历者劫持
7. Critique 60 分钟塞 5 个项目——每个 12 分钟，全是表面评论
8. 设计师不接 review / "我做完了你别动"——拒绝迭代的设计师是高薪执行
9. 远程会议所有人静音——表面开完了，实际只 2 个人发声

## 8 条 AI 工具何时用 / 何时不用

1. **Figma AI** 用于"批量改名 / 改间距 / 应用 design system"——日常 30% 时间省下来用于真判断
2. **Figma Make / Design Agent** 用于"快速验证一个 flow 可不可行"——不用于 final 界面
3. **v0** 用于"产品 idea 的 24h 验证"——不用于生产级 UI
4. **Uizard** 用于"PM / Founder 拿手绘草图快速做出可点击原型"——不替代设计师做 final 视觉
5. **Magnific AI** 用于"moodboard 素材升级 + 终稿高清化"——不用于"造一个不存在的素材"
6. **AI critique 辅助**（Figma AI "give you feedback as you work"）用于"自查盲点"——不能替代真实用户测试
7. **不要用 AI 生成 production copy**——AI 文案缺品牌 voice + 缺法律风险意识
8. **不要用 AI 生成"人脸/特定人物"**——legal / ethical / brand 风险都不值得

## 5 条"如果你只能记一条"

1. **Critique 不是 review，是肌肉训练**：Linear 两年 1000+ 修复的核心不是"做了多少 critique"，而是"建立了看见问题的肌肉"。**一周一次、被制度化、有 follow-up 的 critique，比一周三次自由讨论有效十倍**
2. **AI 让"能造"变廉价，让"该造什么"变昂贵**：方向（direction）+ 工艺（craft）= AI 时代设计师的两根脊柱。"Craft is active: choosing, not accepting"——AI 默认产出要拒绝，要追问，要再磨
3. **设计决策必须文档化**：没有 design tokens + 没有 ADR + 没有 design history 的团队，会在 AI 时代被"重新发明轮子"反复消耗。**Figma MCP 把 design system 变成 LLM 的 contract，是这一波最大的一次工作流迁移**
4. **不要把三个评审级别混在一起开**：critique 是设计内部打傻逼决定，stakeholder review 是跨职能对齐方向，ship review 是最后可发布性检查——混着开 = 谁都不满意
5. **设计师一天里最稀缺的不是"画"**：稀缺的是"定调 + 沟通 + 判断"——个人创作模式 80% 时间花在"画"，团队模式 80% 应该是"对齐 / 评审 / 写原则 / 维护 system"

## 资源 URL
- Figma Blog: 《State of the Designer 2026》/ 《What matters when anyone can build》/ 《Hard problems are still hard》/ 《The design agent is here》/ 《TL;DR on MCP》
- Figma AI 产品页（figma.com/ai）
- Linear Blog: 《Quality Wednesdays》/ Linear Method
- NN/g: 《Closing the Loop: What to Do After a Design Critique Ends》/ 《The Return of the UX Generalist》/ 《5 Stages of UX Career Progression》/ 《What Designers Actually Struggle with on Product Teams》
- Wikipedia: Design thinking / Interaction design / User experience design / Design review
- Frank Chimero: 《Why vs How》
- Atlassian Design / Material Design 3 / Stripe Design / v0.app / Uizard / Magnific AI
