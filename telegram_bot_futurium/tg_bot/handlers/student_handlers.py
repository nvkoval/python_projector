# from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from tg_bot.texts.texts import TEXTS

# Hendler for answer if this is a student
async def student_start(callback: CallbackQuery):
    await callback.message.answer(TEXTS["student_q1"])
    await callback.answer()


def register_student_start(dp: Dispatcher):
    dp.register_callback_query_handler(student_start, text="student")
