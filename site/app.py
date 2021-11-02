import os

import requests
from flask import Flask, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy


DAO_ADDRESS = os.getenv("DAO_ADDRESS")
DAO_ADDRESS = "0x6b175474e89094c44da98b954eedeac495271d0f"
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
API_KEY = os.getenv("API_KEY")
API_KEY = "ckey_f17f2cba6bad472a97955f7b7da"
CHAIN_ID = os.getenv("CHAIN_ID")
CHAIN_ID = 1

BASE_URL = "https://api.covalenthq.com"
HISTORICAL_VALUE_ENDPOINT = f"v1/{CHAIN_ID}/address/{DAO_ADDRESS}/portfolio_v2"
AUTH_QUERY = f"?&key={API_KEY}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


class HistoricalPrice(db.Model):
    day = db.Column(db.DateTime, primary_key=True)
    quote_rate = db.Column(db.Float, nullable=False)


@app.route('/refresh', methods=["POST", "OPTIONS"])
def refresh():
    # TODO: Is this necessary?
    # Review https://stackoverflow.com/a/52875875/7004653
    if request.method == "OPTIONS":
        print("OPTIONS")
        return _build_cors_preflight_response()
    elif request.method == "POST":
        print("POST")
        url = f"{BASE_URL}/{HISTORICAL_VALUE_ENDPOINT}/{AUTH_QUERY}"
        response = requests.get(url)
        historical_price_data = response.json()["items"][0]["holdings"]
        quote_rate = historical_price_data[0]["quote_rate"]
        print(f"QUOTE RATE: {quote_rate}")
        return {
            "code": 200,
            "quote_rate": quote_rate
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
