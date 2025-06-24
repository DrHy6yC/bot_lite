from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import  Message


from bot.config import SETTINGS
from bot.create_bot import bot
from bot.keyboard import start_questionnaire_key


router = Router(name="router_admin")

@router.message(
    Command("id_chat"),
    F.from_user.username.in_({SETTINGS.ID_ADMIN, SETTINGS.ID_SUPER_USER})
)
async def id_chat_and_user(message: Message) -> None:
    await message.answer(
        text=f"Чат: {message.chat.id}"
             f"Пользователь: {message.from_user.id}",
    )


@router.message(
    Command("download"),
    F.from_user.username.in_({SETTINGS.ID_ADMIN, SETTINGS.ID_SUPER_USER})
)
async def get_download(message: Message) -> None:
    await message.delete()
    await bot.send_message(
        chat_id=SETTINGS.ID_CHANNEL,
        text="Получить памятку",
        reply_markup=start_questionnaire_key,
    )
