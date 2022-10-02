from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pathlib import Path
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
import os
import asyncio

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN
from cut_image import cutting
from Static_video import StaticVideoCreate


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

video_creator = StaticVideoCreate()

button_hi = KeyboardButton('Получить видео 📹')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message, ):
    me = await bot.get_me()
    your_name = message.from_user.first_name
    await message.answer(
        f'Привет, {your_name}!\nЧтобы создать клевую эмоцию тебе понадобиться классная картинка и короткий трек',
                         reply_markup=greet_kb)
    await message.answer(f'Отправь мне картинку прямо сюда')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    # await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

    msg = text(bold('Я могу ответить на следующие команды:'),
               '/voice', '/photo', '/group', '/note', '/file', '/testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


async def handle_file(file: types.File, path: str):
    await bot.download_file(file_path=file.file_path, destination=path)


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def voice_message_handler(message: types.Message):
    user_id = message.from_user.id
    voice = await message.voice.get_file()
    path = f'mp3_voice/{user_id}.mp3'
    await handle_file(file=voice, path=path)


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def doc_handler(message: types.Message):
    user_id = message.from_user.id
    audio = await message.audio.get_file()
    path = f'mp3_voice/{user_id}.mp3'
    await handle_file(file=audio, path=path)


@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    image = await message.photo[-1].get_file()
    path = f'images/{user_id}.jpg'
    await handle_file(file=image, path=path)


@dp.message_handler(lambda message: message.text == "Получить видео 📹")
async def process_note_command(message: types.Message):

    user_id = message.from_user.id
    path_voice = f'mp3_voice/{user_id}.mp3'
    path_image = f'images/{user_id}.jpg'
    path_video = f'videos/{user_id}.mp4'
    cutting(path_image, path_image)
    video_creator.create_static_video(path_voice, path_image, path_video)
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
    await bot.send_video_note(message.from_user.id, video_note=open(path_video, 'rb'))



# @dp.message_handler(commands=['in_num'])
# async def get_number(message: types.Message):
#     user_id = message.from_user.id
#     await message.reply("Напиши свое число")

# @dp.message_handler(commands=['out_num'])
# async def give_number(message: types.Message):
#     user_id = message.from_user.id
#     await message.reply(f"Вот твое число: ")


# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def get_number(message: types.Message):
#     num = message.text
#     # num = message.text
#     with open(f'text_from_user/{message.from_user.id}.txt','w') as file:
#         file.write(num)

if __name__ == '__main__':
    executor.start_polling(dp)


