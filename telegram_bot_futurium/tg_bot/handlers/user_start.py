from aiogram import Dispatcher
from aiogram.types import Message
from tg_bot.keyboards.inline import create_inline_kb
from tg_bot.texts.texts import TEXTS


# hendler for /start command
async def cmd_start(message: Message):
    text = TEXTS['hello']
    keyboard = create_inline_kb(2, "student", "interested")
    await message.answer(text, reply_markup=keyboard)





def register_cmd_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
