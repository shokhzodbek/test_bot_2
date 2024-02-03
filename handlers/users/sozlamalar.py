from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.menu import menu

from loader import dp


@dp.message_handler(Command('sozlamalar'))
async def bot_info(message: types.Message):
    await message.answer(f"Sozlamalar, {message.from_user.full_name}!",reply_markup=menu)




@dp.message_handler(Command('darslar'))
async def bot_darslar(message: types.Message):
    await message.answer(f"shaxa darsa kun , {message.from_user.full_name}!")





