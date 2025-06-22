from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Создаем клавиатуру с инлайн-кнопками
my_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кнопка 1", callback_data="btn1"),
        ],
    ]
)