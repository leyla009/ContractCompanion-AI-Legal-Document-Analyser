import pypdf
from docx import Document

def extract_text_from_pdf(file_path):
    """Iterates through a PDF and extracts text layer data."""
    text = ""
    reader = pypdf.PdfReader(file_path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def extract_text_from_docx(file_path):
    """Iterates through paragraphs in a Microsoft Word file."""
    doc = Document(file_path)
    text = [paragraph.text for paragraph in doc.paragraphs]
    return "\n".join(text)

def extract_text(file_path, file_type):
    """Unified engine to router files by their specific type extension."""
    if file_type == "pdf":
        return extract_text_from_pdf(file_path)
    elif file_type == "docx":
        return extract_text_from_docx(file_path)
    elif file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format.")
