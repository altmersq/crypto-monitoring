from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command
from app.keyboards import keyboards as kb
from aiogram.types import CallbackQuery
from app.services.binance_api import *
from app.utils.utils import *

router = Router()


monitoring_tasks = {}


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Hi! I can notify you about a change in one of the top 10 cryptocurrencies by more than 10%. "
        "You can change the settings by clicking on the \"configure\" button. To get started, "
        "click the \"start monitoring\" button.",
        reply_markup=kb.get_start_keyboard()
    )


@router.callback_query(F.data == "start_monitoring")
async def handle_start_monitoring(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id

    if chat_id in monitoring_tasks:
        await callback_query.answer("Monitoring is already running.")
        return

    await callback_query.answer("Monitoring started!")

    threshold = 0.1
    task = asyncio.create_task(start_monitoring(callback_query.bot, chat_id, threshold))
    monitoring_tasks[chat_id] = task


@router.message(F.text.lower() == "stop monitoring")
async def handle_stop_monitoring(message: Message):
    chat_id = message.chat.id

    if chat_id in monitoring_tasks:
        task = monitoring_tasks.pop(chat_id)
        task.cancel()
        await message.answer("Monitoring stopped!", reply_markup=kb.get_start_keyboard())
        await message.message.edit_text("Monitoring has been stopped.", reply_markup=kb.get_start_keyboard())
    else:
        await message.answer("No monitoring is running.", reply_markup=kb.get_start_keyboard())


