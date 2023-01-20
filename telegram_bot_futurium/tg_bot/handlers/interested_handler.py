from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from tg_bot.keyboards.inline import create_inline_kb
from tg_bot.texts.texts import TEXTS


# Hendler for answer if this is a people, who interested in styding
async def interested_start(callback: CallbackQuery):
    keyboard = create_inline_kb(1, "format_education", "price", "english_level")
    await callback.message.answer(text=TEXTS["interested_q1"], reply_markup=keyboard)
    await callback.answer()

def register_interested_person(dp: Dispatcher):
    dp.register_callback_query_handler(interested_start, text="interested")
