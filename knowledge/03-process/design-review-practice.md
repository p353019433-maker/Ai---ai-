---
name: design-review-practice
description: 设计评审实战 - 批评四层 / 3 分类反馈 / 三级评审 / 8 句句式模板 / 公开 vs 私下 / AI 10 套路审稿 / 5 大奖项评审机制
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计评审实战手册：从"我觉得不行"到专业反馈

## 一句话总结
**设计评审是结构化的产品决策会，不是审美辩论**——用"目标→证据→影响"取代"我喜欢/不喜欢"，24 小时内闭环、3 步反馈、3 级评审，把别人的稿子当系统而不是艺术品。

## 1. 批评四层：先把"在哪一层"对齐

Vignelli 反复强调：批评要先分层，否则甲方说"蓝色不好看"、总监说"信息密度太高"、你说"留白不舒展"——三人在三个层面吵。Vignelli/Rand/Poynor 一致的四层框架：

| 层级 | 关注点 | 典型发言 | 评审时该追问 |
|---|---|---|---|
| **个人偏好** | 我喜不喜欢 | "我总觉得这蓝色怪怪的" | 你的偏好有没有数据/用户支撑？ |
| **工艺（Craft）** | 像素级执行 | "行高不一致、间距没对齐 8pt" | 能不能给一条 lint 规则？ |
| **历史（Context）** | 行业/品牌传承 | "这不像我们" "iOS 早不用拟物了" | 引用的是什么先例？哪年？哪本规范？ |
| **理论（Theory）** | 设计原则/学科逻辑 | "这违反了格式塔接近性" "一致性被破坏" | 原则的优先级？和业务目标冲突时让谁？ |

**实操**：每次评审前 30 秒在白板写下"我们今天在哪一层"。当有人说"我不喜欢"，立刻 push 回去："这是个人偏好，还是有具体原则？"——这一句话就能砍掉 50% 的无效会议。

## 2. Critique Session 主持：5 步流程 + 24h 闭环

主持一场评审的不是最 senior 的人，是最有结构的人。NN/g 的标准流程：

**会前（24h）**
- 写会议说明文档：目标（1 句）、不在范围（3 条）、用户/场景（最多 3 张截图）、决策需要什么
- 文件命名：`[项目]_critique_v3_[日期].fig`——让评审者 0 上下文进入

**会中（45 分钟）**
1. **对齐（5min）**：主持人重述目标 + persona + 范围。所有人点头
2. **作者讲故事（5min）**：先讲"我为什么这样选"，不要解释每个像素
3. **Round Robin（20min）**：按顺序发言，每人说 "1 件有效的 + 1 个问题"
4. **深度讨论（10min）**：主持人把分歧归到 4 层（见主题 1），让矛盾显形
5. **行动闭环（5min）**：当场决定 A/P/C（见主题 3），分配 owner 和 due

**会后（24h 内）**
- Slack 发 recap：3 件事改了、3 件事不改及原因、下次评审日期
- 关键点：每改一次，发"这个改了因为你提了 X"——这是建立反馈文化唯一的方法

**反例**：会开完 3 周没动静，下次评审没人愿意认真说。

## 3. 3 分类反馈：Action / Persuade / Clarify

NN/g 的核心分类，决定了反馈是**要求**、**建议**还是**提问**：

| 类型 | 定义 | 句式 | 例 |
|---|---|---|---|
| **Action** | 客观可改，必须做 | "请把间距统一到 8" | "字号改 16，对比度达 4.5:1" |
| **Persuade** | 主观建议，给理由 | "我建议……因为……" | "建议主按钮用实心，因为次要操作会更高频" |
| **Clarify** | 我没懂，先解释 | "为什么这里用 modal？" | "这个状态机的出口是？" |

**判断表**（贴在工位上）：
- 有明确规范/数据支撑？→ **Action**
- 是品味/权衡？→ **Persuade**（必须给理由）
- 是没看懂/信息缺失？→ **Clarify**（先别下结论）

