import requests
from bs4 import BeautifulSoup
url = 'https://www.moneycontrol.com/mutual-funds/kotaktaxsaverregularplang/portfolio-holdings/MKM518'

def soupify(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

