from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tg_bot.texts.texts import TEXTS

def create_inline_kb(row_width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    inline_kb = InlineKeyboardMarkup(row_width=row_width)
    if args:
        [inline_kb.insert(InlineKeyboardButton(
                            text=TEXTS[button],
                            callback_data=button)) for button in args]
    if kwargs:
        [inline_kb.insert(InlineKeyboardButton(
                            text=text,
                            callback_data=button)) for button, text in kwargs.items()]
    return inline_kb
