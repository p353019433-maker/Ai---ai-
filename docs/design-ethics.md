---
name: design-ethics
description: 设计伦理与暗黑模式 - 13 类 dark patterns / 真实罚款数字 / GDPR 第 7/25 条 / 4 大伦理框架 / AI 训练数据
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计伦理与暗黑模式

## 一句话总结
**道德设计不是增长的敌人，而是品牌的护城河**——把"用户自主"放进产品核心 KPI，短期会损失一点转化，长期会赢得信任、规避监管罚款、并把"做有良心的产品"变成最难被复制的竞争壁垒。

## 一、起源与定义

**"Dark pattern"** 一词由英国用户体验设计师 **Harry Brignull** 于 **2010.7.28** 注册 darkpatterns.org 域名时正式提出，原意是"命名并羞辱那些故意欺骗用户做本不想做的事情的界面"。2023 年他出版《Deceptive Patterns》一书。

该网站目前由 Brignull 与法学学者 Mark Leiser、Cristiana Santos 共同运营，演变为兼具案例库与法律倡导功能的资源中心。Brignull 后期推动术语从"dark patterns"改为"deceptive design"（直接定性为"欺骗"），与英国 CMA 合作将其纳入消费者保护语言。

**3 层语义**：
- **故意性**——界面经过 A/B 测试优化的"刻意"选择
- **不对称利益**——设计师/PM/增长团队得益，用户损失金钱/时间/隐私/尊严
- **可识别性**——一旦命名，它就不能再以"行业惯例"为借口

**监管现实**：欧盟 GDPR / Digital Services Act / Data Act，美国 FTC 多次开出数亿美元罚单。**一个被命名为"dark pattern"的产品，今天承担的不只是舆论风险，而是真金白银的合规负债**。

## 二、13 类暗色模式详解

deceptive.design 当前正式分类 13 类：

1. **Confirmshaming（确认羞辱）**——"不，谢谢，我不想变得更美"。用道德绑架让用户不敢点拒绝按钮
2. **Hidden Costs / Drip Pricing**——先报低价，最后一步冒出服务费/税/手续费
3. **Comparison Prevention**——故意把价格/规格打散，让竞品对比几乎不可能
4. **Disguised Ads**——把 Sponsored 内容设计成原生卡片或"编辑推荐"
5. **Forced Action**——要解锁功能必须先做某事（关注、分享、邀请好友）
6. **Hard to Cancel / Roach Motel**——注册一秒，退订三十天；HP 墨盒取消订阅后即停印
7. **Hidden Subscription**——Noom 因"难以察觉的自动续费"被罚 6200 万美元
8. **Nagging**——关闭后还反复弹窗请求开启通知
9. **Obstruction**——Meta 在欧盟被 NOYB 在 11 国投诉：让用户走 10 步才能拒绝追踪
10. **Preselection**——默认勾选"加入营销邮件"是 GDPR 第 7 条明确违规
11. **Sneaking / Basket Sneaking**——结算时静默加入额外保险、捐赠、订阅
12. **Trick Wording**——拒绝按钮用"我记得您曾拒绝"，制造心理负担
13. **Visual Interference**——把"接受所有"做成高亮，"管理偏好"做成灰色小字

**2019 年学术研究**横扫 11,000 个购物网站，发现 **1,818 个暗色模式实例**，分布 15 个类别。挪威消费者委员会 2018 年《Deceived by Design》直接点名 Facebook / Google / Microsoft。

## 三、真实罚款数字（具象化"伦理"）

| 公司 | 罚款 | 原因 |
|---|---|---|
| **Epic Games / Fortnite** | **2.45 亿美元** | 暗黑模式 |
| **TikTok** | **3.45 亿欧元**（爱尔兰 DPC） | 儿童数据违规 |
| **Meta** | **12 亿欧元** | 违规向美国传输数据 |
| **Noom** | 6200 万美元 | 隐藏订阅自动续费 |
| **YouTube** | 1.7 亿美元 | 未经同意收集儿童数据 |
| **TurboTax / Intuit** | 1.41 亿美元 | 欺骗性 UI |
| **TikTok 早期** | 5700 万美元 | 儿童数据违规 |

## 四、GDPR / CCPA 隐私设计

**GDPR（2018）三篇文章构成隐私设计铁三角**：

**第 5 条** ——7 项原则：lawfulness / fairness / transparency、purpose limitation、data minimisation、accuracy、storage limitation、integrity & confidentiality、accountability

**第 7 条** ——同意必须"具体、自由、清晰、可撤回"——**任何默认勾选的退出式同意都是违法**，多重处理目的不能捆绑

**第 25 条** ——把 Ann Cavoukian 1995 年提出的 **Privacy by Design** 写入法律，强制"默认高隐私设置"（Privacy by Default）

**违法代价**：2000 万欧元或全球年营业额 **4%**——2024 TikTok 3.45 亿、2025 Meta 12 亿就是这条法律的具体落地。

