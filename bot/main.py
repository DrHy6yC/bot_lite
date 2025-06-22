import asyncio
import logging
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, User

sys.path.append(str(Path(__file__).parent.parent))

from bot.config import SETTINGS
from bot.keyboard import download_guide_key , start_questionnaire_key, age_key, aim_key, tutor_key

TOKEN = SETTINGS.TG_TOKEN

dp = Dispatcher()

bot = Bot(token=TOKEN)

async def get_bot_name(bot_: Bot) -> str:
    me = await bot_.get_me()
    return me.username



# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message, state: FSMContext, bot: Bot) -> None:
    bot_name = await get_bot_name(bot)
    await message.answer(
        text=f"Привет, {message.from_user.first_name}!\n"
             f"Это Бот - {bot_name}, я задам Вам три вопроса, после чего вы получите бесплатный гайд",
        reply_markup=start_questionnaire_key,
    )
    await state.set_state(StudentFSM.age)

@dp.message(
    Command("id_chat"),
    F.from_user.username.in_({SETTINGS.ID_ADMIN, SETTINGS.ID_SUPER_USER})
)
async def id_chat_and_user(message: Message) -> None:
    await message.answer(
        text=f"Чат: {message.chat.id}"
             f"Пользователь: {message.from_user.id}",
    )


@dp.message(
    Command("download"),
    F.from_user.username.in_({SETTINGS.ID_ADMIN, SETTINGS.ID_SUPER_USER})
)
async def get_download(message: Message) -> None:
    await bot.send_message(
        chat_id=SETTINGS.ID_CHANNEL,
        text="Получить гайд",
        reply_markup=download_guide_key,
    )


# Определение состояний
class StudentFSM(StatesGroup):
    age = State()
    aim = State()
    tutor = State()
    end = State()


@dp.callback_query(F.data == "download_guide")
async def start_fsm(callback: types.CallbackQuery,state: FSMContext):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text=f"Привет, {callback.from_user.first_name}!\n"
             f"Это Бот - {name_bot}, я задам Вам три вопроса, после чего вы получите бесплатный гайд",
        reply_markup=start_questionnaire_key,
    )
    await state.set_state(StudentFSM.age)


@dp.callback_query(F.data == "start_questionnaire")
@dp.callback_query(StudentFSM.age)
async def process_age(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Сколько вам лет?",
        reply_markup=age_key,
    )
    await state.set_state(StudentFSM.aim)


@dp.callback_query(StudentFSM.aim)
async def process_aim(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(age=callback.data)
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="С какой целью изучаете/хотите изучать английский?",
        reply_markup=aim_key
    )
    await state.set_state(StudentFSM.tutor)



@dp.callback_query(StudentFSM.tutor)
async def process_tutor(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(aim=callback.data)
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Занимаетесь ли вы с репетитором на данный момент?",
        reply_markup=tutor_key,
    )
    await state.set_state(StudentFSM.end)


# Обработчик для состояния пола
@dp.callback_query(StudentFSM.end)
async def process_gender(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(tutor=callback.data)
    data = await state.get_data()
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Спасибо за информацию, вот ссылка https://github.com/DrHy6yC/",
    )
    await bot.send_message(
        chat_id=SETTINGS.ID_INFO_CHAT,
        text=f"Имя: {callback.from_user.full_name},\n"
             f"Логин: {callback.from_user.username},\n"
             f"Возраст: {data['age']},\n"
             f"Цель: {data['aim']},\n"
             f"Занимается ли с репетитором: {data['tutor']}",
    )
    await state.clear()


# Обработчик команды /cancel для выхода из FSM
@dp.message(Command("cancel"))
@dp.message(Command("отмена"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Опрос прерван",
        reply_markup=ReplyKeyboardRemove()
    )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Принудительная остановка бота')