import asyncio
import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from bot.create_bot import bot, dp
from bot.handlers.admin import router as router_admin
from bot.handlers.commands import router as router_commands
from bot.handlers.get_natural_english_guide import router as router_get_natural_english_guide


async def main() -> None:
    dp.include_router(router_admin)
    dp.include_router(router_commands)
    dp.include_router(router_get_natural_english_guide)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Принудительная остановка бота')
