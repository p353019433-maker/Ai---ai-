---
name: design-decision-handbook
description: 设计决策总纲 v6 - 把 53 份设计 memory + 11 组主题串成决策树 + 8 元原则 + 12 步检查（2026-06 整理）
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计决策总纲 v6（2026 整理版）

## 一句话总结
当你面对一个设计问题不知道怎么办时，先看这份——它告诉你"该看哪份"以及"跨领域的元原则是什么"。

## 0. 综合索引与基础
- **[MEMORY.md](MEMORY.md)** — 完整 68 份文件索引（2026-06 刷新）
- [design-philosophy-master.md](design-philosophy-master.md) — 东方美学 + 西方现代主义融合
- [design-ultimate-handbook.md](design-ultimate-handbook.md) — 9 轮研究综合
- [github-design-aesthetics.md](github-design-aesthetics.md) — GitHub 设计项目漫游
- [method-autonomous-overnight-learning.md](method-autonomous-overnight-learning.md) — 一晚学习法
- ~~design-ai-de-slop.md~~ → 2026-06-06 清理时移除，内容并入 [design-ai-prompt.md](design-ai-prompt.md)

## 1. 53 份设计领域 memory 索引（按主题分 11 组）

### 1.1 元索引 & 总纲（3 份）
- [design-decision-handbook.md](design-decision-handbook.md) — 本文件
- [design-ultimate-handbook.md](design-ultimate-handbook.md) — 9 轮研究综合
- [design-philosophy-master.md](design-philosophy-master.md) — 哲学总纲

### 1.2 AI 时代设计方法论（5 份）
- [design-ai-prompt.md](design-ai-prompt.md) — 提示词工程 + 反 slop 清单（已吸收 de-slop 内容）
- [design-ai-workflow.md](design-ai-workflow.md) — 11 AI 工具地图 + 4 步 pipeline
- [design-ai-products.md](design-ai-products.md) — LLM UI / Agent UX / Prompt-as-UX
- [design-handoff.md](design-handoff.md) — Figma → 代码交付全流程
- [design-ab-testing.md](design-ab-testing.md) — 统计 / 样本量 / 6 工具 / Feature Flag

### 1.3 Cursor + Figma 端到端 & 真实代码库（2 份，2026-06 新增）
- [design-cursor-figma-loop.md](design-cursor-figma-loop.md) — Cursor + Figma MCP 端到端实操
- [design-real-codeteardown.md](design-real-codeteardown.md) — Linear/Stripe/Vercel/Apple/GitHub 设计系统代码级拆解

### 1.4 评审 & 工作流（2 份）
- [design-workflow-critique.md](design-workflow-critique.md) — 评审三级 + AI 工具何时用 + 职业路径
- [design-review-practice.md](design-review-practice.md) — 批评四层 + 8 句句式模板

### 1.5 设计系统（2 份）
- [design-system-build.md](design-system-build.md) — 6 步搭建 / 3 层 token / Storybook
- [design-systems-comparison.md](design-systems-comparison.md) — Primer/Carbon/Polaris/Atlassian/SLDS

### 1.6 视觉工艺（7 份）
- [design-typography-practice.md](design-typography-practice.md) — 字号比例 / 可变字体 / clamp
- [design-typography-craft.md](design-typography-craft.md) — 字体工艺史 + 字距 + 光学尺寸
- [design-color-contrast.md](design-color-contrast.md) — oklch / WCAG / 14 语义 token
- [design-layout-grid.md](design-layout-grid.md) — 8pt + 12 列 + container queries
- [design-component-patterns.md](design-component-patterns.md) — 12 组件 + 状态机
- [design-microcopy.md](design-microcopy.md) — 30 Before/After + 8 模板
- [design-motion-microinteractions.md](design-motion-microinteractions.md) — 缓动 + 4 阶段

