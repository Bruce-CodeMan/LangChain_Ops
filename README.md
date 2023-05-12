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