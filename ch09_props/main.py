from Rectangle import Rectangle

def main():
    r = Rectangle(12,2)
    r1 = Rectangle(12,2)

    print(r.longueur)

    print(r)

    # if r.__eq__(r1):

    # result = r == r1?"ok":"ko"
    result = "ok" if r==r1 else "ko"
    print(result)
    # if r == r1:
    #     print("ok")
    # else: 
    #     print("ko")


    b = Bougie()
    m = Moteur(b)

if __name__ == "__main__":
    main()