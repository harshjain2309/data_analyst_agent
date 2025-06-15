# app.py
import streamlit as st
from tools import DATAFRAMES
from main import load_file, run_agent_question
import os

st.set_page_config(page_title="Data Analyst Agent", layout="wide")
st.title("Data Analyst Agent using Llama-4 (Together.ai)")

# File uploader
uploaded_file = st.file_uploader("Upload your file (.txt, .csv, .pdf, .docx, .xlsx, .jpg)", type=["txt", "csv", "pdf", "docx", "xlsx", "xls", "png", "jpg", "jpeg"])

if uploaded_file:
    # Save file to disk
    file_path = f"temp/{uploaded_file.name}"
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load content
    doc_text, df_or_sheet = load_file(file_path)

    if doc_text:
        st.subheader("📄 Extracted Text:")
        st.text(doc_text[:2000])  # preview only

    if df_or_sheet is not None:
        if isinstance(df_or_sheet, dict):
            st.subheader("🧾 Excel Sheets Detected:")
            for sheet_name, df in df_or_sheet.items():
                st.write(f"**Sheet: {sheet_name}**")
                st.dataframe(df.head())
        else:
            st.subheader("🧾 CSV Preview:")
            st.dataframe(df_or_sheet.head())

    st.success("✅ File processed. You can now ask questions!")

# Question input
st.subheader("💬 Ask a Question")
user_question = st.text_input("Type your question:")

if user_question and uploaded_file:
    with st.spinner("Thinking..."):
        answer = run_agent_question(user_question)
    st.success("✅ Answer:")
    st.write(answer)

    if "plot.png" in answer:
        st.image("plot.png")