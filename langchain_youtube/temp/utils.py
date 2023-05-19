import os
from datetime import datetime


def transcribe_audio(segments):
    """
        Split the text into the srt file
    """
    video_filename = "./temp/sample"

    for segment in segments['segments']:
        start_time = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
        end_time = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
        text = segment['text']
        segment_id = segment['Id'] + 1
        segment = f"{segment_id}\n{start_time} --> {end_time}\n{text[1:] if text[0] == ' ' else text}\n"

        srt_filename = os.path.join(f"{video_filename}.srt")
        with open(srt_filename, 'a', encoding='utf-8') as f:
            f.write(segment)
        
    return srt_filename