#!/usr/bin/env python3
"""
AI Security Magazine PDF Generator
Converts HTML to professional PDF using WeasyPrint
"""

from weasyprint import HTML
import os

def generate_pdf():
    """Generate PDF from HTML template"""

    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, 'content', 'issue-01.html')
    output_path = os.path.join(base_dir, 'output', 'AI_Security_Magazine_Issue_01.pdf')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("🚀 Generating AI Security Magazine PDF...")
    print(f"   HTML Source: {html_path}")
    print(f"   Output: {output_path}")

    # Convert HTML to PDF
    try:
        HTML(filename=html_path).write_pdf(output_path)

        # Get file size
        file_size = os.path.getsize(output_path)
        file_size_mb = file_size / (1024 * 1024)

        print(f"\n✅ PDF successfully generated!")
        print(f"   File size: {file_size_mb:.2f} MB")
        print(f"   Location: {output_path}")

        return output_path

    except Exception as e:
        print(f"\n❌ Error generating PDF: {e}")
        raise

if __name__ == "__main__":
    generate_pdf()
