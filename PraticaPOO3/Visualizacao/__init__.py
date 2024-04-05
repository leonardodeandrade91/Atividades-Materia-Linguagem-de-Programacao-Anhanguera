from Video import Video
from Gafanhoto import Gafanhoto

class Visualizacao:
    __espectador = None
    __filme = None

    def __init__(self, espectador, filme):
        self.__espectador = espectador
        self.__filme = filme
        self.__filme.setViews(self.__filme.getViews() + 1)
        self.__espectador.setTotAssistido(self.__espectador.getTotAssistido() + 1)

    def __del__(self):
        del self.__espectador
        del self.__filme

        print("Objeto Visualizacao Destruído!")

    def avaliar(self):
        self.__filme.setAvaliacao(5)

    def avaliarNota(self, nota):
        self.__filme.setAvaliacao(nota)

    def avaliarPorc(self, porc):
        nova = 0

        if porc <= 20:
            nova = 3
        elif porc > 20 and porc <= 50:
            nova = 5
        elif porc > 50 and porc <= 90:
            nova = 8
        else:
            nova = 10

        self.__filme.setAvaliacao(nova)

    def toString(self):
        return f"\nEspectador = {self.__espectador.toString()}\nFilme = {self.__filme.toString()}"

    def getEspectador(self):
        return self.__espectador

    def getFilme(self):
        return self.__filme

    def setEspectador(self, espectador):
        self.__espectador = espectador

    def setFilme(self, filme):
        self.__filme = filme