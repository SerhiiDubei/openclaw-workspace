---
name: document-converter
description: Convert PDF and DOCX files to plain text for analysis. Use when you need to extract text content from documents.
---

# Document Converter

Convert PDF and DOCX files to plain text.

## Supported Formats
- PDF (.pdf)
- Word (.docx)

## Usage

### Convert PDF
```bash
python scripts/convert-pdf.py /path/to/file.pdf
```

### Convert DOCX
```bash
python scripts/convert-docx.py /path/to/file.docx
```

### Python API
```python
from scripts.convert_pdf import extract_text_from_pdf
text = extract_text_from_pdf("/path/to/file.pdf")
```

## Output
Plain text saved to stdout or specified output file.
