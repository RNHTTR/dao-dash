import requests
from sqlalchemy import *

ens = "maker.eth"
base_url = "https://api.covalenthq.com"
chain_id = 1
address = "maker.eth"
historical_value_endpoint = f"v1/{chain_id}/address/{address}/portfolio_v2"
auth_query = "?&key=######"
url = f"{base_url}/{historical_value_endpoint}/{auth_query}"
response = requests.get(url)

historical_price_data = response.json()['items'][0]['holdings']
price_history = []
for day in historical_price_data:
    price_history.append({"day": day['timestamp'], "quote_rate": day['quote_rate']})

metadata = MetaData()

historical_price = Table(
	"historical_price",
	metadata,
	Column("day", DateTime, primary_key=True),
	Column("quote_rate", Float)
)

# connection_string = "postgresql+psycopg2://<root mac user>@localhost:5433/dao-dashboard"
# connection_string = "postgresql+psycopg2://user:password@:5433/dao-dashboard"
connection_string = "postgresql+psycopg2://dashboard@localhost:5432/dao-dashboard" # <-- This doesn't work yet. Need to figure out how to create user/role

engine = create_engine(connection_string)

conn = engine.connect()
conn.execute(historical_price.insert(), price_history)
result = conn.execute(text("select * from historical_price"))
result.fetchone()