from Rectangle import Rectangle

class Carre(Rectangle):

    def __init__(self, cote=0):
        super().__init__(cote, cote)
        print(f'{__class__.__name__} {cote=}')
        self._cote = cote

    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self,cote):
        self._cote = cote