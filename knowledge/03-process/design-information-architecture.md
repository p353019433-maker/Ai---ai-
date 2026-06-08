---
name: design-information-architecture
description: 信息架构深度 - Rosenfeld & Morville 4 系统 / 5 种组织模型 / Card Sort / Tree Test / 顶级产品 IA 案例
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 信息架构（Information Architecture, IA）深度

## 一句话总结
**信息架构（IA）不是画界面，而是设计"用户能否找到、能否理解"的结构方式**——导航迷路、搜索失灵、内容混乱，**80% 是 IA 问题而非 UI 问题**。

## 一、IA 基础：Rosenfeld & Morville 四大系统

**Richard Saul Wurman 1976 TED 演讲**首次提出 IA 一词，但真正奠定学科基础的是 Peter Morville 与 Louis Rosenfeld 合著的《Information Architecture for the World Wide Web》（1998 首版），被奉为"信息架构的圣经"。

**四大互锁系统**：
- **组织系统（Organization Systems）**——决定内容如何分组与排序（字母/时序/主题/用户任务/热度）
- **标签系统（Labeling Systems）**——决定给每个节点起什么名字（分类名/链接文案/按钮文本）
- **导航系统（Navigation Systems）**——决定用户怎么在结构里移动（全局/面包屑/相关推荐/站点地图）
- **搜索系统（Search Systems）**——决定用户怎么用关键词跳到目标（索引/查询语法/排序/补全）

**Dan Brown 8 原则**：Objects / Choices / Disclosure / Exemplars / Front Doors / Multiple Classification / Focused Navigation / Growth

**NN/g 强调**："IA 是站点的信息骨架，导航只是浮出水面的冰山尖"——若先画导航再补 IA，是"低效甚至危险"的倒序工程。

## 二、5 种组织结构模型

- **层级（Hierarchical / Tree）**——最经典。首页 → 一级 → 二级 → 内容页。优点清晰可预测；缺点是"每个内容只能属于一个父类"，逼用户走预设路径
- **分面（Faceted Classification）**——源于 1933 图书馆员 S.R. Ranganathan 的"分面分类法"，1990s UC Berkeley Flamenco 项目（Marti Hearst）带入数字产品。**同一商品可同时按品牌、价格、颜色、评分多维过滤**；2014 统计全美 50 大电商中约 40% 已采用分面搜索
- **Hub-and-Spoke（轮辐式）**——以"主页"或"仪表盘"为枢纽，所有功能以辐射状从枢纽发出。**SaaS 产品（Linear / Notion / Slack）几乎全用此模型**——避免深路径，鼓励"回到中心再出发"
- **数据库模型**——不预设结构，由用户动态查询与组合。Notion Database / Airtable 属此类，灵活性最高但学习成本也最高
- **超文本**——节点之间自由互链。Wikipedia 早期是典型，缺点是用户易迷失（"lost in hyperspace"）

**经验法则**：B2C 内容站用**层级 + 分面**；SaaS 工具用**轮辐 + 数据库**；知识库用**超文本 + 搜索**。

## 三、标签系统：Controlled Vocabulary vs Folksonomy

- **受控词表（Controlled Vocabulary）**——设计者预定义"首选术语"，通过 bijection 消除同义词、近义词、多义词歧义。类型：主题词表/叙词表/分类法/本体。优势稳定可预测；劣势脱离用户语言
- **大众分类法（Folksonomy）**——用户自由打 tag。Delicious（2003）开创社交书签，Flickr（2004-2005）推向大众。优点反映用户真实语言；缺点拼写不一致、缺乏同义词处理
- **实战**：高频高价值用受控词表（导航/菜单/按钮）；长尾/UGC 用 folksonomy + 审核；用**同义词环**（synonym ring）把"账号/账户/Account"在搜索层归一

## 四、导航模式

**NN/g**："IA 与导航是骨架与皮肤的关系——导航可见，IA 不可见"

- **全局导航（Global）**——跨页面恒定，承载顶层 IA。Apple.com 横向顶栏 12 个一级入口是教科书
- **局部导航（Local）**——每个章节内的小型目录，如 Stripe Docs 左侧栏按 Payments/Revenue/Money management 分组
- **上下文导航（Contextual）**——嵌入正文中的"相关链接""下一步"
- **分面导航（Faceted）**——把过滤选项作为导航使用
- **顺序导航（Sequential）**——强引导流（注册流程、Onboarding），用户只能向前或向后

