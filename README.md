# 凯冰文章配图与封面

> 用固定的凯冰 V2 日系休闲形象，为中文文章创作正文隐喻配图与封面主视觉。

正文：16:9 横版、白底轻手绘 · 封面：聚焦主题、适配缩略图与平台裁切 · Codex Skill

## 当前版本是什么

这是一个面向中文文章的 Codex Skill。正文模式先理解文章中的认知锚点，再为值得配图的锚点发明可见场景，让凯冰进入核心因果关系；封面模式从定稿标题和文章核心承诺提炼一个清楚的主视觉张力。

当前正式支持：

- 分析文章并规划正文配图 shot list
- 生成单张或成组的正文隐喻配图，修改已有正文图
- 从定稿标题和核心承诺生成文章封面主视觉，检查缩略图识别与平台裁切
- 保持凯冰 V2 在正文与封面中的身份一致性

封面与正文图是两种模式：正文图解释关系，封面帮助读者在缩略图中认出主题与张力，各自使用不同的构图和验收规则。角色设定稿不在本 Skill 的生成范围内。

## 凯冰 V2

凯冰是一位清新、安静、有主见的日系休闲少女。她不是战士、工作人员或内容助手，也不是贴在画面角落的吉祥物。

稳定识别点：

- 白色休闲棒球帽，正面红色五角星
- 冰蓝色齐下巴短发
- 柔和暗红色针织开衫
- 象牙白上衣与藏青短裙
- 红橙色眼睛与克制、自然的表情

### V2.1 身份母版

![凯冰 V2.1 身份母版](kevinbee-illustrations/assets/ip-reference/v2.1/00-canonical-master.png)

### 五视图结构

![凯冰 V2.1 五视图](kevinbee-illustrations/assets/ip-reference/v2.1/01-turnaround-five-view.png)

### 头部四视图

![凯冰 V2.1 头部结构](kevinbee-illustrations/assets/ip-reference/v2.1/02-head-construction-four-view.png)

### V2.3 正文 Q 版母版

![凯冰 V2.3 正文 Q 版正面](kevinbee-illustrations/assets/ip-reference/v2.3/00-strong-q-master-front.png)

### V2.3 独立角度参考

![凯冰 V2.3 正面三分之四](kevinbee-illustrations/assets/ip-reference/v2.3/q-form-views/02-front-three-quarter.png)

![凯冰 V2.3 左向侧面](kevinbee-illustrations/assets/ip-reference/v2.3/q-form-views/03-left-profile.png)

![凯冰 V2.3 背面](kevinbee-illustrations/assets/ip-reference/v2.3/q-form-views/04-back.png)

V2.3 是重新设计的大头帽、短躯短腿 Q 版，不是把标准人物在画布上缩小。圆厚膝鞋与显幼态的视觉比例可以成立；固定的是白帽红星、蓝发、红色开衫、安静有主见的气质和跨角度造型。旧 V2.2 轻 Q 及其表情、动作、正文示例保存在 `archive/development-v2/retired-v2.2-runtime/`，不再参与默认生图。

## 强 Q 正文场景探索

![连续画线隐喻探索](archive/development-v2/explorations/q-form-study-2026-09-28/17-continuity-pencil-scene.png)

这张探索图只验证强 Q 形象能进入文章隐喻，不是默认的铅笔或构图模板。每篇文章仍从正文重新发明场景；正式正文图需按当前文章单独生成与验收。

## 正文配图视觉原则

- 默认 16:9 横版，白色或极浅暖白背景
- 轻而自然的手绘线条，少量克制水彩
- 一张图只表达一个核心关系
- 凯冰通常占画面约 15%–30%
- 默认无文字；确有必要时只使用 1–3 个短中文标注
- 凯冰可以经历、选择、承受、同行或轻微影响场景，不必每次操作机器；单纯旁观不算参与
- 不做 PPT、复杂架构、真实 UI、战斗海报或角色站桩图

## 封面视觉原则

- 围绕一个文章主对象与一处可见张力，不把多个案例拼成海报目录
- 主题道具、空间关系与凯冰的表情、动作、景别、占比一起设计；不固定人物和标题的位置
- 区分文章长标题与封面短主题词；已确认的图内文字完整、准确、可读，不能用文章长标题硬塞
- 标题的光影与渐隐等质感按主题选择，不固定套用；无字版保留排字区域
- 按目标平台检查裁切，并在约 240px 宽的缩略图下验证辨识度

## 固定身份，开放表达

- 固定凯冰的脸、帽星、发型、服装结构、配色和强 Q 身体逻辑。
- 不固定每篇文章的隐喻物件、动作、观察角度、角色站位或参与方式。
- 先从文章发明隐喻，再按需加载最少的角色参考；不能从已有姿势反向套用文章。
- 正式角度图只校准当前画面的人物造型，不是姿势模板。同一语义有多个合格方案时，应保留变化并避免连续复用。

## 安装

