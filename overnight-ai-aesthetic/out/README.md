# Article Bodies

这个目录保存 `overnight-ai-aesthetic` 采集到的本地正文。

## 重要文件

- [`SYNTHESIS.md`](SYNTHESIS.md)：V2 阶段 16 轮采集后的综合总结。
- [`IMPROVEMENTS.md`](IMPROVEMENTS.md)：采集过程日志、黑名单域名、关键词演化、方法论反思。

## 正文文件

`a-*.md` 文件是文章正文，命名格式大致为：

```text
a-{cycle}-{timestamp}-q{quality}-{slug}.md
```

含义：

- `cycle`：采集轮次。
- `timestamp`：采集时间。
- `q`：质量分。
- `slug`：来源标题简化名。

这些正文是原始 corpus 的主体。不要直接按文件名逐个读，优先从 [`../aggregate/reading-priority-list.csv`](../aggregate/reading-priority-list.csv) 或 [`../aggregate/reading-by-topic.csv`](../aggregate/reading-by-topic.csv) 进入。