**核心规则**：Action 不需要理由（参考 WCAG、Material 规范就是答案）；Persuade 必须给 1 句理由；**Clarify 永远先于 Persuade**——你没懂就评价，是会上最大的浪费。

## 4. 三级评审：别把 stakeholder review 当 critique

NN/g 的三级模型，关键在**目的、参与人、产物都不同**：

| | **Critique** | **Stakeholder Review** | **Ship Review** |
|---|---|---|---|
| **目的** | 提升设计质量 | 对齐范围/优先级 | 上线前最后闸门 |
| **参与人** | 设计师 3-6 人 | 跨职能（PM/Eng/数据/法务） | 设计师 + Eng Lead + PM |
| **频率** | 每周 1-3 次 | 阶段门（1-2 周） | 上线前 1 次 |
| **产物** | Action 清单 | 决策记录（ADR） | 上线 checklist |
| **失败信号** | 全是 Persuade 没结论 | 设计师被"教"做设计 | 发现 P0 但没人有权力改 |

**关键区分**：
- Critique 里**设计师是 owner**，反馈是给设计师的输入
- Stakeholder Review 里**PM 是 owner**，设计是要被验收的交付物
- Ship Review 里**Eng Lead 是闸门**，讨论的是"还能不能上"而不是"好不好"

## 5. 8 句 Critique 句式模板（直接复制）

把"我觉得"替换成下面任意一句，1 秒升级为专业反馈：

1. **目标检视**："如果目标是把转化率从 3% 提到 5%，这个 CTA 设计是帮助还是阻碍？"
2. **影响分析**："我注意到 X，这可能导致用户 Y，因为 Z。"
3. **替代方案**："这里如果换成 A 而不是 B，会发生什么？"
4. **规范引用**："Material 3 规定主操作应该用 Filled 按钮，我们现在用 Text 按钮是为什么？"
5. **数据挑战**："这个判断有什么数据支撑？验证方法是什么？"
6. **用户代理**："一个 65 岁的用户第一次用，会发生什么？"
7. **极限测试**："如果内容是 10 倍长，这个布局还成立吗？"
8. **历史先例**："Airbnb 的 detail 页为什么不做这件事？有公开的复盘吗？"

**反例（禁用）**："不好看""太花了""感觉不对"——这些直接打回，让对方重说。

## 6. 公开 vs 私下反馈 8 条决策树

| 场景 | 公开 | 私下 | 不说 |
|---|---|---|---|
| 这是工艺问题（像素级） | ✓ | | |
| 涉及作者的能力/努力 | | ✓ | |
| 多人可能有同样疑问 | ✓ | | |
| 涉及跨职能冲突 | | ✓ | |
| 老板在场，需要保护作者面子 | | ✓ | |
| 错误会影响全组认知 | ✓ | | |
| 是品味不是问题 | | | ✓ |
| 你也不确定对不对 | | | ✓（先私下问自己） |

**黄金规则**：能用工艺/规范/数据说的，公开；只能用品味/直觉/个人经验说的，先私下问自己"我 100% 确定吗？"，不确定就闭嘴。

## 7. AI 输出 10 个套路审稿清单

AI 出的稿子有非常稳定的"指纹"，逐项打勾：

1. **配色**：高饱和紫蓝渐变 + 玻璃拟物 → 换成单色 + 中性灰
2. **字体**：通篇 Inter / Geist → 加一个衬线对比
3. **插图**：3D 抽象几何人物 / 模糊渐变球 → 删或换真实摄影
4. **布局**：所有卡片圆角 16、阴影模糊 40 → 收紧到 8 和 16
5. **文案**："赋能、打造、闭环、生态" → 用产品名 + 动词
6. **图标**：每个功能都配图标 → 只给核心 3 个功能配
7. **Hero**：超大背景图 + 居中标题 → 信息密度优先
8. **动效**：所有 hover 都用 300ms ease → 只在主操作加
9. **细节**：假用户头像（ThisPersonDoesNotExist）→ 改字母占位
10. **结构**：4 列 feature grid → 改成 1 列 + 1 个深挖

