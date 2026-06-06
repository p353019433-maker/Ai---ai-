# AI Aesthetic Learning Archive

这个仓库保存两组 agent 的设计美学学习成果，全部以普通文件提交，没有打包、没有压缩、没有删除原始内容。

## 内容总览

| 目录 | 文件数 | 体量 | 作用 |
|---|---:|---:|---|
| [`overnight-ai-aesthetic/`](overnight-ai-aesthetic/) | 2276 | 约 35MB | 原始语料库：采集、评分、聚合、文章正文 |
| [`claude-design-memory/`](claude-design-memory/) | 63 | 约 856KB | 整理后的设计知识库：总纲、专题手册、哲学与案例 |

## 两套成果的关系

`overnight-ai-aesthetic/` 是 corpus：它负责把大量设计文章、wiki、设计刊物、历史材料抓下来，并按质量和主题做基础分类。

`claude-design-memory/` 是 memory：它负责把前期学习结果整理成可读、可检索、可复用的设计知识手册。

简单说：

- 想看原始材料、文章正文、来源列表：读 [`overnight-ai-aesthetic/`](overnight-ai-aesthetic/)。
- 想直接应用设计判断、反 AI 套路、UI/UX/字体/色彩/设计系统知识：读 [`claude-design-memory/`](claude-design-memory/)。

## 推荐阅读路径

1. 先读 [`claude-design-memory/design-decision-handbook.md`](claude-design-memory/design-decision-handbook.md)。
2. 再读 [`claude-design-memory/design-philosophy-master.md`](claude-design-memory/design-philosophy-master.md)。
3. 需要完整总纲时读 [`claude-design-memory/design-ultimate-handbook.md`](claude-design-memory/design-ultimate-handbook.md)。
4. 要回到原始 corpus 时读 [`overnight-ai-aesthetic/HANDOFF.md`](overnight-ai-aesthetic/HANDOFF.md)。
5. 真正精读文章时，从 [`overnight-ai-aesthetic/aggregate/reading-priority-list.csv`](overnight-ai-aesthetic/aggregate/reading-priority-list.csv) 选路径，再打开 [`overnight-ai-aesthetic/out/`](overnight-ai-aesthetic/out/) 下对应正文。

## 当前状态

这份仓库是“学习成果归档 + 可读入口整理”，不是最终教材。最有价值的下一步不是继续采集，而是把两边合并消化成一套更短、更可执行的设计审美操作系统。
