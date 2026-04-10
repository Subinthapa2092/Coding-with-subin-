### Default dict:: 

from collections import defaultdict 

# d = defaultdict(list)
# print(d["Name"])

stocks = [("Nabil",400),("Hidcl",300),("Nabil",420),("Nabil",432)]

grouped = defaultdict(list)
count = defaultdict(int)

for name, price in stocks: 
    grouped[name].append(price)
    count[name] += 1 
print(grouped)
print(count)