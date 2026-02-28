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
version: '2026.02.04'
---

# Interactive HTML Slide Generator

## Instructions

Act as an expert Frontend Developer and Presentation Designer to generate a "Keynote-quality" single-file HTML presentation by assembling pre-defined components.

### 1. Preparation

First, read the reference files to load the design system and templates.
**Theme Selection**: Determine the visual theme based on the user's request:

- **Cyberpunk** (Default): Dark, neon, futuristic. Use `skills/slides/themes/cyberpunk.css`.
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
- **Constraints**:
  - Max 5-7 bullet points per slide.
  - Max 3-4 cards per slide.
  - Use `.scrollable` for code/tables.
  - Use `.compact` for dense content.
  - Split content into multiple slides if it exceeds limits.

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
- **Overflow Protection**: Always wrap potentially overflowing content (code blocks, long lists) in containers with explicit `min-height: 0` or `.scrollable` class.

## Content Guidelines

| Element | Max      | Action if Exceeded |
| ------- | -------- | ------------------ |
| Bullets | 7        | Split slide        |
| Cards   | 4        | Use Grid Compact   |
| Code    | 15 lines | Use `.scrollable`  |

**Code Block Formatting**: Always include explicit empty lines between commands/logical groups in code blocks for readability.

## Final Check

- **Theme Check**: Did you inject the correct CSS file based on user intent?
- **Script Check**: Is `[TOTAL_SLIDES_COUNT]` replaced with a number?
- **Structure Check**: Does the final HTML contain the full CSS and JS inline?
