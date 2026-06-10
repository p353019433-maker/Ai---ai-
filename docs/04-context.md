# 04 · 语境 — 平台、可访问性、i18n、伦理、行业、中文

> 蒸馏自：design-app-platforms、design-3d-spatial、design-game-ux、design-i18n-rtl、design-verticals-b2b、design-chinese-circle、design-accessibility、design-inclusivity、design-ethics（原文见 git 历史）

## 一、平台方言

**iOS**：SF Pro（20pt+ 用 Display 紧排，以下用 Text 松排）；body 17pt；TabBar 49pt 3-5 项；按钮圆角 10pt；Dynamic Type 必须穿透全应用；安全区顶 44pt 底 34pt。动效=Spring（可中断可反转，按下 scale 0.97，250-350ms）。
**Material You (M3)**：从壁纸提取主色生成 Tonal Palette（tone 0-100，主色取 40）；Roboto Flex；圆角 7 档（Medium 12dp 默认）；NavigationBar 80dp；动效=easing 曲线 + Container Transform/Shared Axis（不可中断）。
**watchOS**：核心是"瞥一眼"（1-2 秒）；SF Compact；列表行 ≥44pt；动效 <200ms cross-fade 不用 spring。
**跨平台铁律**：抽象只到 30%（逻辑共享，UI 写两份）；**永不在 Android 用 SF Pro**（违反 EULA + metric 不对）；打开详情 iOS 从右 Push、Material 用 Shared Axis Z——别混方言。

**Native vs Custom 评分卡**：80%+ 顶级 app 同方式 → native；自定义需自担无障碍/全状态责任；设计师写不出全状态 spec → native。反例：div 模拟 iOS Switch → VoiceOver 不报 "switch, on"。"不 native"信号：iOS 顶部横向 tab、汉堡菜单独占主导航、Toast 停留 5s+。

**visionOS / 空间**：三窗口模式 Window(0% 沉浸)/Volume(30%)/Space(100%)，**永远不要 100% 沉浸起手**；注视停留 0.3-0.5s=悬停（必须有反馈，勿用"注视 1 秒"代替点击——眼肌疲劳）；Z 轴 5 层（主窗 1.2-1.5m；浮层覆盖主窗时主窗必须 dim 30%；把 5m 内容拖到 0.5m 触发晕动症）；玻璃上文字必须高对比；30 分钟原则 + 至少 3 个退出路径；字号 <14pt 在 1.2m 看不清。

## 二、游戏 UX

- **心流三条件**（Csikszentmihalyi）：清晰目标 / 即时反馈 / 挑战-技能平衡；L4D AI Director 动态调怪维持心流通道。Core Loop：期待奖励→执行→获得，多巴胺在期待阶段已分泌。
- HUD 3 范式：极简沉浸（RDR2 自适应——战斗弹出闲逛消失）/ 高密度可定制（WoW 插件生态）/ Diegetic（Dead Space 血条在脊椎）。
- 失败 3 要素：明确归因 / 低成本重试（3 秒内再开）/ "下次更强"暗示。Dark Souls：死不删档只丢魂+可捡回。
- 战斗反馈三通道：视觉+听觉+机制；Boss 换阶段要有前摇（telegraph）。多模态冗余：颜色+形状+位置+动画（色盲）。
- **F2P 机制识别**（伦理红线参考）：Loot Box=变比强化（老虎机原理）；Battle Pass=FOMO；能量条=主动限速卖加速；双货币让花费心理远离钱包；断签归零=沉没成本；情绪最脆弱时刻弹"特别优惠"。FTC 罚 Fortnite 2.45 亿美元。中国 2016 起要求公布概率。
- 移动：HUD 聚拇指可达区（屏幕下 1/3）；分水岭是"被打断的成本"。跨平台：UI 排版可不同，**反馈节奏/信息优先级必须一致**。

## 三、i18n / RTL

