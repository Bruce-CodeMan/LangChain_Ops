<!--
 * @Date: 2023-05-12 11:06:51
 * @Author: Bruce
 * @Description: 
-->
# 🦜️🔗 LangChain 

## **📖 How to read the PDF file**

**1. Using PyPDF2**

```
from PyPDF2 import PdfReader

pdf_reader = PdfReader("Your file path")

raw_text = ""
for i, v in enumerate(pdf_reader.pages):
    text = v.extract_text()
    if text:
        raw_text += text

print(raw_text[:10])
```

**2. Using PyPDFLoader**

```
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("Your file Path")

doc = loader.load()

print(doc[0])
```

**3. Using PyMuPDFLoader**

```
from langchain.document_loaders improt PyMuPDFLoader

loader = PyMuPDFLoader("Your file Path")

doc = loader.load()
```

## **🚀 How to choose the PDF method?**

```
PyMuPDFLoader is the fastest of the PDF parsing options, 
And contains detailed metadata about the PDF and its pages, 
As well as returns one document per page
```

## **👀 LangChain + PDF**

```
cd langchain_pdf

python main.py

# You can input the question what you want to know about the careforsow.pdf
# You can change your PDF file to query the questions.
```