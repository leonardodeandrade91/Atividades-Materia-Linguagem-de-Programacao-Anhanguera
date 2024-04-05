class Caneta:
    __modelo = ""
    __cor = ""
    __ponta = 0
    __tampada = False

    def tampar(self):
        self.__tampada = True

    def destampar(self):
        self.__tampada = False

    def status(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Cor: {self.__cor}")
        print(f"Ponta: {self.__ponta}")
        print(f"Tampada: {self.__tampada}")

    def __init__(self, m, c, p):
        self.__modelo = m
        self.__cor = c
        self.__ponta = p
        self.tampar()

    def __del__(self):
        print("Objeto Caneta Destruído com Sucesso!")

    def getModelo(self):
        return self.__modelo

    def getPonta(self):
        return self.__ponta

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setPonta(self, ponta):
        self.__ponta = ponta