# Article Bodies — 文章正文

这个目录保存 corpus 采集到的 2266 篇本地正文，按质量分 3 层。

## 质量分层

| 目录 | 文章数 | q 区间 |
|---|---:|---|
| [`tier-1-q90plus/`](tier-1-q90plus/) | 966 | q90–100（含 391 篇满分）|
| [`tier-2-q80-89/`](tier-2-q80-89/) | 796 | q80–89 |
| [`tier-3-q70-79/`](tier-3-q70-79/) | 504 | q70–79 |

## 相关报告

- [`../reports/SYNTHESIS.md`](../reports/SYNTHESIS.md)：V2 阶段 16 轮采集后的综合总结。
- [`../reports/IMPROVEMENTS.md`](../reports/IMPROVEMENTS.md)：采集过程日志、黑名单域名、关键词演化、方法论反思。

## 命名格式

`a-*.md` 文件是文章正文，命名格式大致为：

```text
a-{cycle}-{timestamp}-q{quality}-{slug}.md
```

含义：

- `cycle`：采集轮次（`c1`–`c16`，部分早期文件无此段）。
- `timestamp`：采集时间。
- `q`：质量分（决定所在的 tier 目录）。
- `slug`：来源标题简化名。

这些正文是原始 corpus 的主体。不要直接按文件名逐个读，优先从 [`../index/reading-priority-list.csv`](../index/reading-priority-list.csv) 或 [`../index/reading-by-topic.csv`](../index/reading-by-topic.csv) 进入。
