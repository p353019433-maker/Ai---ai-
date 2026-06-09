# Corpus Research Notes

这个文件是旧 corpus 说明的当前位置版本。原始文章正文已经在蒸馏成批次笔记和综合文档后删除，当前仓库保留的是 metadata、处理账本、批次笔记和综合结果。

## 当前入口

- [`README.md`](README.md)：研究层总入口。
- [`corpus-handoff.md`](corpus-handoff.md)：原 corpus 接手说明的迁移版本。
- [`corpus-synthesis.md`](corpus-synthesis.md)：V2 阶段综合总结。
- [`corpus-improvements.md`](corpus-improvements.md)：采集过程和方法论改进日志。
- [`processed-manifest.csv`](processed-manifest.csv)：1456 条 priority 的处理账本。
- [`corpus-metadata/aggregate-summary.json`](corpus-metadata/aggregate-summary.json)：总量统计。
- [`corpus-metadata/reading-priority-list.csv`](corpus-metadata/reading-priority-list.csv)：高信号文章阅读优先级，按 tier、signal、body 排序。
- [`corpus-metadata/reading-by-topic.csv`](corpus-metadata/reading-by-topic.csv)：按主题组织的阅读清单。
- [`corpus-metadata/all-articles-manifest.csv`](corpus-metadata/all-articles-manifest.csv)：全量 metadata CSV。
- [`corpus-metadata/all-articles-unified.json`](corpus-metadata/all-articles-unified.json)：全量 metadata JSON。
- [`batches/`](batches/)：逐批学习笔记。

## 数据规模

- 合并前记录：6044
- 唯一 URL：6023
- high-signal：1456
- 本地原始正文：已删除

## 证据边界

如果要追溯来源，从 [`corpus-metadata/reading-priority-list.csv`](corpus-metadata/reading-priority-list.csv) 找 title、url、source，再看 [`batches/`](batches/) 和 [`processed-manifest.csv`](processed-manifest.csv) 中的处理状态。

重要细节：JSON metadata 仍保留 `body_head` / `body_tail` 片段，用于审计采集质量和来源上下文。它们不是完整正文库。
