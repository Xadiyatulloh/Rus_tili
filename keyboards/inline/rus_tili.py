from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

rus_tili = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Rus tili', callback_data="rus tili")
        ]
    ]
)