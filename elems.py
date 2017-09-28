class Elem:

    def __init__(self, symb):
        if len(symb) > 1:
            raise ValueError(symb + ": expecting only 1 character")
        self.symb = symb

    def __repr__(self):
        return self.symb

class Wall(Elem):

    def __init__(self, symb='O'):
        Elem.__init__(self, symb)


class Door(Elem):

    def __init__(self, symb='.'):
        Elem.__init__(self, symb)


class Exit(Elem):

    def __init__(self, symb='U'):
        Elem.__init__(self, symb)

class Free(Elem):

    def __init__(self, symb=' '):
        Elem.__init__(self, symb)
