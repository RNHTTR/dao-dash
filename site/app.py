import os
from json import JSONDecodeError

import requests
from flask import Flask, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy


DAO_ADDRESS = os.getenv("DAO_ADDRESS")
DAO_ADDRESS = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
API_KEY = os.getenv("API_KEY")
API_KEY = "ckey_f17f2cba6bad472a97955f7b7da"
CHAIN_ID = os.getenv("CHAIN_ID")
CHAIN_ID = 1

BASE_URL = f"https://api.covalenthq.com/v1/{CHAIN_ID}"
AUTH_QUERY = f"?&key={API_KEY}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


class HistoricalPrice(db.Model):
    day = db.Column(db.DateTime, primary_key=True)
    quote_rate = db.Column(db.Float, nullable=False)


@app.route('/refresh/<query>', methods=["POST", "OPTIONS"])
def refresh(query):
    # TODO: Is this necessary?
    # Review https://stackoverflow.com/a/52875875/7004653
    if request.method == "OPTIONS":
        print("OPTIONS")
        return _build_cors_preflight_response()
    elif request.method == "POST":
        if query == "token_price":
            print("POST")
            url = f"{BASE_URL}/address/{DAO_ADDRESS}/portfolio_v2/{AUTH_QUERY}"
            response = requests.get(url)
            try:
                historical_price_data = response.json()["items"][0]["holdings"]
            except JSONDecodeError:
                return {
                    "code": 500,
                    "token_price": "Error querying API. Try again with Dashboard -> Refresh"
                }
            quote_rate = historical_price_data[0]["quote_rate"]
            print(f"QUOTE RATE: {quote_rate}")
            return {
                "code": 200,
                "token_price": quote_rate
            }
        elif query == "token_holders":
            print("POST")

            url = f"{BASE_URL}/tokens/{DAO_ADDRESS}/token_holders_changes/" \
                  f"{AUTH_QUERY}&starting-block=1&page-size=1"
            response = requests.get(url)
            token_holders = response \
                .json()["data"]["pagination"]["total_count"]
            return {
                "code": 200,
                "token_holders": token_holders
            }
        # return _corsify_actual_response(jsonify(response=200))
    else:
        raise RuntimeError(
            f"Unknown method: {request.method}"
        )

    # # TODO: Convert to flask_sqlalchemy & insert
    # price_history = []
    # for day_data in historical_price_data:
    #     # price_history.append({"day": day_data['timestamp'], "quote_rate": day['quote_rate']})
    #     db.session.add(HistoricalPrice(
    #         day=day_data['timestamp'],
    #         quote_rate=day_data['quote_rate']
    #     ))
    # db.session.commit()


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
