# 🤝 Handoff Guide — overnight-ai-aesthetic Corpus

> 写给接手这个 corpus 的下一个 agent。
> 读完这一份（~5 分钟）就能上手，不用读 SYNTHESIS / IMPROVEMENTS 之外的其他过程文件。

---

## 1. 你接手的是什么

一个**"AI 美学 vs 真实设计"**方向的语料库：

- **目标**：在大量设计类文章里，找出"什么不是 AI 默认套路"—— 反 AI-default 的设计语言 / 反 cyber-slop 案例 / 真实设计师的色彩与字体习惯
- **方法**：自动爬取 + 关键词评分 + 主题分类（v4-v7 迭代过几轮）
- **当前状态**：**采集完成，消化未开始** — 6,044 条 metadata 已整理，正文 2,266 篇已下载本地

---

## 2. 目录结构（清理后）

```
~/corpus/research archive (old path)/    约 13M + 2,266 个正文文件
├── HANDOFF.md                ← 你正在读的
├── aggregate/                13M  ⭐ 主入口
│   ├── README.md               1.9K  目录说明（v1+v2 合并）
│   ├── aggregate-summary.json  728B  总量统计
│   ├── all-articles-manifest.csv  3.3M  ⭐ 6,044 条全量元数据
│   ├── all-articles-unified.json  6.8M  同上 JSON 版
│   ├── reading-priority-list.csv  448K  ⭐ 1,456 高信号已排序
│   ├── reading-by-topic.csv     950K  按主题组织
│   └── high-signal-reading-list.json  1.8M  1,456 高信号 JSON
│
├── out/                     约 20-25M（2,266 个 a-*.md + 2 个笔记）
│   ├── a-*.md × 2,266        ⭐ 唯一本地正文（V2 阶段下载）
│   ├── SYNTHESIS.md            23K  ⭐ V2 自我总结（重要！）
│   └── IMPROVEMENTS.md         26K  ⭐ V2 改进日志（方法论）
```

**已删除的临时文件**（不需要再找）：`state.json` (31M), `CONTENT-INDEX.json`, `CONTENT-MAP.csv`, `INDEX.md`, `RUN-LOG.txt(.1)`, 6 个 `auto-runner*.py`, 6 个 `smoke-test*.py`, `seeds.txt`, `run_two_bursts.sh`

---

## 3. 三个核心入口（按重要性）

### ⭐ `aggregate/reading-priority-list.csv`（**第一个打开**）

- 1,456 条记录，已按 `(tier, -signal, -body)` 排序
- 字段：`priority, tier, session, signal, q, body, source, topics, title, url, path`
- **`path` 字段是绝对路径** — 指向 `out/a-*.md`，可直接用这个关联到本地正文
- **Tier 1 前 30 条** = 黄金起点（Pentagram / AIGA / Typographica）
- 1 = 行号（CSV 标准）

### ⭐ `out/SYNTHESIS.md`

- V2 阶段 16 轮 cycle 的**自我总结**
- 含 Top 50 文章、Cluster 分析、Top 设计师/字体/颜色
- **让你快速理解 corpus 整体地形**，不用一篇篇去读

### ⭐ `out/IMPROVEMENTS.md`

- V2 阶段每轮 cycle 的**方法论日志**
- 记录了：黑名单域名（不能爬）、低信号词表、字体词表演化、国家覆盖
- **避免你重蹈覆辙** — 别再爬 `www.smashingmagazine.com` / `typographica.org` / 各种 wiki 已删的小语种

---

## 4. 数据来源（v1 + v2）

| Session | 策略 | 唯一 URL | 高信号 | 本地正文 |
|---------|------|----------|--------|----------|
| **v1-PROMPT-EXPLORE** | Internet Archive 偏多，历史快照 | 4,514 | 515 (DESIGN, sig≥6) | ❌ **无**（只有 metadata）|
| **v2-overnight** | 当代设计刊物 + 21 国 wiki | 1,530 | 333 (sig≥6) | ✅ 2,266 个 a-*.md |
| **合并** | 去重 | 6,023 | 1,456 | — |

**重要差异**：
- V1 没下载正文（archive.org 内容仅 metadata）→ 想读 V1 内容必须重新爬
- V2 有正文，但只有 2,266 篇 < V2 实际 1,530 的两倍（同一个 URL 可能在不同 cycle 抓了不同长度的快照）
- 6,044 是合并去重前的总数，6,023 是去重后

---

## 5. a-*.md 命名规则

```
a-{cycle号}-{时间戳}-q{质量分}-{标题slug}.md
```

示例：`a-c2-20260603-095038-q96-the-11-types-of-trendy-graphic-design-paul-rand-ha.md`
- `c2` = cycle 2 抓的
- `q96` = 质量分 0.96
- cycle 越大越新

文件大小：4K-28K 不等（V2 body 限制 8000 字符，V1 限制 4000 字符）

---

## 6. 关键字段速查

`reading-priority-list.csv` 字段含义：

