---
name: design-handoff
description: 设计稿到代码交付 - Figma Dev Mode + Code Connect / Style Dictionary / Storybook CSF 3.0 / Chromatic 视觉回归 / 10 模板
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 设计稿到代码交付：执行手册

## 一句话总结
**把 Figma 文件变成生产代码，靠的不是更长的 PRD，而是 5 件固定工具（Figma Dev Mode + Style Dictionary + Storybook + Chromatic + GitHub）按固定顺序跑、跑 7 次以上以后就稳了**。

## 1. Figma Dev Mode：inspect 不只是"看 spec"

Dev Mode 是 Figma 内置的开发视图，按 `Shift + D` 切换。它做的 4 件事，普通 Inspect 模式都做不到：

- **Code Connect**：Dev Mode 里直接展示你仓库里真实组件的代码片段，不是 Figma 自动生成的猜测代码。Figma MCP server（GA 后）把这一层暴露给 Cursor / VS Code / Claude，AI 写代码时拿到的是你设计系统的真实 import 路径
- **Ready for dev**：Frame 状态显式标"Ready for dev / In progress / Done"，避免开发做到一半设计师又改稿
- **Variables 同步**：右侧面板直接显示 token 的代码语法（`--color-bg-primary` / `Color.bgPrimary`），不是 hex 颜色
- **Compare changes**：在 branch 之间做像素 diff，看 PR 修改了哪些 frame

实操：把 dev seat 分配给所有前端，不要让前端用 Design seat 蹭 inspect——Inspect 在 Design seat 上是阉割版，看不到 Code Connect 映射。

## 2. 设计 token 同步：Figma Variables → Style Dictionary → 多端

Figma Variables 是单一事实源，Style Dictionary 是编译器。流程：

1. 设计在 Figma 里建 Collection（Color / Spacing / Radius / Typography），每种 token 一个 Mode（Light / Dark / Mobile / Web）
2. 用 **Tokens Studio** 插件（或 Figma REST API）把 Variables 导出为 DTCG 格式 JSON：`{ "color": { "bg": { "primary": { "$value": "#0F172A", "$type": "color" } } } }`
3. JSON 进 `tokens/` 目录，`config.json` 写 `source: ["tokens/**/*.json"]`
4. `style-dictionary build` 生成 `build/scss/_variables.scss`、`build/css/variables.css`、`build/android/colors.xml`、`build/ios/Colors.swift`
5. CI 里 `pnpm run build:tokens` 在前端构建之前跑，build 产物直接 import

**关键点**：不要让工程师手抄 hex 颜色到 CSS 里——只要有一处手抄，token 就死了。PR 里加 lint：`color-no-hex` 规则强制所有颜色走 `--color-*` 变量。

## 3. Storybook CSF 3.0：组件即文档

CSF 3.0 = ES module 写法 + `Meta` / `StoryObj` 类型 + 内置 autodocs。最小可用示例：

```typescript
import type { Meta, StoryObj } from '@storybook/react';
import { fn } from '@storybook/test';
import { Button } from './Button';

const meta = {
  component: Button,
  args: { onClick: fn() },  // 自动 spy
} satisfies Meta<typeof Button>;
export default meta;

type Story = StoryObj<typeof meta>;
export const Primary: Story = { args: { variant: 'primary', label: '确认' } };
```

把 `tags: ['autodocs']` 加到 meta，Storybook 自动生成 prop table + 控件面板。`@storybook/test` 提供 `canvas.getByRole()` + `userEvent.click()` + `expect().toBeInTheDocument()`，play 函数里写交互测试。

实操：组件库每个 PR 必须带至少一个 story + 一个 play 测试，没有 story 的组件不允许 merge。

## 4. 0 故事 handoff 文档

把"用户故事"扔掉。设计走查文档 7 个固定 section，每 section 1-3 行，不写废话：

```
【背景】这个改动为什么做（一句话）
【目标】上线后量化指标（DAU 涨 5% / 错误率降到 0.1%）
【用户】谁用、什么场景、什么痛点（不超过 50 字）
【技术约束】iOS 15+ / 弱网 / 暗黑模式 / RTL / 旧浏览器
【不做清单】明确不做什么（"不做空状态插画"、"不做手势操作"）
【成功标准】QA 验收的硬条件
【设计资源】Figma URL（带 frame link） + 资产 zip + 字体文件
```

**反模式**：写"让用户感受到温暖"、"提升品牌一致性"——验收时这些不能 pass 也不能 fail。量化或写"不做"。

## 5. 验收流程：4 层必须全跑

