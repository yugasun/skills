# Interactive HTML Slide Generator

Generate high-quality, single-file HTML interactive slide decks. Use this skill when you need to create a presentation, slide deck, or PPT.

## Overview

This skill allows the agent to act as an expert Frontend Developer and Presentation Designer to generate "Keynote-quality" single-file HTML presentations. It uses a component-based approach with pre-defined templates and themes.

## Features

- **Single-file Output**: All CSS, JS, and HTML are bundled into a single `index.html` for easy sharing.
- **Interactive**: Javascript-based navigation and interactions.
- **Responsive**: Adapts to different screen sizes.
- **Themable**: Multiple built-in themes to choose from.

## Usage

When asking the agent to create slides, you can specify a theme or style. The agent will:

1.  **Select a Theme**: Based on your description (Cyberpunk, Corporate, Minimal, Nature).
2.  **Generate Content**: Structure your request into a logical slide outline.
3.  **Assemble**: Inject content, styles, and scripts into the HTML template.

## Available Themes

- **Cyberpunk** (Default): Dark, neon, futuristic.
- **Corporate**: Light, professional, clean blue/slate.
- **Minimal**: Stark, black & white, Swiss style.
- **Nature**: Calm, cream/green, elegant serif fonts.

## Directory Structure

- `SKILL.md`: The main skill definition and instructions for the agent.
- `examples/`: Example output to demonstrate capabilities.
- `templates/`:
    - `template.html`: The base HTML structure.
    - `scripts.js`: The client-side logic for the slides.
    - `layouts.md`: Definitions of available slide layouts.
- `themes/`: CSS files for the different visual themes.
