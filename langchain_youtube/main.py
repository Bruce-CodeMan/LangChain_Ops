import os
import whisper
from langchain.llms import OpenAI
from langchain.document_loaders import YoutubeLoader, SRTLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI
from pytube import YouTube

# Imports Custome Function
from temp import utils

os.environ["OPENAI_API_KEY"] = "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"

# Download the youtube file
# loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=C_78DM8fG6E")

# result = loader.load()

# print(result)

# url = "https://www.youtube.com/watch?v=C_78DM8fG6E"

# video = YouTube(url, use_oauth=True, allow_oauth_cache=True)

# audio = video.streams.filter(only_audio=True).first()

# video_title = video.streams[0].title

# video.streams.get_highest_resolution().filesize

# audio = video.streams.get_audio_only()

# audio.download(output_path="temp")

# model = whisper.load_model("base")

# mp3_file_path = "./temp/sample.mp4"

# About one minute
# transcription = model.transcribe(mp3_file_path)

# utils.transcribe_audio(transcription)

# Use SRTLoader to read srt file
loader = SRTLoader("./temp/sample.srt")
data = loader.load()

# Split the data
text_splitter = TokenTextSplitter.from_tiktoken_encoder(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(data)

llm = OpenAI(temperature=0)
print("Starting to summarize the video")
chain = load_summarize_chain(llm, chain_type="refine", verbose=False)
print(chain.run(docs))
