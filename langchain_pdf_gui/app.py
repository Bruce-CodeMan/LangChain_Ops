'''
@Time          : 2023/05/22 16:17:18
@Author        : Bruce Hsu
@Description   : 
'''
import os
from io import BytesIO
import base64
from pathlib import Path
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 🖲️")

    # Upload the pdf File
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:
        loader = PyPDFLoader(pdf)
        print(loader)

if __name__ == '__main__':
    main()