from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

admin = [
    931619695,
    6314725426,
    421124124
]

storage = MemoryStorage()
TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
