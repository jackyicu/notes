import urllib.request
import json


class data:
    def read(path):
        with open(path, 'r') as f:
            portfolio = json.load(f)
            return portfolio

    def write(path, portfolio):
        with open(path,'w') as f:
            json.dumps(portfolio, f)

class portfolio:
    def get_stock_by_number(number):
        urlbyte = urllib.request.urlopen('http://hq.sinajs.cn/list='+str(number))
        stock = urlbyte.read().decode('gb2312')
        return stock

    def parse(stockinfo, quantity):
        stock = stockinfo.split(',')
        name = stock[0].split('\"')[1]
        currentprice = stock[3]
        marketvalue = float(currentprice) * float(quantity)
        return (name, currentprice, marketvalue)

    def get_portfolio(path):
        totalmarketvalue = 0        
        
        portfolioinfo = data.read(path)
        
        for number, quantity in portfolioinfo.items():
            
            stockinfo = portfolio.get_stock_by_number(number)
            (name, currentprice, marketvalue) = portfolio.parse(stockinfo, quantity)            
            print(name, currentprice, marketvalue)
            float(totalmarketvalue)
            totalmarketvalue += marketvalue
            

        print(totalmarketvalue)

def main():
    path = 'json/portfolio.json'
    portfolio.get_portfolio(path)

main()
