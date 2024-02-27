import os

from clickhouse_sqlalchemy import (Table, engines, get_declarative_base,
                                   make_session, types)
from sqlalchemy import Column, MetaData, create_engine

uri = f'clickhouse://f'{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'@clickhouse:8123'

engine = create_engine(uri, pool_size=20, max_overflow=20)
session = make_session(engine)
metadata = MetaData()

Base = get_declarative_base(metadata=metadata)


class Logs(Base):
    __tablename__ = 'logs'
    url = Column(types.String, primary_key=True)
    category = Column(types.String)
    serial = Column(types.String)
    receive_time = Column(types.DateTime)
    logs_time = Column(types.DateTime)
    category_list = Column(types.String)

    __table_args__ = (
        engines.Memory(),
    )


Base.metadata.create_all(engine, checkfirst=True)
