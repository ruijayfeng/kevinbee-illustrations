# 凯冰生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art with slightly wobbly pencil lines. Lots of empty white space. Sparse short handwritten Chinese annotations in red, orange, and blue. Clean absurd low-tech product-sketch feeling. Soft restrained watercolor-like shading only on 凯冰 and essential objects. No gradients, shadows, paper texture, complex background, commercial vector style, PPT infographic look, realistic UI, character poster composition, or battle key visual.

Recurring IP character required:
凯冰 (KevinBee), a 2.5-to-3-head-tall chibi anime girl with a calm, serious, slightly distant expression; short layered ice-blue bob hair; red-orange eyes; a worn white baseball cap with one clear bright red five-pointed star centered on the front; a crimson red hooded cloak; black combat dress; black choker; red-and-black belt; and black ankle boots. 凯冰 must perform the core conceptual action, not decorate the scene. The red-star cap is the primary recognition point. A slender silver-gray sword and black-red scabbard are optional action tools, never the focal point. Do not call her 赤星 or CHIXING.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：凯冰在哪里、正在做什么、主要低科技物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for line art and structures. Crimson red for 凯冰's cloak, the cap star, key warnings, and results. Ice blue for her hair and secondary state notes. Orange only for the main flow, path, or arrows.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense explainer, character poster, or battle illustration. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this article. It should be clear but not instructional, interesting but not childish, strange but clean.

Negative constraints:
No 赤星, no CHIXING, no missing red star, no replacement symbol on the cap, no long hair, white hair, purple hair, pink idol aesthetic, princess dress, heavy armor, cyberpunk neon, 3D render, photorealism, western superhero style, exaggerated childish expression, or weapon larger than the character.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: 凯冰's red-star cap, ice-blue hair, crimson cloak, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强凯冰参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 凯冰 more central to the conceptual action. 凯冰 should be personally operating, repairing, sorting, connecting, or supporting the strange low-tech structure, not standing beside it. Keep the red-star cap visible, the composition sparse, the line art hand-drawn, and the mood calm rather than cute or heroic.
```