**CCPA（2020）**——"opt-out"路线，赋予消费者 5 权利：知情 / 拒绝出售（首页必须挂"Do Not Sell My Personal Information"链接+800 电话）/ 访问 / 删除 / 不被歧视。**2023 加州进一步立法禁止损害退出选项的欺骗性 UI**，把 dark pattern 写进反不公平竞争法。CCPA 故意违规罚 **7,500 美元/次**。

**Cookie Banner 黄金标准**（EDPB 2020 同意指南后）：
- "全部拒绝"和"全部接受"按钮**等比等色**
- 默认无 cookie
- 同意粒度可按目的拆解（分析/营销/个性化）
- 一键撤回，且撤回按钮不深埋

## 五、AI 训练数据伦理

生成式 AI 让训练数据从"分析素材"变成"生产原料"，引爆 4 类新问题：

**版权**：2023《纽约时报》诉 OpenAI / Getty Images 诉 Stability AI / 艺术家集体诉 Midjourney 三起里程碑。原告主张：模型"记忆并能复述"训练集中的受版权保护内容，已超出合理使用。**欧盟 AI Act 2024** 把"用于训练的基础模型"列为**系统性风险**，要求披露训练数据来源摘要、遵守版权法（包括 opt-out 爬虫协议如 robots.txt 与 TDM 保留权利元数据）。

**真人肖像**：声音克隆让任何人 30 秒样本即可生成足以诈骗家属的"真人语音"。Anthropic/Google/Meta 都在政策中禁止未经同意复刻公众人物，但执行依赖水印与事后追责。

**透明度义务**：欧盟 AI Act 要求生成式 AI 输出"以机器可读方式"标注 AI 生成；中国《生成式人工智能服务管理暂行办法》（2023）也要求"显式标识"。**设计师必须为内容加 provenance / watermark 标识**。

**同意与商业使用**：负责任的做法是 (a) 提供 robots.txt 级别的 TDM 保留；(b) 建立 dataset card / model card；(c) 商业落地前做数据来源审计（DPIA / DPIA for AI）；(d) 提供创作者收入分成或退出渠道（Adobe Firefly 的"仅用授权数据集训练"+ Shutterstock 训练基金是范本）。

## 六、欺骗性 AI 设计

AI 让欺骗规模化、低成本化、个性化，催生 4 种新型 dark pattern：

1. **Chatbot 假装是人**——FTC 2023 明确警告：若 AI 客服/治疗师/陪伴机器人故意冒充真人，违反 Section 5。Air Canada 2024 因聊天机器人给出错误退款承诺被加拿大民事法庭判败诉
2. **假评论与口碑操纵**——Amazon 持续清理机器生成的"五星好评"；FTC 2024.10 新规禁止 AI 生成的虚假评论
3. **操纵性推荐**——TikTok/Instagram Reels "For You"算法已被多起诉讼指控"故意引导青少年接触赌博/减肥/自残内容"。欧盟 DSA 要求大型平台披露推荐系统的"主要参数"并提供"非个性化"开关。**当推荐系统优化的是停留时长而非用户福祉，它就是一台高效的暗黑模式生成器**
4. **Deepfake**——欧盟 AI Act 把 deepfake 列为**高风险用途**——必须清晰披露

针对这些，Anthropic 的 **Constitutional AI** 提供了一种解法：用显式原则列表（"无害、可信、不助长欺骗"）作为模型自我批评与修订的标准，比单纯 RLHF 更可审计、可解释。

## 七、儿童设计伦理

**美国 COPPA（1998，2013 修订）** 适用 13 岁以下，要求"可验证的家长同意"（VPC）作为收集任何个人信息的前置条件。罚则每违规 **53,088 美元**。

**欧盟 GDPR 第 8 条**设定儿童同意年龄为 16 岁以下（成员国可下调至 13 岁）。**英国 ICO 2019《Age Appropriate Design Code》（"GDPR-K"）**——把儿童保护做成 15 条可执行标准，最具杀伤力的是**禁止"like"和"streak"机制**（认为它们构成心理成瘾设计）、禁止信息流广告、禁止数据画像默认开启。

**设计师具体行动**：
- 任何面向 16 岁以下用户的产品必须做 DPIA + 年龄筛查
- 不要做 streak / nudge / variable reward / endless scroll 这类从赌博行业借来的成瘾机制
- 家长控制面板要易发现、易配置、易撤销
- 文案使用儿童能读懂的语言（小学五年级水平），不要用法律话术

## 八、可持续设计 / 绿色 IT

**2024 全球数据中心耗电约 415 TWh，占全球电力消耗 1.5%**，预计 2030 翻倍。训练一次 GPT-3 级模型的碳排放约等于 5 辆汽车终身排放；一次 Google 搜索看似无害，但全人类每天 90 亿次累计惊人。

**Web Performance is Sustainability**：网页每多 1 秒加载，多 10% 跳出率、20% 耗电、多几克 CO₂——**慢本身就是不道德**。

**暗黑模式省电**是有条件的：OLED 屏幕显示纯黑像素可较 LCD **节省 60% 功耗**（即仅消耗 40% 电量），但 LCD 几乎无差别。绿色 IT 的 4R 框架：**Reduce / Reuse / Recycle / Recover**。

