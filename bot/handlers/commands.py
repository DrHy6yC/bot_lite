from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboard import start_questionnaire_key
from bot.state.state import LidFSM
from bot.utils import get_bot_name


router = Router(name="commands")


@router.message(Command("start"))
async def command_start(message: Message, state: FSMContext, bot: Bot) -> None:
    bot_name = await get_bot_name(bot)
    await message.answer(
        text=f"Привет, {message.from_user.first_name}!\n"
             f"Это Бот - {bot_name}, я задам вам три вопроса, ответив на которые, вы получите бесплатную памятку\n"
             f"'Как звучать естественно: фразы, которые вы не найдете в учебниках'",
        reply_markup=start_questionnaire_key,
    )
    await state.set_state(LidFSM.age)
    await message.delete()



@router.message(Command("cancel"))
@router.message(Command("отмена"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        text="Опрос прерван",
        reply_markup=ReplyKeyboardRemove()
    )