**辅助元素**：面包屑必须用 `<nav aria-label="Breadcrumb">` 包裹（W3C APG 规范），当前页用 `aria-current="page"` 标记；站点地图（XML 给爬虫、HTML 给人）是 IA 的"鸟瞰图"。

## 五、搜索设计

搜索系统的核心是**信息检索（IR）**——从文档集合中找出与查询相关的资源，输出**排序**而非精确匹配。

- **全文索引**——倒排索引是基础设施；分词、词形还原（lemmatization）、停用词过滤影响召回
- **相关性排序**——TF-IDF、BM25 经典；现代叠加行为信号（点击/停留/转化）做 Learning to Rank
- **分面搜索**——搜索+过滤互补：用户可先搜再筛，或先筛再搜
- **自动补全**——拼写纠错、热门查询、个性化
- **零结果处理**——比"没找到"更危险的是"没找到且没建议"——必须给同义词、相关词、热门 fallback

**Amazon 把搜索框放在首屏正中、配合分面筛选**——把"找东西"做成核心体验。**搜索不是"找不到时的备胎"，它是 IA 失效的安全网**。

## 六、Card Sorting

让用户告诉你怎么分类。把内容写成卡片，让用户分组并命名，揭示**心智模型**：

- **开放式（Open）**——用户自创类目名。生成性强，适合早期探索
- **闭合式（Closed）**——类目已定，让用户把卡片归入。评估性强，适合验证现有 IA
- **混合式（Hybrid）**——固定类目 + 允许新增
- **Modified-Delphi**——第一个用户全开，后续在前者基础上迭代

**工具**：OptimalSort、UXtweak、UserZoom 提供远程卡片拖拽 + 聚类分析（dendrogram、相似度矩阵）。**NN/g 建议每类用户 15-30 人即可拿到饱和度**。

## 七、Tree Testing

"反向 Card Sorting"——剥离视觉设计，**只测文本树结构**。给用户一棵树和一个任务，看用户点哪条路径。指标：

- **成功率（Success Rate）**——是否找到正确答案（< 60% 即需重构）
- **直达率（Directness）**——没走回头路的比例
- **首屏点击分布**——第一击点在哪是预测成功的最强信号（NN/g 数据：首击正确 > 87% 任务成功）
- **时间与错误路径**——揭示"看起来像但其实不对"的标签

**工具**：Treejack（OptimalWorkshop 旗下）、Chalkmark（早期）、UXtweak。**Louis Rosenfeld 反复强调："Stop Redesigning, Start Tuning"**——在重新设计前先做一次 Treejack 基线测试，能省下百万级重做成本。

## 八、真实案例：顶级产品的 IA 决策

- **Amazon**——全球最大分面搜索场。左栏分面（品牌/价格带/评分/Prime）+ 顶部类目层级 + 搜索框 + 强排序。**IA 决策是"任何路径都能到货"**
- **Apple.com**——极简层级 + 巨型 Mega Menu。顶栏 12 个一级入口，每个下钻 2-3 层。**类目名全部是用户语言**（iPhone、Mac）而非内部 SKU
- **Stripe Docs**——以"任务"（Accept payments、Send invoices）作顶层入口，再以"产品"作二级。URL 扁平（`/payments`、`/billing`），符合"目标优先"原则
- **Linear**——纯 Hub-and-Spoke。左侧栏 Inbox/My Issues/Views/Projects 是 4 个枢纽，所有视图都是"过滤器 + 排序"的 Saved Query；**Command-K 调出命令面板直达任何实体**
- **Notion**——Workspace = 树；Database = 灵活视图（Table/Board/Calendar/Timeline），同一数据 5 种呈现。**Page 内是块（block）自由排版——把 IA 控制权下放给用户**
- **GOV.UK**——政府服务 IA 范本。**顶层"按生活事件"**（Having a baby / Driving）而非按政府部门；搜索与导航同权，符合"任务中心" IA

## 做 IA 的 8 步骤

