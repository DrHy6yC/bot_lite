from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from bot.config import SETTINGS
from bot.create_bot import bot
from bot.keyboard import  age_key, aim_key, tutor_key, signup_key
from bot.state.state import LidFSM


router = Router(name="get_natural_english_guide")


@router.callback_query(LidFSM.age, F.data == "start_questionnaire")
async def process_age(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.delete()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Сколько вам лет?",
        reply_markup=age_key,
    )
    await state.set_state(LidFSM.aim)


@router.callback_query(LidFSM.aim)
async def process_aim(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(age=callback.data)
    await callback.answer()
    await callback.message.delete()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="С какой целью изучаете/хотите изучать английский?",
        reply_markup=aim_key
    )
    await state.set_state(LidFSM.tutor)


@router.callback_query(LidFSM.tutor)
async def process_tutor(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(aim=callback.data)
    await callback.answer()
    await callback.message.delete()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Рассматриваете ли вы возможность занятий с репетитором?",
        reply_markup=tutor_key,
    )
    await state.set_state(LidFSM.end)


@router.callback_query(LidFSM.end)
async def process_gender(callback: CallbackQuery, state: FSMContext) -> None:
    button_signup: InlineKeyboardMarkup | None = signup_key if callback.data == "Нет" else None
    await state.update_data(tutor=callback.data)
    data = await state.get_data()
    await callback.answer()
    await callback.message.delete()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Благодарю за информацию\n"
             "Скачать можно здесь👇\n"
             "https://disk.yandex.ru/i/aTw9iwnuUw_iHA",
        reply_markup=button_signup
    )
    try:
        await bot.send_message(
            chat_id=SETTINGS.ID_INFO_CHAT,
            text=f"Имя: {callback.from_user.full_name},\n"
                 f"Логин: {callback.from_user.username},\n"
                 f"Возраст: {data['age']},\n"
                 f"Цель: {data['aim']},\n"
                 f"Занимается ли с репетитором: {data['tutor']}",
        )
    except TelegramBadRequest:
        print(f"Пользователь: @{callback.from_user.username} не писал боту")
    await state.clear()

