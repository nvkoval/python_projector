import asyncio
import logging
from aiogram import Bot, Dispatcher, types
# from aiogram import Command
from bot.config import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher(bot)

# Hendler for /start command
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Hey! \
Вітаємо у Futurium English School боті - \
твоєму помічнику на шляху у вивченні англійської💛 \
\nЩоб ми могли вам краще допомогти - \
підкажіть нам ваш статус у школі ⬇️")

# Polling new updates
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
