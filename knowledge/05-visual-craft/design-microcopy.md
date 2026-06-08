---
name: design-microcopy
description: 微文案实操手册 - 按钮/CTA/表单/错误/空状态/404/确认对话框/AI 改稿清单 + 30 条 Before/After 对照
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 微文案（Microcopy）实战手册

## 一句话总结
**微文案就是 UI 上所有短文字（按钮、标签、错误、空状态、占位符、CTA）。它不是"润色"而是"功能"：用对了用户秒懂、用错了用户秒走**。下面 10 条规则全部可以直接复制粘贴进产品。

## 1. 按钮文案：动词开头，3-8 字

按钮 = 一个动作，所以第一个词必须是动词，且要告诉用户"按下去会发生什么"。

- **首词必须是动词**：`Save` / `Delete` / `Send` / `Continue` / `Create project`。**禁止** `Yes` / `OK` / `Submit` / `Next` 这种万能词
- **长度 3-8 字（英文 1-3 词）**。超过 3 个词要拆成主按钮+辅助按钮
- **写"动作+宾语"**，不要写"动作+修饰"：
  - `Save` 比 `Save changes` 短一点
  - `Save and continue` 是双步操作，主按钮 `Save`，下方给 `Continue` 链接
- **三组近义词辨析**：
  - `Delete` 永久删除，不可恢复
  - `Remove` 从当前列表移除（可能在别处存在）
  - `Archive` 隐藏但保留，30 天内可恢复
  - 电商购物车必须显式 `Remove`（不能假设"数量改 0 = 删除"）
  - 邮件用 `Archive`，文件用 `Trash`，账号用 `Delete`
- **禁用列表**：`OK` / `Cancel` / `Submit` / `Yes` / `No` / `Confirm`
  - `Cancel` 改成 `Keep editing` / `Discard` / `Don't save`
  - `OK` 改成动作本身：`Delete file` / `Send message`
  - `Submit` 改成动词：`Send` / `Sign up` / `Place order` / `Create account`
- **危险操作加对象**：`Delete "Q4 report.pdf"` 比 `Delete` 安全 10 倍

**模板**：`[动词] + [对象]`、`[动词] + [对象] + [结果]`

## 2. CTA 文案：动词 + 收益 + 零风险

CTA 不是"鼓励用户"，是"告诉用户按下后的具体回报"。

- **三段式结构**：`[动词] + [收益] + [去风险]`
- **三种场景对比**：
  - `Start free trial` —— 适合"用户已经决定要试但还没注册"的高意图场景（落地页底部、邮件）
  - `Get started` —— 适合"还不确定要不要试"的产品首页/引导页，去风险化
  - `Try it free` —— 适合"现成 demo/沙盒"，无注册门槛
- **避免空动词**：`Learn more` / `Click here` / `Discover` / `Explore` 都是黑话。改成 `See pricing` / `Watch 2-min demo` / `Browse 50 templates`
- **价格透明原则**：按钮上写清价格或时长。`Start free trial — 14 days, no card` 比 `Start free trial` 转化率高 20%+
- **第一视角 vs 第二视角**：
  - 第二视角（对用户说）：`Start your free trial`
  - 第一视角（用户视角）：`Get my free trial`
  - 第一视角 A/B 测试通常胜出，但"my"滥用会显假，控制在关键节点

**模板**：`[动词] + [名词]`，例如 `Build my resume` / `Send the invite` / `Create my store`

## 3. 表单标签：标签 ≠ 占位符

表单三件套：**Label（标签）** + **Helper（辅助说明）** + **Error（错误）**。

- **Label 用名词或动词+名词**，不能是问句
  - 好：`Email address` / `Password` / `Project name`
  - 坏：`Your email` / `What's your password?` / `Enter email here`
