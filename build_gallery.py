# build_gallery.py v1.2 - Final Path Correction
import os
import re

# --- CONFIGURATION (CORRECTED) ---
# The folder INSIDE 'docs' where your images are now stored.
IMAGE_SOURCE_FOLDER = "docs/art_gallery"

# The final HTML file that will be created or overwritten.
HTML_OUTPUT_FILE = "docs/art-gallery.html"

# --- HTML TEMPLATES ---
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bohemai Art Gallery</title>
    <style>
        :root {{
            --grid-color: rgba(255, 255, 255, 0.05); --text-primary: #e0e0e0;
            --text-secondary: #b0b0b0; --accent-color: #00bfff; --bg-dark-1: #121212;
            --bg-dark-2: #1a1a1a; --bg-dark-3: #333333; --font-main: 'Source Code Pro', monospace;
        }}
        body {{
            background-color: var(--bg-dark-1);
            background-image: linear-gradient(var(--grid-color) 1px, transparent 1px),
                              linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
            background-size: 30px 30px; color: var(--text-primary); font-family: var(--font-main);
            line-height: 1.6; margin: 0; padding: 0;
        }}
        .gallery-container {{ max-width: 1400px; margin: 0 auto; padding: 40px 20px; }}
        .gallery-header {{ text-align: center; border-bottom: 1px solid var(--bg-dark-3); margin-bottom: 40px; padding-bottom: 20px; }}
        .back-link {{ color: var(--text-secondary); text-decoration: none; display: block; margin-bottom: 20px; font-size: 0.9rem; }}
        .back-link:hover {{ color: var(--accent-color); }}
        h1 {{ font-size: 2.5rem; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.1em; }}
        .art-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }}
        .art-item a {{
            display: block;
            border: 2px solid var(--bg-dark-3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            overflow: hidden;
            background-color: var(--bg-dark-2);
            aspect-ratio: 16 / 9;
        }}
        .art-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}
        .art-item a:hover {{
            transform: scale(1.03);
            box-shadow: 0 0 25px rgba(0, 191, 255, 0.5);
            border-color: var(--accent-color);
        }}
    </style>
</head>
<body>
    <div class="gallery-container">
        <div class="gallery-header">
            <a href="index.html" class="back-link">< Back to The Bohemai Project</a>
            <h1>Bohemai Art Gallery</h1>
        </div>

        <div class="art-grid">
{gallery_items}
        </div>
    </div>
</body>
</html>
"""

# IMPORTANT: The image path is now simple because the HTML file and the image folder
# are SIBLINGS inside the 'docs' folder.
ART_ITEM_TEMPLATE = """
            <div class="art-item">
                <a href="LINK_TO_DEVIANTART_PAGE_HERE" target="_blank" rel="noopener noreferrer">
                    <img src="art_gallery/{filename}" alt="{alt_text}" loading="lazy">
                </a>
            </div>"""

def create_alt_text(filename):
    """Creates a clean, human-readable title from a filename."""
    return filename.replace('.webp', '').replace('-', ' ').title()

def main():
    """Scans the art folder and generates the complete HTML file for the gallery."""
    print(f"--- HTML Gallery Builder v1.2 ---")
    
    if not os.path.exists(IMAGE_SOURCE_FOLDER):
        print(f"🔴 ERROR: The source folder '{IMAGE_SOURCE_FOLDER}' was not found.")
        return

    image_files = [f for f in os.listdir(IMAGE_SOURCE_FOLDER) if f.endswith('.webp')]
    if not image_files:
        print(f"🔴 ERROR: No .webp images found in '{IMAGE_SOURCE_FOLDER}'.")
        return
        
    image_files.sort()
    print(f"✅ Found and sorted {len(image_files)} images.")

    all_html_items = []
    for filename in image_files:
        alt_text = create_alt_text(filename)
        item_html = ART_ITEM_TEMPLATE.format(filename=filename, alt_text=alt_text)
        all_html_items.append(item_html)

    final_grid_html = "".join(all_html_items)
    final_page_html = PAGE_TEMPLATE.format(gallery_items=final_grid_html)

    with open(HTML_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_page_html)

    print(f"\n--- MISSION COMPLETE ---")
    print(f"✅ Successfully built your new gallery.")
    print(f"   The file '{HTML_OUTPUT_FILE}' has been created/updated.")

if __name__ == "__main__":
    main()
