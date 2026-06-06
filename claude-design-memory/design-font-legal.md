---
name: design-font-legal
description: 字体授权 + 设计法律 + 合同 - SIL OFL / Adobe Fonts / Monotype / 商业字体 / 嵌入权 / 字体陷阱 / NDA 4 必写 / 设计合同 6 必写 / 版权归属 / 作品保护期
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5d5620e2-fe64-4257-9223-e9fdc60a418c
  addedDate: 2026-06-06
---

# 字体授权 + 设计法律 + 合同：执行手册

## 一句话总结
**字体授权是 99% 设计师忽视的合规陷阱——用错字体可能让公司赔 6 位数**。Inter/IBM Plex 用 SIL OFL 免费，但 Trajan Pro / Futura / Helvetica 商用要 Monotype 授权。**NDA 漏写"作品归属" = 客户说设计是他的**。设计合同 6 必写条款比字体选择还重要。

## 1. 字体授权 4 大类型（必懂）

### (1) SIL OFL（Open Font License）— 95% 设计师首选
- **完全免费商用**——> 永久、全球、任何用途
- **可嵌入**——> web、app、PDF、打印
- **可修改**——> 可裁切子集、可加 hinting
- **唯一义务**：不能单独卖字体本身（如 "OFL 字体打包卖 $50" 违规）
- **代表字体**：
  - **Inter**（Rasmus Andersson，前 GitHub）
  - **IBM Plex**（IBM 免费 + 开源）
  - **JetBrains Mono**（JetBrains）
  - **Source Sans / Source Serif**（Adobe 开源）
  - **Noto Sans**（Google 覆盖 150+ 语言）
  - **Fira Code**（Mozilla）
  - **Recursive**（Arrow Type）
  - **Manrope** / **Plus Jakarta Sans** / **Outfit** 等新派

**学到的**：选字体先看 SIL OFL，免去一切烦恼

### (2) Adobe Fonts（Typekit）— 设计行业标准
- **Creative Cloud 订阅包含**——> 月费 $54.99 起
- **商用授权**——> 网页、印刷、视频、嵌入式
- **不能用 web 嵌入卖给客户**（如果客户没 Adobe CC）
- **代表字体**：
  - **Proxima Nova**（Mark Simonson）
  - **Source Han Sans**（Adobe + Google + 合作，免费但有特殊 license）
  - **Myriad Pro**（Adobe）
  - **Acumin Pro**（Adobe）
  - **Minion Pro** / **Myriad Pro**（Adobe 经典）

**学到的**：Adobe CC 订阅 = 1000+ 字体商用授权，**但只是订阅期间**——> 取消订阅后字体必须从网站移除

### (3) Monotype / Linotype — 商业字体巨头
- **单字体 / 字体家族授权**——> 按年 / 永久
- **价格**：单字体 $30-$500，家族 $100-$5000+
- **必须明确**：
  - Desktop license（桌面应用 = Sketch / Figma 渲染）
  - Web license（@font-face 嵌入 = 按月活 / 域名）
  - App license（嵌入 iOS / Android = 按下载量）
  - Broadcast / Film license（视频字幕）
- **代表字体**：
  - **Helvetica / Helvetica Neue**（Linotype，商用 $300+）
  - **Futura**（Monotype，商用 $150+）
  - **Trajan Pro**（Monotype，商用 $200+）
  - **Avenir**（Monotype）
  - **Frutiger**（Linotype）
  - **Times New Roman**（Monotype，多数系统已预装）
  - **Arial**（Monotype，系统字体免费但商用嵌入仍需 license）

**学到的**：**系统预装的字体商用嵌入仍可能需 license**——> Arial 在 macOS 预装，但 web 嵌入需 Monotype 授权

### (4) 独立设计师字体（Foundry）— 高端定制
- **付费单字体 / 家族**——> 一次性或订阅
- **代表 foundry**：
  - **Klim Type Foundry**（Söhne / Söhne Mono / National 2 / Etion）
  - **Commercial Type**（Graphik / Atlas / Druk）
  - **Production Type**（Pangram Sans / Mirador）
  - **Type Together**（Cartograph / Adelle）
  - **Grilli Type**（GT Sectra / GT Pressura / GT America）
  - **ABC Dinamo**（ABC Diatype / Repro / Monument Extended）
