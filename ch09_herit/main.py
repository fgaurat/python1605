from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo
import json

def affiche_surface(o:ICalcGeo):
    
    print(f"get_surface {o.get_surface():.2f}")

def main():
    r = Rectangle(12,2)
    c = Carre(2)
    ce = Cercle(2)

    print(c.cote)
    c.cote=10
    print(c)
    affiche_surface(r)
    affiche_surface(c)
    affiche_surface(ce)
    Carre.toto=12
    print(c.toto)


if __name__ == "__main__":
    main()