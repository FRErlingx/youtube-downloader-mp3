from pytube import YouTube
import moviepy.editor as mp
import os

video_url = str(input("Insert YouTube video link/Insérer le lien d'une vidéo YouTube : "))

yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()

file_path = os.path.join("C:/Users/<Username>/Download", video.default_filename)
video.download("C:/Users/lilia/Music/New")

clip = mp.AudioFileClip(file_path)
new_file_path = os.path.join("C:/Users/<Username>/Download", video.default_filename[:-4] + ".mp3")
clip.write_audiofile(new_file_path)

os.remove(file_path)
