from postgresql import Database
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
db = Database()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)