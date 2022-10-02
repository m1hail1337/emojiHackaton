import os;

class MusicCutter:
    def __init__(self):
        pass
    def cut(self, start_sec, end_sec):
        duration = end_sec - start_sec
        os.system(os.path.abspath("ffmpeg.exe") + ' -ss ' + str(start_sec) + ' -i "output\\195. Evanescence — Bring Me To Life.mp3" -t ' + str(duration) + ' -c copy "cuts\\195. Evanescence — Bring Me To Life.mp3"')

mc = MusicCutter()

mc.cut(10, 12)