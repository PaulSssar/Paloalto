import asyncio
import datetime
import logging

from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import LOG_TIME
from db.db import (get_count, get_last_receive_time, get_not_resolved_count,
                   get_top_not_resolved, get_top_unknown, get_unknown_count)

router = Router()
logs_task = None


async def parse_top(sites):
    for site in sites:
        url = site[0][0]
        logging.info(url)
        count = site[1]
        yield url, count


@router.message(CommandStart())
async def logs(message: Message):
    while True:
        unknown = await get_top_unknown()
        not_resolved = await get_top_not_resolved()
        unknown_parsed = parse_top(unknown)
        not_resolved_parsed = parse_top(not_resolved)
        not_resolved_data = [f"{data[0]} - {data[1]}" async for data in not_resolved_parsed]
        unknown_data = [f"{data[0]} - {data[1]}" async for data in unknown_parsed]
        await message.answer(text=f'Период логов - с {await get_last_receive_time()} {datetime.datetime.now()}\n'
                                  f'Общее кол-во записей={await get_count()}\n'
                                  f'Кол-во not-resolved={await get_not_resolved_count()}\n'
                                  f'Кол-во unknown={await get_unknown_count()}\n '
                                  f'Top 5 unknown: \n'
                                  f'{chr(10).join(unknown_data)}\n'
                                  f'Top 5 not-resolved: \n'
                                  f'{chr(10).join(not_resolved_data)}\n')
        await asyncio.sleep(LOG_TIME)
