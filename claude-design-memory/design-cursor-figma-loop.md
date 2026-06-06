---
name: design-cursor-figma-loop
description: Cursor + Figma MCP 端到端实操 - MCP server 配置 / 3 核心工具 / Code Connect 映射 / 5 步标准工作流 / 10 常见错误
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
  addedDate: 2026-06-06
---

# Cursor + Figma MCP 端到端实操：执行手册

## 一句话总结
**Figma MCP 把 Figma 变成 Cursor 的"语义化图层"——AI 拿到的是带 Code Connect 映射的真实组件代码，不是 hex 颜色。** 用对的工作流让 Cursor 写代码时**直接 import 你设计系统的真实组件**，告别"AI 重新发明轮子 + 设计师回头改 50 个错位像素"。

## 1. Figma MCP 是什么 / 不是什么

**是**：
- Figma 官方 2024-2025 推出的 MCP server
- 把 Figma 文件结构（frames、layers、components、variables）暴露给 Cursor / Claude / VS Code / 其他 IDE
- 让 AI 在写代码时**像设计师一样看 Figma**，但输出真实代码
- Code Connect 集成：AI 拿到的不是 Figma 自动生成的"猜测代码"，是你仓库里的真实 import 路径

**不是**：
- 不是"截图识别"（v0 / Lovable 那种）——> 那种只能用于原型
- 不是"Figma 转代码"工具（Anima / Locofy 那种）——> 那些生成一次性代码
- 不是"自动同步"——> 每次 Cursor 写代码都需要**显式**让 AI 读 Figma frame
- 不是"万能钥匙"——> 设计师改了 Figma 后，Cursor 写过的代码**不会自动更新**

## 2. 安装配置（5 步）

### Step 1: 拿到 Figma Personal Access Token
1. 登录 figma.com → Account Settings → Personal Access Tokens
2. 创建 token，scope 选 `File content`（必需）+ `Library`（Code Connect 必需）
3. 复制 token，存到环境变量

### Step 2: 安装 MCP server
```bash
# 方式 A：npx（推荐，无需安装）
npx -y @figma/mcp-server

# 方式 B：本地安装
npm install -g @figma/mcp-server
```

### Step 3: 配置 Cursor
打开 `~/.cursor/mcp.json`（Mac）或 `%APPDATA%\Cursor\mcp.json`（Windows）：
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@figma/mcp-server"],
      "env": {
        "FIGMA_PERSONAL_ACCESS_TOKEN": "figd_xxxxxxxxxxxxx"
      }
    }
  }
}
```

### Step 4: 重启 Cursor
Cursor 自动加载 MCP server。Tools 面板应该出现 `figma.*` 工具。

### Step 5: 验证
在 Cursor Chat 里输入：`/list_tools`，应该看到：
- `figma.get_design_context` — 读 Figma frame
- `figma.get_screenshot` — 截 frame 渲染图
- `figma.create_frame` — 在 Figma 里建 frame
- `figma.get_metadata` — 读图层结构
- `figma.get_variable_defs` — 读 Variables / Tokens
- `figma.set_text` — 改文字
- `figma.delete_node` — 删节点
- `figma.create_component` — 建组件
- `figma.get_code_connect_map` — 读 Code Connect 映射
- `figma.send_file` — 复制文件

## 3. Code Connect 配置（关键！）

**没有 Code Connect，MCP 的价值只剩 30%**。配置步骤：

### 3.1 在 Figma 库组件上挂 Code Connect
- 打开 Figma 文件 → 选中组件 → 右侧 Dev Resources → Add → Code Connect
- 输入仓库路径 + import 路径 + props 映射
- 例：Button 组件
  - `import path: src/components/Button`
  - `import code: import { Button } from '@/components/Button'`
  - props: `variant: {type: enum, value: "{value}"}`

### 3.2 在仓库根目录创建 `figma-code-connect.json`
```json
{
  "codeConnect": {
    "src/components/Button": {
      "imports": [
        "import { Button } from '@/components/Button'"
      ],
      "props": {
        "variant": { "type": "enum", "value": "{value}" },
        "size": { "type": "enum", "value": "{value}" },
        "disabled": { "type": "boolean", "value": "{value}" }
      }
    },
    "src/components/Input": {
      "imports": ["import { Input } from '@/components/Input'"],
      "props": {
        "type": { "type": "enum", "value": "{value}" },
        "placeholder": { "type": "string", "value": "{value}" }
      }
    }
  }
}
```

### 3.3 提交 `figma-code-connect.json` 到仓库
Figma 每次刷新会拉取这个文件。PR 改了 → Figma 自动更新。

## 4. 5 步标准工作流（实操）

### 场景：设计师在 Figma 改了定价页 CTA，前端要同步实现

**Step 1: 设计师把 frame 标 "Ready for dev"**
- Figma frame 顶部小圆点 → Ready for dev
- 写上 Slack 消息："Pricing page CTA changed, see frame 1234"
- 提供 frame URL（带 node-id）：`figma.com/file/xxx?node-id=1234-5678`

**Step 2: 前端在 Cursor 打开项目，Cmd + L 打开 Chat**

**Step 3: 引用 Figma frame URL**
```
请实现这个 frame 的代码：
https://figma.com/file/xxx?node-id=1234-5678

