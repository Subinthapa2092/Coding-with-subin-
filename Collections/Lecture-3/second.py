### deque 

from collections import deque 

d = deque([1,2,3,4,5,7,8,9])

### begin : 0, end : 10 

d.append(10) 
d.appendleft(0)
d.appendleft(-1)
d.append(11)
print(d)
### For the Removing element 

d.pop()
d.popleft()
print(d)