- **Figma 验收**：像素 diff < 1px 偏差（用 Figma Compare branch 或 Avocode / Pixelmatch）。误差源：字号、圆角、间距、阴影模糊半径、token 映射
- **实现验收**：开发自测每个 story，play 测试全过
- **跨设备验收**：Chromatic 跑 iOS Safari / Android Chrome / Desktop Chrome / Firefox / Edge 的 5 个 viewport 截图。`@chromatic-com/storybook` 自动归档 story，无需手写
- **a11y 验收**：Chromatic 内置 axe 扫描，AAA 关键项 0 违规——color contrast 4.5:1、focus ring 可见、alt 文本非空、tab 顺序符合 DOM

`chromatic --project-token=$CHROMATICPROJECT_TOKEN --exit-zero-on-changes` 在 CI 里跑，PR 必卡视觉回归。

## 6. 设计师 + 前端协作模式

固定三件事：

- **设计走查（Design Review）**：开发做完 push PR，设计师在 Storybook deployed URL（Chromatic 自动部署）上 review，不是看 PR diff。每周 1 次固定时间，30 分钟过完
- **联合编码（Pair on Component）**：新组件由设计师 + 前端一起写 30 分钟，前端写代码，设计师在 Storybook 里实时调 token 值。1 次联合编码抵 3 轮 PR review
- **设计 QA 清单**：设计师 review 时对照 6 条——间距用 token？颜色用 token？hover/active/disabled 状态齐？加载/空/错误态齐？dark mode 跑过？文案用 i18n key？

**不要让设计师看 PR 截图**——截图分辨率失真、设计稿在 Figma 里、跑版本在 Storybook 里，三者对齐在 Storybook 上做。

## 7. 设计系统维护实战

组件 PR 必须走 4 步：

1. **提案**：用 GitHub Issue 模板 `component-proposal.md`，写"为什么需要 / 现有组件为什么不够 / 视觉草图"
2. **评审**：设计系统 owner + 至少 1 个使用方团队 lead review
3. **合并**：组件进 `packages/ui`，带 story + test + a11y 验证 + Chromatic 截图
4. **Deprecation**：旧组件不删，加 `@deprecated` JSDoc 标签 + 控制台 warning，半年后用 codemod 批量替换。`npx @codeshift/cli` 写 codemod

`packages/ui` 用 Changesets 做版本管理：`pnpm changeset` → 选 bump 类型 → 自动生成 CHANGELOG → bot 提 PR

## 8. AI 时代的 handoff

AI 工具改变的不是流程，是协作入口：

- **Figma MCP server**：在 Cursor / Claude / VS Code 里直接 `get_design_context(frameId)`，AI 拿到的是带 Code Connect 映射的真实代码路径，不是 hex 颜色
- **v0 / Lovable / Bolt**：从 Figma 截图或 URL 生成 React 组件，但只能用于原型、不能进生产。生产必须用 Storybook 真实组件
- **Figma Make**（Config 2024 公布）：在 Figma 里直接生成 React 代码片段，带 Code Connect
- **Cursor + Style Dictionary**：把 `tokens/` 目录加入项目 context，AI 写新组件时自动用 token

AI 写 60% 的样板代码，人类 review 40% 的 token 映射 + 业务逻辑——但 human 永远是 token 守门人。

## 模板 1：Handoff 文档

```markdown
## 背景
新用户 onboarding 第一步转化率 38%，低于行业 50% 基线。

## 目标
D7 激活率从 22% 提升到 30%。

## 用户
首次访问、未登录、桌面端 Chrome 优先。

## 技术约束
- iOS 15+ / Android 10+
- 支持 Safari 14
- 暗黑模式必须
- 不做 RTL

## 不做清单
- 不做引导视频
- 不做社交登录
- 不做 A/B 测试（v1 单一版本）

## 成功标准
- [ ] Lighthouse 性能分 > 90
- [ ] axe a11y 0 critical
- [ ] Storybook 5 个 story 全过
- [ ] Chromatic 5 viewport 像素 0 diff
- [ ] 转化率埋点上报

## 设计资源
- Figma: https://figma.com/file/xxx?node-id=123
- Storybook: https://chromatic.com/library?appId=xxx
- 资产: https://drive.google.com/xxx
```

## 模板 2：Style Dictionary config.json

```json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "build/css/",
      "files": [{ "destination": "variables.css", "format": "css/variables" }]
    },
    "scss": {
      "transformGroup": "scss",
      "buildPath": "build/scss/",
      "files": [{ "destination": "_variables.scss", "format": "scss/variables" }]
    },
    "ios": {
      "transformGroup": "ios-swift",
      "buildPath": "build/ios/",
      "files": [{ "destination": "Tokens.swift", "format": "ios-swift/class.swift" }]
    },
    "android": {
      "transformGroup": "android",
      "buildPath": "build/android/",
      "files": [
        { "destination": "colors.xml", "format": "android/colors" },
        { "destination": "dimens.xml", "format": "android/dimens" }
      ]
    }
  }
}
```

