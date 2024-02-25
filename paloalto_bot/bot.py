import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers.hanlers import router


async def main():
    bot = Bot(token=os.getenv("TOKEN")
    dp = Dispatcher()
    dp.include_router(router)
    await bot.set_my_commands(
        commands=[BotCommand(command='/start', description='Запуск бота')
                  ]
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
