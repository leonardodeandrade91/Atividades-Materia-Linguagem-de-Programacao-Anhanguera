from Pessoa import Pessoa

class Gafanhoto(Pessoa):
    __login = ""
    __totAssistido = 0

    def __init__(self, nome, idade, sexo, login):
        super().__init__(nome, idade, sexo)
        self.__login = login
        self.__totAssistido = 0

    def __del__(self):
        print("Objeto Gafanhoto Destruído!")
    def assistirMaisUm(self):
        self.__totAssistido += 1

    def toString(self):
        return f"Gafanhoto: \n{super().toString()}\nLogin = {self.__login}\nTotAssistido = {self.__totAssistido}"

    def getLogin(self):
        return self.__login

    def getTotAssistido(self):
        return self.__totAssistido

    def setLogin(self, login):
        self.__login = login

    def setTotAssistido(self, totAssistido):
        self.__totAssistido = totAssistido