- **价格**：单字体 $50-$200，家族 $200-$2000+

**学到的**：**高端字体不便宜**——> Söhne 完整家族商用约 $2000-$5000。但品牌感是免费的字体给不了的

## 2. 7 个字体授权陷阱（必查）

### 陷阱 1: 个人免费 vs 商用免费
- **Font Squirrel** 标 "Free for commercial use"——> 真的吗？
- 99% 真的，但**少数字体 OFL 协议禁止单独销售**——> 嵌入到产品卖没事
- **永远检查 license 文件**（`OFL.txt` / `License.txt`）

### 陷阱 2: 桌面授权 vs Web 授权
- **Desktop license**：用于 Sketch / Figma / Photoshop
- **Web license**：用于 @font-face 嵌入网站
- **两者通常分开买**——> Monotype / Klim 都这样
- **陷阱**：只买桌面没买 web = 设计师能设计，但网站不能上线

### 陷阱 3: 单域名 vs 多域名
- **Web license 通常按域名**——> example.com 一个 license
- **陷阱**：客户有 5 个子域名 = 5 个 license 或 multi-domain license
- **Always check**：是 `www.example.com` 一个还是 `*.example.com` 通配

### 陷阱 4: 按月活收费
- 一些字体厂按网站月活分级：1 万 / 10 万 / 100 万 / 无限
- **陷阱**：100 万月活需 enterprise license，单价 $5000+
- **Always check**：你网站 100 万 UV 用什么 tier

### 陷阱 5: App 内嵌
- 嵌入 iOS / Android app = App license
- **通常按下载量分级**
- **陷阱**：游戏内嵌 1000 万下载量 = 字体厂可能收你 $50,000+
- **Always check**：app 嵌入单独 license

### 陷阱 6: 修改和重新分发
- OFL 允许修改、嵌入、重新分发
- Monotype / Klim 多数**不允许修改**——> 改字距 / 改轮廓违反 license
- **Always check**：你能"裁切子集"吗？能"加 hinting"吗？

### 陷阱 7: Logo 字体使用
- **很多字体 license 禁止用于 logo**——> 即使是 OFL 字体
- 一些 foundry 单独卖 "logo license"——> 永久、全球、可修改
- **Always check**：Söhne 用于 logo 需额外买 logo license（约 $5000-$10000）

## 3. 8 个推荐的免费 SIL OFL 字体组合

### 组合 1: 现代 SaaS（推荐）
- **Inter**（正文 / UI）
- **Fraunces**（Display 衬线）
- **JetBrains Mono**（代码 / 数据）
- **覆盖**：95% SaaS 需求

### 组合 2: 编辑 / 出版
- **Source Serif 4**（正文）
- **Inter**（UI）
- **JetBrains Mono**（注释）
- **覆盖**：博客 / 杂志 / 长文

### 组合 3: 多语言
- **Noto Sans**（拉丁 / 阿拉伯 / 希伯来 / 印度）
- **Noto Serif**（Display）
- **IBM Plex Sans Arabic**（阿拉伯特化）
- **覆盖**：5+ 语种

### 组合 4: 高密度 B2B
- **IBM Plex Sans**（正文 / UI）
- **IBM Plex Mono**（代码 / 数据）
- **IBM Plex Serif**（Display）
- **覆盖**：金融 / 医疗 / 企业

### 组合 5: 品牌感强
- **Manrope**（标题）
- **Inter**（正文）
- **JetBrains Mono**（代码）
- **覆盖**：初创 / SaaS 营销

## 4. 设计合同 6 必写条款

### 条款 1: 作品归属（Work for Hire）
**必写**：
- "本合同为 Work for Hire（雇佣作品）"——> 美国法律术语
- "设计师同意作品（含视觉、文案、代码）所有 IP 归客户"
- "设计师保留作品集展示权（如不写明，客户可禁止）"

