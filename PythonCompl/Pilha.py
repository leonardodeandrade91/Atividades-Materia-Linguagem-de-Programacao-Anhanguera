class Pilha:
    __marca = ""
    __carga = 0

    def __init__(self, marca):
        self.__marca = marca
        self.__carga = 100

    def apresentacao(self):
        print(f"A marca da pilha é {self.__marca}.")
        print(f"A carga da pilha é {self.__carga}%.")

    def getMarca(self):
        return self.__marca

    def getCarga(self):
        return self.__carga

    def setMarca(self, marca):
        self.__marca = marca

    def setCarga(self, carga):
        self.__carga = carga