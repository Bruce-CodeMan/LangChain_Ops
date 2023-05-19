import os
from langchain.llms import OpenAI
from langchain.document_loaders import YoutubeLoader
from pytube import YouTube

os.environ["OPENAI_API_KEY"] = "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"

# loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=C_78DM8fG6E")

# result = loader.load()

# print(result)

url = "https://www.youtube.com/watch?v=C_78DM8fG6E"

video = YouTube(url, use_oauth=True, allow_oauth_cache=True)

audio = video.streams.filter(only_audio=True).first()

video_title = video.streams[0].title

video.streams.get_highest_resolution().filesize

audio = video.streams.get_audio_only()

audio.download(output_path="temp")