---
name: slides
description: Generate high-quality, single-file HTML interactive slide decks. Use this skill when the user asks to create a presentation, slide deck, or PPT.
trigger_keywords:
  - slide
  - slides
  - presentation
  - ppt
  - PPT
  - keynote
  - 演示文稿
  - 幻灯片
author: Yuga Sun
version: '2026.04.14'
---

# Interactive HTML Slide Generator

## Instructions

Act as an expert Frontend Developer and Presentation Designer to generate a "Keynote-quality" single-file HTML presentation by assembling pre-defined components.

### 1. Preparation

First, read the reference files to load the design system and templates.
**Theme Selection**: Determine the visual theme based on the user's request. **If the user does not specify a theme, always default to Cyberpunk.**

- **Cyberpunk** (**DEFAULT — use this when no theme is specified**): Dark, neon, futuristic. Use `skills/slides/themes/cyberpunk.css`.
- **Corporate**: Light, professional, clean blue/slate. Use `skills/slides/themes/corporate.css`.
- **Minimal**: Stark, black & white, Swiss style. Use `skills/slides/themes/minimal.css`.
- **Nature**: Calm, cream/green, elegant serif fonts. Use `skills/slides/themes/nature.css`.

Read the selected CSS file, plus:

- **Template**: `skills/slides/templates/template.html`
- **Scripts**: `skills/slides/templates/scripts.js`
- **Layouts**: `skills/slides/templates/layouts.md`

### 2. Content Strategy

- **Analyze**: Transform user input into a logical 8-12 slide outline.
- **Visuals**: Use **Nano Banana Pro** to generate high-quality images if needed.
- **Constraints** (CRITICAL — slides are fixed 1280×720px, overflow is hidden and will clip content):
  - Max **5** bullet points per slide (each bullet max 1-2 lines). If more, **must split** into multiple slides.
  - Max **3** cards per grid slide. 4 cards only with `.compact` class and very short card content (title + 1 line).
  - Max **10** lines of code. Longer code **must** use `.scrollable`.
  - Use `.compact` for dense content to reduce font sizes and spacing.
  - **Always prefer splitting into more slides** over cramming content. More slides is better than clipped content.
  - Each slide's text content (title + body) must fit within ~520px of vertical space (720px minus padding and title).
  - **Never nest** multiple content blocks (e.g., bullets + cards + code) on the same slide.

### 3. Assembly Process

Construct the single `index.html` file by injecting content into the template:

1.  **Load Template**: Start with the content of `template.html`.
2.  **Inject CSS**: Replace `/* CSS_INJECTION_POINT */` with the content of the **selected theme CSS file**.
3.  **Inject JS**: Replace `/* JS_INJECTION_POINT */` with the content of `scripts.js`.
    - **CRITICAL**: Inside the injected script, find `[TOTAL_SLIDES_COUNT]` and replace it with the actual integer number of slides (e.g., `12`).
4.  **Generate Slides**: Create HTML for each slide using patterns from `layouts.md`.
    - _Note for Minimal Theme_: When using grid layouts, ensure you strictly follow the HTML structure as CSS borders rely on precise nesting.
5.  **Inject Slides**: Replace `<!-- SLIDES_INJECTION_POINT -->` with the generated slide HTML.

### 4. Output

Save the final assembled file to `slides/<ppt-name>/dist/index.html`.

## Design Philosophy

- **Responsive**: The system uses a specific "vertical scroll on mobile, single slide on desktop" logic. **Do not modify the core media queries in the CSS.**
- **Overflow Protection**: The slide container has `overflow: hidden` — any content exceeding the 720px slide height **will be silently clipped and invisible** to the audience. This is the #1 quality issue to avoid.

### Overflow Prevention Rules

1. **Height Budget**: Each slide has ~520px usable content height (720px - 50px×2 padding - ~100px title). Plan content to fit within this budget.
2. **When in doubt, split**: It's always better to have 2 short slides than 1 overflowing slide.
3. **Use `.compact` class** on `slide-container` when content is borderline — it reduces font sizes and spacing.
4. **Use `.scrollable` class** on `content-area` for code blocks or tables that cannot be shortened.
5. **Avoid tall cards**: Card content should be title + 1-2 short lines max. Long descriptions inside cards will cause overflow.
6. **No stacking**: Do not stack a subtitle paragraph + bullets + cards on the same slide.

## Content Guidelines

| Element       | Max      | Action if Exceeded              |
| ------------- | -------- | ------------------------------- |
| Bullets       | **5**    | **Split into 2 slides**         |
| Cards         | **3**    | Use `.compact` or split slide   |
| Code lines    | **10**   | Use `.scrollable` on content-area |
| Subtitle text | 1 line   | Move details to next slide      |
| Card body     | 2 lines  | Shorten or split to bullets     |

**Code Block Formatting**: Always include explicit empty lines between commands/logical groups in code blocks for readability.

**Slide Splitting Strategy**: When content exceeds limits, split by sub-topic. For example:
- "Features" with 8 bullets → "Core Features" (4 bullets) + "More Features" (4 bullets)
- A slide with bullets + code → one slide for explanation, one for code example

## Final Check

- **Theme Check**: Did you inject the correct CSS file based on user intent?
- **Script Check**: Is `[TOTAL_SLIDES_COUNT]` replaced with a number?
- **Structure Check**: Does the final HTML contain the full CSS and JS inline?
- **Overflow Check** (CRITICAL): Review every slide — does any slide have more than 5 bullets, more than 3 cards, or mixed content types? If yes, split it. **No content should be clipped at the bottom of any slide.**
