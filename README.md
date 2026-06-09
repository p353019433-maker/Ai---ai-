# AI Aesthetic Design Knowledge Base

这个仓库现在只保留三层结构：

```text
docs/      可直接阅读和使用的设计知识库
research/ 研究过程、批次笔记、manifest、metadata、方法论日志
corpus/   原始正文移除后的证据路由说明
```

目标：去掉旧的多套目录名，把“成品 / 过程 / 原料”分清楚。

## 先读什么

如果你只是想用这套知识：

1. [`docs/README.md`](docs/README.md) — 可读知识库入口
2. [`docs/design-decision-handbook.md`](docs/design-decision-handbook.md) — 按问题路由到具体文件
3. [`docs/APPLIED-DESIGN-JUDGMENT.md`](docs/APPLIED-DESIGN-JUDGMENT.md) — 反 AI-slop 的应用判断
4. [`docs/LESS-AMNESIAC-DESIGN.md`](docs/LESS-AMNESIAC-DESIGN.md) — 核心洞察：坏 AI 设计是“失忆”的设计
5. [`docs/DESIGN-LAB-PROTOCOL.md`](docs/DESIGN-LAB-PROTOCOL.md) — 下一阶段：真实项目验证协议

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

## 维护检查

```bash
python3 scripts/check-docs.py
```

这个检查会验证 Markdown 本地链接、核心 handover 统计和旧路径引用。JSON metadata 仍保留 `body_head` / `body_tail` 片段用于审计上下文；它们不是完整正文库。
