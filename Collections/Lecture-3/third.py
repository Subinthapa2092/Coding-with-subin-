### ChainMap 

from collections import ChainMap 

d1 = {"Name1":"Subin Thapa","Roll_NO1":32}
d2 = {"Name2":"Angat Sitoula","Roll_NO2":1}

d = ChainMap(d1,d2)
# print(d)
# print(d["Name2"])
d["Name1"] = "Bivek Subedi"
print(d)