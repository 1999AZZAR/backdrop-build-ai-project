from pydub import AudioSegment

audio = AudioSegment.from_file("/media/azzar/Betha/Download/project/telegram bot/response.mp3", format="mp3")
speedup = audio.speedup(playback_speed=1.2)
speedup.export("final.wav", format="wav")

