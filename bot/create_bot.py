from aiogram import Bot, Dispatcher

from bot.config import SETTINGS

TOKEN = SETTINGS.TG_TOKEN

dp = Dispatcher()

bot = Bot(token=TOKEN)
