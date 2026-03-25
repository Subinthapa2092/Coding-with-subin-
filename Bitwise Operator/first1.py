### Bitwise And Operator:: 
a = 10 
b = 5 
result = a & b ### a = 10= 1010 b = 5 = 101
##               1010
###              0101
##               0000 = 0 
print(result)
### Bitwise Or Operator:: 
a = 10 
b = 5 
result = a | b 
print(result)
##               1010
###              0101
##               1111   = 15 
### Bitwise Xor Operator:
a = 10 
b = 5 
result = a ^ b 
print(result)
##               1010
###              0101
##               1111   = 15 
### Bitwise Not Operator 
a = 10 
result = ~(a) ## result = -(a+1) = -(10+1) = -11
print(result)
### Bitwise Left Shift Operator :: << 
a = 10 
result = a << 2 
### a = 10 = 1010 << 2 = 101000 = 40 
print(result)
### forumla = a * 2**n = 10 * 2**2 = 10* 4 = 40 
a = 20 
result = a >> 2 
### a = 20 = 10100 >> 2 = 00101 =5 
print(result)
### formula  : result = a/2**2 = 20 /4 = 5 
