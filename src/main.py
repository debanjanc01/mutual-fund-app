from flask import Flask
from flask_restful import Api, Resource
import fundholdings
import json

app = Flask(__name__)
api = Api(app)

class FundHoldingsRes(Resource):
    def get(self):
        url = 'https://www.moneycontrol.com/mutual-funds/kotaktaxsaverregularplang/portfolio-holdings/MKM518'
        holding = fundholdings.fetch_holdings(url)
        return holding.toJSON()

api.add_resource(FundHoldingsRes, "/kotak")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)