```bash
git clone https://github.com/ruijayfeng/kevinbee-illustrations.git
cd kevinbee-illustrations
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./kevinbee-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后可以这样调用：

```text
Use $kevinbee-illustrations 为这篇中文文章规划并生成几张凯冰 V2 正文配图。
```

## 使用方式

### 只规划，不生图

```text
Use $kevinbee-illustrations 先不要生成图片。
分析下面这篇文章，挑选真正值得视觉化的认知锚点，给出 4–6 张 shot list。

<粘贴文章>
```

### 直接生成

```text
Use $kevinbee-illustrations 为下面这篇文章生成 4 张正文配图。
保持凯冰 V2 形象一致；默认无文字，每张只表达一个核心关系。

<粘贴文章>
```

### 单个观点

```text
Use $kevinbee-illustrations 为这个观点生成一张正文配图：

真正的选择不是找到最亮的路，而是放弃其他同样可能的路。
```

### 修改已有图片

```text
Use $kevinbee-illustrations 编辑这张图：
保持凯冰身份、姿态和核心隐喻不变，只删除错误文字，不新增物件。
```

### 生成文章封面

```text
Use $kevinbee-illustrations 为这篇已定稿文章生成一张封面主视觉。
标题：<定稿标题>
目标平台：<平台或所需画幅>
依据正文提炼一个主对象和一个核心张力；默认无字，留出标题安全区。

<粘贴文章>
```

若要标题直接出现在封面中，明确提供短主题词，例如 `Seed-2.1-pro-0915`，并要求与凯冰的动作、主题道具一起构图；不是把文章完整标题缩小放进画面。见 [有字封面调用示例](examples/prompts.md#有字封面)。

更多调用示例见 [examples/prompts.md](examples/prompts.md)。

## Skill 的工作方式

正文模式：找出文章的核心判断和转折，只在需要解释关系的位置发明隐喻；让凯冰进入核心因果关系，检查身份、参与方式与画幅，保存原图及最终正文版本。标准形象使用 V2.1 身份层，正文全身使用 V2.3 强 Q 层。

封面模式：依据主题和文章核心承诺，聚焦一个主对象与张力；同步设计凯冰、道具和文字的空间关系，检查原尺寸、准确文字与缩略图。封面不直接放大正文隐喻图，也不伪装成角色海报。

## 目录结构

```text
.
├── README.md
├── examples/
│   └── prompts.md
├── docs/
│   ├── character-direction-v2.md
│   └── upstream-analysis.md
├── archive/
│   ├── legacy-v1/                # 旧战斗形象与旧案例
│   └── development-v2/           # V2 探索、退役的轻 Q 与过渡资产
├── tests/
│   └── article-body/             # 前向测试、失败对照、原图与最终裁切
└── kevinbee-illustrations/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   ├── manifest.yaml
    │   └── ip-reference/          # V2.1 标准身份 + V2.3 正文 Q 版
    ├── references/
    │   ├── ip-core.md
    │   ├── character-model-v2.3.md
    │   ├── article-body-style.md
    │   ├── article-body-prompt.md
    │   ├── cover-style.md
    │   ├── cover-prompt.md
    │   ├── cover-qa.md
    │   ├── composition-patterns.md
    │   └── qa-checklist.md
    └── scripts/
        └── validate.py
```

真正安装到 Codex 的目录只有 `kevinbee-illustrations/`。`archive/` 和 `tests/` 保留设计证据与前向测试，但不进入默认生成上下文。

## 设计上的单一真值

- 凯冰是谁：只由 `references/ip-core.md` 定义
- 比例、角度与参考选择：由 `references/character-model-v2.3.md` 定义
- 正文图长什么样：由 `references/article-body-style.md` 定义
- 如何构造提示词：由 `references/article-body-prompt.md` 定义
- 如何发明隐喻：由 `references/composition-patterns.md` 定义
- 如何验收：由 `references/qa-checklist.md` 定义
- 封面视觉、提示词与验收：分别由 `references/cover-style.md`、`references/cover-prompt.md`、`references/cover-qa.md` 定义
- 哪张图该在何时加载：由 `assets/manifest.yaml` 定义

正文依赖顺序是：角色身份 → 角色结构 → 隐喻构图 → 正文风格 → 提示词 → QA。封面另按封面视觉、提示词与验收规则执行。后层不得重写前层，测试和历史资产也不得进入运行时清单。

## 上游与署名

本项目基于 [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) 演化而来，继承了“认知锚点、一图一义、物理隐喻”的文章配图方法，并重新设计了 KevinBee 角色与生成结构。

详细溯源与差异分析见 [docs/upstream-analysis.md](docs/upstream-analysis.md)。

作者：凯冰（KevinBee）

- GitHub：[ruijayfeng](https://github.com/ruijayfeng)
- 微信：`STAR2023415`
- 邮箱：`fz.dev@foxmail.com`

## License

MIT License。详见 [LICENSE](LICENSE) 与 [NOTICE.md](NOTICE.md)。
