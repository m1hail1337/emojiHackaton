import telebot
import os
import uuid
from voice_recognition import VoiceRecognizer
from random import randint

api_token = '5605341256:AAE2tBHd0HI5P_BZTdVjYdy-RpOhdpGoZ50'

bot = telebot.TeleBot(api_token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(content_types=["voice"])

def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    voice_file = bot.download_file(file_info.file_path)
    filename = str(randint(0, 100))
    file_name_full = "./voice/" + filename + ".ogg"
    file_name_full_converted = "./voice_2_mp3/" + filename + ".mp3"
    with open(file_name_full, 'wb') as new_file:
        new_file.write(voice_file)
    os.system(os.path.abspath("ffmpeg") + " -i " +
              file_name_full + "  " + file_name_full_converted)
    # with open('new_file.ogg', 'wb') as new_file:
    #     new_file.write(voice_file)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)