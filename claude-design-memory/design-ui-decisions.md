---
name: design-ui-decisions
description: UI 微决策的 if-then 规则手册 - 按钮/微文案/状态机/表单/通知/模态/导航/数据展示 - 来自 NN/g + Refactoring UI + LukeW
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# UI 设计决策框架（if-then 规则手册）

## 一句话总结
UI 设计每天有几十次微决策，本文用 NN/g Nielsen 启发式、Refactoring UI、Luke Wroblewski 等可追溯资源，把这些决策固化为可复用的"if X then Y"规则。

## 一、按钮层级与位置
**核心规则**：按钮的视觉权重 = 它的"承诺"。一个屏幕上只有 1 个 primary。

- **if 1 主操作** → 填充实色 + 品牌主色 + 白字（Stripe Pay）
- **if 1 主 + 1 次** → 主填充实色，次 outline/ghost（GitHub PR + Cancel）
- **if 破坏性** → 红色 outline 不填充实色（Mailchimp 删除）
- **if > 3 个按钮** → 重新设计流程，过多 = 决策瘫痪
- **if 表单底部** → 主操作必须在右下方（F-pattern 阅读终点）

## 二、微文案（按钮 / 错误 / 占位符 / 空状态）
**核心规则**：说"人话"、说"动作"、说"后果"。**永远不用内部术语**（NN/g #2）。

- **if 写按钮** → 动词 + 宾语（"Delete file" 而非 "Yes"）—— NN/g 证实误操作率降 30%+
- **if 写错误** → 模板"[什么错了] + [为什么] + [怎么修]"（"Password must be at least 8 chars, including a number"）
- **if 写占位符** → **永远不用 placeholder 代替 label**（NN/g 已证伪）—— 只做示例（"e.g., 555-1234"）
- **if 写空状态** → 模板"[这是什么] + [为什么空] + [怎么填充]"（Notion 空白页 "Type '/' for commands"）
- **if 写成功反馈** → 给出具体结果（"3 files uploaded to 'Marketing Q4'"）

**禁忌**：错误码（"Error 500"）、技术黑话、被动语态、调侃语气（生产环境）。

## 三、状态机（Loading / Empty / Error / Success / Partial）
**核心规则**：5 状态是 UI 的"人格"。Luke Wroblewski：**优先骨架屏而非旋转图标**——前者传达"内容即将出现"，后者只传达"系统在思考"。

- **if < 100ms** → 不显示加载（避免闪烁）
- **if 100ms-1s** → 骨架屏（LinkedIn 灰条）
- **if 1s-10s** → 骨架屏 + 进度（"Uploading 2 of 5 files..."）
- **if > 10s** → 进度条 + 取消 + 预计剩余
- **if 空状态** → 永远不要留白（Slack："Send a message to get started" + 插画）
- **if 错误** → retry 按钮 + 联系支持链接（GitHub 500 页面）
- **if 部分成功** → 明确告诉"10 中 8 成功 2 失败" + 失败详情

**LinkedIn 数据**：改用骨架屏后，感知加载速度提升 20%。

## 四、表单设计
**核心规则**：减少认知负荷 + 防止错误（NN/g #5 "Error Prevention"）。

- **if 写 label** → 永远 top-aligned（NN/g：比 left-aligned 快 2 倍，眼球只纵向移动）
- **if 标记必填** → 红色 `*` 标必填，可选标 "(optional)"；**if 全必填** → 不标必填只标可选
- **if 验证时机** → 失焦后立即验证，**不要在输入时弹红**（"Validating..." → "✓" → 错误时再红）
- **if 显示错误** → 红色边框 + 下方文字 + 错误图标（**不要只靠颜色**，8% 男性色盲）
- **if 选下拉** → 超过 7 项才用下拉，2-7 项用 radio/segmented，2 项用 toggle（LukeW "Dropdowns UI of Last Resort"）
- **if 主按钮** → 始终右下，"Save" 在 "Cancel" 右

**真实案例**：UK GOV.UK 表单 = 行业标杆，完成率从 60% → 80%+。

## 五、通知模式（Toast / Banner / Modal / Inline）
**核心规则**：选择取决于**中断等级** + **是否需要操作**（NN/g "Popups 10 趋势"）。

- **if 提示 + 不操作 + 自动消失** → Toast（"Message sent" 3-5s）
- **if 重要 + 不操作 + 不应消失** → Banner（顶部条永久）
- **if 关键 + 需要操作** → Modal（"Type DELETE to confirm"）
- **if 上下文相关 + 不打断** → Inline（PR 评论旁 "Build failed"）

**具体规则**：
- Toast 最多 1 个，3s 后可关闭，**不要用 toast 做错误**（用户错过）
- Banner 黄/红/蓝/绿，永可关闭，不堆 logo
- Modal 必须有明确关闭、Esc、点击遮罩关闭、焦点返回
- **绝对不要**用 modal 做 newsletter/cookie/广告

