import requests
import time
from bs4 import BeautifulSoup
import getresponse

input_text = 'mirae+asset+tax'

url = 'https://www.moneycontrol.com/mf/mf_info/mfsearch.php?search_str=' + input_text

soup = getresponse.soupify(url)


data = []
table = soup.find('table', {'class':'srch_tbl'})
table_body = table.find('tbody')

rows = table_body.find_all('a')
for row in rows:
    href = row.get('href')
    name = row.text
    print(href)
    print(name)
    
print(data)
#with open('some.txt', 'w', encoding="utf-8") as f:
#    f.write(response.text)