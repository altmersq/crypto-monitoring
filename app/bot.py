import asyncio
from aiogram import Bot, Dispatcher
import logging
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv
from app.handlers import common_handlers
from app.cfg_reader import config


async def main():
    load_dotenv()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_routers(common_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