**陷阱**：
- 漏写 = 客户可主张设计师"保留版权"
- 漏写作品集展示权 = 客户禁止设计师用作品集

### 条款 2: 修改轮数
**必写**：
- "包含 X 轮修改"——> 通常 2-3 轮
- "超出 X 轮，按 $Y / 轮 或 $Y / 小时收费"
- "重大范围变更（重设计核心页面）按新项目计费"

**陷阱**：
- 漏写 = 客户无限改稿
- 漏写单价 = 协商时尴尬

### 条款 3: Kill Fee（解约费）
**必写**：
- "客户在 X 阶段前解约，支付 Y% 总额"
- "设计师在 X 阶段前解约，扣除实际成本后退款"
- "建议**：30% / 50% / 75% 按阶段"

**陷阱**：
- 漏写 = 客户随时解约，设计师白做
- 漏写 = 设计师也随时跑路，客户损失

### 条款 4: 付款时间表
**必写**：
- "首付 50%（签合同）+ 中期 30%（设计阶段完成）+ 尾款 20%（交付）"
- "发票 7 / 14 / 30 天内付清"
- "逾期按 X% / 月 利息"
- "所有金额含 / 不含税"

**陷阱**：
- 100% 尾款 = 客户拿了稿不付钱
- 没利息条款 = 拖 6 个月不付钱

### 条款 5: 交付物清单
**必写**：
- "交付物包含：Figma 文件、PDF、PNG、字体文件、源码（如适用）"
- "不包含：印刷、视频拍摄、第三方授权（字体 / 摄影）"
- "格式：Figma + Figma export (PDF) + 关键页面 PNG"

**陷阱**：
- 漏写字体文件 = 客户用错字体
- 漏写源码 = 客户无法开发

### 条款 6: NDA / 保密
**必写**：
- "双方对项目信息保密 X 年（通常 2-5 年）"
- "设计师不得在 NDA 期内公开客户产品细节"
- "客户不得公开设计师报价（保护商业关系）"
- "违约金：$Y / 每次违反"

**陷阱**：
- 漏写 = 客户可对公众公开报价 / 工作流
- 漏写违约金 = 违反没后果

## 5. NDA 4 必写条款

### 条款 1: 保密范围
- "保密信息包括：商业计划、技术架构、用户数据、未发布产品"
- "不保密：公开信息、设计师已知的信息"
- **陷阱**：范围过宽 = 设计师不能写 "我为 XX 做过 X"

### 条款 2: 保密期限
- "签署起 X 年"——> 通常 2-5 年
- "产品发布后 X 年"
- **永久保密**用于核心商业秘密（罕见）

### 条款 3: 允许的披露
- "设计师可在保密期内：作品集展示（脱敏）、求职面试（脱敏）"
- **陷阱**：过严 = 设计师无法求职

### 条款 4: 违约救济
- "违约方支付违约金 $Y"
- "守约方可申请禁令（紧急停止）"
- "律师费由违约方承担"

## 6. 版权 4 大要点

### (1) 设计作品保护期
- **美国**：个人作品 = 死后 70 年；雇佣作品 = 首次发表后 95 年 或 创作后 120 年
- **中国**：个人作品 = 死后 50 年
- **欧盟**：个人作品 = 死后 70 年
- **学到的**：**雇佣作品保护期更长**——> 公司资产

### (2) 商标（Logo）保护期
- 商标注册后 10 年（可续展无限次）
- 必须使用才保护（3 年不用可被撤销）
- **学到的**：logo 一定要注册商标

### (3) 字体本身受版权保护
- **是**——> 字体作为软件受版权保护
- **不**——> 字体作为实用工具不受专利保护
- **学到的**：抄袭字体厂的设计 = 版权侵权

### (4) 字体作为作品元素
- 字体在 logo / 海报 / 网站 = 视觉作品的一部分
- logo 设计 = 受保护（注册商标）
- 字体在 logo 中使用 = 需 logo license

## 7. 5 大常见法律风险

