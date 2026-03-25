#### 
## Even or Odd 
number = 6
if number & 1:
    print("Odd")
else:
    print("Even")
### number = 6 = 110 & 001 = 000 = 0 
### Swap two number without using the temp 
a = 10 
b = 20 
## swap b =  10, a = 20 
a = a ^ b ### a = 01010 , b = 10100 = 11110 = 30 
b = a^ b ### a = 30 = 11110 , b = 20 = 10100 = 01010 = 10 
## a = 30, b = 10 
a = a ^ b ## a = 30 = 11110 , b = 10 = 01010 , a = 10100 = 20 
## b = 10, a = 20 
print(b)
print(a)