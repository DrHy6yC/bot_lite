import asyncio

from aiogram import F, Router
from aiogram.enums import ChatMemberStatus
from aiogram.types import CallbackQuery

from bot.config import SETTINGS
from bot.create_bot import bot
from bot.keyboard import choice_key, emoji_key


router = Router(name="get_free_guide")


@router.callback_query(F.data == "channel_button")
async def start_get_free_guide(callback: CallbackQuery):
    await callback.answer()
    chat_member = await bot.get_chat_member(
        chat_id=callback.from_user.id,
        user_id=bot.id
    )
    is_bot_chat_exists = chat_member.status != ChatMemberStatus.LEFT
    print(is_bot_chat_exists)
    if is_bot_chat_exists:
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=f"Привет! Это бот Елизаветы — репетитора, который знает, "
                 f"что английский бывает сложным… но не обязан быть скучным 🙃"
                 f" Вот твой гайд: «Сила наречий"
                 f" и прилагательных в английском» ⤵️",
        )
        file_id = "BQACAgIAAxkBAAP1aH4hxbgx97jU8cImLC8_VAor8oQAAmdyAAIl9fBLniC9XHsm0KQ2BA"
        await bot.send_document(
            chat_id=callback.from_user.id, document=file_id)
        # TODO Сделать задачи в celery
        await asyncio.sleep(180)
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="А вот тебе маленький эмо-тест:\n"
                 "Как бы ты описал(a) себя сегодня в 3-х emoji? 👇",
            reply_markup=emoji_key,
        )
        # TODO Сделать задачи в celery
        await asyncio.sleep(600)
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="Знаешь, что самое сложное в изучении английского? "
                 "Не выучить слова, а начать их использовать без страха,"
                 " что скажешь что-то не так.\n"
                 "Если хочешь попробовать — давай потренируемся вместе.\n\n"
                 "✔️ Помогу заговорить проще и увереннее.\n"
                 "✔️ Без зубрёжки и стресса.\n"
                 "✔️ С разбором твоих реальных ситуаций, а не учебных "
                 "диалогов из 2005 года.\n\n"
                 "Хочешь посмотреть, как это - заниматься со мной? "
                 "Тыкай на кнопку, расскажу все детали.",
            reply_markup=choice_key,
        )
    # TODO Сделать проверку, писал ли боту человек
    else:
        await callback.answer(
            text = f"Сначала напиши боту {SETTINGS.NAME_BOT}",
            show_alert = True
        )

@router.callback_query(F.data == "super_tired")
async def start_get_free_guide(callback: CallbackQuery):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="О, ну конечно. Классика: мозг как Wi-Fi — вроде есть, "
             "но не ловит. Ничего, английским тоже можно заниматься "
             "в режиме энергосбережения."
    )


@router.callback_query(F.data == "extremely_motivated")
async def start_get_free_guide(callback: CallbackQuery):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Мотивация? В 2025? Ты точно человек? А как тебе такое - ты "
             "приходишь с настроем, я притворяюсь, что тоже в ресурсе,м?:)"
    )

@router.callback_query(F.data == "anxious")
async def start_get_free_guide(callback: CallbackQuery):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Кофе и тревога — комбо века. Но ты молодец, что всё равно "
             "здесь. Разберёмся со всем, no panic ;)"
    )

@router.callback_query(F.data == "full_of_energy")
async def start_get_free_guide(callback: CallbackQuery):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Ого, у нас тут спикинг-рок-звезда врывается! Всё, держись, "
             "английский — мы идем зажигать⚡️"
    )

@router.callback_query(F.data == "idk")
async def start_get_free_guide(callback: CallbackQuery):
    await callback.answer()
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Ну и не надо решать всё сразу — это не ЕГЭ. Просто читай "
             "дальше, что-то точно откликнется (если не сегодня, то скоро "
             "точно)."
    )
