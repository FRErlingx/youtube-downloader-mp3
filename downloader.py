from pytube import YouTube
import moviepy.editor as mp
import os

video_url = str(input("Insert YouTube video link/Insérer le lien d'une vidéo YouTube : "))

yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
video.download("C:\Users\%USERNAME%\Downloads")

file_path = "C:\Users\%USERNAME%\Downloads" + video.default_filename

clip = mp.AudioFileClip(file_path)
clip.write_audiofile("C:\Users\%USERNAME%\Downloads" + video.default_filename[:-4] + ".mp3")

os.remove(file_path)