### 1.7 平台 & 场景（8 份，含 3 新增）
- [design-app-platforms.md](design-app-platforms.md) — iOS HIG / Material You / visionOS / watchOS
- **[design-3d-spatial.md](design-3d-spatial.md)** — visionOS / Vision Pro / 空间交互（2026-06 新增）
- **[design-i18n-rtl.md](design-i18n-rtl.md)** — Unicode bidi / 8 反转点 / 逻辑属性 / 翻译工作流（2026-06 新增）
- **[design-verticals-b2b.md](design-verticals-b2b.md)** — 医疗 HIPAA / 金融 PCI-DSS / 工业 HMI / 车载 CarPlay 4 大行业（2026-06 新增）
- [design-web-aesthetics.md](design-web-aesthetics.md) — editorial / brutalist / scrollytelling
- [design-game-ux.md](design-game-ux.md) — Core Loop / 心流 / HUD 3 范式
- [design-service-design.md](design-service-design.md) — Journey Map / Blueprint / Double Diamond
- [design-information-architecture.md](design-information-architecture.md) — IA 4 系统 / Card Sort / Tree Test

### 1.8 工艺 & 工艺哲学（5 份）
- [design-data-visualization.md](design-data-visualization.md) — Tufte / Few / Cleveland-McGill
- [design-product-critique.md](design-product-critique.md) — 10 真实产品案例
- [design-studios-cases.md](design-studios-cases.md) — 7 设计公司工艺传统
- [design-history-movements.md](design-history-movements.md) — 7 设计运动
- [design-code-craft.md](design-code-craft.md) — Knuth / 命名 / 反 AI
- [design-criticism.md](design-criticism.md) — 批评四层 / NN/g / 8 句句式

### 1.9 商业 / 创业 / 教育 / 法律 / 中文设计（6 份，含 4 新增）
- [design-business.md](design-business.md) — Pentagram / Lippincott / MetaDesign
- [design-education-career.md](design-education-career.md) — 自学 18 月路径
- **[design-startup-studio.md](design-startup-studio.md)** — 6 起步模式 / Freelance→Micro→合伙→SaaS→课程→投资（2026-06 新增）
- **[design-font-legal.md](design-font-legal.md)** — SIL OFL / Monotype / 字体陷阱 / NDA 4 必写 / 合同 6 必写（2026-06 新增）
- **[design-education-teaching.md](design-education-teaching.md)** — 5 模式 / 4 教学原则 / 学习金字塔 / Refactoring UI 案例（2026-06 新增）
- **[design-chinese-circle.md](design-chinese-circle.md)** — 站酷 / UI 中国 / 思源黑体 / 中文排版特殊处理（2026-06 新增）

### 1.10 包容 / 伦理 / 用户研究（4 份）
- [design-accessibility.md](design-accessibility.md) — WCAG 2.2 9 新规则
- [design-inclusivity.md](design-inclusivity.md) — 7 原则 / Curb Cut / 神经多样性
- [design-ethics.md](design-ethics.md) — 13 dark patterns / GDPR / 4 伦理框架
- [design-user-research.md](design-user-research.md) — 5 用户原则 / 8 研究方法

### 1.11 设计哲学（14 份）
- [design-philosophy-japan-nordic.md](design-philosophy-japan-nordic.md) — wabi-sabi / shibui / Muji / Hygge
- [design-philosophy-modernism-sources.md](design-philosophy-modernism-sources.md) — Rams / Bauhaus / Swiss / Rand
- [design-philosophy-color-perception.md](design-philosophy-color-perception.md) — 色彩心理学 / Gestalt / UX 定律
- [design-philosophy-typography-history.md](design-philosophy-typography-history.md) — Garamond→Helvetica→Inter
- [design-philosophy-architecture.md](design-philosophy-architecture.md) — 安藤忠雄 / 柯布西耶 / Kahn
- [design-philosophy-brand-graphics.md](design-philosophy-brand-graphics.md) — Pentagram / Vignelli / Rand
- [design-philosophy-photography.md](design-philosophy-photography.md) — 决定性瞬间 / 等价
- [design-philosophy-dataviz.md](design-philosophy-dataviz.md) — Tufte / Few / McCandless
- [design-philosophy-experience-ux.md](design-philosophy-experience-ux.md) — Flow / SDT / 12 动画原则
- [design-philosophy-italian-modern.md](design-philosophy-italian-modern.md) — 米兰派
- [design-philosophy-movements-depth.md](design-philosophy-movements-depth.md) — 7 运动哲学内核
- [design-philosophy-iconic-brands.md](design-philosophy-iconic-brands.md) — Apple / 航空 / 手表
- [design-philosophy-reading-paths.md](design-philosophy-reading-paths.md) — F-pattern / Bezold / Müller-Lyer
- [design-philosophy-master.md](design-philosophy-master.md) — 东方+西方总纲

