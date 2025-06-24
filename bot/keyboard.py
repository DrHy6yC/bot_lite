from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="К памятке", callback_data="start_questionnaire"),
        ],
        [
            InlineKeyboardButton(text="Записаться на бесплатное пробное занятие", url="https://t.me/m/oezso4AyYzNi"),
        ],
    ]
)

start_questionnaire_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить памятку", callback_data="get_guide"),
        ],
    ]
)
start_alert_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", url="https://t.me/QuickQuizFreeBot"),
            InlineKeyboardButton(text="Нет", url="https://t.me/QuickQuizFreeBot"),
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

signup_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Записаться на бесплатное пробное занятие", url="https://t.me/m/oezso4AyYzNi"),
        ]
    ]
)