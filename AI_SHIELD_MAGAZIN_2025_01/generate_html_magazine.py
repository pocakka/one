#!/usr/bin/env python3
"""
AI Shield Magazin - HTML Generator
Converts all markdown articles to a single beautiful HTML magazine
"""

import os
import re
import json
from pathlib import Path
import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension

# Paths
BASE_DIR = Path(__file__).parent
CONTENT_DIR = BASE_DIR / "01_tartalom"
OUTPUT_FILE = BASE_DIR / "04_vegleges" / "magazin.html"
CONFIG_FILE = BASE_DIR / "00_metadata" / "config.json"
CSS_FILE = BASE_DIR / "03_sablonok" / "magazine_styles.css"

# Load config
with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Rovatok map
ROVATOK = {
    "hirek": {"name": "Hírek & Trendek", "icon": "📰"},
    "kezdoknek": {"name": "Kezdőknek", "icon": "🌱"},
    "csaladi": {"name": "Családi AI", "icon": "👨‍👩‍👧‍👦"},
    "vallalati": {"name": "Vállalati Fókusz", "icon": "🏢"},
    "szakertoi": {"name": "Szakértői Műhely", "icon": "🔬"},
    "termekkorkep": {"name": "Termékkörkép", "icon": "🛡️"},
    "interju": {"name": "Interjú", "icon": "💬"},
    "hasznos": {"name": "Hasznos", "icon": "🔧"},
}

def extract_metadata(content):
    """Extract YAML frontmatter from markdown"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1].strip()
            body = parts[2].strip()

            # Simple YAML parsing (not full spec, but works for our case)
            metadata = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip().strip('"')

            return metadata, body

    return {}, content

def convert_markdown_to_html(md_content):
    """Convert markdown to HTML with extensions"""
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'nl2br'
    ])

    html = md.convert(md_content)

    # Convert blockquotes with emoji prefixes to callout boxes
    html = re.sub(
        r'<blockquote>\s*<p>💡 \*\*TIPP:\*\*',
        '<div class="callout callout-tip"><p>',
        html
    )
    html = re.sub(
        r'<blockquote>\s*<p>⚠️ \*\*FIGYELEM:\*\*',
        '<div class="callout callout-warning"><p>',
        html
    )
    html = re.sub(
        r'<blockquote>\s*<p>🎯 \*\*GYORS ÖSSZEFOGLALÓ:\*\*',
        '<div class="callout callout-summary"><p>',
        html
    )
    html = html.replace('</p></blockquote>', '</p></div>')

    return html

def get_articles_by_rovat(rovat_dir):
    """Get all markdown files in a rovat directory"""
    articles = []
    rovat_path = CONTENT_DIR / rovat_dir

    if rovat_path.exists():
        for md_file in sorted(rovat_path.glob("*.md")):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            metadata, body = extract_metadata(content)
            articles.append({
                'filename': md_file.name,
                'metadata': metadata,
                'body': body,
                'html': convert_markdown_to_html(body)
            })

    return articles

def generate_cover_html():
    """Generate cover page HTML"""
    return f"""
    <div class="cover">
        <div class="cover-title">AI SHIELD</div>
        <div class="cover-subtitle">Védelem az AI korszakban</div>

        <!-- Placeholder for cover image -->
        <div style="
            width: 400px;
            height: 400px;
            background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.05));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 120px;
            margin: 2rem 0;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        ">🛡️</div>

        <div class="cover-issue">2025 Január | 1. szám</div>
        <div class="cover-tagline">Családoknak • Vállalatoknak • Szakértőknek</div>
        <div style="margin-top: 2rem; font-size: 0.9rem; opacity: 0.8;">
            26 cikk | 8 rovat | ~180 perc olvasás
        </div>
    </div>
    """

def generate_toc_html():
    """Generate table of contents"""
    toc_html = """
    <div class="toc">
        <h2>📖 Tartalomjegyzék</h2>
    """

    article_number = 1

    for rovat_dir, rovat_info in ROVATOK.items():
        articles = get_articles_by_rovat(rovat_dir)

        if articles:
            toc_html += f"""
        <div class="toc-section">
            <div class="toc-section-title">{rovat_info['icon']} {rovat_info['name']}</div>
            """

            for article in articles:
                title = article['metadata'].get('title', 'Untitled')
                toc_html += f"""
            <div class="toc-item">
                <span class="toc-item-number">{article_number}.</span>
                <span class="toc-item-title">{title}</span>
                <span class="toc-item-page">•</span>
            </div>
                """
                article_number += 1

            toc_html += """
        </div>
            """

    toc_html += """
    </div>
    """

    return toc_html

def generate_article_html(article, rovat_icon):
    """Generate HTML for a single article"""
    metadata = article['metadata']
    title = metadata.get('title', 'Untitled')
    read_time = metadata.get('readTime', '5 perc')
    difficulty = metadata.get('difficulty', 'Közép')

    # Placeholder image based on article filename
    img_name = Path(article['filename']).stem
    img_placeholder = f"""
    <div style="
        width: 100%;
        height: 300px;
        background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        color: white;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    ">{rovat_icon}</div>
    """

    return f"""
    <article class="article">
        <div class="article-meta">
            <span class="article-meta-item">📖 {read_time} olvasás</span>
            <span class="article-meta-item">🎯 {difficulty}</span>
        </div>

        <h2 class="article-title">{title}</h2>

        {img_placeholder}

        <div class="article-content">
            {article['html']}
        </div>
    </article>
    """

def generate_full_html():
    """Generate complete HTML magazine"""

    # Read CSS
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css_content = f.read()

    html = f"""
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Shield Magazin - 2025 Január</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">

    <style>
{css_content}
    </style>
