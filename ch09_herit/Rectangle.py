from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):
    cpt=0

    def __init__(self,longueur=0,largeur=0):
        assert longueur>=0
        assert largeur>=0
        print(f'def __init__(self,{longueur},{largeur})')
        self._longueur=longueur
        self._largeur=largeur
        Rectangle.cpt+=1

    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,longueur):
        assert longueur>0
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        assert largeur>0
        self._largeur = largeur
    
    def get_surface(self):
        return self._longueur *self._largeur

    @staticmethod
    def get_cpt(hgfhgf):
        return Rectangle.cpt

    def __str__(self) -> str:
        return f"{__class__.__name__} => {self._longueur=}, {self._largeur=}"

    
    def __eq__(self, __o):
        # assert isinstance(__o,Rectangle)
        return self._longueur == __o._longueur and self._largeur == __o._largeur

    
    def __le__(self, __o: object):
        pass

    def __del__(self):
        print("def __del__(self)")
        Rectangle.cpt-=1