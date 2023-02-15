import logging
import json
import random
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from decouple import config
API_TOKEN = config('TELE_API_KEY')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

folder_answers ='lesson21/answers'
init_file = json.load(open(folder_answers+'init.json', 'r', encoding='utf-8'))
def get_random_answer(path):
     with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")




@dp.message_handler()
async def echo(message: types.Message):
   if message.text in init_file:
    path = folder_answers + init_file[message.text]
    answer = get_random_answer (path)
    await message.answer(answer)
   else:
    await message.answer
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)