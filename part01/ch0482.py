def add(*data):
    print(data)
    print(type(data))
    r=0
    for d in data:
        r+=d
    return r

# r = add(l) # 15
r = add(1,2,3,4,5)
print(r)

l =[1,2,3,4,5]
r = add(*l)
print(r)

print(50*'-')


def say_hello(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print("hello",kwargs['name'],kwargs['age'],sep=" - ")

say_hello(age=45,name='toto',job="dev",town="Paris")

d = {'age': 45, 'name': 'toto', 'job': 'dev', 'town': 'Paris'}
say_hello(**d)


def test_args(*args,**kwargs):
    print(args)
    print(kwargs)

test_args((1,5),(2,8),100,name="toto",job="dev")


def the_func(**a):
    print(a)

the_func(a=12,b=12)