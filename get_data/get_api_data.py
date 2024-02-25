import asyncio
import datetime as dt
import os
import xml.etree.ElementTree as ET

from config import UPDATE_TIME, URL
from db.models import Logs, engine
from get_token import base64_encode
from requests_data import request_get


def get_time_update():
    last_receive_time = dt.datetime.now() - dt.timedelta(seconds=UPDATE_TIME)
    formatted_time = str(last_receive_time.strftime("%Y/%m/%d %H:%M:%S"))
    return formatted_time


async def get_data(url):
    credentials = await base64_encode(f'{os.getenv("USER")}:{os.getenv("PASSWORD")}')
    api_data = await request_get(url, credentials)
    return api_data


async def parse_xml(xml, key, all_obj=False):
    root = ET.fromstring(xml)
    if xml:
        if all_obj:
            data = root.findall(key)
        else:
            data = root.find(key).text
        return data
    return None


async def get_job():
    xml = await get_data(URL + f'?type=log&log-type=url&query=( receive_time geq "{get_time_update()}" )')
    key = './/job'
    if xml:
        job = await parse_xml(xml, key)
        return job
    return None


async def get_api_data():
    job = await get_job()
    xml = await get_data(URL + '?type=log&action=get&job-id=' + job)
    key = './/entry'
    data = await parse_xml(xml, key, True)
    return data


async def save_data():
    data = await get_api_data()
    with engine.connect() as connection:
        for site in data:
            misc = site.find('misc').text
            receive_time = site.find('receive_time').text
            receive_time = dt.datetime.strptime(receive_time, '%Y/%m/%d %H:%M:%S')
            category = site.find('category').text
            serial = site.find('serial').text
            high_res_timestamp = site.find('high_res_timestamp').text
            high_res_timestamp = dt.datetime.strptime(high_res_timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
            category_list = site.find('url_category_list').text
            connection.execute(Logs.__table__.insert().values(
                url=misc,
                receive_time=receive_time,
                category=category,
                serial=serial,
                logs_time=high_res_timestamp,
                category_list=category_list
            ))
    await asyncio.sleep(UPDATE_TIME)

while True:
    asyncio.run(save_data())