- RTL 用户 5 亿+。**8 个反转点**：text-align 用 start/end；**`padding-inline-start` 永不用 `padding-left`**；`border-start-start-radius`；图标——不对称镜像（箭头/面包屑），对称不镜像（搜索/关闭），emoji 永不镜像；**阿拉伯文中数字仍 LTR**（`<span dir="ltr">` 保护）；日期用 `Intl.DateTimeFormat`；货币用 `Intl.NumberFormat`（欧洲 `100,00 €`、印度 `₹1,00,000`）；`dir="rtl"` 自动反转 flex。
- CSS 逻辑属性浏览器支持 98%+，全面替代物理属性。
- 字体回退按语言切：阿拉伯 IBM Plex Sans Arabic→Noto；中文 PingFang SC→Microsoft YaHei→Source Han Sans；混排用 `unicode-bidi: plaintext`；永不用单字体覆盖所有语言。
- **测试 5 件套**：整页 dir=rtl 镜像；伪本地化长度（德文比英文长 30-50%，用 `[[[Tëšt]]]`）；数字日期；**双向混排（阿英混排是最大 bug 源）**；截断。CI 必跑 RTL 视觉回归。
- 翻译：机翻+母语校对=95% 商业项目最佳；法律/医疗必须母语。反面教材：Twitter 2014 RTL 重构花 6 个月（硬编码 padding-left）。

## 四、可访问性（WCAG 2.2）

- **AA 是法律事实标准**（Section 508、欧洲 EAA 2025、ADA 诉讼）。AAA 仅用于关键任务局部。
- **2.2 九条新规**（2023-10）关键四条：2.5.8 目标 ≥24×24px（AA）；2.5.7 拖拽必有单指替代（排序列表必须配上移/下移按钮）；2.4.11 焦点不被 sticky header 遮挡；3.3.8 认证不能强制记忆/抄写（支持密码管理器、passkey；登录别加 CAPTCHA）。
- **ARIA 第一原则：能用语义 HTML 就不用 ARIA**（`<button>` > `<div role="button">`）。陷阱：aria-hidden 不可挂聚焦元素；aria-invalid 必配 aria-describedby；成功用 polite、错误用 assertive；优先原生 `<dialog>`+showModal()（自动 inert/Esc/焦点管理）。
- 键盘：Esc 关闭并**回到触发元素**；skip link；`:focus-visible` outline 3px+offset 2px；`outline: none` 是头号反模式；工具栏用 roving tabindex。
- 读屏测试组合：NVDA+Firefox（最准）、VoiceOver+Safari、TalkBack+Chrome。盲人高手听速 400 wpm，靠标题结构构建"页面地图"——**信息层级比像素精度更重要**。
- Alt 决策树：信息图=完整描述 / 装饰图=`alt=""`（空 alt 非无 alt）/ 链接图=描述动作 / 头像旁有名字=`alt=""`。SVG 图标按钮：button 加 `aria-label`，svg 加 `aria-hidden`。
- 表单：label 必显示；错误三通道（红+图标+文字）；`autocomplete` 属性；结果在 `role="status"` 播报。
- CI：axe-core + Playwright；**自动化只能抓 30-40% 的 a11y bug**。

## 五、包容性

- Microsoft 情境性障碍光谱：永久（类风湿）/临时（抱婴儿）/情境（戴手套）——**"Solve for one, extend to many"**。Curb Cut Effect：1945 退伍兵坡道→全民受益。
- 数据：约 8% 男性色盲（永远色彩+形状+位置多通道）；阅读障碍 10%；ADHD 5-7%；光敏癫痫 0.5-1%（避免闪烁）；运动障碍全球 7.5%。
- 案例：Be My Eyes（930 万志愿者，2023 接 GPT-4V）；Xbox Adaptive Controller；Apple Personal Voice。Universal design 的限制：低视力与畏光的需求会冲突——不存在覆盖所有人的单一方案。

## 六、伦理与 dark patterns

