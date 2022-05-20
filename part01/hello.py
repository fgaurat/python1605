import copy

print("Hello !")

# TheWorldIsFlat => UpperCamelCase
# theWorldIsFlat => camelCase
# the_world_is_flat => snake_case
# the-world-is-flat => Kebab case


the_world_is_flat = True

if the_world_is_flat:
    print("Be careful not to fall off!")


s = "Hello world"
i = 25
print(type(i))
i1 = "12"
i2 = "2"
i3 = int(i1)+int(i2)
print(i3)
s1 = "la valeur de i : "+str(i)
print(s)
print(type(s))
print(s1)
print(type(s1))

s2 = "L'orage gronde"
print(s2)
s2 = 'L\'orage\ngronde'
print(s2)
s2 = """Du texte avec 
des retours"""
print(s2)

# path = "c:\\toto\\nunu"
print("-"*50)
path = r"c:\toto\nunu"
print(path)
print("-"*50)
word = 'Python'
# print(word[6])

toto = 'Python'
print(hex(id(word)))
print(hex(id(toto)))

a = 1
b = 1
print(hex(id(a)))
print(hex(id(b)))


l = [10, 20, 30, 40]
l1 = l[:]
l[0] = 1000
print(type(l))
print(l)
print(l1)


l = [
    [10, 20],
    [30, 40],
    [50, 60]
]
# l1=l[:]  # shallow copy
l1=copy.deepcopy(l)
l[0][0] = 1000
print(l)
print(l1)


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

    