from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import (CallbackQuery, Message, ContentType,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from tg_bot.keyboards.inline import create_inline_kb

from tg_bot.texts.texts import TEXTS


# Handler for /contact command
async def contact_command(message: Message):
    text = TEXTS["contact"]
    text_url = TEXTS["contact_url"]
    url = TEXTS["url"]
    keyboard_url = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text=text_url, url=url)
    keyboard_url.add(button)
    await message.answer(text, reply_markup=keyboard_url)


async def bot_echo(message: Message, state="*"):
    await message.answer(f"It's your echo: {message.text}")


def register_contact_command(dp):
    dp.register_message_handler(contact_command, commands='contact')


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state='*',
                                content_types=ContentType.ANY)
