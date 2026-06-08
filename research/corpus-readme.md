# Overnight AI Aesthetic Corpus

这是原始语料库目录。它保存了自动采集、评分、聚合后的设计美学 corpus，以及 2266 篇本地正文。

## 目录结构

| 路径 | 作用 |
|---|---|
| [`HANDOFF.md`](HANDOFF.md) | 接手说明，解释 corpus 的来源、状态、坑和推荐使用路径 |
| [`aggregate/`](aggregate/) | 聚合后的全量 metadata、阅读优先级、主题阅读清单 |
| [`out/`](out/) | 本地正文、V2 阶段总结、方法论日志 |

## 关键入口

- [`aggregate/aggregate-summary.json`](aggregate/aggregate-summary.json)：总量统计。
- [`aggregate/reading-priority-list.csv`](aggregate/reading-priority-list.csv)：高信号文章阅读优先级，按 tier、signal、body 排序。
- [`aggregate/reading-by-topic.csv`](aggregate/reading-by-topic.csv)：按主题组织的阅读清单。
- [`aggregate/all-articles-manifest.csv`](aggregate/all-articles-manifest.csv)：全量 metadata CSV。
- [`aggregate/all-articles-unified.json`](aggregate/all-articles-unified.json)：全量 metadata JSON。
- [`out/SYNTHESIS.md`](out/SYNTHESIS.md)：V2 阶段综合总结。
- [`out/IMPROVEMENTS.md`](out/IMPROVEMENTS.md)：采集过程和方法论改进日志。

## 数据规模

- 合并前记录：6044
- 唯一 URL：6023
- high-signal：1456
- 本地正文：2266

## 使用方式

先读 [`HANDOFF.md`](HANDOFF.md)，再看 [`out/SYNTHESIS.md`](out/SYNTHESIS.md) 建立全景。

如果要精读文章，从 [`aggregate/reading-priority-list.csv`](aggregate/reading-priority-list.csv) 选目标，再打开其中 `path` 对应的 [`out/`](out/) 正文。

这套 corpus 的状态是：采集已经足够，真正缺的是精读、消化、综合。
