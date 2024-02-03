from aiogram import types

from loader import dp
import logging

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    logging.info(message)
    await message.answer(message.text)
