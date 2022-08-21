import os
import logging
from gtts import gTTS # Google voice recognition engine
from dotenv import load_dotenv
from pydub import AudioSegment
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or '/help' command
    """
    greeting = ' 0 '  # TODO: Write a greeting message
    await message.reply(greeting)


@dp.message_handler(content_types=['text'])
async def send_audio(message: types.Message):
    """
    This handler get user text message and return audio message
    """
    text = message.text
    if len(text) > 40: # If text is too long, we decline the text
        text = "Слишком длинный текст, я пока слабый Интеллект. Приношу свои извинения."
    tts = gTTS(text=text, lang='ru') # text recognition to mp3
    tts.save('message.mp3')
    audio = open('message.mp3', 'rb')
    audio = AudioSegment.from_file('message.mp3', 'mp3')
    audio.export("message.ogg", format='mp3') # mp3 to ogg
    voice = open('message.ogg', 'rb') # creating voice message
    await message.reply_voice(voice)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
