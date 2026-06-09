# Research — Process and Audit Layer

这里放研究过程，不是应用手册。

## 入口

- [`processed-manifest.csv`](processed-manifest.csv)：1456 条 priority 的处理账本，区分 deep read / duplicate / reference / missing source 等。
- [`batches/`](batches/)：batch-001 到 batch-025 的逐批学习笔记。
- [`learning-notes-index.md`](learning-notes-index.md)：旧 learning-notes 索引。
- [`corpus-synthesis.md`](corpus-synthesis.md)：原 corpus 的 V2 综合总结。
- [`corpus-improvements.md`](corpus-improvements.md)：采集过程和方法论改进日志。
- [`corpus-handoff.md`](corpus-handoff.md)：原 corpus 接手说明。
- [`corpus-metadata/`](corpus-metadata/)：全量 metadata、priority list、topic list。

## 关键 metadata

- [`corpus-metadata/reading-priority-list.csv`](corpus-metadata/reading-priority-list.csv)：1456 条高信号阅读优先级。
- [`corpus-metadata/reading-by-topic.csv`](corpus-metadata/reading-by-topic.csv)：按主题组织的阅读清单。
- [`corpus-metadata/all-articles-manifest.csv`](corpus-metadata/all-articles-manifest.csv)：全量文章 metadata。
- [`corpus-metadata/all-articles-unified.json`](corpus-metadata/all-articles-unified.json)：全量 metadata JSON。

## 注意

这个目录的作用是可审计，不是好读。想直接应用设计判断请看 [`../docs/`](../docs/)。

JSON metadata files still retain `body_head` and `body_tail` audit excerpts for
source-tracing context. These excerpts are not full article bodies.
