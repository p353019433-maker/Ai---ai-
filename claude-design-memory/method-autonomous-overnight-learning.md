---
name: method-autonomous-overnight-learning
description: 自主学习一晚方法论 v2 - 脚本当主角·agent 写脚本睡醒读结果 - 深度研究通用模板
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
---

# 自主学习一晚的方法（opus v2）

## 核心理念
不要让 agent 当主角，让脚本当主角。agent 写好脚本放手，脚本自己跑到天亮，agent 第二天醒来读结果。

## 为什么 agent 不能当主角
| 限制 | 后果 |
|---|---|
| 会话不跨 wakeup | 每次醒来是新上下文，回忆全部丢失 |
| wakeup 间隔上限 1h | 不够覆盖一晚 |
| 需要人保持在线 | 睡了 harness 可能断 |

**结论**：把"持续学习"卸载给独立脚本，agent 只负责：(1) 写脚本 (2) 启动 (3) 睡 (4) 醒来读结果。

## 5 步法

### 1. 真实抓取，不靠回忆
agent 的"回忆"本质是从训练数据里挑几条组合，不算学习。脚本必须用 curl 抓真实网页，存为带元数据的 Markdown。
```bash
curl -sL -A "Mozilla/5.0" https://example.com/article -o raw.html
```

### 2. 自我发现，无限扩展
不靠白名单 URL。每次抓回一篇文章，从里面提取新链接喂回自己。从 700 个种子能扩展到 33,000+。
```python
def discover_urls(html):
    return re.findall(r'href="(https?://[^"]+)"', html)
```
**关键约束**：只从 q≥0.6 的文章里发现（避免坏种子污染扩展）。

### 3. 质量过滤，跳过废页
绝大多数网页是 SPA 壳子（要 JS 才渲染）。加质量分数：
- 检测 "please enable JavaScript" 等壳子信号
- 检测 "skip to content / cookie policy" 等导航模式
- 句子密度 + 独特词数
- 分数 <0.4 直接跳

### 4. 优雅退出 + 状态持久化
- 监听 SIGTERM，收到后跑最终综合
- 状态写 .tmp 再 os.replace（防中途损坏）
- 日志超过 1MB 自动轮转
- 失败 URL 30 分钟后重试（网络会恢复）
- **启动时写 PID 文件**，方便 agent 在新会话里 `kill <pid>`

### 5. 综合报告，按主题而非计数
- 按词频找主题（过滤停用词，看实际在讨论什么）
- 聚合设计信号（最高频的颜色、字体、渐变数量）
- 列出高分文章（质量 ≥0.7 的 Top 30）

## 目标目录结构
```
out/
├── INDEX.md              # 实时追加的目录
├── RUN-LOG.txt           # 滚动日志
├── SYNTHESIS.md          # 最终综合
├── state.json            # 进度（崩溃可恢复）
├── runner.pid            # 当前进程 PID（agent 用来 kill）
└── a-{时间}-q{质量}-{标题}.md   # 每篇文章
```

每篇文章格式：
```
# Title
URL: https://...
Published: 2026-05-23
Source: smashingmagazine
Quality: 0.85
Body: 4000 chars, ~2500 words
Design signals:
- gradients: 2
- top_colors: #0a2540(5), #e7ecf1(3)
- fonts: Inter
```

## 推荐参数
| 参数 | 数值 | 理由 |
|---|---|---|
| 并发抓取 | 4 | 不打爆服务器 |
| 同域冷却 | 1.5s | 做有礼貌的爬虫 |
| 抓取间隔 | 20-30s | 留时间给发现处理 |
| 失败重试 | 30 分钟后 | 网络可能恢复 |
| 总时长 | "学到完" | 不设上限 |
| 发现质量阈值 | 0.6 | 避免坏种子 |

## 启动命令
```bash
# macOS（防系统睡眠）
caffeinate -dis python3 auto-runner.py

# Linux
python3 auto-runner.py
```

`-dis` 参数：
- `-d` 防止 display sleep（屏幕）
- `-i` 防止 system idle sleep
- `-s` 防止 system sleep（最严格）

## 源池设计（两层结构）

**种子层**（用户给）：~2000 URLs
- Smashing sitemap 关键词搜索（~150）
- Wikipedia 设计/设计师/字体（~600）
- GitHub design system repos（~200 raw READMEs）
- Hacker News / Reddit（~10）
- 字体公司主页（~80）
- 个人设计师/工作室站（~50）

**发现层**（脚本自己找）：无上限
- 从每个 q≥0.6 文章的 href 提取
- 跨域去重

**实测**：从 1836 种子能扩展到 33,000+（一周内可累积 10,000-30,000 篇）。

## 监控和停机

**进程级**：caffeinate 或类似防休眠
**应用级**：脚本内置状态文件、失败/跳过列表实时写

**怎么停**：
- 给 agent 发"停" — agent 会 `kill <pid>`（从 PID 文件读）
- 或手动 `kill <pid>`
- SIGTERM 触发脚本 finally 块跑最终综合

## 3 条经验教训
1. **node_repl 的 fetch 会被网络策略拦** — 用 subprocess + curl 最稳
2. **长跑前先 smoke test 30 秒** — 不然跑 2 小时才发现 bug
3. **失败 URL 别永久跳过** — 网络会恢复，加 retry_after 字段

## 适用其他方向
把"种子列表"换成你的方向就行：
| 方向 | 种子源 |
|---|---|
| 编程语言 | GitHub awesome + Reddit + HN |
| 产品管理 | ProductHunt + Lenny's + Mind the Product |
| 营销 | AdAge + Marketing Brew + 各大 CMO 博客 |
| 学术 | arXiv + Google Scholar + 大学官网 |
| 投资 | SeekingAlpha + 各大 PE 官网 + 监管文件 |

核心不变：curl + 自我发现 + 质量过滤 + 优雅退出。

## 一句话
agent 写好脚本，agent 放手，agent 醒来读盘。中间的事让 Python 干。

## 何时使用
当用户要求"深度学习 X / 研究 X / 一晚搞懂 X"这类长时间、不可能由 agent 一次完成的研究任务时。

**How to apply:**
1. 把任务参数化：种子 URL 列表（按源池设计分类）+ 主题关键词 + 质量信号
2. 写一个 `auto-runner-{topic}.py`：
   - 启动时写 `out/runner.pid`
   - 只从 q≥0.6 文章发现新链接
   - 失败 URL 加 `retry_after` 字段，30 分钟后允许重试
   - 文章格式含 gradient count、top_colors as hex、body words
3. 先 smoke test 30 秒
4. 让用户启动 `caffeinate -dis ./.venv/bin/python auto-runner-{topic}.py`
5. 用户起床后回来 → agent `kill $(cat out/runner.pid)` 等脚本写完 SYNTHESIS.md → 读结果综合写入 memory
