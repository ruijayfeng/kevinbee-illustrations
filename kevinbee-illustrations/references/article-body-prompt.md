# 正文配图提示词组装

每张图单独生成。常规正文全身以 `assets/ip-reference/v2.1/03-article-form-master.png` 为主要参考；纯正面、侧面或背面构图改用 `article-views/` 中最接近目标角度的单图。不要同时加载标准身份母版或标准五视图，它们会把正文身体拉长。头肩近景才使用标准身份母版与对应头部视图。

不要复制一个永远不变的巨型提示词。按当前文章填充以下结构，删掉无关项。

```text
Use case: illustration-story
Asset type: standalone 16:9 Chinese article-body illustration

Identity reference:
Image 1 is the closest KevinBee V2.1 compact article-form reference. Preserve its identity, slightly enlarged head, shortened limbs, hair, hat, clothing construction, palette and angle structure. Static poses may remain strongly compressed; dynamic poses may lengthen only enough to stay natural and must remain visibly more compact than the standard character form.
{从 ip-core.md 的“提示词身份片段”取用必要内容；参考图已经稳定时可缩短}

Core idea:
{只写这张图要表达的一个判断、变化或关系}

Scene metaphor:
{为当前文章新发明的具体物理场景}

KevinBee's participation:
{经历 / 选择 / 同行 / 影响 / 必要时操作；写清姿态与视线}

Composition:
Wide horizontal composition, pure white or very light warm-white background, at least 35% quiet negative space. KevinBee occupies about {15%-30%} of the frame. {主要物件与空间关系}.

Style:
Fresh Japanese editorial illustration, light natural hand-drawn pencil or fine-pen linework, restrained soft watercolor on KevinBee and only the essential object. Clear but not instructional, imaginative but not childish.

Text:
{No text / exact 1-3 short Chinese labels in quotes}

Constraints:
One image communicates one idea. Preserve the red-star white cap, ice-blue bob, muted-red cardigan and calm independent expression. KevinBee is naturally present in the conceptual world and has no fixed occupation. Do not copy prior examples.

Avoid:
Weapons, combat outfit, cape, tactical gear, worker or assistant styling, mascot behavior, battle-poster composition, formal diagram, PPT layout, realistic UI, dense labels, top-left title, complex background, gradients, texture, watermark.
```

## 编辑已有图片

编辑时重复列出不变量：角色身份、核心隐喻、画幅和所有必须保留的物件。一次只改一个问题。

### 去除错误文字

```text
Remove only the incorrect text and its underline or callout. Fill the area with the same clean background. Preserve KevinBee's identity, pose, composition, metaphor, linework, colors and aspect ratio. Add nothing new.
```

### 让参与方式更自然

```text
Keep the core idea and sparse composition, but change KevinBee's relationship to the scene from a worker operating the structure to a person naturally experiencing, observing, choosing, following or lightly influencing it. Preserve her V2 identity and casual outfit. Do not add tools, uniforms or extra labels.
```

## 输出尺寸

图像工具返回 3:2 时：

1. 保留原始文件。
2. 检查能否安全居中裁切为 16:9。
3. 若会切掉红星白帽、手脚、核心物件或必要留白，重新生成更宽松的构图，不强行裁切。
