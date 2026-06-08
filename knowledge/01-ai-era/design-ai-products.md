---
name: design-ai-products
description: AI 时代的产品设计 - LLM UI/生成式 UX/Agent UX/Prompt-as-UX/不确定性/伦理 - 来自 Anthropic/Cursor/v0/Lovable 等真实产品分析
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# AI 产品设计（AI 时代的产品设计）

## 一句话总结
AI 产品的 UX 本质是设计"人机协作的协议"——把 LLM 不可预测的能力包进可解释、可纠正、可分支的界面中，让用户在每一次生成中既保有控制感又能放手让模型去做。

## 一、LLM 对话 UI 五大模式
1. **Streaming**：token-by-token 输出 + Stop 按钮随时打断
2. **Regenerate**：放每条回答下方，提供廉价试错
3. **Edit**：直接在消息上改 prompt（比重新输入省认知）
4. **Branch**：对话树 = 可恢复检查点（Claude Code Esc+Esc、ChatGPT "从这条消息展开"）
5. **Feedback**：thumbs 是事后标注，Anthropic 把它升级为 RLHF 数据源

**关键发现**（NN/g）：用户面对"低可预测性"系统会自我收敛到简单任务——**86% 智能助手任务是单步操作**。所以对话 UI 必须主动暴露"我能做什么"的脚手架。

## 二、生成式 UI 三大代表
1. **Claude Artifacts**：对话旁开辟画布，代码/文档/SVG 变可迭代产物（对话 + 产物分屏）
2. **v0**：Prompt → Build → Publish 三段式，Design Mode 让用户"在生成物上直接改"
3. **Claude Design**（Anthropic Labs 2026）：品牌资产 + 设计系统 + 产出物打包为 bundle，调色板滑杆代替纯 prompt

**设计要点**：生成式 UI 给生成物**可寻址、可版本化、可被工具调用**的形态。

## 三、Agent 产品 UX
**最大风险**："它在我不知道的时候做了什么"。

四个值得拆解：
- **Replit Agent 4**：并行 fork + 无限画布可视化进度
- **GitHub Copilot**：多 surface（IDE / github.com / CLI / Chat App）接管
- **Claude Code**：Plan Mode 四阶段（探索/计划/实施/提交）+ Stop hook + subagent 评审
- **Cursor Composer 2.5**：Mission Control 网格 + Autonomy Slider 显式表达"走多远"

**Anthropic 三铁律**（[Building Effective Agents](https://anthropic.com/engineering/building-effective-agents)）：保持简单、显式透明、poka-yoke 工具（让工具参数本身防错）。

## 四、Prompt-as-UX
**最大痛点不是"说什么"，是"我能说什么"**——articulation barrier。

具体做法：
- **结构化输入**：Notion AI 选"翻译/总结/改写"+ 补内容
- **Prompt Suggestions**：Claude.ai 启动给 3 个具体场景示范
- **Prompt Controls**：Cursor `@file` 引用、Figma Make 点选 + 描述、Claude Code `/init` 引导式生成 CLAUDE.md

## 五、AI 反馈设计
**反直觉**：thumbs up/down 是最弱反馈——它滞后且颗粒度粗。

**有效层级**（从细到粗）：
1. **行内接受/拒绝**：Cursor `Tab`/`Esc`（生成瞬间）
2. **区块级 regenerate**：Claude.ai 选中段落重写
3. **结构化理由反馈**：Bolt.new 用自动化测试代替用户评分
4. **状态反转**：Claude Code `/rewind` 回到任意 checkpoint

**时机洞察**：反馈越接近生成瞬间越有效。**把反馈分布到整个交互链，不堆在结尾。**

## 六、不确定性 UI
LLM 会自信地胡说，UI 必须直接处理（[Anthropic Opus 4.8](https://anthropic.com/news/claude-opus-4-8) 强调"模型更可能标记不确定性"）：
- **置信度可见**：Perplexity 引用句末标来源
- **草稿/假设标签**：OpenAI Deep Research 单独展示过程文件
- **Effort Control**：Opus 4.8 切"快而浅"/"慢而深"
- **Plan Mode**：先出方案再执行，不确定性在执行前拦截

## 七、伦理与可解释性
- **Google PAIR Guidebook**：心模型/可解释性/信任/反馈/错误恢复五大章节
- **Foundation Models 风险**（[arxiv 2108.07258](https://arxiv.org/abs/2108.07258)）：基础模型缺陷会通过同质化被所有下游产品继承
- **Anthropic usersafety@anthropic.com**：把伦理设计成**用户可触发的功能**，不是公司内部流程

## 八、Anthropic 自己的设计哲学
**"AI 能力越大，UI 诚实义务越大"**——不藏 prompt、不藏工具调用、不藏失败概率。
- Claude Code 反复主题："Context window 是稀缺资源"
- Agent SDK 暴露 hooks/subagents/permissions/sessions 四个底座——不抽象掉"AI 在做什么"

## 可复用原则
1. 长任务 → "分阶段" UI（探索→计划→实施→验证）
2. 生成式输出 → "对话 + 产物"分屏
3. Agent → "自主 + 监督"双轨（自动验证 + Stop hook + 人工 approval）
4. Prompt → hybrid UI（按钮/模板/引用语法替代自由文本）
5. 不确定性 → "显式思考可见性"（工具调用、来源、置信度）
6. 反馈 → 分散到每一刻（行内/区块/checkpoint）
7. 伦理 → "人类接管路径"做成产品功能
8. 协作 → agent 工作日志当 UI 一等公民

## 反面教材（不要做）
1. 在每个按钮上加 sparkles（NN/g 警告"AI 视觉符号通胀"）
2. "Powered by AI" 当价值主张
3. 默认开启全自主 agent 模式
4. 把 prompt 框当唯一输入方式
5. 隐藏工具调用和思考过程
6. 用聊天框承担所有功能（Artifacts/Canvas/Code View 才是产物舞台）
7. thumbs up/down 当唯一反馈通道
8. 省略"人类可以随时停"按钮

## AI 时代 vs 传统设计的 5 差异
1. **可逆性 > 一致性**：checkpoint/rewind/branch 取代 undo
2. **能力边界本身就是产品**：onboarding 任务 = 展示"在我这能做什么"
3. **反馈是训练数据**，不只是产品功能
4. **诚实 > 能力**：Opus 4.8 把"更可能说不"当发布亮点
5. **"思考可见性"是新型 affordance**：传统靠形状颜色，AI 时代靠"它在想什么/查什么/为什么这么答"

## 资源 URL
- code.claude.com/docs/en/best-practices
- anthropic.com/engineering/building-effective-agents
- anthropic.com/news/claude-opus-4-8
- anthropic.com/news/claude-design-anthropic-labs
- pair.withgoogle.com/
- nngroup.com/articles/intelligent-assistants-poor-usability-high-adoption
- nngroup.com/articles/designing-ai-study-guide
- cursor.com, v0.dev, lovable.dev, bolt.new, replit.com/agent
