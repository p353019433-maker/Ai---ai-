# Corpus — Raw Article Evidence

这里保存原始文章正文证据库。

- [`articles/`](articles/)：2266 篇本地正文，文件名保留原采集命名。

配套索引在 [`../research/corpus-metadata/`](../research/corpus-metadata/)：

- `reading-priority-list.csv`
- `reading-by-topic.csv`
- `all-articles-manifest.csv`
- `all-articles-unified.json`

如果要从 priority 找原文，先读 `research/corpus-metadata/reading-priority-list.csv`。其中旧 `path` 字段可能仍指向历史绝对路径；当前仓库内正文统一在 `corpus/articles/`，用文件名对应。
