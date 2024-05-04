# For conversion from mp4/mkv to mp3:
from moviepy.editor import *
# To get the names of the files
import os

def get_names_of_songs(path):
    song_names=[]
    for root, dirs, files in os.walk(path):
        for name in files:
            # We only want to convert files that are .mkv or .mp4
            if name.endswith(("mkv","mp4")):
                song_names.append(name)
    return song_names

song_names = get_names_of_songs("Mp4_files")

for name in song_names:
    # Gets the .mkv/.mp4 file
    video = VideoFileClip("Mp4_files\\"+name)

    # Converts it to and .mp3 file and we want it to end with .mp3 so we change mkv/mp4 part with mp3
    sound = video.audio.write_audiofile("Mp3_files\\"+name.replace("mkv","mp3").replace("mp4","mp3"))