| 字段 | 含义 | 取值范围 |
|------|------|----------|
| `tier` | 来源等级 | 1=curated 设计刊物 > 2=wiki/archive > 3=科学/新闻 > 4=其他语种 wiki > 5=其他 |
| `signal` | 信号分 | 1-9，≥6 是高信号 |
| `q` | 质量分 | 0-1 |
| `body` | body 字符数 | 通常 4000 或 8000 |
| `topics` | 主题分类 | `\|` 分隔：Typography / Color / AI Critique / Layout & Grid / Brutalist / etc. |
| `path` | 本地正文路径 | 绝对路径，V1 大多无效，V2 大多有效 |

---

## 7. 接手后的推荐路径

### 路径 A：先建立全景（30 分钟）

1. 打开 `aggregate/aggregate-summary.json` — 看总量
2. 打开 `out/SYNTHESIS.md` — 读 Top 10 设计师/字体/颜色 + Cluster 分析
3. 打开 `aggregate/reading-priority-list.csv`，按 tier 排序
4. **理解 corpus 在说什么** — 不用读任何正文

### 路径 B：真开始读（看时间）

1. 拿 `reading-priority-list.csv` 的前 30 条（全是 Tier 1 + sig 9）
2. 每条用 `path` 字段读 `out/a-*.md`
3. 同时跑分析（关键词、引用、设计师名）— 在 a-*.md 上做，不是重新爬

### 路径 C：补 V1 缺口（如果你觉得 V1 重要）

1. V1 的 4,514 条 URL 在 `aggregate/...` 里
2. **没下载本地**，需要重新爬（V1 已删，参考 `out/IMPROVEMENTS.md` 的黑名单避免重复踩坑）
3. 写入新的 `out/a-v1-*.md` 文件，遵循同样的命名规则

### 路径 D：基于 SYNTHESIS 写产出

1. 读 `out/SYNTHESIS.md` 找有信号的 cluster
2. 拉对应 a-*.md 出来精读
3. **真正产出**（综述 / 设计语言提炼 / anti-AI 系统设计）— 这是上次的痛点：**采集够了，消化没开始**

---

## 8. 已知坑（**必读**）

1. **V1 没下载本地** — `reading-priority-list.csv` 里 `path` 字段如果指向 V1 文章，**该文件不存在**。需要重新爬
2. **SYNTHESIS 是 V2 视角** — 不含 V1 数据，不要误以为是全量分析
3. **IMPROVEMENTS 是过程日志** — 不需要逐条读，知道"它记录了黑名单域名 + 关键词演化"就行
4. **Tier 5 的 path 大多无效** — 来源杂、质量低，谨慎投入时间
5. **不要重新跑采集脚本** — 脚本全删了（`auto-runner-*.py` 6 个），且 corpus 已经定型；如需新数据，另起任务
6. **aggregate csv 里 `body` 字段是字符数，不是正文** — 正文在 `out/a-*.md`
7. **a-*.md 不是 markdown 渲染的** — 是 plain text + frontmatter，需要自己解析

---

## 9. 黑名单域名（不要爬）

来自 `IMPROVEMENTS.md` 的累积黑名单，**接手时直接复用**：

```
www.smashingmagazine.com   typographica.org   twitter.com
www.facebook.com           www.instagram.com   www.youtube.com
www.google.com             www.linkedin.com    www.fastcompany.com
www.creativebloq.com       www.are.na          typographica.org
books.google.com           doi.org             www.jstor.org
search.worldcat.org        api.semanticscholar.org
assets.fontsinuse.com      vanilla.futurecdn.net
m3.material.io             www.thoughtco.com
bg/mk/ru/he/kk/hi/pa.wikipedia.org   (小语种 wiki 信号低)
```

完整黑名单见 `IMPROVEMENTS.md` Cycle 11（约 80 个域名）。

---

## 10. 文件绝对路径速查

```
/Users/nothingfear/corpus/research archive (old path)/HANDOFF.md                              ← 本文件
/Users/nothingfear/corpus-metadata/README.md
/Users/nothingfear/corpus-metadata/aggregate-summary.json
/Users/nothingfear/corpus-metadata/reading-priority-list.csv   ⭐
/Users/nothingfear/corpus-metadata/reading-by-topic.csv
/Users/nothingfear/corpus-metadata/all-articles-manifest.csv
/Users/nothingfear/corpus-metadata/high-signal-reading-list.json
/Users/nothingfear/../corpus/articles/SYNTHESIS.md                       ⭐
/Users/nothingfear/../corpus/articles/IMPROVEMENTS.md                    ⭐
/Users/nothingfear/../corpus/articles/a-*.md                             ⭐ 2,266 个正文
```

---

## 11. 项目历史背景（一句话版）

- **起因**：用户想系统学"AI 默认设计 vs 真实设计"区别，反 cyber-slop
- **方法**：用 overnight runner 自动爬 → 评分 → 分类（v1-v7 迭代）
- **当前**：corpus 沉淀完毕，6,044 条 metadata + 2,266 篇本地正文
- **未做**：真正的消化、产出、验证 "我懂了"

---

**最后一句**：

> corpus 本身是好的。**缺的不是数据，是产出**。
> 接手时，**先读完 SYNTHESIS.md 决定方向**（10 分钟），再决定读哪些 a-*.md。

— 上一个 agent 留