**合计**：3+5+2+2+2+7+8+5+4+4+14 = **56 份设计相关** + 1 归档 + 2 辅助 = 59 份（不含 code-philosophy-* 11 份）

---

## 2. 决策树（设计问题来了看哪份）

```
我在做什么？
│
├─ 写代码 / 软件
│  ├─ 想让代码有"人手温度" → design-code-craft.md
│  └─ 想提升代码审美 → design-code-craft.md
│
├─ 选字体 / 排版
│  └─ 字体工艺 / 可变字体 / 字距 / 版权 → design-typography-craft.md
│
├─ 评估设计史
│  └─ 想引用某个设计传统 / 运动 → design-history-movements.md
│
├─ 评估真实产品案例
│  └─ 想参考成功案例 / 避开失败教训 → design-product-critique.md
│
├─ 搭建设计系统
│  └─ token / 组件 / 决策哲学 / 5 大系统 → design-systems-comparison.md
│
├─ 团队协作 / 评审 / 职业
│  ├─ critique / 评审三级 / AI 工具 / 路径 → design-workflow-critique.md
│  ├─ 教设计 / 学设计 / 招人 → design-education-career.md
│  └─ 写 critique / 公开批评 / 评奖 → design-criticism.md
│
├─ 商业 / 卖设计
│  └─ 咨询 / token / 课程 / 个人品牌 / 定价 → design-business.md
│
├─ 包容性 / 无障碍
│  └─ WCAG / 通用设计 / Curb Cut / AI 时代新可能 → design-inclusivity.md
│
├─ 评估设计公司
│  └─ Frog / IDEO / Pentagram / Manual / Sagmeister → design-studios-cases.md
│
├─ 设计服务 / 编排体验
│  └─ Journey Map / Service Blueprint / Double Diamond → design-service-design.md
│
├─ 设计游戏 / 沉浸式
│  └─ 心流 / HUD / 死亡循环 / F2P 暗黑 → design-game-ux.md
│
├─ 设计伦理 / 暗黑模式
│  └─ dark patterns / GDPR / AI 训练 / 道德框架 → design-ethics.md
│
├─ 搭信息架构 / 导航 / 搜索
│  └─ IA 4 系统 / Card Sort / Tree Test → design-information-architecture.md
│
├─ 做数据可视化 / dashboard
│  └─ Tufte / Few / Cleveland-McGill / 工具栈 → design-data-visualization.md
│
├─ 设计 LLM / AI 产品
│  └─ AI 产品 UX / prompt-as-UX / 不确定性 / 伦理 → design-ai-products.md
│
├─ 设计 UI（按钮/表单/通知/状态/模态/导航/数据）
│  └─ 微决策规则 → design-ui-decisions.md
│
├─ 设计 App（iOS/Android/visionOS/watchOS）
│  └─ 平台约定、native vs custom、动效方言 → design-app-platforms.md
│
└─ 设计网页（landing/marketing/personal site）
   └─ editorial/brutalist/scrollytelling/现代 CSS/性能 → design-web-aesthetics.md
```

---

## 3. 跨主题的 8 大元原则

