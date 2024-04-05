from Controlador import Controlador

class ControleRemoto(Controlador):
    __volume = 0
    __ligado = False
    __tocando = False

    def ligar(self):
        self.setLigado(True)

    def desligar(self):
        self.setLigado(False)

    def abrirMenu(self):
        print(f"Está ligado? {self.getLigado()}")
        print(f"Está tocando? {self.getTocando()}")
        print(f"Volume: {self.getVolume()}", end = "")

        for i in range(0, self.getVolume() + 1, 2):
            print("|", end = "")

        print("")

    def fecharMenu(self):
        print("Fechando Menu...")

    def maisVolume(self):
        if self.getLigado():
            if self.getVolume() < 100:
                self.setVolume(self.getVolume() + 2)
        else:
            print("ERRO! Está Desligado, Não Posso Aumentar o Volume!")

    def menosVolume(self):
        if self.getLigado():
            if self.getVolume() > 0:
                self.setVolume(self.getVolume() - 2)
        else:
            print("ERRO! Está Desligado, Não Posso Diminuir o Volume!")

    def play(self):
        if self.getLigado() and not self.getTocando():
            self.setTocando(True)

    def pause(self):
        if self.getLigado() and self.getTocando():
            self.setTocando(False)

    def __init__(self):
        self.__volume = 50
        self.__ligado = False
        self.__tocando = False

    def __del__(self):
        print("Objeto ControleRemoto Destruído com Sucesso!")

    def getVolume(self):
        return self.__volume

    def getLigado(self):
        return self.__ligado

    def getTocando(self):
        return self.__tocando

    def setVolume(self, volume):
        self.__volume = volume

    def setLigado(self, ligado):
        self.__ligado = ligado

    def setTocando(self, tocando):
        self.__tocando = tocando