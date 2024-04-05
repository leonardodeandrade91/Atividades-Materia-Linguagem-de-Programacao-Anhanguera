class Pessoa:
    __nome = ""
    __idade = 0
    __sexo = ""

    def fazerAniver(self):
        self.__idade += 1

    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    def __del__(self):
        print("Objeto Pessoa Destruído!")

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getSexo(self):
        return self.__sexo

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setSexo(self, sexo):
        self.__sexo = sexo