### 元原则 1：**少即是多，但少得有判断**
- 通用：Rams "Less but better" / 侘寂 "以空显有"
- UI：1 主按钮 + 大量留白
- 网页：editorial 大字号 + 单色背景 + 1 accent
- 平台：iOS Deference
- 代码：gofmt / SQL 7 libc
- 字体：手工 kerning 1000+ 工时
- 设计史：包豪斯 Universal 字母全小写
- 包容性：少装饰 = 易读 = 服务所有人
- 伦理：少欺骗 = 少罚款 = 服务所有人
- 数据可视化：data-ink ratio 最大化

### 元原则 2：**让系统的隐喻与方言活起来**
- UI：iOS spring vs Material Easing
- 平台：iOS push/pop vs Android up
- 网页：CSS 原生 scroll-driven 而非 GSAP
- AI：Claude Artifacts vs 纯 chat
- 代码：Lua clean C / SQLite 7 libc
- 字体：可变字体 5 轴
- 游戏：Diegetic UI 放在世界里
- 服务：IKEA 动线作为产品

### 元原则 3：**诚实 > 能力**
- AI：Opus 4.8 "更可能说不"
- 网页：brutalist 裸露 HTML
- 性能：80KB 主页
- 平台：native 控件承担平台无障碍
- 代码：PEP 20 "Errors should never pass silently"
- 设计史：Rams 第 6 条诚实
- 伦理：道德设计是品牌护城河
- 数据可视化：标题是结论不是描述
- 包容性：性能即道德

### 元原则 4：**让用户掌控和可逆**
- AI：Claude Code Plan Mode / Esc+Esc / rewind
- UI：永远可逆（NN/g #3）
- 平台：iOS push/pop、Material up
- 网页：breadcrumb 永远可点击
- 代码：Go 命名 + 错误显式
- 设计史：Victor "看见过程"
- 游戏：死亡不删档，可中断性第一
- 服务：Blueprint 标注 fail point
- 伦理：默认 opt-in、撤回按钮不深埋

### 元原则 5：**Opinionated > Configurable**
- 产品：Linear 30 秒 issue 创建击败 Jira 100 配置项
- 设计系统：Polaris 商家优先
- AI 时代：opinionated 软件是稀缺品
- 服务：IKEA 强制动线
- 字体：FF Meta 拒绝多变体
- 商业：Pentagram 合伙制是宪法

### 元原则 6：**工艺痕迹 = 反均值化武器**
- 设计史：Universal 字母几何不完美、Greiman 噪点、Memphis 接缝
- 网页：editorial 故意 overshoot、brutalist 裸露
- 字体：手工 kerning、ink trap、stroke contrast
- AI 时代：手绘回归
- 代码：Knuth literate prog、SQLite "old and boring"、Lua 17k 行
- 包容性：Be My Eyes + GPT-4V = 给 100% 服务
- 服务：Sagmeister 皮肤刻字
- 伦理：手工痕迹反 AI slop

### 元原则 7：**Solve for one, extend to many**
- 包容性：Microsoft Inclusive Design 箴言
- 通用：坡道、字幕、大字号
- 商业：Sagmeister 个人 IP
- 服务：每个用户场景都从一个人开始

### 元原则 8：**结构 > 像素**（新增）
- 信息架构：IA 在原型之前、在界面之前、在像素之前
- 服务设计：UI 是冰山露出水面的尖，Blueprint 才是 90%
- 数据可视化：data-ink ratio + 视觉编码选择 > 装饰
- 字体：kerning 表 1000+ 工时 = 字体的 70% 成本
- 批评：批评四层永远先说站在哪一层

---

## 4. 跨领域的"if-then"决策框架

### 写按钮
- **UI**：1 主 + 1 次 + 1 危险
- **iOS**：填充实色 + 圆角 10pt + SF Pro
- **AI**：行内 Tab/Esc，**不要加 sparkles**
- **产品批评**：Stripe 15 个外观参数 > 1000 个
- **可访问性**：可点击区 ≥ 24×24，图标+文字双通道

