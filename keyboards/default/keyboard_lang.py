from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

langs = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('rus')
        ],
        [
            KeyboardButton('eng')
        ]
    ], resize_keyboard=True
)
