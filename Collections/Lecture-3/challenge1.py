#### stocks = [('NABIL',488), ('HIDCL',248)] 

from collections import deque,ChainMap,namedtuple 

### Structure for the nametuple 

Stock = namedtuple("Stock",["Name","Price"])

### Object 

Stocks = [Stock("NABIL",488),Stock("HIDCL",248),Stock("ADBL",316)]
print("Namedtuple")
for s in Stocks:
    print(s.Name,s.Price)
    
market1 = {"Nabil":488}
market2 = {"HIDCl":248}
combined = ChainMap(market1,market2)
print("Chain Map")
for i,j in combined.items():
    print(i,j)
print(combined)

### deque 
recent_trades = deque(Stocks,maxlen = 2)
print(recent_trades)
print("Deque")
for i in recent_trades:
    print(i.Name,i.Price)