### 写加载状态
- < 100ms 不显示 / 100ms-1s 骨架 / 1-10s 骨架+进度 / > 10s 进度+取消
- **网页**：subtle hover 取代"loading 英雄动画"
- **AI 流式**：cursor 闪烁 + Stop 按钮
- **游戏**：HUD 该消失时就消失

### 写错误信息
- **UI 模板**：什么 + 为什么 + 怎么修
- **AI 模板**：诚实标记不确定性
- **产品批评**：1Password 错误显式 vs Google Buzz 默认公开
- **可访问性**：图标+文字双通道
- **伦理**：错误归因 + 撤回路径必须显式

### 命名
- **代码**：单意图、给读者讲短故事
- **类推**：UI 层级命名 = 代码 API 层级
- **类推**：品牌 token 命名 = 代码 namespace
- **反 AI**：对称命名

### 选择"自定义还是 native"
- **UI**：80%+ 顶级用同样方式 → native
- **AI**：poka-yoke 工具参数防错
- **网页**：现代 CSS 原生能做的，50 行替代 3MB JS 库
- **可访问性**：用 native 控件自动获得 VoiceOver/TalkBack
- **游戏**：核心机制不可被平台破坏

### 字体选择
- **≤12px UI** → Inter / IBM Plex / Söhne
- **大字号标题** → Söhne Breit / Tiempos Headline
- **悬停动效** → GRAD 自定义轴
- **AI**：调色板滑杆代替纯 prompt
- **代码注释**：Atlassian Mono

### 评审一个设计
- **三级**：critique (3-6 设计) → stakeholder → ship
- **三分类**：Action / Persuade / Clarify
- **48h action items 必关闭**
- **公开批评 vs 私下反馈决策**

### 给一个改版打分
- 8 条预警 + 1.2M 签名 + 股价 -15% = 必败
- "为下一个 10 亿用户设计" = 杀现有 1 亿
- "强制整合" 失败率 100%

### 卖设计
- 可重复卖 > 一次性
- 价值定价 > 时薪
- 声誉套利：先曝光后接咨询
- 混合栈：产品 + 咨询 + 教育 + 订阅

### 设计服务（超越 UI）
- 先画 Journey Map（用户感受）+ Blueprint（组织责任）
- 永远同时看前后台
- 触点是时间链不是孤立点

### 检测暗色模式
- 退出是否比进入更难？
- 默认值是否对你有利？
- 拒绝按钮的语言压力？
- 价格最后一步突变？
- 关键信息被视觉弱化？
- 是否被强制做某事才能解锁？
- 倒计时/库存/在线人数？
- 第三方内容被伪造成原生？

### 怀疑一张数据图
- Y 轴从哪开始？
- 有没有图例？
- 样本量 n=?
- 有没有第二根 Y 轴？
- 颜色是否 rainbow？
- 趋势线是否在散点图上硬画？

---

## 5. 7 大警戒

### 警戒 1：AI 出活感
- sparkles 图标泛滥 / "Powered by AI" 当价值主张
- 默认开启全自主 agent / 隐藏工具调用
- thumbs up/down 当唯一反馈
- 省略"人类可以随时停"按钮
- AI critique "看上去都对" = 中位数漂亮
- 训练数据合法性（被起诉）

### 警戒 2：2015 年网页签名
- 全屏 background video + 居中 logo + 3 个并排 icon
- 5 个并列 feature 卡片 + 渐变阴影
- 50% 弹全屏 newsletter modal
- 3MB JS 库跑 200 字滚动 reveal
- 4 列 mega footer + 60 链接

### 警戒 3：AI 代码丑
- 变量名 `userData` / `tempObj` / `result2`
- 抽象层次混乱 / 过度防御 try-catch
- 200 行无叙事结构函数
- hello world 17 个包依赖
- 不对称命名

### 警戒 4："不 native" 反例
- Material 用 iOS 风格胶囊按钮
- iOS 用顶部横向 tab
- 汉堡菜单独占主导航
- 左上"返回"按钮跨平台混用
- 把 SF Pro 用在 Android