- **13 类欺骗设计**（Brignull / deceptive.design）：Confirmshaming（"不，我不想变美"）、Drip Pricing、Forced Action、Roach Motel（注册一秒退订三十天）、Hidden Subscription、Nagging、Obstruction（拒绝追踪要 10 步）、Preselection（默认勾选=GDPR 违规）、Basket Sneaking、Trick Wording、Visual Interference（"接受所有"高亮+"管理偏好"灰色小字）等。2019 研究：11,000 购物网站 1,818 个实例。
- **罚款锚点**：Epic/Fortnite $2.45 亿；TikTok €3.45 亿（儿童数据）；Meta €12 亿；Noom $6200 万；TurboTax $1.41 亿。
- **GDPR 铁三角**：第 7 条同意必须具体自由可撤回（**默认勾选即违法**）；第 25 条 Privacy by Design；罚则 €2000 万或全球营收 4%。Cookie banner 黄金标准：**"拒绝全部"与"接受全部"等比等色**、默认无 cookie、一键撤回。
- **暗黑模式 8 检**：退出比进入难？默认值偏向谁？拒绝按钮的语言压力？价格最后一步突变？关键信息视觉弱化？强制解锁？倒计时/库存压迫？第三方伪装原生？
- **AI 新 dark patterns**：chatbot 冒充真人（Air Canada 2024 败诉）；AI 假评论（FTC 2024.10 禁止）；操纵性推荐（DSA 要求披露+非个性化开关）；deepfake（欧盟 AI Act 列高风险须披露；中国要求显式标识）。
- **儿童**：COPPA 13 岁以下需家长同意（$53,088/次）；英国 ICO 准则**禁止 like 和 streak 机制**（认定为心理成瘾设计）、禁默认画像。
- 可持续：OLED 纯黑省 60% 功耗；每多 1 秒加载 = +10% 跳出。

## 七、垂直行业（B2B 30% 专属约束决定成败）

- **医疗**（错误=死亡）：HIPAA 六必做（PHI 加密、15-30min 自动登出、审计日志、最小权限、BAA）；FHIR/Epic 集成永远显示数据来源；过敏警告不可关闭+必须签名。反模式：emoji 当状态、淡色背景（手术室强光）、<14pt。
- **金融**（错误=罚款+起诉）：永不存 CVV；PAN 遮罩；大额 MFA；KYC 永远解释"为什么问这个"。反模式：模糊数字（要 `$1,247.32` 不要 `$1k+`）、大额移动端无二次确认。
- **工业 HMI**（错误=伤亡）：按钮 ≥60×60px（戴手套）；急停永远显示（大红独立电源）；状态三重冗余（数字+视觉+文本）；**扁平化是反模式（工业要写实 3D）**；滑动操作戴手套失败率高，必须点按。
- **车载**（错误=车祸）：视线离路 2 秒=55 米盲驾；NHTSA 单次操作 <12 秒；物理按钮管音量/温度/双闪；除 HUD 速度外动画全禁。
- **B2B 通用 5 模式**：高密度（14-16px、行高 30-36px）；按角色定制 UI；数据真实性（数字可点击看明细、双时间戳、显示数据源）；键盘党（90% 操作键盘+Cmd-K）；长会话（暗色默认、撤销栈 ≥50 步）。

## 八、中文排版

- **中英 7 差异**：字号 14-15px（中文密度高反而略小）；**行高 1.7-2.0**（必须比西文大）；字重 Medium 起步（Light 难识别）；正文字距 0；行宽 **25-40 字符**（vs 西文 50-75）；按钮高 40-44px；同字号中文信息量比英文少 30%，"呼吸"要多 30%。
- **5 大必处理**：字号下限 14px（移动 <12px 必崩）；行高 1.7-2.0；标点挤压（行尾悬挂 `hanging-punctuation` + `text-justify: inter-ideograph`）；避头尾（行首禁 `、，。`，行尾禁 `（"`）；**中英混排加空格**（"中国 HTML5 开发者"）+ 中文段用全角标点、数字英文半角。
- Token 特殊值：fontSize base 15；lineHeight body 1.8；段落 maxWidth 40ch；字体栈 PingFang SC → Microsoft YaHei → Source Han Sans。
- 免费商用：思源黑体/宋体（OFL）、阿里巴巴普惠体、HarmonyOS Sans、得意黑。方正/汉仪付费且要查授权（360 查字体）。真实锚点：微信 12-14px 高密度、飞书 14-15px。
- 生态：站酷/优设（社区）、MasterGo/即时设计/蓝湖（工具）、iconfont（图标）。