- **Label 永远显示**，不能被 placeholder 替代（输入后即消失，用户记不住自己在填什么）
- **Placeholder 只能放示例**：`e.g., 555-1234` / `you@example.com`。**绝对不能放 Label**
- **必填项用"\*"**（红色）放在 Label 右侧；不要在 Label 写 `Required` 字样
- **可选字段写 `(optional)`**，比例 > 70% 必填时建议反过来标 optional
- **Helper 文字只在必要时出现**：`Password` 旁一行 `At least 8 characters, with 1 number`
- **Label 大小写**：Title Case 用于英文（`Email Address`），Sentence case 用于 UI 描述文字（`Email address`）。按钮用 Sentence case（`Sign up` 比 `Sign Up` 高级）

## 4. 错误信息：什么错了 + 为什么 + 怎么修

错误信息不是"提示用户你失败了"，是"教用户怎么成功"。

- **三段式模板**：
  1. **什么错了**（具体问题）：`Password is too short`
  2. **为什么**（条件/规则）：`Passwords must be at least 8 characters and include 1 number`
  3. **怎么修**（明确动作）：`Try adding 3 more characters` 或示例 `e.g., Sun4rise!`
- **保留用户输入**：报错时不要清空输入框
- **不指责用户**：禁用 `Invalid` / `Illegal` / `Wrong` / `Bad` / `You failed`。改成 `doesn't match` / `isn't quite right` / `needs a number`
- **错误显示位置**：紧贴出错字段下方（不是顶部 banner）。用红色 + 图标 + 加粗，**不要只靠颜色**（色盲用户）
- **不要在用户输完前报错**：`onBlur` 触发，不要 `onChange` 实时跳红（用户还在打字）
- **通用 vs 具体的差距**：
  - 差：`Invalid password`
  - 中：`Password must be at least 8 characters`
  - 好：`Password needs 8+ characters and 1 number. Try something like Sun4rise!`
- **幽默限度**：可以加品牌人设（如 Mailchimp），但不要双关或俚语
- **网络错误不要技术黑话**：不要 `Error 503: Service Unavailable`。改成 `We can't reach our servers right now. Check your connection or try again in a minute.`

**模板**：`[字段名] + [needs/必须] + [具体条件]. [示例/动作].`

## 5. 空状态：4 类对 4 套模板

| 类型 | 标题模板 | 描述模板 | CTA 模板 |
|---|---|---|---|
| 首次使用 | `No [物品] yet` | `Create your first one and it'll show up here.` | `Create your first [物品]` |
| 无搜索结果 | `No results for "[query]"` | `Check your spelling, or try a broader search.` | `Clear filters` / `Search again` |
| 无权限 | `[物品] are private` | `Ask the owner for access, or check your account.` | `Request access` |
| 无网络 | `You're offline` | `We'll sync your changes as soon as you're back online.` | `Retry` / `Work offline` |

- **空状态 = 引导 + 解释 + 行动**三件套，缺一不可
- **不要写**："Wow, such empty!"（无信息）/ "There are no items to display"（机器话）/ "You have not created any projects. Click here to begin!"（累赘）
- **首次使用要给激励**：不止说"还没有"，说"为什么应该有"。`No projects yet — start one to track your tasks across the team.`
- **无结果要给出路**：`No results for "iphne"` 下加一行 `Did you mean: iPhone?`
- **文案长度**：标题 ≤ 6 字，描述 ≤ 20 字，CTA ≤ 4 字

**模板**：`[空事实 1 句] + [原因或激励 1 句] + [动作按钮]`

## 6. 成功反馈：说"做了什么"而不是"成功"

- **具体 &gt; 抽象**：
  - 差：`Success!`
  - 差：`Saved`
  - 好：`3 files uploaded`
  - 更好：`3 files uploaded to "Q4 reports"`
- **三秒原则**：用户点完按钮，3 秒内必须看到反馈。可以是 toast、inline、页面跳转
- **Toast 文案**：`[动词过去式] + [对象/数量]`。位置右下角或顶部，4 秒自动消失
  - `Saved`
  - `Email sent to alice@example.com`
  - `Removed 2 items from cart`
  - `Synced 14 changes`