### 警戒 5：评审失败
- critique 上 stakeholder 大改交互（混级别）
- 会议 60 分钟塞 5 个项目
- 主持人做评论家不做时间管理
- 24h action items 不关闭
- 设计师"我做完了你别动"

### 警戒 6：可访问性漏检
- 占位符代替 label
- 颜色是唯一信息载体
- 模态框无焦点管理
- 视频无字幕
- 可点击区 < 24px
- 16 岁以下产品有 streak/like 机制

### 警戒 7：商业化反模式
- 时薪报价当默认
- 不写修改轮数 / kill fee
- "朋友价"和"市场价"混在一起

### 警戒 8：数据可视化欺骗
- 截断 Y 轴
- 双 Y 轴制造虚假相关
- 3D 饼图
- Rainbow 调色板
- 省略刻度/单位/数据源
- 伪造趋势线

### 警戒 9：信息架构失败
- "先画线框再补 IA"
- 用内部术语命名类目
- 零结果搜索只显示"未找到"
- 跳过 Card Sort + Tree Test

### 警戒 10：服务设计失配
- 前台优化 + 后台失配（手机银行让排队消失但放款还是 7 天）
- 触点断裂（医院预约上线但到院仍要重新填表）

---

## 6. 5 大范式参考

| 产品场景 | 参考 |
|---|---|
| 开发者工具 / 多人协作 | GitHub Primer |
| 企业后台 / 金融 / 医疗 | IBM Carbon |
| 电商 SaaS / 商家后台 | Shopify Polaris |
| 团队协作 / 工单 / Wiki | Atlassian DS |
| 高密度 CRM / 销售管道 | Salesforce SLDS |

---

## 7. 10 大决策问题

### Q1: "我该不该用这个 AI 工具？"
### Q2: "我是该遵守约定还是创新？"
### Q3: "我做的设计是 2015 还是 2026？"
### Q4: "我做的设计对色盲用户友好吗？"
### Q5: "我应该用时薪还是价值定价？"
### Q6: "我是 junior / mid / senior？"
### Q7: "我应该公开批评还是私下反馈？"
### Q8: "我应该接这个改版项目吗？"
### Q9: "我应该画界面还是画整段旅程？"
### Q10: "我做的图是诚实的吗？"

详细答案见 [design-decision-handbook.md](design-decision-handbook.md) 历次版本

---

## 8. 知识库自评（2026-06 刷新）

**memory 总数**：14 哲学 + 39 设计领域 + 3 元索引 + 2 辅助 + 1 归档 + 11 代码哲学 = **70 份**（不含 MEMORY.md 索引）
**总字符数**：约 **700KB**（每份 5-18KB）
**Wave 累计**：8 波研究 + 1 波整理
**累计 WebFetch 调用**：~1500+ 次

**覆盖范围**（按主题分 11 组，详见 §1）：
1. 元索引 & 总纲（3） 2. AI 时代设计（5） 3. Cursor + Figma & 真实代码库（2，**新增**）
4. 评审 & 工作流（2） 5. 设计系统（2） 6. 视觉工艺（7）
7. 平台 & 场景（6，含 3D 空间**新增**） 8. 工艺 & 工艺哲学（6）
9. 商业 & 教育（2） 10. 包容 / 伦理 / 用户研究（5） 11. 设计哲学（14）

**已填补盲点**（2026-06 整理后）：
- ✅ 3D / 空间 / visionOS 设计 → [design-3d-spatial.md](design-3d-spatial.md)
- ✅ Cursor + Figma 端到端实操 → [design-cursor-figma-loop.md](design-cursor-figma-loop.md)
- ✅ 真实生产设计系统代码拆解 → [design-real-codeteardown.md](design-real-codeteardown.md)
- ✅ 国际化 / i18n / RTL 设计 → [design-i18n-rtl.md](design-i18n-rtl.md)
- ✅ 设计师创业 / 微型工作室 → [design-startup-studio.md](design-startup-studio.md)
- ✅ 字体授权 + 设计法律 + 合同 → [design-font-legal.md](design-font-legal.md)
- ✅ 设计教育学 / 课程设计 → [design-education-teaching.md](design-education-teaching.md)
- ✅ 行业垂直：医疗 / 金融 / 工业 / 车载 → [design-verticals-b2b.md](design-verticals-b2b.md)
- ✅ 中文设计圈本土实践 → [design-chinese-circle.md](design-chinese-circle.md)
- ✅ AI 设计去 AI 化（吸收进 [design-ai-prompt.md](design-ai-prompt.md) 第 1/7/8/10 节）
- ✅ 真实用户研究方法、可访问性 WCAG 2.2、包容性、伦理（早期已补）

