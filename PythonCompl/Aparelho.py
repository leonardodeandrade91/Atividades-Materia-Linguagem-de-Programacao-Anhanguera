from Pilha import *

class Aparelho:
    __pl = None

    def __init__(self, pl):
        self.__pl = pl

    def __del__(self):
        del self.__pl

    def ligado(self):
        if self.__pl.getCarga() > 0:
            print(f"O aparelho está ligado e a carga da pilha é de {self.__pl.getCarga()}%.")
        else:
            print("A pilha do aparelho está sem carga!")

    def getPl(self):
        return self.__pl

    def setPl(self, pl):
        self.__pl = pl