from ast import literal_eval
import os

import requests
from flask import Flask, jsonify, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy


DAO_ADDRESS = os.getenv("DAO_ADDRESS")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
API_KEY = os.getenv("API_KEY")
CHAIN_ID = os.getenv("CHAIN_ID")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

class HistoricalPrice(db.Model):
    day = db.Column(db.DateTime, primary_key=True)
    quote_rate = db.Column(db.Float, nullable=False)

    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String, unique=True, nullable=False)
    # email = db.Column(db.String, unique=True, nullable=False)

@app.route('/refresh', methods=["POST", "OPTIONS"])
def refresh():
    # TODO: Is this necessary? Review https://stackoverflow.com/a/52875875/7004653
    if request.method == "OPTIONS": # CORS preflight
        print("OPTIONS")
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        print("POST")
        print(request.data)
        charts = literal_eval(request.data.decode("utf8"))
        print(charts)
        return {"code": 200}
        # return _corsify_actual_response(jsonify(response=200))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))
    # base_url = "https://api.covalenthq.com"
    # historical_value_endpoint = f"v1/{CHAIN_ID}/address/{DAO_ADDRESS}/portfolio_v2"
    # auth_query = "?&key=######"
    # url = f"{base_url}/{historical_value_endpoint}/{auth_query}"
    # response = requests.get(url)
    # historical_price_data = response.json()['items'][0]['holdings']

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
