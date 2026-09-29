# 封面前向测试：构图、文字与宽幅裁切

测试主题：从多张动画截图推断房间空间，再做成可行走的 3D 网页。这里的房间是概念视觉，不宣称复现某个真实产品画面。使用 V2.3 强 Q 三分之四参考图，仅校准凯冰身份与身体设计，不把参考姿势当模板。图片由内置 `image_gen` 生成；缩略图以 240px 宽查看。

| 文件 | 实际尺寸 | 检查结果 |
|---|---:|---|
| `01-no-text.png` | 1672×941 | 无字、动作与角色身份清楚；适合作为约 16:9 横版母图，但帽子过于贴上沿，未通过更扁宽幅的安全区检查。 |
| `02-exact-text.png` | 1536×1024 | `Seed-2.1-pro-0915` 原图逐字正确；宽幅居中裁切会截断下沿文字，故不能作为宽幅成品。`02-wide-center-crop-thumb.png` 保留失败证据。 |
| `03-wide-safe-attempt.png` | 1916×821 | 宽幅安全，但 240px 缩略图中的长版本号太小；不能以“原图正确”代替缩略图可读。 |
| `04-wide-readable-text.png` | 1920×819 | 约 2.35:1 宽幅；文字逐字正确，240px 缩略图可读，白帽红星、脸、手势与微缩房间仍可辨。本轮宽幅有字测试通过。 |

`01-no-text-thumb.png`、`02-exact-text-thumb.png`、`03-wide-thumb.png`、`04-wide-readable-text-thumb.png` 是对应的实际缩略图。本测试没有在公众号编辑器内验证任何特定模板的二次裁切；正式文章仍需按最终展示位检查。

## 通过版的生成提示词

参考图：`kevinbee-illustrations/assets/ip-reference/v2.3/q-form-views/02-front-three-quarter.png`。

```text
Use case: ads-marketing. Asset type: FINAL very-wide article cover designed to be read at only 240 pixels total width. Exact landscape aspect around 2.35:1. Article theme: transforming animation screenshots into a walkable three-dimensional room. This is a single editorial scene, not a product screenshot. Make the ONLY in-image text exactly "Seed-2.1-pro-0915" with all hyphens, digits and periods correct. The title is the dominant information layer: bold, clean, high-contrast, at least 55% OF THE FULL CANVAS WIDTH and visibly legible when the whole cover is reduced to 240px wide. Do not use tiny lettering. Place title across an open spatial band around the action, with generous edge margins and no object crossing any letter. KevinBee, the exact strong-chibi character from the reference, occupies the other major focal region and is clearly visible at thumbnail size: large white baseball cap with one centered red star, ice-blue chin-length bob, calm red-orange eyes, compact strong-Q body with soft narrow shoulders, muted dark-red cardigan, ivory shirt, navy skirt. She is physically aligning one animation frame with the doorway of a small model room so the theme's causal action is clear. Compose title, character, and model as a single balanced wide cover; keep all vital elements away from the top, bottom and side edges. Warm hand-drawn editorial illustration, restrained background detail and strong silhouette, not a UI diagram. Reference controls identity/body design only, not pose. Absolutely no other words, captions, logos, watermarks, duplicate people, or combat imagery.
```

55% 字宽是本次长版本号的纠偏参数，不是 Skill 的固定封面模板。不同文章从自己的主题、文案长度与空间关系重新构图。
