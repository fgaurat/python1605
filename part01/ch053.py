def toto():

    return 0,1,2

t = (0,1,2)

a,b,c,*d = 0,1,2,3,4,5,6

print(a,b,c,d)

basket = set()
basket.add('truc')
basket.add('truc01')
basket.add('truc')

l = list(basket)
print(basket)
print(l)


for b in basket:
    print(b)