- **不要在 toast 里说"成功"**：`Successfully saved!` 是冗余——"Saved" 已经包含了
- **失败也要具体**：`Couldn't send email. Check your connection and try again.`
- **可撤销 = 黄金体验**：危险操作后给 5 秒"Undo"。`Removed. Undo`

**模板**：`[过去式动词] + [具体对象/数量]`

## 7. 404 / 500 / 错误页：人话 + 替代路径

- **404 三件套**：
  1. **一句人话**（不是技术错误码）：`Page not found` / `This page took a wrong turn`
  2. **一句解释**：`The link you followed may be broken, or the page may have moved.`
  3. **一个出路**：`Back to home` / `Search` / `Browse all projects`
- **500 不要"很抱歉给您带来不便"**：直接说 `Something went wrong on our end. Our team has been notified. Try refreshing, or come back in a few minutes.`
- **加品牌人设可以**（如 GitHub 的"工程师修恐龙"插图），但**保底功能不能丢**：必须有"返回首页"或"刷新"按钮
- **保留用户来源**：URL 搜索参数带 `?ref=...`，404 页可以根据来源给个性化建议
- **不要在错误页用销售话术**：`Sign up for our newsletter!` —— 用户此刻是负面的，推销只会更烦

**模板**：`[错误事实] + [可能原因] + [替代动作]`

## 8. 占位符 vs 标签：占位符是示例，标签是答案

**这是新人最常犯的错：用 placeholder 替代 label。**

- **Label 永远显示**（input 外面或上方），告诉用户"这个框是填什么的"
- **Placeholder 灰色文字，消失后无残留**。**只能放示例格式**，不能放提示或要求
- **错误示范**（用 placeholder 替代 label）：
  ```
  ┌─────────────────────────┐
  │  Enter your email       │  ← 输完就消失
  └─────────────────────────┘
  ```
- **正确做法**：
  ```
  Email address
  ┌─────────────────────────┐
  │  you@example.com        │  ← 这是示例，不是 label
  └─────────────────────────┘
  ```
- **为什么不能替代**：
  1. 用户输入后看不到自己填的是什么字段
  2. 错误信息出现时，用户失去上下文
  3. 屏幕阅读器对 placeholder 支持不一致
  4. 用户容易把示例当默认值提交
- **浮动 label（floating label）可以**：Material Design 的样式，标签在框内、未输入时显示、输入后上浮。**但占位符绝对不能替代**

**禁用**：
- 永不：`Click here to enter...`
- 永不：`Required`
- 永不：`Search...`（应该用搜索图标 + aria-label）

**模板**：
- Label：`[名词]`
- Placeholder：`e.g., [示例]` 或 `[格式示例]`

## 9. 确认对话框：陈述结果，不用 Yes/No

- **Yes/No 是反模式**：用户必须读问题才能理解选项。改成陈述结果：
  - 差：`Are you sure you want to delete?` / `Yes` / `No`
  - 好：`Delete "Q4 report.pdf"?` / `Delete` / `Keep`
  - 更好：`Delete "Q4 report.pdf"? This can't be undone.` / `Delete` / `Keep`
- **危险操作加对象** + **加不可逆声明**：
  - `Delete your account? This will permanently remove 142 projects and cannot be undone.`
  - 按钮：`Delete account` / `Keep account`
- **按钮视觉权重匹配危险程度**：
  - 危险按钮用红色实心，Keep/Cancel 用灰色描边
  - **不要主按钮绿色、Cancel 灰色** —— 用户会习惯性按 Enter 走错（Windows 10 错误示范）
- **高危操作二次确认**：删除账号前让用户输入账号名或 `DELETE`。Mailchimp 让你输入 `DELETE` 才能删邮件列表
- **频繁操作给"不再提醒"**：删单个邮件不要确认，删 50 封才确认 + 给 `Don't ask again for 7 days`
- **可撤销 &gt; 二次确认**：5 秒内 `Undo` 比"确定吗"更友好

**模板**：`[陈述句：会发生什么]? [不可逆声明]. [主操作] / [次操作]`

## 10. AI 输出文案改稿清单（看到立刻改）

AI 生成的 UI 文案有 12 个明显套路，对照改：

