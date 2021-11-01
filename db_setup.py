from sqlalchemy import *
from util import get_db_engine


def create_tables(engine, metadata):

    historical_price_table = Table(
        "historical_price",
        metadata,
        Column("day", DateTime, primary_key=True),
        Column("quote_rate", Float)
    )

    metadata.create_all(engine)
