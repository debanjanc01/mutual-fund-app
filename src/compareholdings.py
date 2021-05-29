import fundholdings
import json

url = 'https://www.moneycontrol.com/mutual-funds/kotaktaxsaverregularplang/portfolio-holdings/MKM518'
holding = fundholdings.fetch_holdings(url)
print(holding.toJSON())
print(holding.name)