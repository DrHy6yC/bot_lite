from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


download_guide_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Скачать!", url="https://t.me/QuickQuizFreeBot"),
        ],
    ]
)

start_questionnaire_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Начать опрос", callback_data="start_questionnaire"),
        ],
    ]
)


age_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Младше 15", callback_data="Младше 15"),
        ],
        [
            InlineKeyboardButton(text="15 - 20", callback_data="15 - 20"),
        ],
        [
            InlineKeyboardButton(text="21 - 35", callback_data="21 - 35"),
        ],
        [
            InlineKeyboardButton(text="Старше 36", callback_data="Старше 36"),
        ],

    ]
)

aim_key = InlineKeyboardMarkup(
    inline_keyboard=[
            [
                InlineKeyboardButton(text="Работа/Бизнес", callback_data="Работа/Бизнес"),
             ],
            [
                InlineKeyboardButton(text="Учеба", callback_data="Учеба"),
             ],
            [
                InlineKeyboardButton(text="Путешествия", callback_data="Путешествия"),
             ],
            [
                InlineKeyboardButton(text="Для себя", callback_data="Для себя"),
             ],
    ]
)

tutor_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="Да"),
            InlineKeyboardButton(text="Нет", callback_data="Нет")
        ]
    ]
)