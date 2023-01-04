import asyncio
import logging
from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

# from tg_bot.filters.admin import AdminFilter
from tg_bot.handlers.other_handlers import register_echo, register_contact_command
from tg_bot.handlers.user_start import register_cmd_start
from tg_bot.handlers.interested_handler import register_interested_start
from tg_bot.handlers.student_handlers import register_student_start

from tg_bot.config import load_config
from tg_bot.keyboards.menu_button import set_main_menu


logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    # dp.setup_middleware(EnvironmentMiddleware(config=config))
    pass


def register_all_filters(dp):
    #dp.filters_factory.bind(AdminFilter)
    pass


def register_all_handlers(dp):
    register_cmd_start(dp)
    register_contact_command(dp)
    register_student_start(dp)
    register_interested_start(dp)

    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage
    dp = Dispatcher(bot) # , storage=storage)

    await set_main_menu(dp)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
