# DAO Dash
DAO Dash is a free and open source template built on top of the [Covalent API](https://www.covalenthq.com/) designed to make it simple and straightforward for decentralized autonomous organizations (DAOs) to create dashboards for their key KPIs.

## Setup
> TODO: Eventually this should just all be done in with docker & docker-compose for a single click deployment

* Configure an [Apache Superset](https://superset.apache.org/) instance (we built one on top of Google Cloud SQL with PostgreSQL)
* Install Python3 (DAO Dash is built with Python3.9.1) 
* Install DAO Dash [requirements](site/requirements.txt) using `pip install -r requirements.txt`
* Obtain an API key from https://www.covalenthq.com/
* Set the following environment variables (assumes linux):
```bash
export API_KEY=<your api key>
export CHAIN_ID=1
export SQLALCHEMY_DATABASE_URI=<your sqlalchemy database connection string>
export DAO_ADDRESS=<Ethereum address of your DAO\'s contract>
```
* Clone the repository, and run the app:
```bash
git clone https://github.com/RNHTTR/dao-dash.git
cd dao-dash/site
python app.py
```

## Using DAO Dash
By default, DAO Dash focuses on three metrics:
1. Current token price
2. Current number of token holders
3. 30 Day historical token price

The metrics can be refreshed using the Dashboard > Refresh button in the sidebar. Charts can be edited using Superset by clicking the Explore in Superset button in the sidebar.

> The web app can be extended to include other KPIs by adding additional cards iFrames to the HTML in site/templates/index.html and updating site/static/js/refresh.js to pull fresh data from the Covalent API. Charts can be added to the dashboard using Superset.
