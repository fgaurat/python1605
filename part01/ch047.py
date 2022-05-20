def fib(n=12)->None:    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=100)->None:    # write Fibonacci series up to n
    """return a Fibonacci series up to n."""
    fibo_series = []
    a, b = 0, 1
    while a < n:
        fibo_series.append(a)
        a, b = b, a+b
    
    return fibo_series

fib(1000)
l = fib2(100)
print(l)# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

fib2()

print(50*'-')


n = "Fred"

def say_hello(name=n):
    print("hello "+name)

n ="Toto"
say_hello()


def f(a, L):
    if L==None:
        L=[]
    L.append(a)
    return L


the_list = [10]
print(f(1,the_list))
print(f(1,the_list))

def say_hello(name:str,age:str)->str:
    r = "hello "+name+" "+str(age)
    return r


say_hello('fred',45)
say_hello(name='fred',age=45)



