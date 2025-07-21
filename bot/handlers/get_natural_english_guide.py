from aiogram import F, Router
from aiogram.enums import ChatMemberStatus
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from bot.config import SETTINGS
from bot.create_bot import bot
from bot.keyboard import age_key, aim_key, tutor_key, signup_key, start_questionnaire_key, start_alert_key
from bot.state.state import LidFSM


router = Router(name="get_natural_english_guide")


@router.callback_query(F.data == "start_questionnaire")
async def start_questionnaire(callback: CallbackQuery, state: FSMContext):
    chat_member = await bot.get_chat_member(
        chat_id=callback.from_user.id,
        user_id=bot.id
    )
    is_bot_chat_exists = chat_member.status != ChatMemberStatus.LEFT
    print(is_bot_chat_exists)
    if is_bot_chat_exists:
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=f"Привет, {callback.from_user.first_name}!\n"
                 f"Я задам вам три вопроса, ответив на которые, вы получите бесплатную памятку\n"
                 f"'Как звучать естественно: фразы, которые вы не найдете в учебниках'",
            reply_markup=start_questionnaire_key,
        )
        await state.set_state(LidFSM.age)
    # TODO Убрать, так как не работает как нужно
    else:
        await callback.answer(
            text = "Сначала напиши боту",
            show_alert = True
        )
    await callback.message.delete()


@router.callback_query(F.data == "get_guide")
@router.callback_query(LidFSM.age)
async def process_age(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(LidFSM.age)
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

