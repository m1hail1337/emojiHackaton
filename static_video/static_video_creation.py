from moviepy.editor import AudioFileClip, ImageClip


class StaticVideoCreate:
    def __init__(self):
        pass

    def create_static_video(self):
        # create the audio clip object
        audio_clip = AudioFileClip("voice.mp3")
        # create the image clip object
        image_clip = ImageClip("smile.jpg")
        # use set_audio method from image clip to combine the audio with the image
        video_clip = image_clip.set_audio(audio_clip)
        # specify the duration of the new clip to be the duration of the audio clip
        video_clip.duration = audio_clip.duration
        # set the FPS to 1
        video_clip.fps = 1
        # write the resuling video clip
        video_clip.write_videofile("output.mp4")

video_creator = StaticVideoCreate()
video_creator.create_static_video()
