from collections import deque

l = [1,2,3,4]
print(l)
l.append(5)
print(l)
l.insert(0,0)
print(l)
last = l.pop()
print(l)

d = deque(l)
print(d)
d.popleft()
print(d)