## 模板 3：tokens/colors.json（DTCG 格式）

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "#0F172A", "$type": "color" },
      "secondary": { "$value": "#1E293B", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "#F8FAFC", "$type": "color" },
      "muted": { "$value": "#94A3B8", "$type": "color" }
    }
  }
}
```

## 模板 4：Storybook CSF 3.0 组件 + 交互测试

```typescript
import type { Meta, StoryObj } from '@storybook/react';
import { fn, expect, userEvent, within } from '@storybook/test';
import { LoginForm } from './LoginForm';

const meta = {
  component: LoginForm,
  tags: ['autodocs'],
  args: { onSubmit: fn() },
} satisfies Meta<typeof LoginForm>;
export default meta;

type Story = StoryObj<typeof meta>;

export const Default: Story = {};

export const FilledAndSubmitted: Story = {
  play: async ({ canvasElement, args }) => {
    const canvas = within(canvasElement);
    await userEvent.type(canvas.getByLabelText('邮箱'), 'user@example.com');
    await userEvent.type(canvas.getByLabelText('密码'), 'secret123');
    await userEvent.click(canvas.getByRole('button', { name: '登录' }));
    await expect(args.onSubmit).toHaveBeenCalledWith({
      email: 'user@example.com',
      password: 'secret123',
    });
  },
};
```

## 模板 5：Chromatic GitHub Actions

```yaml
# .github/workflows/chromatic.yml
name: Chromatic
on: push
jobs:
  chromatic:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm run build:tokens
      - run: pnpm run build-storybook
      - uses: chromaui/action@v1
        with:
          projectToken: ${{ secrets.CHROMATIC_PROJECT_TOKEN }}
          storybookBuildDir: storybook-static
          exitZeroOnChanges: true
```

## 模板 6：设计走查 checklist（设计师用）

```
- [ ] 所有颜色来自 token（无 hex/字面颜色）
- [ ] 所有间距来自 token（无 px 字面值）
- [ ] hover / active / focus / disabled 状态完整
- [ ] 加载 / 空 / 错误 / 成功 4 态都有
- [ ] 暗黑模式已切并对比
- [ ] 焦点环可见（不靠颜色单一通道）
- [ ] 文案用 i18n key（无硬编码中文/英文）
- [ ] 触摸目标 ≥ 44x44 (iOS) / 48x48 (Android)
- [ ] 长内容 / 短内容 / RTL 3 种情况跑过
- [ ] 动效附 timing token（无手填 200ms）
```

## 模板 7：PR 验收 checklist（reviewer 用）

```
- [ ] Storybook story 新增/更新
- [ ] play 交互测试覆盖关键路径
- [ ] Chromatic 截图 0 diff（或已 review accept）
- [ ] axe a11y 0 critical / 0 serious
- [ ] token 使用 100%（grep 无 hex 颜色）
- [ ] bundle size 增量 < 5KB
- [ ] i18n key 已加（无硬编码文案）
- [ ] 旧组件 deprecation 标记已加
```

## 模板 8：组件提案 Issue 模板

```markdown
## 组件名
Tooltip

## 为什么需要
当前 hover 提示散落在 12 处，行为不一致（延时 / 位置 / 文案截断）。

## 现有组件为何不够
Popover 太重（带遮罩），Hint 组件不支持富文本。

## API 草案
```typescript
<Tooltip content="提示文案" placement="top" delay={300}>
  <Button>触发元素</Button>
</Tooltip>
```

## 视觉草图
[Figma 链接]

## 影响范围
- 替换 12 处散落实现
- 涉及 4 个团队

## A11y 要求
- 键盘可达（focus 显示，blur 隐藏）
- screen reader 朗读 content
- 不阻断底层交互
```

## 模板 9：Figma Dev Mode + Code Connect 完整配置

**1. 在 Figma 库组件上挂 Code Connect**：
- 选中组件 → 右侧面板 → Dev Resources → Add → Code Connect

**2. `figma-code-connect.json`（仓库根目录）**：

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
    }
  }
}
```

**3. Figma MCP server（Cursor / Claude）配置**：

```json
// ~/.cursor/mcp.json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@figma/mcp-server"],
      "env": { "FIGMA_PERSONAL_ACCESS_TOKEN": "${env:FIGMA_TOKEN}" }
    }
  }
}
```

**4. 在 Cursor 里**：Cmd + L 打开 Composer，引用 Figma frame URL，AI 直接读 component props + Code Connect 映射，输出 `import { Button } from '@/components/Button'`。

## 模板 10：Deprecation 流程