### 风险 1: 字体未授权
**案例**：某初创公司用了 Helvetica Neue 在网站，没买 Linotype 授权，被发律师信赔 $50,000
**修正**：永远查 license

### 风险 2: Stock 图未授权
**案例**：某电商网站用了 Shutterstock 图片未授权，赔 $8,000
**修正**：用 Unsplash / Pexels（CC0） 或自己拍

### 风险 3: NDA 漏写
**案例**：设计师在 Twitter 公开客户产品截图，被起诉违反 NDA
**修正**：NDA 必写 + 4 必写条款

### 风险 4: 合同漏写归属
**案例**：设计师为客户做 logo，作品集展示被起诉侵权（因为没写"设计师保留展示权"）
**修正**：合同必写"设计师保留作品集展示权"

### 风险 5: 第三方资源未授权
**案例**：设计师用了 Google Fonts 的字体（OFL 没事），但混了 Monotype 字体在 PDF 嵌入 = 侵权
**修正**：所有字体来源明确 license 文档

## 8. 字体授权速查表

| 字体 | 授权 | 商用 | Web 嵌入 | App 嵌入 | Logo | 价格 |
|---|---|---|---|---|---|---|
| **Inter** | SIL OFL | ✓ | ✓ | ✓ | ✓ | 免费 |
| **IBM Plex** | SIL OFL | ✓ | ✓ | ✓ | ✓ | 免费 |
| **JetBrains Mono** | SIL OFL | ✓ | ✓ | ✓ | ✓ | 免费 |
| **Fraunces** | SIL OFL | ✓ | ✓ | ✓ | ✓ | 免费 |
| **Proxima Nova** | Adobe Fonts | ✓ (CC) | ✓ | ✓ | ✓ | CC 订阅 |
| **Helvetica** | Linotype | ✗ (需买) | ✗ (需买) | ✗ (需买) | ✗ (需 logo license) | $300+ |
| **Futura** | Monotype | ✗ (需买) | ✗ (需买) | ✗ (需买) | ✗ | $150+ |
| **Söhne** | Klim | ✗ (需买) | ✗ (需买) | ✗ (需买) | ✗ (需 logo license) | $2000+ |
| **GT Sectra** | Grilli | ✗ (需买) | ✗ (需买) | ✗ (需买) | ✗ | $500+ |
| **Arial** | Monotype | ✓ (系统预装) | ✗ (需买) | ✗ (需买) | ✗ | 系统预装 |

## 9. 4 个字体加载的法律陷阱

### 陷阱 1: 系统字体商用嵌入
- Arial / Helvetica / Times New Roman 系统预装 = 桌面免费
- **Web 嵌入需 Monotype 授权**——> 用户系统预装不算商用
- 例：你的网站用 `font-family: Arial` 触发 @font-face = 需 web license

### 陷阱 2: Google Fonts CDN
- Google Fonts 免费 = OFL 字体
- **但** ——> 欧洲 GDPR 担心 Google CDN 收集 IP
- **解决**：用 `next/font` self-host 或 Bunny Fonts（GDPR 友好 CDN）

### 陷阱 3: Subsetting
- 裁切字体子集（只保留需要的字符）——> OFL 允许，Monotype 不允许
- **Always check**：你能 subset 吗？

### 陷阱 4: Modifying
- 改字距 / 改轮廓 ——> OFL 允许（但不能单独卖修改版）
- Monotype 多数不允许
- **Always check**：你能 modify 吗？

## 10. 设计作品保护清单

### 设计师角度
- ✓ 注册商标（logo）
- ✓ 写明 Work for Hire
- ✓ 写明作品集展示权保留
- ✓ NDA 4 必写
- ✓ 修改轮数 + kill fee
- ✓ 付款时间表
- ✓ 交付物清单

### 客户角度
- ✓ 写明 IP 归属客户
- ✓ 写明不侵犯第三方版权（字体 / 图片 / 视频）
- ✓ 写明设计师独立责任（如设计师侵权，设计师自己担）
- ✓ 写明交付后责任（用户使用导致侵权，与设计师无关）

## 11. 8 个工具 / 资源

