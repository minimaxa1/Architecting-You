# build_gallery.py v1.0 - The Automated HTML Generator
import os
import re

# --- CONFIGURATION ---
# The folder inside 'docs' where your final, compressed images are stored.
IMAGE_SOURCE_FOLDER = "docs/art_gallery"

# The final HTML file that will be created or overwritten.
HTML_OUTPUT_FILE = "docs/art-gallery-images.html"

# --- HTML TEMPLATES ---

# This is the main template for the entire page.
# The '{gallery_items}' placeholder will be replaced with the generated image grid.
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

# This is the template for a single image in the grid.
ART_ITEM_TEMPLATE = """
            <div class="art-item">
                <a href="LINK_TO_DEVIANTART_PAGE_HERE" target="_blank" rel="noopener noreferrer">
                    <img src="images/{filename}" alt="{alt_text}" loading="lazy">
                </a>
            </div>"""

def create_alt_text(filename):
    """Creates a clean, human-readable title from a filename."""
    return filename.replace('.webp', '').replace('-', ' ').title()

def main():
    """Scans the art folder and generates the complete HTML file for the gallery."""
    print(f"--- HTML Gallery Builder v1.0 ---")
    
    if not os.path.exists(IMAGE_SOURCE_FOLDER):
        print(f"🔴 ERROR: The source folder '{IMAGE_SOURCE_FOLDER}' was not found.")
        print(f"   Please make sure you have moved your compressed images into this folder.")
        return

    # Find all the .webp files in the art folder
    image_files = [f for f in os.listdir(IMAGE_SOURCE_FOLDER) if f.endswith('.webp')]
    
    if not image_files:
        print(f"🔴 ERROR: No .webp images found in '{IMAGE_SOURCE_FOLDER}'.")
        return
        
    # --- AUTO SORT SMARTS ---
    # Sort the files alphabetically for a consistent, predictable order.
    image_files.sort()
    print(f"✅ Found and sorted {len(image_files)} images.")

    all_html_items = []
    for filename in image_files:
        alt_text = create_alt_text(filename)
        
        # Populate the template for this single image
        item_html = ART_ITEM_TEMPLATE.format(
            filename=filename,
            alt_text=alt_text
        )
        all_html_items.append(item_html)

    # Join all the individual items into one big HTML block
    final_grid_html = "".join(all_html_items)
    
    # Inject the generated grid into the main page template
    final_page_html = PAGE_TEMPLATE.format(gallery_items=final_grid_html)

    # Write the final result to the output file
    with open(HTML_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_page_html)

    print(f"\n--- MISSION COMPLETE ---")
    print(f"✅ Successfully built your new gallery.")
    print(f"   The file '{HTML_OUTPUT_FILE}' has been created/updated.")
    print("\nNext steps:")
    print("1. Open the new art-gallery.html to review.")
    print("2. (Optional) Manually update the 'LINK_TO_DEVIANTART_PAGE_HERE' for each item.")
    print("3. Commit the 'docs' folder to GitHub.")

if __name__ == "__main__":
    main()