import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
