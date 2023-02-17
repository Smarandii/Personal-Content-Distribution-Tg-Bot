from aiogram import Bot, Dispatcher, executor, types as aiogram_types
from PersonalContentDistributionTgBot.my_secrets import API_TOKEN
from aiogram.types import ContentType

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
