# from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from tg_bot.texts.texts import TEXTS


# Hendler for answer if this is a people, who interested in styding
async def interested_start(callback: CallbackQuery):
    await callback.message.answer(TEXTS["interested_q1"])
    await callback.answer()


def register_interested_start(dp: Dispatcher):
    dp.register_callback_query_handler(interested_start, text="interested")
