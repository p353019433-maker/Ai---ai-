# AI Aesthetic Design Knowledge Base

这个仓库现在只保留三层结构：

```text
docs/      可直接阅读和使用的设计知识库
research/ 研究过程、批次笔记、manifest、metadata、方法论日志
corpus/   原始文章正文证据库
```

目标：去掉旧的多套目录名，把“成品 / 过程 / 原料”分清楚。

## 先读什么

如果你只是想用这套知识（docs/ 已于 2026-06 蒸馏为 7 份）：

1. [`docs/README.md`](docs/README.md) — 入口与快速路由
2. [`docs/00-core.md`](docs/00-core.md) — 核心判断：坏 AI 设计是”失忆”的设计 + 十原则 + 冲突取舍
3. [`docs/01-craft.md`](docs/01-craft.md) — 工艺数值规则（字体/色彩/布局/组件/动效）
4. [`docs/06-practice.md`](docs/06-practice.md) — 反 slop 清单、prompt 模板、验证协议

如果你要审计研究过程：

- [`research/README.md`](research/README.md)
- [`research/processed-manifest.csv`](research/processed-manifest.csv)
- [`research/batches/`](research/batches/)
- [`research/corpus-metadata/reading-priority-list.csv`](research/corpus-metadata/reading-priority-list.csv)

如果你要追溯原文证据（原始正文已蒸馏后删除，见下）：

- [`corpus/README.md`](corpus/README.md) — 说明正文为何删除、证据现在去哪找
- [`research/batches/`](research/batches/) — 读完高信号文章后的蒸馏笔记
- [`research/corpus-metadata/reading-priority-list.csv`](research/corpus-metadata/reading-priority-list.csv) — 文章清单与来源 URL

## 当前诚实标签

这是一个 **可审计的设计研究档案 + 应用综合层**，还不是已经被真实项目充分验证过的设计操作系统。

下一步不该默认继续采集，而是选一个真实项目，把原则用上，记录哪里错、哪里冲突、哪里被用户反馈推翻。

## 重构说明

旧目录已经合并：

- `claude-design-memory/` → `docs/`
- `learning-notes/` → `docs/` + `research/batches/` + `research/processed-manifest.csv`
- `overnight-ai-aesthetic/aggregate/` → `research/corpus-metadata/`
- `overnight-ai-aesthetic/out/a-*.md` → 蒸馏进 `research/batches/` 后删除（2266 篇原始正文不再保留）
- `overnight-ai-aesthetic/out/SYNTHESIS.md` → `research/corpus-synthesis.md`
- `overnight-ai-aesthetic/out/IMPROVEMENTS.md` → `research/corpus-improvements.md`

知识与综合内容没有语义删除，只是把复杂结构压平；原始文章正文则在蒸馏成批次笔记后整体移除，元数据 CSV 的 `path` 列已相应清空。