**剩余盲点**（2026-06 全清）：
无。9 个原始盲点全部填补。下次 Wave 候选仅基于"用户实际项目需求"决定。

---

## 9. 新兴资源 URL（2026-06 更新）

- [developer.chrome.com/docs/css-ui/scroll-driven-animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations) — 现代 CSS scroll-driven
- [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic agent 哲学
- [developer.apple.com/wwdc/](https://developer.apple.com/wwdc/) — visionOS / SwiftUI 设计参考
- [help.figma.com/hc/en-us/articles/32132100880855](https://help.figma.com/hc/en-us/articles/32132100880855-Guide-to-the-Figma-MCP-server) — Figma MCP server 官方文档
- [primer.style/](https://primer.style/) + [polaris.shopify.com/](https://polaris.shopify.com/) + [atlassian.design/](https://atlassian.design/) + [carbondesignsystem.com/](https://carbondesignsystem.com/) + [lightningdesignsystem.com/](https://www.lightningdesignsystem.com/) — 5 大公开设计系统
- [nngroup.com/articles/](https://www.nngroup.com/articles/) — NN/g 全部可用性研究
- [webaim.org/](https://webaim.org/) — Web 可访问性
- [servicedesigntools.org](https://www.servicedesigntools.org/) — 服务设计工具库
- [observablehq.com](https://observablehq.com/) — 数据可视化 notebook
- [pair.withgoogle.com](https://pair.withgoogle.com/) — Google People + AI Research

---

## 10. 工作流：做设计时的 13 步检查（v6）

每次做设计决策前，**按顺序问这 13 个问题**：

1. **属于哪个平台/范式？** → 看对应 memory（决策树 §2）
2. **是 2D 还是 3D / 空间？** → 若是后者，跳 [design-3d-spatial.md](design-3d-spatial.md)
3. **有 80%+ 顶级产品用同样方式吗？** → 跟着做
4. **最简方案能否达到目标？** → "Less but better"
5. **可逆性如何？** → 破坏性操作必 undo
6. **反 AI 出活感？** → 7 大警戒检查
7. **可访问性 OK？** → WCAG 2.2 AA 必做清单
8. **评审机制怎么开？** → 三级评审 + 三分类
9. **端到端工具链选对了吗？** → Cursor + Figma MCP + 真实代码库（见 [design-cursor-figma-loop.md](design-cursor-figma-loop.md) / [design-real-codeteardown.md](design-real-codeteardown.md)）
10. **决策怎么沉淀？** → token / ADR / design history
11. **怎么定价/卖？** → 价值定价 + 合同 4 必写
12. **前后台是否同步？** → Blueprint + 触点链
13. **数据是否诚实？** → Y 轴 + 视觉编码 + 样本量

如果任何问题答不上来，回到对应 memory 找答案。

---

## 11. 变更日志
- **v6（2026-06-06）**：索引从 20 份扩到 60 份；归档 design-ai-de-slop.md；新增 9 份盲点（3D 空间 / Cursor-Figma / 真实代码库 / i18n-RTL / 设计师创业 / 字体法律 / 设计教育学 / 行业垂直 / 中文设计圈）；工作流从 11 步扩到 13 步；盲点全部填补
- **v5（2026-05）**：吸收 8 波研究综合
- **v4（2026 初）**：4 波研究综合
- **v1-v3**：早期 Wave 1-3 写入
