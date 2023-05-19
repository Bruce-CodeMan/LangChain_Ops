import os
from langchain.llms import OpenAI
from langchain.document_loaders import YoutubeLoader

os.environ["OPENAI_API_KEY"] = "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"

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=C_78DM8fG6E")

result = loader.load()

print(result)