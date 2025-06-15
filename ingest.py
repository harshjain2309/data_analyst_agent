from PyPDF2 import PdfReader
from docx import Document
import pandas as pd
import pytesseract
from PIL import Image

def load_txt(path):
    return path.read_text()

def load_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def load_excel(path):
    dfs = pd.read_excel(path, sheet_name=None)
    return dfs  # dict of DataFrames

def load_csv(path):
    return pd.read_csv(path)

def load_image(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)