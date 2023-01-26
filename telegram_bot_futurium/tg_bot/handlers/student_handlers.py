# from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from tg_bot.keyboards.inline import create_inline_kb, finish_kb_student, payment_kb
from tg_bot.texts.texts import TEXTS
from tg_bot.misc.gsheets import worksheet_num, num_class_left


# Hendler for answer if this is a student
async def student_start(callback: CallbackQuery):
    keyboard = create_inline_kb(1, "review", "want_pay", "want_num_lesson")
    await callback.message.answer(TEXTS["student_q1"], reply_markup=keyboard)
    await callback.answer()


# Hendler for enter name
async def student_enter_name(callback: CallbackQuery):
    await callback.message.answer(TEXTS["enter_name"], parse_mode="HTML")
    await callback.answer()


# Handler for correct name and get a number of lessons
async def student_lessons_left(message: Message):
    name = message.text
    if name in worksheet_num.col_values(2):
        class_left = int(num_class_left(name))
        keyboard = create_inline_kb(1, "yes", "later")
        if class_left >= 0:
            text = TEXTS["left_class_start"] + f"{class_left}" + TEXTS["left_class_paid"]
            await message.answer(text=text, reply_markup=keyboard)
        else:
            text = TEXTS["left_class_start"] + f"{abs(class_left)}" + TEXTS["left_class_no_paid"]
            await message.answer(text)
            await message.answer(TEXTS["payment"], reply_markup=payment_kb)
            await message.answer(TEXTS["thanks_after_pay"])
            await message.answer(TEXTS["finish"], reply_markup=finish_kb_student)
    else:
        await message.answer(text=TEXTS["no_name"])
        await message.answer(TEXTS["enter_name"], parse_mode="HTML")


# Hendler for later pay
async def student_pay_later_thanks(callback: CallbackQuery):
    await callback.message.answer(TEXTS["good"])
    await callback.message.answer(TEXTS["finish"], reply_markup=finish_kb_student)
    await callback.answer()


# Hendler for pay in advance
async def student_pay_in_advance(callback: CallbackQuery):
    await callback.message.answer(TEXTS["payment"], reply_markup=payment_kb)
    await callback.message.answer(TEXTS["thanks_after_pay"])
    await callback.message.answer(TEXTS["finish"], reply_markup=finish_kb_student)
    await callback.answer()


def register_student(dp: Dispatcher):
    dp.register_callback_query_handler(student_start, text="student")
    dp.register_callback_query_handler(student_enter_name, text="want_num_lesson")
    dp.register_message_handler(student_lessons_left,
                                regexp='[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+\s+[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]')
    dp.register_callback_query_handler(student_pay_later_thanks, text="later")
    dp.register_callback_query_handler(student_pay_in_advance, text="yes")
