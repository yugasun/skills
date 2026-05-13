# Illustration Workflow

Use this file only when `Illustration Decision` is not `none`.

The decision block and illustration brief are workflow artifacts. Keep them in working notes or agent output, not in the final publishable blog Markdown, unless the user explicitly asks to retain them.

## Decision Rubric

Before generating any image, answer these four questions:

1. Is the article abstract enough or long enough that readers may benefit from visual pacing?
2. Do existing Mermaid diagrams and tables already carry the information effectively?
3. Will an image improve understanding, rhythm, or scene-setting instead of acting as decoration?
4. Why is the correct decision `none`, `cover-only`, or `cover-and-sections`?

Use this mapping:

| Decision | Use When | Default Action |
| --- | --- | --- |
| `none` | The article is short, concrete, or already well explained by Mermaid and tables | Do not generate images |
| `cover-only` | The article is long or abstract and benefits from one thesis-aligned cover image | Generate `cover.png` |
| `cover-and-sections` | The article is long and has 2+ meaningful conceptual transitions | Generate `cover.png` and `section-1.png` to `section-3.png` as needed |

If you cannot describe a concrete `scene_anchor`, fall back to `none`.

When the decision includes `cover.png`, prefer a banner-style cover by default. The visual goal is closer to a polished tech blog hero image than to a cinematic poster or character illustration.

## Brief Contract

Every generated image needs a structured brief.

Required fields:

- `slug`
- `image_role`
- `article_title`
- `article_mode`
- `core_thesis`
- `article_summary`
- `target_section`
- `image_purpose`
- `scene_anchor`
- `must_include_elements`
- `avoid_elements`
- `composition`
- `visual_mood`
- `keywords`

Rules:

- `scene_anchor` must describe one drawable scene or visual metaphor.
- `must_include_elements` should list concrete visual elements, not abstract adjectives.
- `avoid_elements` should actively block generic AI-art tropes that do not serve the article.
- Section images must not repeat the same scene anchor as the cover image.
- If Mermaid or tables already explain the structure, the image should support rhythm and theme, not duplicate the diagram.
- Cover images should default to banner composition: wide frame, clear focal area, generous whitespace for editorial breathing room, and no textual overlay baked into the image.

## Output Format

Use this structure for working notes, not for the final published article body:

```markdown
## Illustration Decision

- decision: [none / cover-only / cover-and-sections]
- rationale: [why this article needs or does not need images]

## Illustration Brief

- slug: [article slug]
- image_role: [cover / section-1 / section-2 / section-3]
- article_title: [article title]
- article_mode: [架构解读型 / 工具介绍型 / 方案实践型 / 对比分析型]
- core_thesis: [one-sentence thesis]
- article_summary:
  - [what problem the article studies]
  - [what mechanism, conflict, or tradeoff it explains]
  - [optional: scope or recommendation]
- target_section: [full-article or the matching H2 section]
- image_purpose: [题图 / 章节过渡图 / 概念氛围图]
- scene_anchor: [single drawable scene or metaphor]
- must_include_elements:
  - [element 1]
  - [element 2]
  - [element 3]
- avoid_elements:
  - [avoid 1]
  - [avoid 2]
  - [avoid 3]
- composition: [viewpoint, framing, whitespace direction]
- visual_mood: [restrained, structural, editorial, realistic, etc.]
- keywords:
  - [keyword 1]
  - [keyword 2]
  - [keyword 3]

## Image Generation Plan

- model: [qwen-image-2.0-pro / qwen-image-max / qwen-image-plus]
- mode: [sync / async]
- prompt_extend: [on / off]
- negative_prompt_profile: [baseline plus topic-specific exclusions]
- expected_output_dir: public/static/images/posts/<slug>/
- expected_files:
  - [cover.png / section-1.png / ...]
- markdown_targets:
  - [where each image will be inserted]
- block_if_failed: true
```

## Model Defaults

| Situation | Model | Mode | `prompt_extend` | Why |
| --- | --- | --- | --- | --- |
| Architecture analysis, mechanism breakdown, tool commentary | `qwen-image-2.0-pro` | `sync` | off | Best default for thesis fidelity |
| Realistic workspace, product scene, or physical environment | `qwen-image-max` | `sync` | off | Use only when the scene is already clear |
| Lower-cost exploration or explicit async need | `qwen-image-plus` | `async` | off | Use when cost or async execution matters |

Default generation settings:

- Aspect ratio: `16:9`
- Preferred size: `1664*928`
- Image count: `1`
- Default output directory: `public/static/images/posts/<slug>/`
- Default filenames: `cover.png`, `section-1.png`, `section-2.png`, `section-3.png`
- Keep `prompt_extend` off unless the first direction is semantically correct but visually under-specified

## Cover Banner Defaults

Use this default art direction for `cover.png` unless the article clearly needs a more literal scene:

- treat the cover as a modern tech blog banner, not a poster
- keep the composition clean, professional, and editorial
- prefer abstract or structural tech motifs over characters or literal mascots
- use a high-contrast dark or light background
- allow a warm orange accent near `#ef7070` when it helps the theme
- do not render text into the image
- avoid watermarks and decorative UI clutter

Preferred first-pass prompt shape for `cover.png`:

