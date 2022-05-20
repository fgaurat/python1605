def main():
    b = 1
    c = 3
    a = b/c
    l = [a, b, c]
    result = "la valeur de {} = {}/{}".format(a, b, c)
    result = "la valeur de {} = {}/{}".format(*l)
    print(result)

    result = "la valeur de {val_a} = {val_b}/{val_c}".format(val_b=1, val_c=3, val_a=1/3)
    d = {
            "val_a": 1/3, 
            "val_b": 1, 
            "val_c": 3
            }
    result = "la valeur de {val_a} = {val_b}/{val_c}".format(**d)


    # s = r"c:\toto\number" #raw
    b=100
    c=3
    a=b/c
    s = f"fstring le résultat de {b} / {c} = {a:.2%}"
    print(s)

    s1 = f" {d['val_a']}"

    print(f"{b=},{c=},{a=}")


    a = 1.00000000000000002
    b = 1.00000000000000001
    if a==b:
        print("ok")

    print(a-b)

if __name__ == "__main__":
    main()