**设计师可以做的小事**：
- 默认使用系统字体而非 web font
- 图片用 AVIF/WebP、自动按视口缩放
- 视频默认静音预览，点击才加载高清
- 暗色模式让用户主动选，不要硬切
- 设计"轻量版"页面给低网速地区
- 在产品页**披露碳足迹**（Stripe、Apple 都做了）

## 九、4 大道德设计框架

**Microsoft Responsible AI（2019）6 原则**：Fairness（公平）/ Reliability & Safety / Privacy & Security / Transparency / Accountability / Inclusiveness。落地工具：RAI Dashboard、Office of Responsible AI、Customer Copyright Commitment。

**Google People + AI Guidebook（PAIR）**：23 个问题（如"AI 失败时会发生什么""AI 何时该主动、何时该等待""如何向用户解释不确定性"）。

**Anthropic Constitutional AI**：用"宪法"（原则列表，如"不帮助造成伤害""尊重隐私""不撒谎"）替代部分 RLHF，让模型自我批评与修订。

**IEEE Ethically Aligned Design（2016 启动，2019 第一版）8 原则**：Human Rights、Well-being、Data Agency、Effectiveness、Transparency、Accountability、Awareness of Misuse、Competence。配套标准如 IEEE 7001-2021。

**交集**：4 个框架都强调三件事——(a) **可解释性**（用户能看懂系统在做什么）；(b) **可撤回性**（用户能随时退出）；(c) **可问责**（出错时能定位责任主体）。

## 8 条识别暗色模式的可复用清单

1. **退出是否比进入更难？**——若注册 1 步、退订 10 步，就是 Roach Motel
2. **默认值是否对你有利？**——预选加入营销邮件、预选加购保险，都是 Preselection
3. **拒绝按钮的"语言压力"？**——"不，谢谢，我不想变聪明"是 Confirmshaming
4. **价格在最后一步突变？**——Drip Pricing 的标志
5. **关键信息被视觉弱化？**——灰色小字、低对比，是 Visual Interference
6. **是否被强制做某事才能解锁？**——关注、分享、邀请好友才能用，是 Forced Action
7. **倒计时/库存/在线人数？**——若无真实后端支持，就是伪 Urgency
8. **第三方内容是否被伪造成原生？**——Sponsored 不标注，是 Disguised Ads

## 8 条 Privacy by Design 具体实践

1. **数据最小化**——只问业务必需字段
2. **目的限定**——明确告知并锁定用途
3. **默认高隐私**——所有共享/追踪默认关闭
4. **同意粒度细**——按目的拆分 toggle
5. **可撤回且容易找**——撤回入口与同意入口同等可见
6. **数据生命周期管理**——设定保留期限，到期自动删除
7. **DPIA（数据保护影响评估）**——任何涉及大规模/敏感数据/AI 的新功能上线前必须做
8. **用户导出/删除权**——自助面板一键下载、一键删除

## 8 条 AI 时代的伦理设计原则

1. **AI 生成内容必须可识别**——显式水印 + 元数据水印双保险
2. **不确定性必须被表达**——概率、置信度、模型版本
3. **AI 失败时优雅降级**——设计 fallback 到人工/规则/空状态
4. **个性化 ≠ 操纵**——推荐系统加"非个性化"开关与"用户福祉指标"
5. **训练数据要可审计**——发布 dataset card / model card
6. **创作者退出机制**——尊重版权 opt-out，必要时提供分成
7. **儿童数据零容忍**——16 岁以下默认无画像、无追踪、无成瘾机制
8. **建立内部 AI 伦理委员会**——产品上线前过 RAI 审查

## 5 条"如果你只能记一条"

1. **Deceptive Design 短期能换 2-5% 转化，长期会让品牌贴上"骗子"标签；一次 FTC 罚单就是数亿美元，且不可撤销**。道德设计不是软指标，是财务风险对冲
2. **GDPR 第 7 条 + 第 25 条是设计师必读的两条法律**——前者规定"默认勾选就是违法"，后者要求"默认高隐私"
3. **AI 产品的护城河是"可解释"**——用户能在 5 秒内判断系统在做什么、为什么这么做、出错找谁
4. **性能即道德**——省 1 秒加载时间 = 省碳 = 省用户时间 = 省电
5. **儿童的"like"和"streak"机制是 2024 年后监管重点**——英国 ICO 已明确禁止

## 资源 URL
- deceptive.design/ / darkpatterns.org/ / wikipedia.org/wiki/Dark_pattern / Deceptive_design / Harry_Brignull
- gdpr.eu/ / en.wikipedia.org/wiki/General_Data_Protection_Regulation / Privacy_by_design
- en.wikipedia.org/wiki/California_Consumer_Privacy_Act / Children's_Online_Privacy_Protection_Act
- en.wikipedia.org/wiki/Responsible_AI / Ethically_aligned_design / Sustainable_design / Green_computing
- pair.withgoogle.com/ / microsoft.com/en-us/ai/responsible-ai / anthropic.com/constitutional-ai
- eff.org/ / smashingmagazine.com/2019/05/dark-patterns/ / nngroup.com/articles/deceptive-patterns/
