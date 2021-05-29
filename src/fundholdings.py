import getresponse
import json

class Holding():
    def __init__(self, name, sector, sector_total_per, value, total_per, change_per, oneyear_high, oneyear_low, qty, qty_change, mcap, mcap_total_per):
        tname = name.replace('\n','')
        tname = tname.strip()
        if tname[0] == '-' or tname[0] == '#':
            tname = tname[1:]
        self.name = tname
        self.sector =sector
        self.sector_total_per = sector_total_per
        self.value = value
        self.total_per = total_per
        self.change_per = change_per
        self.oneyear_high = oneyear_high
        self.oneyear_low = oneyear_low
        self.qty = qty
        self.qty_change = qty_change
        self.mcap = mcap
        self.mcap_total_per = mcap_total_per

class FundHolding():
    def __init__(self, name, holdings):
        self.name = name
        self.holdings = holdings

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def fetch_holdings(url = ''):
    holdings = list()
    
    soup = getresponse.soupify(url)

    table = soup.find('table', {'id':'equityCompleteHoldingTable'})

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        tds = row.find_all('td') 
        holding = Holding(tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text, tds[11].text)
        holdings.append(holding)
    
    fh = FundHolding(url,holdings)
    return fh

