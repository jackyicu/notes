from urllib import request

num = input('Please input stock number:')
urlbyte = request.urlopen('http://hq.sinajs.cn/list='+str(num))
contents = urlbyte.read().decode('gb2312')
stockinfo = contents.split(',')
name = stockinfo[0].split('\"')[1]
startprice = stockinfo[1]
lastendprice = stockinfo[2]
currentprice = stockinfo[3]
highestprice = stockinfo[4]
lowestprice = stockinfo[5]
date = stockinfo[30]
time = stockinfo[31]

print('stock name: ', name)
print('starting price: ', startprice)
print('end price of yesterday: ', lastendprice)
print('current price: ', currentprice)
print('highest price: ', highestprice)
print('lowest price: ', lowestprice)
print('updated date: ', date)
print('updated time: ', time)
