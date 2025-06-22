import asyncio
import logging
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

sys.path.append(str(Path(__file__).parent.parent))

from bot.config import settings
from bot.keyboard import my_button

TOKEN = settings.TG_TOKEN

dp = Dispatcher()



# Обработка нажатия на кнопку
@dp.callback_query(F.data == "btn1")
async def handle_button1(callback: types.CallbackQuery):
    await callback.answer("Вы нажали Кнопку 1!", show_alert=True)

# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text="Выберите действие:",
        reply_markup=my_button,
    )


# Определение состояний
class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()


# Обработчик команды /start, который запускает FSM
@dp.message(Command("me"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Привет! Давай познакомимся. Как тебя зовут?",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Form.name)


# Обработчик для состояния имени
@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично! Сколько тебе лет?")
    await state.set_state(Form.age)


# Обработчик для состояния возраста
@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число!")
        return

    await state.update_data(age=int(message.text))
    await message.answer("Какой у тебя пол? (М/Ж)")
    await state.set_state(Form.gender)


# Обработчик для состояния пола
@dp.message(Form.gender)
async def process_gender(message: Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ["м", "ж"]:
        await message.answer("Пожалуйста, введите 'М' или 'Ж'")
        return

    data = await state.get_data()
    await message.answer(
        f"Спасибо за информацию!\n"
        f"Ты: {data['name']}, {data['age']} лет, пол: {'мужской' if gender == 'м' else 'женский'}"
    )
    await state.clear()


# Обработчик команды /cancel для выхода из FSM
@dp.message(Command("cancel"))
@dp.message(Command("отмена"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Опрос прерван",
        reply_markup=ReplyKeyboardRemove()
    )

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Принудительная остановка бота')