```typescript
// 1. 标记弃用
/** @deprecated use `<NewButton>` instead. Will be removed in v3.0 (2026-12-31) */
export const OldButton: React.FC<Props> = (props) => {
  if (process.env.NODE_ENV === 'development') {
    console.warn('[OldButton] deprecated, use <NewButton>');
  }
  return <NewButton {...migrateProps(props)} />;
};

// 2. codemod 批量替换（用 ts-morph 或 jscodeshift）
// transforms/old-button-to-new.ts
export default function transformer(file, api) {
  const j = api.jscodeshift;
  return j(file.source)
    .find(j.JSXIdentifier, { name: 'OldButton' })
    .replaceWith(j.jsxIdentifier('NewButton'))
    .toSource();
}

// 3. 半年后删除组件
git rm src/components/OldButton.tsx
```

## 5 工具角色分工

| 工具 | 角色 | 唯一职责 |
|------|------|----------|
| **Figma** | 设计单一事实源 | 视觉 + Variables + Code Connect 映射 |
| **Style Dictionary** | Token 编译器 | DTCG JSON → CSS / iOS / Android / 多端 |
| **Storybook** | 组件文档 + 沙盒 | story = 文档 = 测试 = demo |
| **Chromatic** | 视觉回归 + 部署 | 像素 diff + a11y + Storybook 托管 |
| **GitHub** | 流程编排 | PR review + CI + Changesets + 部署 |

**铁律**：每个工具只做一件事，不重叠。Figma 不写代码，Storybook 不存 token，Chromatic 不跑单元测试，GitHub 不审设计。

## 10 条"如果你在做 handoff，记住这些"

1. **token 不能手抄**：所有颜色、间距、圆角、字号 100% 走 token，PR grep 检查
2. **Code Connect 必须配**：没配 Code Connect，Dev Mode 输出的代码就是垃圾
3. **每个组件必须带 story**：没有 story = 不存在
4. **每个关键交互必须带 play 测试**：点击、输入、提交、状态切换
5. **Chromatic 是 PR 必卡项**：视觉回归 0 diff 才能 merge
6. **handoff 文档 7 section**：背景/目标/用户/约束/不做/标准/资源——少了"不做"section 必返工
7. **设计师 review 走 Storybook URL**，不是 PR diff
8. **暗黑模式在第一版就要做**，不要写"v2 再加"
9. **组件用 Changesets 版本化**，不要改一处全量发版
10. **AI 写 60% 代码、人类 review 100% token 映射**——AI 不知道你的命名约定

## 5 条反面教材

1. **截图当 handoff**：设计师截一张图丢群里，工程师凭记忆写——必然偏差，且无法验收
2. **hex 颜色散落 CSS**：Figma 改了 Variables 但代码里还是 `#0F172A`，token 形同虚设
3. **Storybook 只跑 dev、CI 不跑**：本地通过、生产环境崩，Chromatic 必须 CI 卡
4. **设计改稿不带 Figma frame link**：群里说"按钮改一下"，没人知道改的是哪个
5. **deprecation 不留时间窗**：直接删组件，全公司 PR 报错——必须先 `@deprecated` 6 个月、console.warn、再 codemod、再删除

## 5 条"如果你只能记一条"

1. **Token 是唯一真相**：所有视觉决策在 Figma Variables 里改一次，全端通过 Style Dictionary 自动同步
2. **Story = 文档 = 测试 = demo**：CSF 3.0 一个 story 文件覆盖 4 个用途，不要再单独写 Confluence 页面
3. **Chromatic 是设计系统的 CI**：没有视觉回归就没有设计系统，因为没人发现 token 漂移
4. **handoff 文档写"不做"比写"做"重要**：明确边界才能 1 周内交付，否则 1 个月还在讨论
5. **AI 是加速器不是替代品**：Figma MCP + Cursor 让样板代码快 10 倍，但 token 命名、a11y、业务语义仍由人类定

## 资源 URL
- help.figma.com/hc/en-us/sections/14506167389835-Dev-Mode
- help.figma.com/hc/en-us/articles/15023121244245-Code-Connect
- help.figma.com/hc/en-us/articles/15339616035355-Variables-in-Figma
- figma.com/blog/figma-dev-mode-may-2024/ / figma.com/blog/whats-new-figma-config-2024/ / figma.com/dev-mode/
- styledictionary.com/docs/ / install/ / docs/format/css/
- storybook.js.org/docs/writing-stories / configure / writing-tests/visual-testing / writing-tests/interaction-testing
- storybook.js.org/docs/essentials/controls / api/csf / sharing/publish-storybook
- chroma tic.com/docs / docs/test / features/visual-regression
- zeroheight.com/
- figma.com/blog/figma-config-2024-developer-handoff/
- help.figma.com/hc/en-us/articles/8085703779223-Dev-Mode-handoff
- uxpin.com/studio/blog/design-handoff/ / smashingmagazine.com/2020/04/figma-handoff/ / 2018/05/design-handoff-dos-dont/
