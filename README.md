# AI 平台图标库

AI 平台的 App Store 官方图标，按国内 / 国外分开存放，供观略引擎企业宣传片与销售朋友圈素材使用。

## 国内平台（`domestic/`，8 个）

| 文件 | 平台 | App Store 应用 |
|---|---|---|
| `doubao.png` | 豆包 | 豆包 - 生活工作 AI 助手 |
| `deepseek.png` | DeepSeek | DeepSeek - AI 智能助手 |
| `tongyi-qianwen.png` | 通义千问 | 千问 - 阿里AI助手 |
| `yuanbao.png` | 腾讯元宝 | 元宝-腾讯全能AI助手 |
| `kimi.png` | Kimi | Kimi |
| `wenxin-yiyan.png` | 文心一言 | 文心 - 百度旗下全能AI助手 |
| `zhipu-qingyan.png` | 智谱清言 | 智谱清言 - 一站式解放AI生产力 |
| `xunfei-xinghuo.png` | 讯飞星火 | 讯飞星火-越用越懂你的AI助手 |

## 国外平台（`international/`，9 个）

| 文件 | 平台 | App Store 应用 |
|---|---|---|
| `chatgpt.png` | ChatGPT | ChatGPT |
| `claude.png` | Claude | Claude by Anthropic |
| `gemini.png` | Gemini | Google Gemini |
| `grok.png` | Grok | Grok |
| `perplexity.png` | Perplexity | Perplexity: AI Agent & Search |
| `copilot.png` | Microsoft Copilot | Microsoft Copilot |
| `meta-ai.png` | Meta AI | Meta AI |
| `muse.png` | Muse（Meta） | Muse from Meta |
| `le-chat.png` | Le Chat（Mistral） | Vibe by Mistral（ex-Le Chat） |

## 规格

- 全部为 PNG，512×512 px，取自 iTunes Search API 的 `artworkUrl512`（国内走 CN 区、国外走 US 区）。
- 备注：Le Chat 已更名为 Vibe by Mistral，图标为 Mistral 官方当前 artwork，文件仍沿用 `le-chat.png`。

## 来源与使用

- 图标来源：Apple App Store 官方 artwork（各应用的商标权归各自厂商所有）。
- 仅供公司宣传素材内部使用，不得对外分发或声称拥有这些商标。

## 更新

应用换图标时，重新跑 `fetch_icons.py`（需联网调 iTunes Search API），核对后再提交。