- **fontsinuse.com** —— 字体使用案例库
- **fonts.google.com** —— Google Fonts（OFL 字体）
- **fonts.bunny.net** —— GDPR 友好 Google Fonts 镜像
- **fontstand.com** —— 字体月租
- **myfonts.com** —— Monotype / Linotype 商城
- **commercialtype.com** —— 高端 foundry
- **klim.co.nz** —— Klim Type Foundry
- **abcDinamo.com** —— ABC Dinamo
- **grillitype.com** —— Grilli Type
- **lokalise.com** —— 翻译平台（虽不是字体，但合同常引用）

## 12. 5 个反面教材

1. **Trajan Pro 商业滥用**：某品牌用 Trajan Pro 做 logo，未授权 Monotype logo license = 律师信
2. **Helvetica Neue Web 嵌入**：未买 Linotype web license = 律师信
3. **设计师公开客户产品**：未签 NDA 公开 = 客户起诉违反保密
4. **设计师作品集用客户稿**：未签"作品集展示权保留" = 客户起诉侵权
5. **字体 subset 违反 OFL**：subset 后单独卖 = 违反 OFL（嵌入到产品卖 OK）

## 13. 10 条"如果你在做设计 + 法律，记住这些"

1. **首选 SIL OFL 字体**——> Inter / IBM Plex / JetBrains Mono 覆盖 95% 需求
2. **商业字体必看 license**——> 单字体 / 域名 / 月活 / app 下载量
3. **Helvetica / Futura 商用必买**——> Monotype 律师团队专门发信
4. **设计合同 6 必写**——> Work for Hire / 修改轮数 / Kill Fee / 付款 / 交付 / NDA
5. **NDA 4 必写**——> 范围 / 期限 / 允许披露 / 违约救济
6. **logo 必注册商标**——> 10 年保护可续展
7. **作品集展示权必保留**——> 否则客户起诉
8. **字体不能 subset 单独卖**——> OFL 也禁止（嵌入到产品卖 OK）
9. **系统字体 Web 嵌入需 license**——> Arial 系统预装 ≠ web 商用免费
10. **永远留 license 文档**——> 未来诉讼唯一证据

## 5 条"如果你只能记一条"

1. **首选 SIL OFL 字体**——> Inter + IBM Plex + JetBrains Mono 覆盖 95%
2. **设计合同 6 必写**——> 漏 1 条就可能赔 6 位数
3. **NDA 4 必写**——> 否则客户说你是公开
4. **logo 必注册商标**——> 否则被别人抢注
5. **永远留 license 文档**——> 律师信唯一证据

## 资源 URL
- scripts.sil.org/OFL — SIL OFL 规范
- www.adobe.com/products/adobe-fonts.html — Adobe Fonts
- www.myfonts.com — Monotype / Linotype 商城
- commercialtype.com — 高端 foundry
- klim.co.nz — Klim Type Foundry
- grillitype.com — Grilli Type
- abcdinamo.com — ABC Dinamo
- type-together.com — Type Together
- fonts.bunny.net — GDPR 友好字体 CDN
- creativecommons.org/licenses/by/4.0/ — CC BY 许可
- fonts.google.com — Google Fonts
- thenounproject.com / unsplash.com / pexels.com — 图标 / 图片资源
- uspto.gov/trademark — 美国商标注册
- ic.gc.ca/eic/site/cipointernet-internetopic.nsf/eng/home — 加拿大商标
- cnipa.gov.cn — 中国商标

## 跨引用
- [design-typography-practice.md](design-typography-practice.md) — 字体加载技术
- [design-typography-craft.md](design-typography-craft.md) — 字体工艺史
- [design-business.md](design-business.md) — 设计商业化 + 合同
- [design-education-care.md](design-education-career.md) — 设计师职业 + 合同
- [design-i18n-rtl.md](design-i18n-rtl.md) — 多语言字体选择
- [design-system-build.md](design-system-build.md) — 字体作为 token
- [design-real-codeteardown.md](design-real-codeteardown.md) — 真实代码中的字体加载
