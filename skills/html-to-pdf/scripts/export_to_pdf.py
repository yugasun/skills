import os
from playwright.sync_api import sync_playwright

def export_to_pdf(input_path: str, output_path: str, debug: bool = False):
    """
    Export a presentation HTML file to PDF using Playwright in mobile emulation mode.
    
    Args:
        input_path: Path to the HTML file (local path or URL)
        output_path: Path where the PDF will be saved
        debug: If True, runs the browser in headed mode for inspection.
    """
    with sync_playwright() as p:
        # Use a custom viewport of 768px width to trigger the mobile breakpoint in CSS.
        # iPhone 12 Pro is 390px, but 768px is the exact max-width boundary in the CSS.
        # We also force 'is_mobile' to ensure mobile behaviors if any.
        browser = p.chromium.launch(headless=not debug)
        context = browser.new_context(
            viewport={'width': 768, 'height': 1024},
            is_mobile=True,
            device_scale_factor=2
        )
        page = context.new_page()

        # Handle file paths
        if not input_path.startswith(('http://', 'https://', 'file://')):
            abs_path = os.path.abspath(input_path)
            url = f'file://{abs_path}'
        else:
            url = input_path

        print(f"Loading {url} in mobile mode (768px)...")
        if debug:
            print("Debug mode enabled: Browser launched in headed mode.")
            
        page.goto(url)
        
        # Emulate screen media to ensure CSS @media (max-width: 768px) applies
        # instead of print styles which might differ or be missing.
        page.emulate_media(media="screen")
        
        # Inject CSS to force background printing
        page.add_style_tag(content="""
            body {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
        """)
        
        # Wait for content to stabilize
        # The chart simulation runs every 3000ms, but initial load should be quick.
        page.wait_for_load_state('networkidle')
        
        # Add a small buffer for JS execution (ECharts, etc)
        # Increased to 5s for better rendering stability
        page.wait_for_timeout(10000)

        # Get the full height of the page content
        total_height = page.evaluate("document.body.scrollHeight")
        print(f"Detected page height: {total_height}px")

        if debug:
            print("Page loaded. Pausing for inspection...")
            print("Press Enter in the terminal to proceed with PDF generation (or failure if headed)...")
            # In headed mode, we might want to just look at it.
            # page.pause() opens the inspector, which is better.
            page.pause()

        # Ensure directory exists for output
        output_dir = os.path.dirname(os.path.abspath(output_path))
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print(f"Generating PDF to {output_path}...")
        
        try:
            # Generate PDF
            # Use 'width' and 'height' instead of 'format' to capture the long page
            page.pdf(
                path=output_path,
                width='768px',
                height=f'{total_height}px',
                print_background=True
            )
            print("Export completed successfully.")
        except Exception as e:
            if debug:
                print(f"Could not generate PDF in debug (headed) mode: {e}")
                print("To generate the PDF, run without --debug.")
            else:
                raise e
        
        browser.close()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Export HTML to PDF")
    parser.add_argument("input", help="Input HTML file path or URL")
    parser.add_argument("output", help="Output PDF file path")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode with visible browser")
    
    args = parser.parse_args()
    export_to_pdf(args.input, args.output, args.debug)
