trades= [('NABIL',488), ('HIDCL',248), ('NABIL',490)]

from collections import Counter 

stock_list = []

for name,price in trades:
    stock_list.append(name)
print(stock_list)
count = Counter(stock_list)
print(count)
## Easy Way; 

couting = Counter(name for name,price in trades)
print(couting)