| AI 套路 | 改写方向 |
|---|---|
| `Welcome to your [X]!` | 直接删，写产品名 + 主 CTA |
| `Let's get started!` | 换成具体动作：`Create your first project` |
| `Click here to begin!` | 删 `Click here`，写成动词开头 |
| `You have not created any [X].` | 缩短为 `No [X] yet` |
| `Are you sure you want to [X]?` | 改成陈述：`[X]? This can't be undone.` |
| `Success!` / `Done!` | 换成具体：`3 files uploaded` |
| `Oops! Something went wrong.` | 换成具体：`Couldn't reach the server. Check your connection.` |
| `Invalid input` | 换成具体：`Email must include @` |
| `Please enter your [X]`（label） | 改成名词：`Email address` |
| `Submit`（按钮） | 改成动词：`Sign up` / `Send` |
| `Thank you for your submission!` | 改成具体：`We'll review and reply within 24 hours.` |
| `We are sorry for the inconvenience.` | 改成具体：`Server error. Our team has been notified.` |
| `... and start your journey today!` | 删掉所有 `!` 之外的情感词 |

**改稿的 5 个必做动作**：
1. 删所有 `!` 之外的感叹号
2. 删所有 `Please` / `Kindly` / `We are sorry`
3. 删所有 `Welcome to ...` / `Let's ...`
4. 把所有 `Click here` 换成动作本身
5. 把所有 `Submit` / `OK` / `Yes` 换成动词+对象

## 30 条微文案改写对照表（Before / After）

| # | Before | After | 类别 |
|---|---|---|---|
| 1 | Welcome to your dashboard! Let's get started! | New project | 引导 |
| 2 | Click here to begin! | Create your first project | 引导 |
| 3 | Submit | Sign up | 按钮 |
| 4 | OK | Save changes | 按钮 |
| 5 | Cancel | Keep editing | 按钮 |
| 6 | Yes / No | Delete / Keep | 按钮 |
| 7 | Delete | Delete project | 按钮 |
| 8 | Remove | Remove from team | 按钮 |
| 9 | Archive | Archive project | 按钮 |
| 10 | Save | Save changes | 按钮 |
| 11 | Continue | Next step | 按钮 |
| 12 | You have not created any projects. Click here to begin! | No projects yet | 空状态 |
| 13 | No items to display | No items in this folder | 空状态 |
| 14 | There are no results | No results for "iphne" | 空状态 |
| 15 | Page not found | Page not found — the link may be broken | 404 |
| 16 | Error 503 | We can't reach our servers. Try again in a minute. | 错误 |
| 17 | Invalid password | Password must be 8+ characters with 1 number | 错误 |
| 18 | Invalid email | Email must include @ | 错误 |
| 19 | Wrong format | Use format: 555-123-4567 | 错误 |
| 20 | Success! | 3 files uploaded | 反馈 |
| 21 | Saved! | Saved | 反馈 |
| 22 | Done! | Email sent to alice@example.com | 反馈 |
| 23 | Your email (placeholder) | Email address (label) + you@example.com (placeholder) | 表单 |
| 24 | Enter your password | Password (label) | 表单 |
| 25 | Your name | Full name | 表单 |
| 26 | Start your free trial | Start free trial — 14 days, no card | CTA |
| 27 | Learn more | See pricing | CTA |
| 28 | Click here | Read the docs | CTA |
| 29 | We are sorry for the inconvenience | Something went wrong. Try refreshing. | 错误页 |
| 30 | Are you sure you want to delete? | Delete "Q4 report.pdf"? This can't be undone. | 确认 |

## 8 个可复用模板

### 模板 1：按钮
```
[动词] + [对象]
例如：Save / Delete file / Send message / Create project / Add member
```

### 模板 2：错误信息
```
[字段] + [needs/必须] + [具体规则]. [示例/建议].
例如：Password must be 8+ characters with 1 number. Try Sun4rise!
```

### 模板 3：空状态
```
[空事实] — [激励/原因].
[CTA 按钮]
例如：No projects yet — start one to track your team's tasks.
      [Create project]
```

