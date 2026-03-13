#!/usr/bin/env python3
"""Convert DOCX to plain text."""

import sys
import argparse

def extract_text_from_docx(docx_path):
    """Extract text from DOCX file."""
    try:
        from docx import Document
    except ImportError:
        print("Error: python-docx not installed. Run: pip install python-docx", file=sys.stderr)
        sys.exit(1)
    
    text = ""
    try:
        doc = Document(docx_path)
        paragraphs = []
        for para in doc.paragraphs:
            if para.text.strip():
                paragraphs.append(para.text)
        text = "\n\n".join(paragraphs)
    except Exception as e:
        print(f"Error reading DOCX: {e}", file=sys.stderr)
        sys.exit(1)
    
    return text.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert DOCX to text")
    parser.add_argument("docx_path", help="Path to DOCX file")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = parser.parse_args()
    
    text = extract_text_from_docx(args.docx_path)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text saved to {args.output}")
    else:
        print(text)