要求：
1. 使用 src/components/Button 真实组件（不要重新写按钮）
2. 用 design tokens（@/lib/tokens.ts），不要写 hex
3. 写 prop interface
4. 加 Storybook story
5. 跑 Playwright 截图对比
```

**Step 4: Cursor 调用 `figma.get_design_context`**
AI 拿到：
- Frame 名称 "Pricing CTA / Primary"
- 所有图层结构
- 真实 Code Connect 映射：`Button` 组件 prop `variant: "primary"`, `size: "lg"`
- Variables：颜色 → `Color.accent.primary`，间距 → `Spacing.4`

**Step 5: Cursor 输出代码**
```tsx
import { Button } from '@/components/Button';
import { Text } from '@/components/Text';
import { tokens } from '@/lib/tokens';

export const PricingCTA = () => {
  return (
    <section className="flex flex-col items-start gap-4 p-6">
      <Text variant="display" className={tokens.text.fg.primary}>
        Start your 14-day free trial
      </Text>
      <Text variant="body" className={tokens.text.fg.muted}>
        No credit card required. Cancel anytime.
      </Text>
      <Button variant="primary" size="lg" onClick={onStartTrial}>
        Start free trial
      </Button>
    </section>
  );
};
```

**附带产出**：
- Storybook story（自动）
- Playwright 测试（自动）

## 5. 3 个核心工具详解

### 5.1 `get_design_context(frameId)`
**作用**：读 frame 的完整设计信息（图层 + tokens + Code Connect）

**最佳实践**：
- 给 AI 一个 frame ID 或 URL，**不要给整页**——> 大 frame 会超出 context
- 配合 `get_screenshot` 用：先看截图理解视觉，再读 context 写代码
- 大组件拆成 2-3 个 sub-frame，分别 get

**反模式**：
- 一次 get 整个页面（5MB context 用完）
- 不带 Code Connect 上下文，AI 看不到真实组件名

### 5.2 `get_screenshot(frameId)`
**作用**：拿 frame 的 PNG 渲染

**最佳实践**：
- 用于"理解整体视觉"（颜色/排版/层级）
- 用于 Playwright 视觉回归（跑 `chromatic` 对比）
- 截图分辨率：2x retina（`?scale=2`）

**反模式**：
- 用截图代替 get_design_context——> AI 拿到的是像素而不是语义
- 一次截 5+ 屏——> 5MB 截图 token 烧光

### 5.3 `create_frame(fileId, name, structure)`
**作用**：让 AI 在 Figma 文件里**创建** frame

**最佳实践**：
- 设计师让 AI "建一个空 frame 在 Pricing 页右侧，我先填"——> 不需要打开 Figma
- 用于 code-to-design：写完代码 → 让 AI 在 Figma 还原 frame → 视觉回归
- 用于"快速原型"：描述"做一个 12 列 60/40 分割的 pricing card" → AI 建 frame

**反模式**：
- 让 AI 改设计师已发布的 frame（除非用 Figma branch + 评审流程）
- 用 AI create frame 替代完整设计流程——> 仍是"AI 出活感"风险

## 6. Code Connect 完整模板（直接复制）

```json
{
  "codeConnect": {
    "src/components/Button": {
      "imports": ["import { Button } from '@/components/Button'"],
      "props": {
        "variant": { "type": "enum", "value": "{value}" },
        "size": { "type": "enum", "value": "{value}" },
        "disabled": { "type": "boolean", "value": "{value}" }
      }
    },
    "src/components/Input": {
      "imports": ["import { Input } from '@/components/Input'"],
      "props": {
        "type": { "type": "enum", "value": "{value}" },
        "placeholder": { "type": "string", "value": "{value}" }
      }
    },
    "src/components/Card": {
      "imports": ["import { Card } from '@/components/Card'"],
      "props": {
        "padding": { "type": "enum", "value": "{value}" },
        "elevation": { "type": "enum", "value": "{value}" }
      }
    },
    "src/components/Text": {
      "imports": ["import { Text } from '@/components/Text'"],
      "props": {
        "variant": { "type": "enum", "value": "{value}" },
        "as": { "type": "enum", "value": "{value}" }
      }
    }
  }
}
```

**命名约定**：
- 文件路径用相对仓库根（`src/components/Button`）
- import 用别名（`@/components/Button`）
- 组件名用 PascalCase，文件路径保持一致
- props key 严格匹配 Figma layer 名称

## 7. 10 个常见错误（看到 X 必改）

### 错误 1: 不挂 Code Connect 就用 MCP
**症状**：AI 输出 `<button className="bg-blue-500 ...">` 而不是 `<Button variant="primary" />`
**修正**：必须先在 Figma 组件上挂 Code Connect，AI 才会知道用真实组件

### 错误 2: 一次 get 整个页面
**症状**：Cursor context 爆，AI 输出截断
**修正**：拆 frame，按 section 分别 get

### 错误 3: 给 AI hex 颜色期望
**症状**：AI 输出 `style={{color: '#2563EB'}}` 绕过 token 系统
**修正**：明确写"用 design tokens，不要写 hex"

### 错误 4: 让 AI 改 Figma 已发布 frame
**症状**：设计师发现自己的设计被 AI 改坏
**修正**：用 Figma branch（AI 改 branch，设计师 review 后 merge）

### 错误 5: 不写 props interface
**症状**：AI 输出 `function Button(props) { return <button {...props} /> }` — TypeScript 失败
**修正**：在 prompt 里明确"写 prop interface extends ButtonHTMLAttributes"

### 错误 6: 跳 Storybook
**症状**：组件没 story，没法评审
**修正**：每次必带"加 Storybook story with autodocs"

### 错误 7: 没视觉回归
**症状**：代码跟 Figma 差 2px，没人发现
**修正**：用 Chromatic 跑 `chromatic --project-token=$TOKEN`

### 错误 8: 直接读 .figma 私有 API
**症状**：用 Figma REST API 硬读，token 烧光
**修正**：走 MCP server，它已经做了缓存 + 优化

### 错误 9: 给整个 Figma 文件 URL
**症状**：AI 试图 get 整个文件的所有 frame
**修正**：给单个 frame URL（带 node-id）

### 错误 10: 让 AI 重新发明组件
**症状**：AI 写了一个"新按钮"，但库里有 `Button`
**修正**：必须配置 Code Connect + 在 prompt 里强调"用现有组件库"

## 8. 5 步标准 prompt 模板（复制即用）

### 模板 1：新组件实现
```
请实现 [frame URL]