1. **盘点内容与目标**——用 Excel/Notion 数据库列全实体、属性、关系，画实体关系图
2. **做开放 Card Sorting（15+ 用户）**——发现用户自然心智模型与类目命名
3. **用聚类分析生成候选 IA**——从 dendrogram 提炼 2-3 套候选树
4. **跑 Tree Testing 验证**——每套树 50+ 任务，看成功率与首击分布
5. **设计标签系统**——高频入口用受控词表，UGC 配 folksonomy + 同义词环
6. **选择组织模型**——B2C 走层级 + 分面，SaaS 走轮辐 + 数据库，文档走超文本 + 搜索
7. **画站点地图**——人手一图，全员对齐结构
8. **上线后用搜索日志 + 行为数据持续调优**——IA 是产品，不是文档

## 8 条 IA 反模式

1. **"先画线框再补 IA"**——等于把房子建好再改地基
2. **用内部术语命名类目**（如"SKU 管理"而不是"商品"）——用户不会用员工黑话搜索
3. **每个内容只允许一个父类**——违背用户多重心智路径
4. **分面数量失控**——一屏 30 个过滤项等于无 IA
5. **零结果搜索只显示"未找到"**——浪费了挽回机会
6. **面包屑用箭头 / 斜杠但不真实反映层级**——可访问性灾难
7. **无站点地图**——用户和搜索引擎都失去鸟瞰能力
8. **不测就上**——跳过 Card Sort + Tree Test 等于在 IA 上赌博

## 8 条真实网站 IA 教训

1. **Amazon**——分面搜索 + 强排序 = 任何路径都能到货；反面是首页信息密度过高，新用户迷失
2. **Apple.com**——12 个一级入口 + Mega Menu；反面是娱乐与服务混排，Vision Pro 等新品位阶不清
3. **Stripe Docs**——任务优先于产品；URL 扁平利于 SEO；用户找"如何开订阅"比"订阅 API 文档"更顺
4. **Linear**——命令面板 + Saved Query 让你无需记住 IA；反面是新手不知有何视图，需 Onboarding
5. **Notion**——把 IA 控制权下放给用户 = 终极灵活；反面是团队 IA 失控变成"垃圾抽屉"
6. **GOV.UK**——按"生活事件"组织而非按部门；牺牲部门 KPI 视角，换来用户极简路径
7. **Wikipedia**——超文本自由互链；反面是"lost in hyperspace"——面包屑与目录页是必要的稳定锚点
8. **企业内部 CMS（SharePoint 旧版）**——类目由 IT 拍板，与业务部门心智脱节，最终全员改用"全局搜索"绕过 IA——这是 IA 失败的典型结局

## 5 条"如果你只能记一条"

1. **IA 在原型之前、在界面之前、在像素之前**——它是结构，不是皮肤。Rosenfeld 反复说"Stop redesigning, start tuning"，因为重画界面不解决结构问题
2. **找不到内容不是搜索的锅，是 IA 的锅**——80% 的"搜索不准"源自标签错乱、类目错位、入口缺失；修搜索只是给破屋子装报警器
3. **用 Card Sort 听用户说，用 Tree Test 看用户做**——开放分类揭示心智，封闭测试揭示可达，两者缺一不可
4. **顶级产品 = 让用户两条腿走路**——Amazon、Stripe、Linear 都同时提供"层级浏览"与"搜索跳转"双通道；剥夺任何一条，都会丢失 30%+ 用户
5. **IA 永远在演化**——产品长出新功能、新用户、新场景，IA 就要重测、重构、重新文档化；它不是一次性 deliverable，而是产品生命周期里的持续工程

## 资源 URL
- uxbooth.com/articles/information-architecture-101/ / en.wikipedia.org/wiki/Information_architecture
- en.wikipedia.org/wiki/Card_sorting / Tree_testing / Faceted_search / Information_retrieval
- en.wikipedia.org/wiki/Controlled_vocabulary / Folksonomy
- nngroup.com/articles/information-architecture/ / ia-vs-navigation/ / card-sorting/ / tree-testing/
- interaction-design.org/literature/topics/information-architecture
- figma.com/blog/information-architecture/ / smashingmagazine.com/category/information-architecture/
- optimalworkshop.com/ / usability.gov/ / gov.uk/service-manual/design
- apple.com / stripe.com/docs / linear.app / notion.so (IA 案例)
