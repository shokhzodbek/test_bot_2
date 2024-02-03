from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import IsGroup
import logging

@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"assalomu alekum , {message.from_user.full_name}!")


@dp.message_handler(IsGroup(),text='salom')
@dp.message_handler(IsGroup(),text='hi')
async def hi (message: types.message):
    logging.info(message)
    await message.answer(f'va aleykum assalom,yaxshimisan!!{message.from_user.full_name}')
    