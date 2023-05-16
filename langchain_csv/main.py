'''
Date: 2023-05-12 14:59:21
Author: Bruce
Description: 
'''
import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Set the Environment variable, just change your own account
os.environ["OPENAI_API_KEY"] = "sk-xxx"

# Load the csv file
loader = CSVLoader(file_path="./price.csv",
                    csv_args={
                        'delimiter': ',',
                        'fieldnames': [
                            'prodName', 
                            'prodCat', 
                            'lowPrice', 
                            'highPrice', 
                            'avgPrice', 
                            'pubDate', 
                            'unitInfo', 
                            'place'
                        ]
                    })

data = loader.load()

print(data[0])

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()

# Store the vectors
db = Chroma.from_documents(data, embeddings)

# Use RetrievalQA Chain
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever, input_key="question")

while True:
    query = input("Please input the question what you want to know?\n")
    resp = qa({"question": query})
    print(resp)