from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import IsPrivate
import logging

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"assalomu alekum , {message.from_user.full_name}!")
    

@dp.message_handler(IsPrivate(),text='salom')
@dp.message_handler(IsPrivate(),text='hi')
async def hi (message: types.message):
    logging.info(message)
    await message.answer(f'assalomu alekum  va aleykum assalom,yaxshimisiz!!  {message.from_user.full_name}')
    