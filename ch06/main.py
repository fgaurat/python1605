import fibo as the_fibo
import sys
from fibo import fib as remote_fib, fib2

# the_fibo.fib(1000)
def fib(a):
    print("local fib",a)



    # print("module name",__name__)
    # fib(1000)
    # remote_fib(1000)
    # print(the_fibo.fib2(1000))


def main():

    if len(sys.argv) >1:
        print(sys.argv[-1])
        val = int(sys.argv[-1])
        remote_fib(val)
    else:
        print("Merci, d'ajouter un paramètre")

if __name__ == "__main__":
    main()