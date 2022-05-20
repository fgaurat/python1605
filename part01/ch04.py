# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


l = ['Toto','Titi','Tata','Tutu']

s = slice(0,2)
print(l[s])
print(s.start)
print(s.stop)

for v in l:
    print(v)

for i in range(len(l)):
    print(i)
    print(l[i])

print(type(range(len(l))))

print(list(range(len(l))))



for i,v in enumerate(l,start=1):
    print(i,v)
print(50*'-')

# Rechercher Tata dans l
# l = ['Toto','Titi','Tata','Tutu']

for v in l:
    print(v)
    if v == 'Tatas':
        print("ok")
        break
else:
    print("Tatas ko")


for v in l:
    pass
    print(v)



