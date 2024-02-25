import os

from clickhouse_sqlalchemy import engines, get_declarative_base
from sqlalchemy import Column, MetaData, create_engine, types

uri = f'clickhouse://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@clickhouse:8123'

engine = create_engine(uri)
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
