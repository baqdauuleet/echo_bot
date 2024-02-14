from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config

bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет! Я эхо-бот, я повторяю сообщения которые мне отправляют пользователи.')

@dp.message_handler()
async def process_echo_message(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)