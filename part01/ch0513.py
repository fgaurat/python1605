

import math


l = []
for i in range(6):
    l.append(i)

print(l) # [0,1,2,3,4,5]

l = list(map(lambda i:i,range(6)))

l = [i for i in range(6)]

print(l)
# comprehension de list
# list par intention
l = [math.exp(i) for i in range(6)]
print(l)


names = [" fred   ","robert   ","   jean"]

clean_names = [name.strip() for name in names]
print(names)
print(clean_names)


vec = [[1,2,3], [4,5,6], [7,8,9]]

for v in vec:
    for i in v:
        print(i)
        l.append(i)

l = [i for v in vec for i in v]


keys = ('name','job','age')
values = ('fred','dev','45')

data = list(zip(keys,values))
print(data)