### 模板 4：成功 toast
```
[过去式动词] + [对象/数量]
例如：Saved / 3 files uploaded / Email sent to alice@example.com
```

### 模板 5：确认对话框
```
[动作] + [对象]? [不可逆声明].
[主操作按钮] / [次操作按钮]
例如：Delete "Q4 report.pdf"? This can't be undone.
      [Delete]  [Keep]
```

### 模板 6：CTA
```
[动词] + [收益] + [去风险/限定]
例如：Start free trial — 14 days, no card
```

### 模板 7：表单 Label
```
[名词]  (Sentence case)
例如：Email address / Password / Project name
```

### 模板 8：404 / 500
```
[事实] — [原因/状态]
[替代动作按钮]
例如：Page not found — the link may be broken.
      [Back to home]  [Search]
```

## 10 条"如果你在做文案，记住这些"

1. **第一词必须是动词**——按钮不是名词
2. **删除所有 `Please` / `Kindly`**——它们是邮件客套，不是 UI
3. **删除所有 `Welcome to...!`**——AI 的招牌口水话
4. **用具体数字代替"几个"**——`3 files` 比 `some files` 好 10 倍
5. **错误信息永远包含"怎么修"**——告诉用户下一步做什么
6. **占位符 ≠ 标签**——标签必须永远显示
7. **危险按钮写对象**——`Delete "Q4.pdf"` 比 `Delete` 安全
8. **Yes/No 反模式**——改成陈述结果
9. **不要在用户输完前报错**——`onBlur` 而不是 `onChange`
10. **每个感叹号都要审查**——UI 里 90% 的 `!` 可以删

## 5 条反面教材（看到立刻改）

1. **"Welcome to your dashboard! Let's get started!"** —— AI 套话，零信息量。改成产品名 + 第一个动作
2. **"Are you sure?"** —— 没说会发生什么。改成 `Delete "Q4 report.pdf"? This can't be undone.`
3. **"Invalid input"** —— 没告诉用户怎么修。改成 `Email must include @. Try you@example.com.`
4. **"Submit"** —— 没动作信息。改成 `Sign up` / `Send` / `Place order`
5. **"Oops! Something went wrong."** —— 没具体问题、没修复路径。改成 `Couldn't upload the file. Check your connection and try again.`

## 5 条"如果你只能记一条"

1. **第一词必须是动词**——按钮、CTA、确认对话框、错误修复动作，全部以动词开头
2. **错误信息 = 什么错了 + 为什么 + 怎么修**——三件套缺一不可
3. **占位符不能替代标签**——标签永远显示，占位符只放示例
4. **删除所有 `Welcome to...!` / `Let's get started!` / `Oops!`**——AI 标志口水话，删掉产品立刻高级
5. **用具体代替抽象**——`3 files uploaded` 永远比 `Success!` 强

## 资源 URL
- nngroup.com/articles/microcopy/ / popups-10-problematic-trends/ / confirmation-dialog/ / placeholders-in-form-fields/
- nngroup.com/articles/error-message-guidelines/ / empty-state-design/ / call-to-action-buttons/ / button-design/ / reset-and-cancel-buttons/
- smashingmagazine.com/2017/05/microcopy-form-design/ / 2015/12/error-messages/ / 2018/06/microcopy-ux-form-design/
- smashingmagazine.com/2017/02/microcopy-rules/ / 2020/03/empty-states-mobile-app/
- uxwritinghub.com/microcopy/ / error-messages/ / button-text/ / empty-states/
- uxdesign.cc/microcopy-101-913e7cf5ae6f
- copyhackers.com/2017/05/microcopy-form-cta-buttons/ / 2018/01/form-microcopy/
- en.wikipedia.org/wiki/Microcopy / UX_writing
- interaction-design.org/literature/topics/microcopy
- uxdesigninstitute.com/blog/ux-writing/ / microcopy-best-practices/
- stripe.com/docs/api/errors / airbnb.com / notion.so (微文案范本)
