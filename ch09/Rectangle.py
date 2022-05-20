
class Rectangle:
    cpt=0

    def __init__(self,longueur=0,largeur=0):
        assert longueur>=0
        assert largeur>=0
        print(f'def __init__(self,{longueur},{largeur})')
        self._longueur=longueur
        self._largeur=largeur
        Rectangle.cpt+=1

    def get_longueur(self):
        return self._longueur
    
    def get_largeur(self):
        return self._largeur

    def set_longueur(self,longueur):
        assert longueur>0
        self._longueur = longueur
    
    def set_largeur(self,largeur):
        assert largeur>0
        self._largeur = largeur
    
    def get_surface(self):
        return self._longueur *self._largeur

    @staticmethod
    def get_cpt(hgfhgf):
        return Rectangle.cpt

    def __del__(self):
        print("def __del__(self)")
        Rectangle.cpt-=1