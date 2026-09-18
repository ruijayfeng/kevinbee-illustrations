# KevinBee Illustrations 上游溯源与重构分析

> 调研日期：2026-09-17  
> 证据范围：只使用 GitHub 仓库元数据、提交历史与仓库文件。本文的“当前版本”指 `ruijayfeng/kevinbee-illustrations@b7d6378`；“上游”指 `helloianneo/ian-xiaohei-illustrations@91b5608`。

## 结论先行

可以把当前项目理解成一个**固定凯冰 IP 的文章正文配图 Skill**：它会从文章中挑选认知锚点，设计 4–8 张 shot list，再用凯冰参与低科技隐喻动作的方式生成图片。

但按仓库现在的明确边界，它**不是封面 Skill，也不是完整的 IP 设计 Skill**。README 把“商业海报或封面 KV”列为默认不输出，`SKILL.md` 也只定义了 16:9 正文配图工作流。因此，如果未来目标是同时覆盖“正文配图 / 封面 / IP 相关设计”，应把它重构成共享同一 IP 资产的多场景系统，而不是继续向当前单一 prompt 里追加规则。

最重要的上游结论是：

1. 当前仓库不是从零设计，而是 GitHub 明确登记的 [`helloianneo/ian-xiaohei-illustrations`](https://github.com/helloianneo/ian-xiaohei-illustrations) fork。GitHub API 中 `fork=true`，`parent` 和 `source` 都指向该仓库（[当前仓库元数据](https://api.github.com/repos/ruijayfeng/kevinbee-illustrations)）。
2. 当前仓库完整继承上游截至 [`91b5608`](https://github.com/helloianneo/ian-xiaohei-illustrations/commit/91b560849e8f883922cc2fa8a358a668caa94105) 的 9 个提交；之后仅有 6 个分叉提交，集中在凯冰适配、重命名和样例替换（[当前分支提交历史](https://github.com/ruijayfeng/kevinbee-illustrations/commits/main/)）。
3. 分叉后保留了上游的产品定位、目录结构、shot list 工作流、8 类构图、提示词槽位、QA 结构和输出路径。真正新增的是凯冰角色设定、角色负面约束、品牌命名及凯冰样例资产。
4. 当前版本最大的退化不是“规则不够多”，而是**产品承诺、参考资产和实际使用场景互相冲突**：文档说正文配图且禁止角色海报，但 README 展示的 8 张图却主要是立绘、三视图、战斗和角色动作；文档要求 16:9，当前 22 张样例里没有一张是 16:9。
5. 最值得重构的是“职责分层”：将 IP 真值、画面场景、构图策略、生成适配、验收标准分开。先做一致性与可验证性，再扩封面和 IP 设计能力。

## 一、上游与分叉关系

### 1. GitHub 关系

| 项目 | 当前仓库 | 上游仓库 |
|---|---|---|
| GitHub | [`ruijayfeng/kevinbee-illustrations`](https://github.com/ruijayfeng/kevinbee-illustrations) | [`helloianneo/ian-xiaohei-illustrations`](https://github.com/helloianneo/ian-xiaohei-illustrations) |
| GitHub 类型 | fork | 独立源仓库 |
| `parent` / `source` | 均为 `helloianneo/ian-xiaohei-illustrations` | 无 |
| 共同历史终点 | [`91b5608`](https://github.com/helloianneo/ian-xiaohei-illustrations/commit/91b560849e8f883922cc2fa8a358a668caa94105) | 当前 HEAD 也是 `91b5608` |
| 当前 HEAD | [`b7d6378`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/b7d6378c6b82779549e8e323aee4620e336838cd) | [`91b5608`](https://github.com/helloianneo/ian-xiaohei-illustrations/commit/91b560849e8f883922cc2fa8a358a668caa94105) |

当前分支相对上游领先 6 个提交、落后 0 个提交；上游在共同祖先后没有新提交，因此本次重构不存在“先同步上游更新”的前置任务。上游另有 [`v1.0.0`](https://github.com/helloianneo/ian-xiaohei-illustrations/tree/v1.0.0) 标签，当前 fork 没有版本标签，这也意味着当前改造尚未形成自己的可发布版本边界。完整差异可从 [GitHub 跨 fork 比较页](https://github.com/helloianneo/ian-xiaohei-illustrations/compare/main...ruijayfeng:kevinbee-illustrations:main) 查看。

当前 fork 从共同祖先以后有 6 个提交：

- [`7ba365d`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/7ba365db4d9aa8b524f2e1d5baa9358543a78c83)：将小黑改造成 Kaibing IP，并替换首批图片。
- [`9aa1f92`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/9aa1f9288d2d01a02e96bc04615fd98fd860d511)：完成“小黑 / Xiaohei / Kaibing → 凯冰 / KevinBee”重命名、重画 09–14 和作者信息迁移。
- [`04f74b2`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/04f74b28c68d390b6d0bb9f752347103b7e7ffc9)：仓库改名为 `kevinbee-illustrations`。
- [`0c4b3d5`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/0c4b3d5c53c987e1718e0c030baadbc1c0299c5c)：用 gpt-image-2 重画 09–14。
- [`b853fc9`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/b853fc97e84ec6e8d560bb92d12bf78178417594)：README 更新。
- [`b7d6378`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/b7d6378c6b82779549e8e323aee4620e336838cd)：删除 README 的相关项目章节。

因此，这不是“参考上游思想后重新实现”的关系，而是**直接继承上游全部历史后做角色替换和局部增强**。

### 2. 当前仓库的溯源文档反而变弱了

GitHub 自身仍能证明 fork 关系，但当前 README 末尾只写“详细见原fork仓库”，没有给出仓库链接（[当前 README](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/README.md)）。`NOTICE.md` 也只描述 KevinBee 品牌和当前作者，没有说明上游来源（[当前 NOTICE](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/NOTICE.md)）。

这不影响 GitHub 的技术分叉关系，但降低了仓库内自说明性。重构时应恢复清晰的 `Lineage / Attribution` 章节，至少写明上游仓库、共同祖先和“继承了什么 / 改了什么”。

## 二、设计继承对照

### 1. 定位：几乎原样继承，只替换 IP

上游把自己定义为“为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图”，强调从文章中寻找“认知锚点”，输出 16:9 白底手绘隐喻图；当前版本保留同样的对象、媒介、认知锚点和 16:9 目标，仅将“小黑”替换成“凯冰”（[上游 README](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/91b560849e8f883922cc2fa8a358a668caa94105/README.md)，[当前 README](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/README.md)）。

所以当前项目的准确产品定义是：

> 用固定凯冰 IP，把中文文章中的判断、流程、状态和隐喻，转成正文中的手绘解释图。

“封面”和“IP 设计”并没有从上游继承，也没有在分叉后正式加入。相反，当前 README 仍明确排除商业海报、封面 KV 和纯角色立绘方向。

### 2. Skill 结构：文件分工一一对应

| 职责 | 上游 | 当前 | 变化判断 |
|---|---|---|---|
| 主入口 | `ian-xiaohei-illustrations/SKILL.md` | `kevinbee-illustrations/SKILL.md` | 结构、章节、步骤数基本不变 |
| 风格真值 | `references/style-dna.md` | 同名 | 加入凯冰配色、水彩与角色海报禁令 |
| IP 真值 | `references/xiaohei-ip.md` | `references/kevinbee-ip.md` | 用更复杂的凯冰角色规格替换小黑 |
| 构图方法 | `references/composition-patterns.md` | 同名 | 8 类结构和原创隐喻三步法保留 |
| 提示词 | `references/prompt-template.md` | 同名 | 模板槽位保留，扩展角色描述与负面词 |
| QA | `references/qa-checklist.md` | 同名 | 基本保留，新增红星白帽与反战斗海报检查 |
| Agent 展示信息 | `agents/openai.yaml` | 同名 | 品牌名称和默认调用词替换 |
| 示例 | `assets/examples/` | 同路径 | 从 14 张正文隐喻图变为 8 张角色图 + 6 张隐喻图 |

可直接对照 [上游 Skill](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/91b560849e8f883922cc2fa8a358a668caa94105/ian-xiaohei-illustrations/SKILL.md) 与 [当前 Skill](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/SKILL.md)。两者都是 106 行，且都采用“消化正文 → 配图策略 → 单张生成 → 检查迭代 → 保存交付”的五步流程。

### 3. 工作流：上游骨架完整保留

以下核心工作流均来自上游：

- 先判断哪些段落值得配图，不平均铺图；
- 默认先出 4–8 张 shot list；
- 每张图选择一种结构类型；
- 每张只表达一个核心结构；
- 每张单独生成，不拼图；
- 生成后按 QA 清单检查；
- 保存到 `assets/<article-slug>-illustrations/`。

当前分叉的实质变化，是把每一步的动作主体从“小黑”换成“凯冰”，并要求凯冰承担操作、修补、分拣、连接、守护等核心动作（[当前 Skill](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/SKILL.md)）。

### 4. 构图与原创方法：继承度很高

上游和当前版本都有同样的 8 类基础结构：Workflow、系统局部、前后对比、角色状态、概念隐喻、方法分层、地图路线、小漫画分镜；也都有同样的“抽象概念 → 物理动作 → 低科技物件 → 角色承担动作”原创隐喻方法（[上游构图规则](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/91b560849e8f883922cc2fa8a358a668caa94105/ian-xiaohei-illustrations/references/composition-patterns.md)，[当前构图规则](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/references/composition-patterns.md)）。

当前主要是措辞替换和动作合理化，例如把“小黑卡在机器里、拉错线”改成“凯冰操作机器、拉线、守门、修补”。方法论本身没有新增：没有按文章体裁、传播目标、封面需求或平台规格形成新的决策树。

### 5. 提示词：新增了角色一致性，但继承了单模板局限

上游模板已有完整槽位：Visual DNA、Recurring IP、Theme、Structure type、Core idea、Composition、Suggested elements、Chinese labels、Color use、Constraints，以及两个图像编辑提示（[上游提示词](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/91b560849e8f883922cc2fa8a358a668caa94105/ian-xiaohei-illustrations/references/prompt-template.md)）。

当前版本保留这些槽位，新增：

- 2.5–3 头身、冰蓝短发、红橙眼、白帽红星、猩红斗篷、黑色战斗服等外观描述；
- 凯冰与关键物件允许克制的水彩着色；
- 红星优先识别、武器不喧宾夺主；
- “赤星 / CHIXING”、发色漂移、偶像、公主、重甲、霓虹、3D、写实等负面约束；
- 去标题和增强凯冰参与感的编辑提示。

这是当前分叉最实质的能力增强（[当前提示词](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/references/prompt-template.md)）。但它仍是一个巨型静态模板，没有把“固定 IP 身份”“文章语义”“构图”“画面规格”“平台场景”模块化组合。

### 6. QA：角色一致性增强，但仍然不可执行

当前 QA 在上游的白底、留白、少字、颜色职责、非 PPT、非旧案例复刻基础上，新增了红星白帽、非角色海报、非战斗主视觉等要求（[上游 QA](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/91b560849e8f883922cc2fa8a358a668caa94105/ian-xiaohei-illustrations/references/qa-checklist.md)，[当前 QA](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/references/qa-checklist.md)）。

但上下游都只有文字清单，没有自动检查脚本、样例清单、尺寸验证、文件命名验证、禁词扫描或人工验收记录。因此 QA 是“提醒”，还不是“质量门”。

## 三、当前分叉真正新增了什么

### 1. 更具体的 IP 角色真值

`kevinbee-ip.md` 明确了一个可重复使用的角色锚点体系：

- 一级锚点：白帽正面居中的红色五角星；
- 二级锚点：冰蓝短发、猩红斗篷；
- 气质：沉默、坚定、克制、略疏离；
- 角色职责：修补、分拣、连接、压制、记录、守护、搭建、测试；
- 失败边界：偶像、吉祥物、儿童卡通、纯立绘、战斗主视觉、武器抢戏。

这是从上游“小黑”的极简轮廓角色，升级为更强品牌识别度的人形 IP（[凯冰 IP 文件](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/references/kevinbee-ip.md)）。

### 2. 更具体的颜色语义

当前 `style-dna.md` 指定了黑色 `#2B2B2B`、猩红 `#D62828`、冰蓝 `#A6C8E6`、暖白 `#E6E6E6` 和浅肤色 `#FFD6C7`，并把猩红与冰蓝同时用于角色识别和信息语义（[当前风格 DNA](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/kevinbee-illustrations/references/style-dna.md)）。这是上游所没有的品牌色层。

### 3. 角色参考资产

当前增加了标准全身、三视图、半身、拔剑、夜巡、守护、日常和 Q 版动作等 8 类角色参考，并保留 6 张正文隐喻案例；这些变化集中在 [`9aa1f92`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/9aa1f9288d2d01a02e96bc04615fd98fd860d511) 与 [`0c4b3d5`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/0c4b3d5c53c987e1718e0c030baadbc1c0299c5c)。

这使仓库具备了“角色设定资料”的雏形，但还没有把它组织成可用于不同任务的角色资产系统。

## 四、哪些地方发生了退化或形成了新债务

### 1. 参考资产与产品定位冲突

上游 README 展示的 8 张图全部是文章隐喻配图，安装包内 14 张也全部是约 16:9 的文章图（[上游示例目录](https://github.com/helloianneo/ian-xiaohei-illustrations/tree/91b560849e8f883922cc2fa8a358a668caa94105/ian-xiaohei-illustrations/assets/examples)）。

当前 README 展示的 8 张图却是全身立绘、三视图、肖像、拔剑、夜巡、守护、日常和 Q 版动作（[当前 README 示例](https://github.com/ruijayfeng/kevinbee-illustrations/blob/b7d6378c6b82779549e8e323aee4620e336838cd/README.md)）。这与同一 README 中“不是角色海报”“不输出封面 KV”，以及 Skill 中“禁止 character poster / battle key visual”互相冲突。

本地资产尺寸进一步证明了问题：

- `examples/images/` 的 8 张：6 张为 `1024×1536` 竖图，1 张 `1536×1024` 横图，1 张 `1254×1254` 方图；
- `kevinbee-illustrations/assets/examples/09–14`：6 张均为 `1536×1024`，即 3:2；
- 上游 14 张安装包样例：基本为 `1672×941`，约等于 16:9。

换言之，当前仓库反复要求“16:9”，但实际 22 张样例中没有一张是 16:9。对依赖视觉参考的图像模型而言，这比文字规则缺失更严重。

### 2. 从“案例库”退化成“角色图 + 少量案例”

上游安装包里有 14 张覆盖断点、最小闭环、分拣、一材多用、承接、三类来源、内容职责、话术工具箱、常见坑、信息井、压机、发酵、承重和信任桥等不同结构的正文图。

当前安装包保留 14 张总数，但前 8 张变成角色设定图，只剩后 6 张承担正文隐喻校准。名义数量没变，**任务覆盖度下降**。这会让生成模型更容易学到“凯冰长什么样”，却更难学到“凯冰如何在正文隐喻中行动”。

### 3. 复杂角色挤压了文章语义预算

上游“小黑”只有黑色轮廓、白点眼、细腿和空表情，角色描述很短；当前凯冰需要稳定发型、帽子、红星、眼色、斗篷、服装、腰带、鞋、比例、气质和武器边界。

这是品牌识别度的提升，也是生成难度的提升。当前做法把所有外观信息直接塞进每张图的 prompt，角色一致性、文章隐喻、构图和中文文字争抢同一个生成注意力预算。仓库没有提供角色参考图选择规则、参考图优先级、角色一致性测试或“简化形态”降级策略。

### 4. 规则重复，单一事实来源并未真正建立

白帽红星、冰蓝短发、猩红斗篷、非可爱、非战斗海报等规则同时出现在：

- `SKILL.md`；
- `style-dna.md`；
- `kevinbee-ip.md`；
- `prompt-template.md`；
- `qa-checklist.md`；
- README 与 prompt 示例。

上游已经有一定重复；分叉后因为角色更复杂，重复显著放大。修改角色设定或扩展任务类型时，需要同步多处文本，容易漂移。

### 5. QA 与仓库内容不自洽

QA 要求 16:9、非角色海报、非战斗主视觉；README 却把大量竖版角色图与拔剑战斗图作为“示例效果”。当前缺少任何自动检查去发现这种矛盾。

建议至少把以下项目自动化：

- 图片宽高比与最小尺寸；
- 根目录展示图与安装包样例的角色、用途和哈希清单；
- 旧品牌词（Ian、小黑、Xiaohei、Kaibing、旧仓库名）扫描；
- 必需文件与 YAML frontmatter；
- README 链接有效性；
- 样例类型标签和用途声明。

### 6. 重复资产与仓库体积是继承债务，分叉后被放大

上游已将 README 的 8 张展示图与安装包样例重复保存；当前也完全复制这套方式。当前 `examples/images/01–08` 与 `kevinbee-illustrations/assets/examples/01–08` 是逐字节相同的 8 组文件，分别约占 19 MB，形成约 19 MB 的可消除重复。

这不是当前分叉原创的问题，但高分辨率角色图让成本更大。重构时可以保留一个 canonical 资产目录，通过文档引用或发布脚本生成安装包，而不是在 Git 中维护两份真值。

### 7. 提交了过时的工作记忆

[`9aa1f92`](https://github.com/ruijayfeng/kevinbee-illustrations/commit/9aa1f9288d2d01a02e96bc04615fd98fd860d511) 新增了 `.workbuddy/memory/`。其中长期记忆仍写旧项目标题、旧仓库名 `kaibing-illustrations` 和历史状态。这些内容不是 Skill 运行所需，却可能误导后续维护者或 Agent。它应移出发布仓库，或改为正式、当前有效的迁移记录。

### 8. 仓库展示元数据仍有品牌迁移残留

GitHub API 返回的当前仓库 description 仍是 `Kaibing IP hand-drawn metaphor illustrations...`，没有对齐 KevinBee 品牌（[仓库元数据](https://api.github.com/repos/ruijayfeng/kevinbee-illustrations)）；README 中的 X/Twitter 也实际链接到 GitHub，末尾“详细见原fork仓库”没有链接。这些不影响 Skill 运行，却会削弱公开仓库的可信度和可理解性。

### 9. 可扩展性仍停留在单 IP、单场景、单模板

上下游都把角色、场景、画幅和输出规则硬编码在同一套文件里。当前虽然品牌化更强，但没有出现以下扩展点：

- `mode`: `article-body` / `cover` / `ip-sheet` / `social-card`；
- `aspect`: 16:9 / 3:2 / 1:1 / 3:4 / 平台尺寸；
- `character-variant`: Q 版 / 标准比例 / 头像 / 动作简化形态；
- `render-profile`: 手绘隐喻 / 封面主视觉 / 角色设定稿；
- 平台与文字安全区；
- 参考图选择与优先级；
- 每种 mode 独立的 prompt 与 QA。

因此，直接把“封面”和“IP 设计”写进当前 `SKILL.md` 会继续增加冲突，而不是形成可维护的能力。

## 五、建议的重构方向

### 第一阶段：先把当前正文配图 Skill 做正确

目标不是加功能，而是建立一致的 1.0 基线。

1. 明确唯一产品承诺：先只承诺 `article-body`。
2. 建立单一 IP 真值文件：外形、气质、识别锚点、禁止项只在一个文件定义；其他文件只引用。
3. 将角色参考与正文案例分目录：例如 `assets/ip-reference/` 与 `assets/article-examples/`。
4. 补齐 8–12 张真正 16:9、凯冰参与核心动作的正文案例；角色立绘不再冒充正文效果图。
5. 为所有样例增加 manifest：文件、用途、画幅、角色形态、构图类型、是否可进入生成上下文。
6. 增加仓库校验脚本与 CI，使图片比例、重复文件、旧品牌词、断链和结构漂移能自动失败。

### 第二阶段：把 Skill 改成“共享 IP 核心 + 场景路由”

建议结构：

```text
kevinbee-design/
├── SKILL.md                    # 识别任务、选择 mode、按需读取
├── references/
│   ├── ip-core.md              # 唯一角色真值
│   ├── visual-tokens.md        # 色彩、线条、材质、字体/文字规则
│   ├── modes/
│   │   ├── article-body.md
│   │   ├── cover.md
│   │   └── ip-sheet.md
│   ├── composition/
│   │   ├── metaphor.md
│   │   ├── cover.md
│   │   └── character.md
│   ├── prompts/
│   │   ├── article-body.md
│   │   ├── cover.md
│   │   └── ip-sheet.md
│   └── qa/
│       ├── common.md
│       ├── article-body.md
│       ├── cover.md
│       └── ip-sheet.md
└── assets/
    ├── ip-reference/
    ├── article-examples/
    ├── cover-examples/
    └── manifest.yaml
```

这里的关键不是目录更漂亮，而是让三件事不再互相污染：

- **IP 不变项**：凯冰是谁；
- **场景变量**：正文配图、封面、设定稿各自解决什么问题；
- **生成实现**：不同场景该使用什么构图、画幅、参考图、提示词和 QA。

### 第三阶段：再正式加入封面与 IP 设计

封面不是“把正文图放大”。它需要独立定义：

- 信息层级：标题、副标题、署名和品牌标识；
- 视觉焦点：角色、主题物和标题之间的主次；
- 平台规格与裁切安全区；
- 有字版 / 无字版；
- 角色姿态与视线引导；
- 缩略图可读性。

IP 设计也不是“多生成几张立绘”。它需要：

- canonical turn-around；
- 表情、动作、道具和服装变化规则；
- 识别锚点优先级；
- 可变与不可变属性；
- 多画风时的身份保持；
- 版本号与资产验收。

这两个 mode 都应复用 `ip-core.md`，但各自拥有独立 prompt、示例和 QA。

## 六、建议保留与建议重做

### 建议保留

- “认知锚点，而非平均配图”的文章分析原则；
- 一图一核心结构；
- 低科技物件 + 物理动作 + 角色承担动作的隐喻方法；
- 8 类基础构图作为正文配图库的起点；
- 凯冰的白帽红星、冰蓝短发、猩红斗篷三级识别系统；
- 生成后迭代而非一次成图的意识；
- `assets/<article-slug>-illustrations/` 的交付习惯。

### 建议重做

- README 的示例区与产品边界；
- 样例资产的画幅、分类与上下文加载规则；
- 重复分散的角色规则；
- 单个巨型 prompt；
- 只能人工阅读的 QA；
- 无链接的上游说明；
- `.workbuddy/memory/` 这类过时内部状态；
- 把正文配图、封面、角色设定混在一起的品牌表达。

## 最终判断

当前项目的价值不在于它已经是一套成熟的“凯冰视觉设计系统”，而在于它已经有了两个不错的种子：

1. 上游留下的一套简洁、有效的文章隐喻工作流；
2. 当前分叉新增的一套有识别度的凯冰角色锚点。

现在的粗糙感，主要来自这两个种子还没有被真正融合：上游的工作流仍按极简小黑角色设计，当前却把更复杂的凯冰设定和角色图直接覆盖在上面。最合理的优化路径不是继续加形容词，而是先建立“IP 核心—任务场景—生成策略—质量门”的分层系统。