</head>
<body>
    """

    # Add cover
    html += generate_cover_html()

    # Add TOC
    html += generate_toc_html()

    # Add all articles by rovat
    for rovat_dir, rovat_info in ROVATOK.items():
        articles = get_articles_by_rovat(rovat_dir)

        if articles:
            # Rovat header
            html += f"""
    <section class="section-header">
        <div class="section-header-icon">{rovat_info['icon']}</div>
        <h1 class="section-header-title">{rovat_info['name']}</h1>
    </section>
            """

            # Articles
            for article in articles:
                html += generate_article_html(article, rovat_info['icon'])

    # Footer
    html += """
    <footer style="
        text-align: center;
        padding: 3rem;
        background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
        color: white;
        margin-top: 3rem;
    ">
        <div style="font-size: 2rem; font-weight: 900; margin-bottom: 1rem;">AI SHIELD MAGAZIN</div>
        <div style="font-size: 1.2rem; margin-bottom: 1rem;">2025 Január | 1. szám</div>
        <div style="opacity: 0.9;">© 2025 AI Shield. Minden jog fenntartva.</div>
        <div style="margin-top: 1rem; opacity: 0.8;">info@aishield.hu | https://aishield.hu</div>
        <div style="margin-top: 2rem; font-size: 0.9rem;">
            <strong>Következő szám: 2026 Február - AI az oktatásban</strong>
        </div>
    </footer>

</body>
</html>
    """

    return html

def main():
    """Main execution"""
    print("🚀 AI Shield Magazin HTML Generator")
    print("=" * 50)

    # Generate HTML
    print("📝 Generating HTML...")
    html_content = generate_full_html()

    # Write to file
    print(f"💾 Writing to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Done! HTML magazine created:")
    print(f"   📄 {OUTPUT_FILE}")
    print(f"   📊 File size: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB")
    print()
    print("📖 To view: Open the HTML file in your browser")
    print("🖨️  To print to PDF: File → Print → Save as PDF")
    print()
    print("🎨 For better images, generate with DALL-E using:")
    print("   02_kepek/IMAGE_GENERATION_GUIDE.md")

if __name__ == "__main__":
    main()
