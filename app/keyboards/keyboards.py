from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def get_start_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            #InlineKeyboardButton(text="Configure", callback_data="configure"),
            InlineKeyboardButton(text="Start Monitoring", callback_data="start_monitoring")
        ]
    ])
    return keyboard


def stop_monitoring_keyboard():
    kb = [
        [KeyboardButton(text="Stop monitoring")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard=True)
    return keyboard
