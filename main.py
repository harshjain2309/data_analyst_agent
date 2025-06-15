# main.py
from pathlib import Path
from ingest import load_txt, load_docx, load_pdf, load_csv, load_excel, load_image
from vectorstore import create_vectorstore_from_text
from tools import DATAFRAMES
from agent import get_agent

def load_file(filepath: str):
    path = Path(filepath)
    ext = path.suffix.lower()

    if ext == ".txt":
        return load_txt(path), None
    elif ext == ".docx":
        return load_docx(path), None
    elif ext == ".pdf":
        return load_pdf(path), None
    elif ext == ".csv":
        df = load_csv(path)
        DATAFRAMES["main"] = df
        return "", df
    elif ext in [".xls", ".xlsx"]:
        sheets = load_excel(path)
        DATAFRAMES.update(sheets)
        return "", sheets
    elif ext in [".png", ".jpg", ".jpeg"]:
        return load_image(path), None
    else:
        return "Unsupported file type", None

def run_agent_question(question):
    agent = get_agent()
    return agent.run(question)

if __name__ == "__main__":
    filepath = input("Enter path to file: ")
    question = input("Ask something about your data: ")

    doc_text, tables = load_file(filepath)

    if doc_text:
        vs = create_vectorstore_from_text(doc_text)

    response = run_agent_question(question)
    print("Answer:", response)