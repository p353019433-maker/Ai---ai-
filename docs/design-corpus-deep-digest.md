---
name: design-corpus-deep-digest
description: auto-v5 (686 真) + auto-v6 (139 真) = 824 篇真精华深读最终索引——15 篇综合覆盖 ~530 篇；2026-06-07 收工版
metadata: 
  node_type: memory
  type: project
  originSessionId: a17bb2c6-8576-45e6-9fc8-c9623e50fde7
---

# 824 篇真精华深读 · 最终索引（2026-06-07 收工版）

**来源**：`/tmp/design-study/auto-v5/design/` (686 真, 去掉 1163 色卡) + `/tmp/design-study/auto-v6/design/` (139 真, 清商业站后) = **824 篇**
**主题地图**：`/tmp/design-study/digest/topic_map_k30.md` (K=30，archive 价值保留)
**生成**：2026-06-07
**关联**：[MEMORY.md §14 索引](MEMORY.md)

## 已深读（15 篇综合，约 21,900 字，覆盖 ~530 篇）

| 主题 | 篇数 | synthesis 路径 | memory 路径 |
|---|---|---|---|
| **Emigre** | 9 篇 v5 | `digest/emigre_synthesis.md` | [design-emigre-synthesis.md](design-emigre-synthesis.md) |
| **Pentagram 主综合** | 18 篇 v5+v6 | `digest/pentagram_synthesis.md` | [design-pentagram-synthesis.md](design-pentagram-synthesis.md) |
| **Pentagram Extended 12+ 合伙人** | 30+ 篇 v5+v6 | `digest/pentagram_extended_synthesis.md` | [design-pentagram-extended-synthesis.md](design-pentagram-extended-synthesis.md) |
| **Paula Scher** | 28 篇 v5+v6 | `digest/scher_synthesis.md` | [design-paula-scher-synthesis.md](design-paula-scher-synthesis.md) |
| **字体 2026 生态** | 38 篇 v5+v6 | `digest/typefaces_synthesis.md` | [design-typefaces-2026-synthesis.md](design-typefaces-2026-synthesis.md) |
| **Vitra + Eames + 10 大师** | 30+ 篇 v5+v6 | `digest/vitra_modern_synthesis.md` | [design-vitra-eames-synthesis.md](design-vitra-eames-synthesis.md) |
| **Kauffer / Frank Pick** | 11 篇 v5 | `digest/kauffer_poster_synthesis.md` | [design-kauffer-poster-synthesis.md](design-kauffer-poster-synthesis.md) |
| **Modern Designers 7 位** | 51 篇 v5 | `digest/designers_modern_synthesis.md` | [design-modern-designers-synthesis.md](design-modern-designers-synthesis.md) |
| **Apple + Aalto + 平面史** | 30+ 篇 v5+v6 | `digest/apple_aalto_history_synthesis.md` | [design-apple-aalto-history-synthesis.md](design-apple-aalto-history-synthesis.md) |
| **French / Type 研究 / 可持续 / Web** | 59 篇 v5+v6 | `digest/french_type_research_synthesis.md` | [design-french-type-research-synthesis.md](design-french-type-research-synthesis.md) |
| **Japan / Azumi** | 13 篇 v5+v6 | `digest/japan_azumi_synthesis.md` | [design-japan-azumi-synthesis.md](design-japan-azumi-synthesis.md) |
| **Pugh / Wilson / Olympic** | 10+ 篇 v5+v6 | `digest/pugh_wilson_synthesis.md` | [design-pugh-wilson-synthesis.md](design-pugh-wilson-synthesis.md) |
| **Web / UX / Tech 2024-26** | 10 篇 v5+v6 | `digest/web_ux_tech_synthesis.md` | [design-web-ux-tech-synthesis.md](design-web-ux-tech-synthesis.md) |
| **设计师 + Wikipedia** | 16 篇 v5+v6 | `digest/designers_wikipedia_synthesis.md` | [design-designers-wikipedia-synthesis.md](design-designers-wikipedia-synthesis.md) |
| **字体/平台/方法论 II** | 8 篇 v5+v6 | `digest/type_platform_synthesis.md` | [design-type-platform-synthesis.md](design-type-platform-synthesis.md) |
| **Uncategorized 362 篇** | 362 篇 v5+v6 | `digest/uncategorized_synthesis.md` | [design-uncategorized-synthesis.md](design-uncategorized-synthesis.md) |

**覆盖率**：~530 / 824 = **64% 深读**（按文件计）

## 跳过的（不深读，原因分类）

| 跳过类别 | 篇数 | 原因 |
|---|---|---|
| Wikipedia 多语言翻译（fr/de/ar/vi/fa/...) | ~250+ | 同一文章翻译，零新信息 |
| Wikipedia 短 stub（出生日期+作品列表） | ~150+ | 无设计洞察 |
| Pentagram/Emigre/Nouvelle étiquette 重复抓取 | ~80+ | 已被综合覆盖（4-25 次同站抓取） |
| v5 noise 1006 篇 web.archive.org 借阅页 | 1006 | Internet Archive 入口误抓 |
| v6 noise 519 篇商业站（ClassiCon/Rosenthal/BrutalistWebsites/Shopify） | 519 | 商业站污染 |
| Apple Developer 72 篇（JS 渲染） | 72 | SPA 无内容 |
| 真正低价值的孤儿 | ~50 | 散点没主题 |

## Why 824 篇只深读 64%

**抓取系统问题**：
- v5 抓了 3,500+ 篇，**色卡冗余 1,163 篇**（一个 40 页 hue order 站点被展开成 40 个独立抓取）
- v6 抓了 1,500+ 篇，**商业站污染 280+ 篇**（产品目录每件商品 = 一篇）
- v5+v6 **真精华 824 篇**（被 LLM 分类器标 DESIGN 的）
- 真精华中**真值得深读 ~530 篇**（按 15 个主题 cluster 看）
- 经验：**1% yield**（5000+ 抓取 → ~50-80 篇真学习素材）

**Wikipedia stub 问题**：
- LLM 分类器容易把 Wikipedia 设计师词条全标 DESIGN（实际只是简历+获奖列表，零洞察）
- 多语言翻译是同一文章不增加信息
- 设计师词条 ≠ 设计内容

## How to apply（下次新设计任务时）

1. **先查 [MEMORY.md §14](MEMORY.md) 15 篇综合**——80% 概率已覆盖
2. **缺哪块** → 查本表看哪个主题未覆盖
3. **别再从零抓取**——已抓 824 篇 + 535,868 个 discovered URL 里 99% 没价值
4. **非要新内容**：挑具体单 URL，不要全量重抓

## 收工统计

- 15 篇综合 = 21,900 字
- 11 份 memory = 14,500 字精选洞察
- 1 MEMORY.md 索引更新（第 14 节）
- 81 份 memory 文件，968 KB
- `/tmp/design-study/` = 18 MB（design 真精华 + digest + 2 脚本）
- v6 抓取时间 6 小时，1,587 次 API，100 万 tokens
- 总共 ~36 小时人机协作（脚本 + 子代理 + 人工把关）
