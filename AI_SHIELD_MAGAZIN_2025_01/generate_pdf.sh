#!/bin/bash
# AI Shield Magazin - PDF Generator Script

echo "📄 AI Shield Magazin - PDF Generator"
echo "===================================="
echo ""

# Check if wkhtmltopdf is installed
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "❌ wkhtmltopdf not found!"
    echo ""
    echo "Install it:"
    echo "  Ubuntu/Debian: sudo apt-get install wkhtmltopdf"
    echo "  Mac: brew install wkhtmltopdf"
    echo "  Windows: https://wkhtmltopdf.org/downloads.html"
    echo ""
    echo "Or use browser: Open magazin.html → Ctrl+P → Save as PDF"
    exit 1
fi

# Paths
HTML_FILE="04_vegleges/magazin.html"
PDF_FILE="04_vegleges/AI_Shield_Magazin_2025_01.pdf"

# Check if HTML exists
if [ ! -f "$HTML_FILE" ]; then
    echo "❌ HTML file not found: $HTML_FILE"
    echo "Run: python3 generate_html_magazine.py"
    exit 1
fi

echo "📝 Converting HTML to PDF..."
echo "   Input: $HTML_FILE"
echo "   Output: $PDF_FILE"
echo ""

# Generate PDF
wkhtmltopdf \
  --enable-local-file-access \
  --print-media-type \
  --page-size A4 \
  --margin-top 10mm \
  --margin-bottom 10mm \
  --margin-left 15mm \
  --margin-right 15mm \
  --enable-javascript \
  --javascript-delay 1000 \
  --no-stop-slow-scripts \
  --title "AI Shield Magazin - 2025/01" \
  "$HTML_FILE" \
  "$PDF_FILE"

# Check if successful
if [ $? -eq 0 ]; then
    FILE_SIZE=$(du -h "$PDF_FILE" | cut -f1)
    echo ""
    echo "✅ PDF Successfully Generated!"
    echo "   📄 File: $PDF_FILE"
    echo "   📊 Size: $FILE_SIZE"
    echo ""
    echo "📖 Open with:"
    echo "   Linux: xdg-open $PDF_FILE"
    echo "   Mac: open $PDF_FILE"
    echo "   Windows: start $PDF_FILE"
else
    echo ""
    echo "❌ PDF generation failed!"
    echo "Try browser method: Open $HTML_FILE → Print → Save as PDF"
fi
