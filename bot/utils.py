from aiogram import Bot


async def get_bot_name(bot_: Bot) -> str:
    me = await bot_.get_me()
    return me.username
