from Rectangle import Rectangle

def main():
    r = Rectangle(12,2)
    print(f"{Rectangle.cpt=}")
    r1 = Rectangle(12,2)
    r2 = Rectangle(12,2)
    r3 = Rectangle(12,2)
    r4 = Rectangle(12,2)
    print(f"{Rectangle.cpt=}")


    assert r.get_longueur() == 12
    print(r.get_longueur()) # 12
    assert r.get_largeur() == 2
    print(r.get_largeur())
    
    r.set_longueur(10)
    assert r.get_longueur() == 10   
    print(r.get_longueur()) # 10

    assert r.get_surface() == 20
    print(r.get_surface())

    print(type(r))
    print(r.__class__.__name__)

    print(f"{Rectangle.cpt=}")
    del r
    del r1
    del r2
    print(f"{Rectangle.cpt=}")
    

if __name__ == "__main__":
    main()