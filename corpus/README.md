# Corpus — 原始语料库

这是原始语料库目录（原 `overnight-ai-aesthetic`）。它保存了自动采集、评分、聚合后的设计美学 corpus，以及 2266 篇本地正文。

> 消化后的成品知识库在 [`../knowledge/`](../knowledge/)。

## 目录结构

| 路径 | 作用 |
|---|---|
| [`reports/`](reports/) | 综合总结、方法论日志、接手说明 |
| [`index/`](index/) | 聚合后的全量 metadata、阅读优先级、主题阅读清单 |
| [`articles/`](articles/) | 2266 篇本地正文，按质量分 3 层 |

### articles/ 质量分层

| 目录 | 文章数 | q 区间 |
|---|---:|---|
| [`articles/tier-1-q90plus/`](articles/tier-1-q90plus/) | 966 | q90–100（含 391 篇满分）|
| [`articles/tier-2-q80-89/`](articles/tier-2-q80-89/) | 796 | q80–89 |
| [`articles/tier-3-q70-79/`](articles/tier-3-q70-79/) | 504 | q70–79 |

## 关键入口

- [`reports/HANDOFF.md`](reports/HANDOFF.md)：接手说明，解释 corpus 的来源、状态、坑和推荐使用路径。
- [`reports/SYNTHESIS.md`](reports/SYNTHESIS.md)：V2 阶段 16 轮采集综合总结。
- [`reports/IMPROVEMENTS.md`](reports/IMPROVEMENTS.md)：采集过程和方法论改进日志。
- [`index/aggregate-summary.json`](index/aggregate-summary.json)：总量统计。
- [`index/reading-priority-list.csv`](index/reading-priority-list.csv)：高信号文章阅读优先级，按 tier、signal、body 排序。
- [`index/reading-by-topic.csv`](index/reading-by-topic.csv)：按主题组织的阅读清单。
- [`index/all-articles-manifest.csv`](index/all-articles-manifest.csv)：全量 metadata CSV。
- [`index/all-articles-unified.json`](index/all-articles-unified.json)：全量 metadata JSON。

## 数据规模

- 合并前记录：6044
- 唯一 URL：6023
- high-signal：1456
- 本地正文：2266

## 使用方式

先读 [`reports/HANDOFF.md`](reports/HANDOFF.md)，再看 [`reports/SYNTHESIS.md`](reports/SYNTHESIS.md) 建立全景。

如果要精读文章，从 [`index/reading-priority-list.csv`](index/reading-priority-list.csv) 选目标，再到 [`articles/`](articles/) 对应质量层下打开正文。

## 待收拾

- `index/` 下的 CSV/JSON 里 `path` 列仍是原作者机器的绝对路径（`/Users/nothingfear/.../out/...`），需改写为指向 `articles/tier-*/` 的仓库相对路径。
- 采集已经足够，真正缺的是精读、消化、综合。
