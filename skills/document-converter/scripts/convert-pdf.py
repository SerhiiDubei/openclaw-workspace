#!/usr/bin/env python3
"""Convert PDF to plain text."""

import sys
import argparse

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    try:
        import pdfplumber
    except ImportError:
        print("Error: pdfplumber not installed. Run: pip install pdfplumber", file=sys.stderr)
        sys.exit(1)
    
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
    except Exception as e:
        print(f"Error reading PDF: {e}", file=sys.stderr)
        sys.exit(1)
    
    return text.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to text")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = parser.parse_args()
    
    text = extract_text_from_pdf(args.pdf_path)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text saved to {args.output}")
    else:
        print(text)
