'''
Date: 2023-05-12 11:07:30
Author: Bruce
Description: 
'''

import os
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Set the Environment variable, just change your own account
os.environ["OPENAI_API_KEY"] = "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"

# Read the PDF
loader = PyMuPDFLoader("./careforsow.pdf")
doc = loader.load()

# If the file is a long document, you can split up
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# pages = splitter.split_documents(doc)

# Use Chromadb to store the vectors
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(doc, embeddings)

# Use retriever to index
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Create QA chain to question answer
chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Question Answering
while True:
    query = input("please input the question what you want to know?\n")
    result = chain({"query": query})
    print(result["result"])