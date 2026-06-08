# AI Aesthetic Learning Archive

这个仓库保存两组 agent 的设计美学学习成果，全部以普通文件提交，没有打包、没有压缩、没有删除原始内容。

仓库分两侧：**`knowledge/`（成品）** 与 **`corpus/`（原料）**。

## 内容总览

| 目录 | 文件数 | 体量 | 作用 |
|---|---:|---:|---|
| [`knowledge/`](knowledge/) | 64 | 约 856KB | 整理后的设计知识库：总纲、专题手册、哲学与案例（按 10 个主题分目录）|
| [`corpus/`](corpus/) | 2276 | 约 35MB | 原始语料库：采集、评分、聚合、文章正文（按 3 个质量层分目录）|

## 两套成果的关系

`corpus/`（原 `overnight-ai-aesthetic`）是 **corpus**：把大量设计文章、wiki、设计刊物、历史材料抓下来，按质量和主题做基础分类。

`knowledge/`（原 `claude-design-memory`）是 **memory**：把前期学习结果整理成可读、可检索、可复用的设计知识手册。

简单说：

- 想直接应用设计判断、反 AI 套路、UI/UX/字体/色彩/设计系统知识：读 [`knowledge/`](knowledge/)。
- 想看原始材料、文章正文、来源列表：读 [`corpus/`](corpus/)。

## 目录骨架

```
knowledge/                 ← 成品知识库（10 个主题目录）
├── 00-handbooks/          ← 3 大总纲
├── 01-ai-era/  02-tooling/  03-process/
├── 04-design-systems/  05-visual-craft/  06-platforms/
├── 07-philosophy/  08-context/  09-meta/
└── MEMORY.md              ← 完整逐份索引

corpus/                    ← 原始语料
├── reports/              ← SYNTHESIS / IMPROVEMENTS / HANDOFF
├── index/                ← 聚合元数据、阅读优先级、主题清单
└── articles/             ← 2266 篇正文，按质量分层
    ├── tier-1-q90plus/   (966)
    ├── tier-2-q80-89/    (796)
    └── tier-3-q70-79/    (504)
```

## 推荐阅读路径

1. 先读 [`knowledge/00-handbooks/design-decision-handbook.md`](knowledge/00-handbooks/design-decision-handbook.md)。
2. 再读 [`knowledge/00-handbooks/design-philosophy-master.md`](knowledge/00-handbooks/design-philosophy-master.md)。
3. 需要完整总纲时读 [`knowledge/00-handbooks/design-ultimate-handbook.md`](knowledge/00-handbooks/design-ultimate-handbook.md)。
4. 要回到原始 corpus 时读 [`corpus/reports/HANDOFF.md`](corpus/reports/HANDOFF.md) 与 [`corpus/reports/SYNTHESIS.md`](corpus/reports/SYNTHESIS.md)。
5. 真正精读文章时，从 [`corpus/index/reading-priority-list.csv`](corpus/index/reading-priority-list.csv) 选目标，再到 [`corpus/articles/`](corpus/articles/) 对应质量层下打开正文。

## 当前状态

这份仓库刚完成一次**结构重构**（2026-06）：顶层改为 `knowledge/` + `corpus/`，知识库按主题分目录，语料按质量分层。

下一步是"收拾内容"——尚待处理项见各目录 README，主要包括：
- 校准各索引文件里对不齐的文件计数与失效的跨文档链接。
- `corpus/index/` 里的 CSV/JSON 仍是原作者机器的绝对路径，需改写为仓库相对路径并对应到新的 tier 目录。
- 把两侧合并消化成一套更短、更可执行的设计审美操作系统。
