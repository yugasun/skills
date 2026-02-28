---
name: html-to-pdf
description: Export HTML files to PDF using Playwright with mobile emulation and custom viewport settings. Use this skill when the user asks to convert HTML to PDF, export presentations to PDF, or generate PDF documents from web pages.
---

# HTML to PDF Export

Export HTML files (local or URLs) to PDF using Playwright with configurable viewport and mobile emulation.

## Quick Start

Use the provided script to export HTML to PDF:

```bash
uv run {baseDir}/scripts/export_to_pdf.py input.html output.pdf
```

Export urls:

```bash
uv run {baseDir}/scripts/export_to_pdf.py https://example.com output.pdf
```

## Key Features

- **Mobile Emulation**: 768px viewport for mobile-optimized rendering
- **Background Printing**: Preserves colors and backgrounds
- **Dynamic Content**: Waits for JavaScript execution (ECharts, animations, etc.)
- **Full Page Capture**: Auto-detects page height for complete output
- **Debug Mode**: Visual inspection before PDF generation

## Technical Details

### Viewport Configuration

- **Width**: 768px (matches CSS `@media (max-width: 768px)` breakpoint)
- **Height**: 1024px initial, expands to full content
- **Device Scale**: 2x for retina displays
- **Mobile Mode**: Enabled to trigger mobile-specific behaviors

### Rendering Pipeline

1. **Load**: Opens URL in Chromium browser with mobile viewport
2. **Wait**: Network idle + 10s buffer for JS execution
3. **Measure**: Calculates full page height via `scrollHeight`
4. **Export**: Generates PDF with exact dimensions
5. **Cleanup**: Closes browser and context

### Wait Times

Default wait: **10 seconds** after network idle

Adjust for heavy JS/animations:

```python
# In export_to_pdf.py, modify:
page.wait_for_timeout(15000)  # 15 seconds
```

## Dependencies

Install Playwright:

```bash
pip install playwright
playwright install chromium
```

## Common Use Cases

1. **Slide Decks**: Export presentation HTML with animations and charts
2. **Reports**: Convert dynamic dashboards to static PDFs
3. **Documentation**: Generate PDF versions of web documentation
4. **Newsletters**: Archive HTML emails as PDFs

## Troubleshooting

### Missing Backgrounds

Already handled by injecting:
```css
body {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
```

### Content Cut Off

The script auto-detects page height. If issues persist:
- Check if content is position: fixed/absolute
- Verify viewport width triggers correct CSS breakpoints
- Increase wait timeout for slow-loading content

### Charts Not Rendering

Increase wait time in script:
```python
page.wait_for_timeout(15000)  # or more
```

## Script Reference

See `scripts/export_to_pdf.py` for the complete implementation. The script is self-contained and can be used directly from the command line or imported as a module.
