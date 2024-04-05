from abc import ABC, abstractmethod

class Pessoa(ABC):
    __nome = ""
    __idade = 0
    __sexo = ""
    __experiencia = 0

    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__experiencia = 0

    def __del__(self):
        print("Objeto Pessoa Destruído!")
    def toString(self):
        return f"Pessoa: \nNome = {self.__nome}\nIdade = {self.__idade}\nSexo = {self.__sexo}\nExperiencia = {self.__experiencia}"

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getSexo(self):
        return self.__sexo

    def getExperiencia(self):
        return self.__experiencia

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setSexo(self, sexo):
        self.__sexo = sexo

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia