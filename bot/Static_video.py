from moviepy.editor import AudioFileClip, ImageClip


class StaticVideoCreate:
    def init(self):
        pass

    def create_static_video(self, path_voice, path_image, path_out):
        # create the audio clip object
        audio_clip = AudioFileClip(path_voice)
        # create the image clip object
        image_clip = ImageClip(path_image)
        # use set_audio method from image clip to combine the audio with the image
        video_clip = image_clip.set_audio(audio_clip)
        # specify the duration of the new clip to be the duration of the audio clip
        video_clip.duration = audio_clip.duration
        # set the FPS to 1
        video_clip.fps = 10
        # write the resuling video clip
        video_clip.write_videofile(path_out)


# path_voice = 'mp3_voice/AwACAgIAAxkBAANaYzhI8MnYIfutJwo2MifBiRmPwcUAAmggAALVbcFJkmT4H3jApQQqBA.mp3'
# path_image = 'images/tet.jpg'
# path_out = 'videos/test.mp4'