## 六、模态选择（Modal / Drawer / Popover / Inline / New Page）
**核心规则**：模态的本质是"中断"。NN/g：用户对"为业务目标"的模态有"本能的厌恶"。

- **if 完全专注 + 阻断背景** → Modal（键盘焦点陷阱）
- **if 频繁进出 + 不破坏主任务** → Drawer（Linear issue 详情，Gmail 写邮件）
- **if 简单信息 + 轻量** → Popover/Tooltip（图标说明）
- **if 一次性细节** → Inline（"Edit" 在原位展开）
- **if 多步骤 + 复杂** → New Page（独立 URL 可分享）

## 七、导航范式（Tab / Sidebar / Breadcrumb / Hub-and-Spoke）
**核心规则**：选择 = 信息架构 + 任务频次 + 屏幕尺寸。NN/g #4：遵循平台惯例（iOS tab bar，桌面 sidebar）。

- **if 同级 3-5 + 高频切换** → Top Tab（macOS Finder）
- **if > 5 + 多层级** → Sidebar（VS Code 文件树）
- **if 层级深 + 需回溯** → Breadcrumb（电商商品页）
- **if 任务流线性 + 一次性** → Hub-and-Spoke（Onboarding 向导）
- **if 主任务单一 + 频繁操作** → Bottom Tab（移动端 Instagram）

**具体规则**：
- Tab ≤ 7；当前 tab 视觉权重最高（粗体+底色+色）
- Sidebar 当前项必须有强指示（左侧色条+背景色+粗体）
- Breadcrumb 永远可点击；首项 = 首页；分隔符 `>` 而非 `/`
- 移动端 bottom tab 最多 5 个，超过合并到 "More"

## 八、数据展示（Table / Card / List / Kanban）
**核心规则**：取决于**信息密度**与**操作类型**。

- **if > 5 列 + 排序/比较/过滤** → Table（Stripe Dashboard）
- **if 2-4 列 + 异构 + 预览** → Card（产品列表，Apple Music）
- **if 1-2 列 + 简单 + 频繁操作** → List（邮件列表，Linear）
- **if 状态驱动 + 流程导向** → Kanban（Trello, Jira）
- **if 时间线** → Timeline/Gantt

**具体规则**：
- Table 第一列左对齐，数字列右对齐，header 加粗+排序指示，支持列排序
- Card 间距 ≥ 16px，高度一致，hover 抬升
- List 单行高度一致，分隔线 1px 灰
- Kanban 列宽 ~280px，列标题 sticky，拖拽有视觉反馈

## 8 条可复用微决策规则
1. **5 秒判断法**（按钮）：扫一眼看出主操作吗？> 5 秒说明太多
2. **状态机规则**：每列表/详情页必须有 5 状态设计稿
3. **模态 5 W 规则**（NN/g）：触发前问 Who/What/When/Where/Why
4. **错误信息三段式**：什么 + 为什么 + 怎么修
5. **加载时长分级**：< 100ms 不显示 / 100ms-1s 骨架 / 1-10s 骨架+进度 / > 10s 进度+取消
6. **下拉选项 7 原则**（LukeW）：2 项 toggle / 2-7 项 radio / > 7 项下拉
7. **弹窗避免清单**（NN/g）：永不用 modal 做 newsletter/cookie/广告/登录前拦截
8. **永远可逆原则**（NN/g #3）：破坏性操作必提供 undo

## 8 条反面教材
1. 占位符代替 label（用户输入后失去字段含义）
2. "Yes/No" 确认对话框（应改为 "Delete file / Keep file"）
3. 登录前强制注册（电商转化率损失 30%+）
4. Modal 套 Modal（焦点错乱，Esc 失效）
5. Toast 报错（3 秒后消失用户错过）
6. 红绿色盲只靠颜色（必须图标+文字）
7. Spinner 滥用（不告诉"快好了"）
8. 3 个主按钮（必有 1 主 2 次的层级）

## 与高级视觉美学的衔接
1. **去 AI 化与"少即是多"一致**：1 主按钮 + 大量留白 + 微妙灰阶 = Apple/Notion/Linear
2. **状态机即品牌人格**：空状态是"品牌与用户第一次对话"
3. **微文案即品牌 tone**：NN/g #2 贴合用户心智 = brand voice 延伸
4. **层级即构图**：按钮层级 = 视觉构图层级 = 安藤忠雄/ Pawson 的层次
5. **东方美学的"留白即信息"**：侘寂/shibui 现代变体 = Notion 空白页 / Things 3

## 资源 URL
- nngroup.com/articles/（启发式、模态、必填字段、占位符、popup 10 问题）
- refactoringui.com（按钮层级、色彩、深度、排版）
- lukew.com/ff（dropdown 原则、避免 spinner）
- smashingmagazine.com/category/ui-design/
- alistapart.com/
- uxdesigninstitute.com/blog/
