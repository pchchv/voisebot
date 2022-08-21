import os
import logging
from dotenv import load_dotenv
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
    greeting = ''  # TODO: Write a greeting message
    await message.reply(greeting)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
