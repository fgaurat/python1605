import traceback

def divi(a,b):
    r = a/b
    return r


def call_divi(a,b):
    r=0
    try:
        r = divi(a,b)
    finally:
        print("close",r)

    return r


def main():
    try:
        a=2
        b=int(input('valeur de b:'))
        c=call_divi(a,b)
        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError !",e)
        # traceback.print_exc()    
    except TypeError as e:
        print("TypeError !",e)

    except ValueError as e:
        print("ValueError !",e)

    except Exception as e:
        print("Exception !",e)
    else:
        print("else")
    finally:
        print("la fin")

if __name__ == "__main__":
    main()