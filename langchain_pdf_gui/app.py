'''
@Time          : 2023/05/22 16:17:18
@Author        : Bruce Hsu
@Description   : 
'''
import os
import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 🖲️")

    # Upload the pdf FIle
    pdf = st.file_uploader("Upload your PDF", type="pdf")

if __name__ == '__main__':
    main()