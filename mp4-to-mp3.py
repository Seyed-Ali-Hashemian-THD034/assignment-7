#mp4-to-mp3
from moviepy import editor

video = editor.VideoFileClip("rap-god-eminem-720p.mp4")
audio = video.audio
audio.write_audiofile("rap-god-eminem-720p.mp3")