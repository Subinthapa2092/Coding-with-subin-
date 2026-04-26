### 
from collections import namedtuple 

### Creating Structure 
Stock = namedtuple('Stock',["Name","Price"])

### Object:: 
s = Stock("Nabil",518)
### Accessed 
print(s.Name)
print(s.Price)

## For loop multiple Object 

s1 = [Stock("ADbl",316),Stock("HIDCL",360)]
for i in s1:
    print(i.Name,i.Price)