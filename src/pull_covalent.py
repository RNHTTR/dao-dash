import requests
from sqlalchemy import *
import sqlalchemy
import constants
from util import json_parse, get_db_engine
from db_setup import *


def build_historical_value_endpoint(chain_id, address):
    return f'{constants.COVALENT_BASE_URL}/{constants.COVALENT_API_VERSION}/{chain_id}/address/{address}/portfolio_v2'


def build_price_history(historical_price_data):
    return [{"day": day['timestamp'], "quote_rate": day['quote_rate']}
            for day in historical_price_data]


def insert_data_into_table(conn, metadata, table_name, data):
    table = metadata.tables[table_name]
    try:
        conn.execute(table.insert(), data)
    except sqlalchemy.exc.IntegrityError:
        # TODO Update this
        print('Primary key already exists')


def main():
    historical_value_endpoint = build_historical_value_endpoint(
        constants.CHAIN_ID, constants.ADDRESS)
    auth_query = "?&key=#####"

    full_url = f"{historical_value_endpoint}/{auth_query}"
    json_response = requests.get(full_url).json()

    historical_price_data = json_parse(
        json_response, ['items', '0', 'holdings'])

    price_history = build_price_history(historical_price_data)

    # TODO externalize db params
    engine = get_db_engine("db_connection_string")

    conn = engine.connect()
    metadata = MetaData(bind=conn)
    metadata.reflect(extend_existing=True)

    insert_data_into_table(conn, metadata, 'historical_price', price_history)


main()
