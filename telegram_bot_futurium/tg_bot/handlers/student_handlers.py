# from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.utils.markdown import hlink

from tg_bot.keyboards.inline import create_inline_kb, finish_kb_student
from tg_bot.texts.texts import TEXTS
from tg_bot.misc.gsheets import worksheet_num, num_lessons_left


# Hendler for answer if this is a student
async def student_start(callback: CallbackQuery):
    keyboard = create_inline_kb(1, "review", "want_pay", "want_num_lesson")
    await callback.message.answer(TEXTS["student_q1"], reply_markup=keyboard)
    await callback.answer()


# Hendler for enter name
async def student_enter_name(callback: CallbackQuery):
    await callback.message.answer(TEXTS["enter_name"], parse_mode="HTML")
    await callback.answer()


# Handler for incorrect name
async def warning_not_name(message: Message):
    await message.answer(text=TEXTS["enter_name_error"], parse_mode="HTML")


# Handler for correct name and get a number of lessons
async def student_lessons_left(message: Message):
    name = message.text
    if name in worksheet_num.col_values(1):
        lessons_left = num_lessons_left(name)
        keyboard = create_inline_kb(2, "yes", "later")
        text = TEXTS["left_lessons_part_1"] + f"{lessons_left}" + TEXTS["left_lessons_paid"]
        await message.answer(text=text, reply_markup=keyboard)
    else:
        await message.answer(text=TEXTS["no_name"])
        await message.answer(TEXTS["enter_name"], parse_mode="HTML")


# Hendler for later pay
async def student_pay_later_thanks(callback: CallbackQuery):
    await callback.message.answer(TEXTS["good"])
    await callback.answer()


# Hendler for later pay
async def student_pay_in_advance(callback: CallbackQuery):
    # Handler for /contact command
    url = TEXTS["url"]
    text = hlink(TEXTS["payment"], url)
    await callback.message.answer(text)
    await callback.message.answer(TEXTS["thanks_after_pay"])
    await callback.message.answer(TEXTS["finish"], reply_markup=finish_kb_student)


def register_student(dp: Dispatcher):
    dp.register_callback_query_handler(student_start, text="student")
    dp.register_callback_query_handler(student_enter_name, text="want_num_lesson")
    dp.register_message_handler(student_lessons_left,
                                regexp='[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+\s+[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]')
    dp.register_callback_query_handler(student_pay_later_thanks, text="later")
    dp.register_callback_query_handler(student_pay_in_advance, text="yes")
    dp.register_message_handler(warning_not_name, content_types='any')