**通用原则**：AI 给你的是 80 分的"平均值"，你只要找出"哪个具体 100 分的产品和你一样"然后朝着它改。

## 8. 设计奖项评审机制：作为评审标准的镜子

| 奖项 | 维度 | 评审机制 | 学到什么 |
|---|---|---|---|
| **Awwwards SOTD** | Design / Usability / Creativity / Content / Dev | 国际 jury + 社区投票；提名制 | 评审有"创意"分，常规合规稿拿不到 |
| **Brand New** | Concept / Execution / Distinctiveness | 编辑单审，不接受公关 | 编辑视角——**有立场**比"四平八稳"重要 |
| **iF Design Award** | Idea / Form / Function / Differentiation / Impact | 49 位国际 jury 两轮盲审 | 强制要 Impact 段——所有评审都要问"so what" |
| **Red Dot** | Function / Aesthetics / Usability / Responsibility | 48 位 jury，分 23 国 | "Responsibility" 维度——可持续/伦理已是一票否决项 |

**借鉴**：把 Awwwards 4 维 / iF 5 维 / Red Dot 4 维合并成内部评审 rubric，比"好不好看"严格 10 倍。

## 10 条"如果你在做评审，记住这些"

1. **会前发文档，会后 24h 发 recap**——这是反馈文化的全部
2. **"我不喜欢"是最贵的反馈**，因为它不可执行
3. **Action 永远先于 Persuade**——能改的先改，品味的事最后吵
4. 一场评审 > 60 分钟 = 没人有结构
5. **Round Robin 比自由发言快 3 倍**，且保护内向者
6. 工艺问题公开说（不伤自尊），能力问题私下说
7. 主持人要把"目标"念 3 次
8. 作者讲 5 分钟，不准解释每个像素
9. 评审记录要写到 issue/PR 里，不是在 Figma comment 里烂掉
10. **没闭环的评审 = 没发生**

## 5 条反面教材

1. **PPT 评审**：20 页 deck 念完 1 小时，没人看稿子
2. **老板先说**：他的意见变成政治正确，其他人都附和
3. **"我再想想"**：评审没决定的事就是没决定
4. **设计师当场辩护**：所有反馈都被挡回去，下次没人说真话
5. **评审后 3 周没动静**：下次评审变成"上次说的你都没改"发泄会

## 3 条"如果你只能记一条"

1. **"我注意到 X，这可能导致 Y，因为 Z"**——这一句比"我觉得"高 5 个段位
2. **会前会后两个文档决定 80% 的反馈文化**，会中只是表演
3. **三级评审分开**：在 critique 里讲 stakeholder 的话 = 在 stakeholder review 里讲 craft 的话 = 双方都失败

## 资源 URL
- nngroup.com/articles/design-critique/ / closing-the-loop/ / what-to-do-after-design-critique/
- nngroup.com/articles/feedback-ux/ / ux-feedback-template/ / actionable-ux-feedback/ / design-critique-questions/
- nngroup.com/articles/3-step-ux-feedback/ / effective-user-research-feedback/ / video-critique-101/ / critique-mistakes/
- nngroup.com/articles/running-perfect-design-critique/ / design-reviews/ / stakeholder-reviews/ / ship-review/
- nngroup.com/articles/peer-review-design/ / feedback-as-defensive/ / feedback-without-defensiveness/ / feedback-culture/ / feedback-tools/
- smashingmagazine.com/2018/07/design-critique/ / 2018/08/critique-questions/ / 2020/11/design-review-async/ / 2021/09/design-review-remote/
- uxpin.com/studio/blog/design-critique/
- figma.com/blog/category/design-process/ / blog/feedback-files/ / blog/design-review-best-practices/
- linear.app/blog / airbnb.design/ / underconsideration.com/brandnew/ / awwwards.com/
- en.wikipedia.org/wiki/Design_criticism / Design_review
