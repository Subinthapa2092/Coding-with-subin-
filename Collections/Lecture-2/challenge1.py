trades= [('NABIL',488), ('HIDCL',248), ('NABIL',490)]
from collections import defaultdict,OrderedDict 

## count, grouped, ordered 
count = defaultdict(int)
grouped = defaultdict(list)
ordered = OrderedDict()

for name,price in trades: 
    grouped[name].append(price)
    count[name] += 1 
print(grouped)
print(count) 

### Ordered 
for name, price in trades: 
    if name not in ordered:
        ordered[name] = []
    ordered[name].append(price)
print(ordered)