要求：
1. 使用 Code Connect 映射的真实组件（src/components/*）
2. 用 design tokens（@/lib/tokens.ts）
3. 写 prop interface 继承原生 HTML 属性
4. 加 Storybook story with autodocs
5. 加 Playwright 测试（关键交互）
6. 跑 `pnpm run lint && pnpm run test` 验证
```

### 模板 2：批量组件实现
```
请实现以下 5 个 frame，按顺序处理：
- [URL 1]: Hero section
- [URL 2]: Feature grid
- [URL 3]: Pricing cards
- [URL 4]: Testimonials
- [URL 5]: Footer

要求：
1. 共享 Layout 组件在 src/components/Layout
2. 每个独立组件 + Storybook + Playwright
3. 用 @/lib/tokens 统一颜色/间距
4. 处理响应式（mobile-first）
```

### 模板 3：Code-to-Design（反向）
```
我刚写完 src/components/PricingCard.tsx 和 story。
请在 Figma 文件 [file URL] 里创建一个新 frame，命名为 "PricingCard / Code Reference"，
按照组件的实际渲染还原 1440×900 desktop view。
```
（设计师用这个验证代码是否真符合 Figma）

### 模板 4：维护 / 修 bug
```
PricingCard 组件在 Figma frame [URL] 改了：
- 主色从 #2563EB 改为 Color.accent.primary
- padding 从 24px 改为 Spacing.4
- 圆角从 12px 改为 Radius.md

请更新：
1. src/components/PricingCard.tsx 的 tokens 引用
2. Storybook story
3. Playwright 截图（用 chromatic 对比）
4. 跑 `pnpm run chromatic` 看 diff
```

### 模板 5：探索 / 多版本
```
请基于 [frame URL] 生成 3 个变体：
- Variant A: 当前严格还原
- Variant B: 简化版（删除一个 CTA）
- Variant C: 实验版（改主色为 Brand.secondary）

每个变体独立文件：A.tsx, B.tsx, C.tsx
不要合并，保持对比。
```

## 9. 5 工具角色分工

| 工具 | 唯一职责 | 何时用 |
|---|---|---|
| **Figma** | 视觉真相源（Variables / Components / Code Connect） | 设计、评审、Code Connect 配置 |
| **Cursor** | 写代码（AI + Editor） | 读 Figma → 写组件 |
| **Storybook** | 组件文档 + 沙盒 | 开发自测、设计师 review |
| **Chromatic** | 视觉回归 + a11y + 部署 | CI 卡 PR |
| **GitHub** | 流程编排（PR + CI + Changesets） | 合并、版本、部署 |

**铁律**：每个工具只做一件事。Figma 不写代码，Cursor 不存 token，Chromatic 不跑单元测试。

## 10. Cursor + Figma MCP 的 8 个反 slop 检查

1. **AI 写新组件绕库**——> 必须 grep 仓库确保不重复
2. **AI 写 hex 颜色**——> PR 必卡 `color-no-hex` lint
3. **AI 写 px 字面值**——> 必须用 token `Spacing.4` 等
4. **AI 用 emoji 当图标**——> 必须用 Lucide / Phosphor
5. **AI 用 Inter 作标题**——> 必须用 Display 字体 token
6. **AI 写 200 行函数**——> 必须拆 < 50 行的子组件
7. **AI 不用 Code Connect**——> PR 必卡"已配置 Code Connect"检查
8. **AI 跳过 a11y**——> CI 必跑 axe，0 critical 必过

## 11. 真实案例：Linear 的 Figma → Cursor 流程

Linear 是用 Figma MCP 端到端最成熟的团队之一。他们的工作流：

1. **设计师在 Figma 建组件 + 配 Code Connect**——> 直接指向 `packages/ui/src/Button.tsx`
2. **设计师把 frame 标 "Ready for dev"**——> 自动触发 Slack 通知给前端
3. **前端在 Cursor 用 MCP get_design_context**——> 拿到完整设计 + Code Connect 映射
4. **Cursor 写代码 + Storybook + Playwright**——> 全套产出
5. **Chromatic 跑视觉回归**——> 自动对比 Figma 和实现
6. **PR merge 后自动发布 Storybook**——> 设计师 review 真实运行版本

**结果**：Linear 的设计系统变更从 1 周缩短到 4 小时。

## 12. 高级：branch-based 设计评审

让 AI 改 Figma 时不破坏已发布设计：

```
1. 设计师创建 Figma branch "feat-pricing-redesign"
2. AI 用 figma.create_frame / set_text 在 branch 上工作
3. 设计师在 branch 上 review，approve
4. AI 用 figma.merge_branch 合并到 main
5. 自动触发前端 Cursor 重新读 Figma
```

**铁律**：
- 永远不在 main Figma file 上让 AI 改——> 永远在 branch
- 每个 branch 对应一个 PR
- 设计师 review branch 后才能 merge

## 13. 10 条"如果你在用 Cursor + Figma MCP，记住这些"

1. **Code Connect 必配**——> 没配 = MCP 价值 70% 损失
2. **一次只 get 一个 frame**——> 大 frame 拆小
3. **必带 Storybook + Playwright**——> 组件不带 story = 不存在
4. **用 design tokens 不用 hex**——> PR 卡 lint
5. **branch 上做 AI 改动**——> 不破坏 main
6. **Chromatic 跑视觉回归**——> 0 diff 才能 merge
7. **prop interface 必写**——> 写 extends 原生属性
8. **A11y 必过 axe**——> 0 critical
9. **5 工具分工不重叠**——> Figma 不写代码
10. **真实截图对比**——> Figma 截图 vs Playwright 截图

## 5 条反面教材

1. **不配 Code Connect 就用 MCP**——> AI 输出垃圾 button HTML
2. **让 AI 改 Figma main file**——> 设计师发现自己设计被改坏
3. **AI 写 hex 颜色**——> 设计系统同步彻底失败
4. **不写 Storybook**——> 组件没评审入口
5. **跳过视觉回归**——> 50 个组件错位 2px，没人发现

## 5 条"如果你只能记一条"

1. **Code Connect = MCP 价值的 70%**——> 不配就别用
2. **AI 在 branch 工作，不在 main**——> 永远不破坏设计师的主稿
3. **Storybook + Playwright + Chromatic 必带**——> 三件套缺一不可
4. **用 design tokens，不用 hex**——> PR 卡 lint 是必须的
5. **一次 get 一个 frame**——> 大 frame 拆小，context 不要爆

## 资源 URL
- help.figma.com/hc/en-us/articles/32132100880855 — Figma MCP server 官方文档
- help.figma.com/hc/en-us/articles/15023121244245 — Code Connect 官方
- cursor.com/docs — Cursor 官方文档
- cursor.com/blog/agent-design — Cursor Agent 设计哲学
- linear.app/blog — Linear 公开的工作流
- chromatic.com/docs — Chromatic 视觉回归
- storybook.js.org/docs — Storybook 文档
- styledictionary.com/docs — Style Dictionary token 同步
- github.com/anthropics/claude-code — Claude Code 配合使用
- figma.com/dev-mode/ — Dev Mode 完整指南

## 跨引用
- [design-handoff.md](design-handoff.md) — Figma → 代码交付全流程
- [design-ai-prompt.md](design-ai-prompt.md) — 写 AI 提示词的最佳实践
- [design-system-build.md](design-system-build.md) — 设计系统构建
- [design-ai-workflow.md](design-ai-workflow.md) — AI 工具地图
- [design-real-codeteardown.md](design-real-codeteardown.md) — 真实代码库拆解（找参考实现）
