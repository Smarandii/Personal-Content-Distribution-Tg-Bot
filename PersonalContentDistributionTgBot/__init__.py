from aiogram import Bot, Dispatcher, executor, types as aiogram_types
from aiogram.types import ContentType
import os

bot = Bot(token=os.environ['API_TOKEN'])
dp = Dispatcher(bot)
