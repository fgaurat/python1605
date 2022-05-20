import time
import timeit


def f1():
    l = []
    for i in range(100):
        l.append(i)

def f2():
    l = list(map(lambda i:i,range(100)))

def f3():
    l = [i for i in range(100)]

def main():
    # start = time.perf_counter()
    # f1()

    # print(time.perf_counter()-start)
    print("f1",timeit.timeit("f1()", setup="from __main__ import f1"))
    print("f2",timeit.timeit("f2()", setup="from __main__ import f2"))
    print("f3",timeit.timeit("f3()", setup="from __main__ import f3"))

if __name__ == "__main__":
    main()