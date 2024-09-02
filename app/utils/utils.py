from aiogram import Bot
from app.services.binance_api import *
import asyncio
from app.keyboards import keyboards as kb


async def check_price_changes_last_hour(bot: Bot, chat_id: int, threshold: float, symbols: list):
    alerts = []

    for symbol in symbols:
        change_percent = await get_price_change_last_hour(symbol)

        if change_percent is not None and abs(change_percent) >= threshold:
            alerts.append(f"{symbol}: changed by {change_percent:.2f}% in the last hour!")

    if alerts:
        await bot.send_message(chat_id=chat_id, text="\n".join(alerts),
                               reply_markup=kb.stop_monitoring_keyboard())


async def start_monitoring(bot: Bot, chat_id: int, threshold: float):
    symbols = await get_top_10_crypto()

    while True:
        await check_price_changes_last_hour(bot, chat_id, threshold, symbols)
        await asyncio.sleep(10)
