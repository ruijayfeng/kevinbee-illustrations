#!/usr/bin/env python3
"""Validate the active KevinBee skill package without third-party dependencies."""

from __future__ import annotations

import hashlib
import re
import struct
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/ip-core.md",
    "references/character-model-v2.2.md",
    "references/article-body-style.md",
    "references/article-body-prompt.md",
    "references/composition-patterns.md",
    "references/qa-checklist.md",
    "assets/manifest.yaml",
    "assets/ip-reference/v2.1/00-canonical-master.png",
    "assets/ip-reference/v2.1/01-turnaround-five-view.png",
    "assets/ip-reference/v2.1/02-head-construction-four-view.png",
    "assets/ip-reference/v2.1/03-article-form-master.png",
    "assets/ip-reference/v2.1/04-standard-to-article-scale.png",
    "assets/ip-reference/v2.1/05-article-form-four-view.png",
    "assets/ip-reference/v2.1/article-views/01-front.png",
    "assets/ip-reference/v2.1/article-views/03-left-profile.png",
    "assets/ip-reference/v2.1/article-views/04-back.png",
    "assets/ip-reference/v2.2/00-q-form-master-front.png",
    "assets/ip-reference/v2.2/01-q-form-four-view.png",
    "assets/ip-reference/v2.2/q-form-views/02-front-three-quarter.png",
    "assets/ip-reference/v2.2/q-form-views/03-left-profile.png",
    "assets/ip-reference/v2.2/q-form-views/04-back.png",
    "assets/ip-reference/v2.2/02-expression-sheet.png",
    "assets/ip-reference/v2.2/03-action-sheet.png",
    "assets/ip-reference/v2.1/head-views/01-front.png",
    "assets/ip-reference/v2.1/head-views/02-front-three-quarter.png",
    "assets/ip-reference/v2.1/head-views/03-left-profile.png",
    "assets/ip-reference/v2.1/head-views/04-back.png",
    "assets/ip-reference/v2.1/turnaround-views/01-front.png",
    "assets/ip-reference/v2.1/turnaround-views/03-left-profile.png",
    "assets/ip-reference/v2.1/turnaround-views/04-rear-three-quarter.png",
    "assets/ip-reference/v2.1/turnaround-views/05-back.png",
    "assets/ip-reference/kevinbee-v2-article.png",
    "assets/ip-reference/kevinbee-v2-standard.png",
    "assets/ip-reference/expression-sheet.png",
    "assets/ip-reference/action-sheet.png",
    "assets/article-examples/information-overload.png",
    "assets/article-examples/decision-path.png",
    "assets/article-examples/v2.2-choice-release.png",
    "assets/forward-tests/v2.2-choice-release-source.png",
)

ACTIVE_TEXT_GLOBS = ("*.md", "*.yaml")
STALE_REFERENCES = (
    "references/kevinbee-ip.md",
    "references/style-dna.md",
    "references/prompt-template.md",
    "assets/examples/",
)
STALE_COPY = (
    "猩红色连帽斗篷",
    "黑色战斗裙",
    "剑是动作工具",
    "像一位安静的现场操作员",
)


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        header = stream.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", header[16:24])


def active_text_files() -> list[Path]:
    files: list[Path] = []
    for pattern in ACTIVE_TEXT_GLOBS:
        files.extend(SKILL_ROOT.rglob(pattern))
    return sorted(set(files))


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (SKILL_ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = SKILL_ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        if not skill.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        if "name: kevinbee-illustrations" not in skill:
            errors.append("SKILL.md name must be kevinbee-illustrations")
        if not re.search(r"^description: .+", skill, re.MULTILINE):
            errors.append("SKILL.md must have a non-empty description")
        for reference in (
            "references/ip-core.md",
            "references/character-model-v2.2.md",
            "references/article-body-style.md",
            "references/article-body-prompt.md",
            "references/composition-patterns.md",
            "references/qa-checklist.md",
            "assets/manifest.yaml",
        ):
            if reference not in skill:
                errors.append(f"SKILL.md does not route to {reference}")

    openai_yaml = SKILL_ROOT / "agents/openai.yaml"
    if openai_yaml.is_file():
        metadata = openai_yaml.read_text(encoding="utf-8")
        if "$kevinbee-illustrations" not in metadata:
            errors.append("agents/openai.yaml default_prompt must mention $kevinbee-illustrations")
        if 'allow_implicit_invocation: true' not in metadata:
            errors.append("implicit invocation policy changed unexpectedly")

    for text_path in active_text_files():
        text = text_path.read_text(encoding="utf-8")
        for stale in STALE_REFERENCES:
            if stale in text:
                relative = text_path.relative_to(SKILL_ROOT)
                errors.append(f"stale active reference in {relative}: {stale}")
        for stale in STALE_COPY:
            if stale in text:
                relative = text_path.relative_to(SKILL_ROOT)
                errors.append(f"stale V1 character copy in {relative}: {stale}")

    manifest_path = SKILL_ROOT / "assets/manifest.yaml"
    if manifest_path.is_file():
        manifest = manifest_path.read_text(encoding="utf-8")
        for relative in re.findall(r'^\s*- file: "([^"]+)"', manifest, re.MULTILINE):
            if not (SKILL_ROOT / "assets" / relative).is_file():
                errors.append(f"manifest points to missing asset: {relative}")

    article_examples = SKILL_ROOT / "assets/article-examples"
    if article_examples.is_dir():
        for image_path in sorted(article_examples.glob("*.png")):
            try:
                width, height = png_dimensions(image_path)
            except ValueError as exc:
                errors.append(f"invalid image {image_path.name}: {exc}")
                continue
            if width * 9 != height * 16:
                errors.append(
                    f"article example is not 16:9: {image_path.name} ({width}x{height})"
                )

    hashes: dict[str, Path] = {}
    assets_root = SKILL_ROOT / "assets"
    if assets_root.is_dir():
        for image_path in sorted(assets_root.rglob("*.png")):
            digest = hashlib.sha256(image_path.read_bytes()).hexdigest()
            if digest in hashes:
                first = hashes[digest].relative_to(SKILL_ROOT)
                second = image_path.relative_to(SKILL_ROOT)
                errors.append(f"duplicate active assets: {first} and {second}")
            else:
                hashes[digest] = image_path

    if errors:
        print("KevinBee skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("KevinBee skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
