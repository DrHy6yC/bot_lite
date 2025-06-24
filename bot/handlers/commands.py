from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboard import start_key
from bot.state.state import LidFSM
from bot.utils import get_bot_name


router = Router(name="commands")


@router.message(Command("start"))
async def command_start(message: Message, state: FSMContext, bot: Bot) -> None:
    bot_name = await get_bot_name(bot)
    await message.answer(
        text=f"Привет, {message.from_user.first_name}!\n"
             f"Меня зовут {bot_name}, я бот-помощник репетитора английского Элизабет.\n"
             f"Я умею проводить краткие опросы, высылать вам полезные материалы, записывать вас на пробное занятие.\n"
             f"В будущем я буду развиваться, так что stay tuned!",
        reply_markup=start_key,
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