```text
Create a modern tech blog banner image for a Chinese technical article.

Title: <article_title>
Tags: <keywords or tags>
Summary: <article_summary condensed to one or two lines>

Style requirements:
- Clean, professional tech blog aesthetic
- Wide banner composition with one clear focal structure or metaphor
- Use orange (#ef7070) as a restrained primary accent when appropriate
- Dark or light background with high contrast
- No text required, focus on abstract tech concepts
- No watermark
```

If the output is too poster-like, too character-centric, or too cinematic, revise toward a flatter editorial banner with fewer subjects and stronger negative space.

## Generation Command

Primary script:

- `scripts/aliyun_image_gen.py`

Detailed API notes:

- [image generation API reference](aliyun-image-gen-api-reference.md)

Recommended first-pass command:

```bash
./scripts/aliyun_image_gen.py generate \
  "$PROMPT" \
  --model qwen-image-2.0-pro \
  --size '1664*928' \
  --image-count 1 \
  --negative-prompt "$NEGATIVE_PROMPT" \
  --no-prompt-extend \
  --download \
  --output-dir public/static/images/posts/<slug>
```

For `cover.png`, you may switch the size to a banner-friendly ratio such as `1024*512` when matching the公众号封面风格 is more important than keeping the generic 16:9 article default.

## Automatic OSS Upload

When the shell already exposes the required OSS environment variables, prefer a single command that generates, downloads, uploads, and returns remote URLs in one run:

```bash
./scripts/aliyun_image_gen.py generate \
  "$PROMPT" \
  --model qwen-image-2.0-pro \
  --size '1664*928' \
  --image-count 1 \
  --negative-prompt "$NEGATIVE_PROMPT" \
  --no-prompt-extend \
  --download \
  --output-dir public/static/images/posts/<slug> \
  --upload-to-oss \
  --upload-prefix "posts/<slug>" \
  --upload-manifest public/static/images/posts/<slug>/upload-manifest.json
```

This command keeps local files in `public/static/images/posts/<slug>/` and additionally returns remote image URLs through stdout or `--json` output.

## Manual OSS Upload Fallback

If images already exist locally and only the upload step needs to be rerun, use:

```bash
./scripts/upload_to_s3.py \
  public/static/images/posts/<slug> \
  "$S3_BUCKET" \
  --prefix "posts/<slug>" \
  --endpoint "$S3_ENDPOINT_URL" \
  --addressing-style path \
  --manifest public/static/images/posts/<slug>/upload-manifest.json
```

Supported configuration sources:

- `S3_BUCKET`
- `S3_ENDPOINT_URL`
- `S3_ACCESS_KEY_ID`
- `S3_SECRET_ACCESS_KEY`
- `S3_REGION`
- `S3_CUSTOM_DOMAIN`
- `S3_PUBLIC_BASE_URL`

Rules:

- Keep the generated local files even when upload succeeds; they remain the local source of truth.
- Prefer `S3_PUBLIC_BASE_URL` when the public CDN or OSS domain differs from the API endpoint.
- After a successful automatic upload, use the returned `remote_urls` or the JSON manifest to rewrite Markdown image references.
- If upload is not configured or fails, fall back to local `/static/images/...` paths and record the blocker.

## Negative Prompt Baseline

```text
low quality, blurry, low resolution, oversaturated, distorted anatomy, malformed hands, messy composition, random text, illegible text, watermark, logo, unrelated dashboard UI, generic futuristic interface, robot face, humanoid android, floating chip, glowing brain, generic neon sci-fi poster, oversimplified flat vector shapes, childish icon illustration
```

Prefer to explicitly suppress:

- robot heads, glowing brains, floating chips
- unrelated dashboards or fake HUD overlays
- generic neon cyberpunk skylines
- decorative vector blobs that do not express the thesis
- poster typography, title text baked into the image, or magazine-cover lettering

## Write-Back Rules

- Insert the cover image after frontmatter and before the first paragraph.
- Insert section images near the start of the matching top-level section.
- Use local Markdown paths when upload is not used or fails:

```markdown
![图片说明](/static/images/posts/<slug>/<file-name>.png)
```

- Use public URLs when OSS upload succeeds:

```markdown
![图片说明](https://<public-base-url>/posts/<slug>/<file-name>.png)
```

- Do not mix local and remote image paths within the same article unless the upload only partially succeeded and the partial fallback is explicitly documented.

## Failure Handling

Do not claim illustration is complete if any of these are still true:

- the image was not generated
- the asset was not saved to `public/static/images/posts/<slug>/`
- Markdown references were not inserted back into the article
- OSS upload was required but no usable public URLs were produced

If generation is blocked, preserve the brief and state the blocker clearly, for example:

- missing `ALIYUN_API_KEY`
- generation failed
- result is off-thesis and needs regeneration
- OSS credentials or public base URL not configured
- upload succeeded but no stable public URL could be derived

## Brief Self-Check

- If `scene_anchor` cannot be drawn as a specific scene, the brief is still too abstract.
- If `must_include_elements` are only words like “AI”, “future”, or “tech”, the brief is underspecified.
- If `avoid_elements` is empty, the model will drift toward generic imagery.
- If the cover and section images share the same scene anchor, the image set is not doing distinct jobs.
