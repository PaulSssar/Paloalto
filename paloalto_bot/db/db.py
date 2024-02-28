import datetime as dt
import os
from collections import Counter

from clickhouse_sqlalchemy import (engines, get_declarative_base, make_session,
                                   types)
from sqlalchemy import Column, MetaData, create_engine

uri = f'clickhouse://{os.getenv("CLICKHOUSE_USER")}:{os.getenv("CLICKHOUSE_PASSWORD")}@clickhouse:8123'

engine = create_engine(uri, pool_size=40, max_overflow=40)

metadata = MetaData()
Base = get_declarative_base(metadata=metadata)


class Logs(Base):
    id = Column(types.Int, primary_key=True)
    url = Column(types.String)
    category = Column(types.String)
    serial = Column(types.String)
    receive_time = Column(types.DateTime)
    logs_time = Column(types.DateTime)
    category_list = Column(types.String)

    __table_args__ = (
        engines.Memory(),
    )


async def get_last_receive_time():
    last_receive_time = dt.datetime.now() - dt.timedelta(seconds=int(os.getenv('LOG_TIME')))
    return last_receive_time


async def get_count():
    last_receive_time = await get_last_receive_time()
    session = make_session(engine)
    count = session.query(Logs.url).filter(Logs.logs_time >= last_receive_time).count()
    return count


async def get_not_resolved_count():
    last_receive_time = await get_last_receive_time()
    session = make_session(engine)
    count_not_resolved = session.query(Logs.url, Logs.category_list).filter(
        Logs.category_list.icontains('not-resolved'), Logs.logs_time >= last_receive_time).count()
    return count_not_resolved


async def get_unknown_count():
    last_receive_time = await get_last_receive_time()
    session = make_session(engine)
    count_unknown = session.query(Logs.url, Logs.category_list).filter(
        Logs.category_list.icontains('unknown'), Logs.logs_time >= last_receive_time).count()
    return count_unknown


async def get_top_unknown():
    last_receive_time = await get_last_receive_time()
    session = make_session(engine)
    query = session.query(Logs.url, Logs.category_list).filter(
        Logs.category_list.icontains('unknown'), Logs.logs_time >= last_receive_time).all()
    top = Counter(query).most_common(5)
    return top


async def get_top_not_resolved():
    last_receive_time = await get_last_receive_time()
    session = make_session(engine)
    query = session.query(Logs.url, Logs.category_list).filter(
        Logs.category_list.icontains('not-resolved'), Logs.logs_time >= last_receive_time).all()
    top = Counter(query).most_common(5)
    return top
