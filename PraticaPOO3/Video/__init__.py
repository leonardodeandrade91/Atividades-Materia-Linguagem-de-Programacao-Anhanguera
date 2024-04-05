from AcoesVideo import AcoesVideo

class Video(AcoesVideo):
    __titulo = ""
    __avaliacao = 0
    __views = 0
    __curtidas = 0
    __reproduzindo = False

    def __init__(self, titulo):
        self.__titulo = titulo
        self.__avaliacao = 1
        self.__views = 0
        self.__curtidas = 0
        self.__reproduzindo = False

    def __del__(self):
        print("Objeto Video Destruído!")

    def like(self):
        self.__curtidas += 1

    def pause(self):
        self.__reproduzindo = False

    def play(self):
        self.__reproduzindo = True

    def toString(self):
        return f"Video: \nTitulo = {self.__titulo}\nAvaliacao = {self.__avaliacao}\nViews = {self.__views}\nCurtidas = {self.__curtidas}\nReproduzindo = {self.__reproduzindo}"

    def getTitulo(self):
        return self.__titulo

    def getAvaliacao(self):
        return self.__avaliacao

    def getViews(self):
        return self.__views

    def getCurtidas(self):
        return self.__curtidas

    def getReproduzindo(self):
        return self.__reproduzindo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAvaliacao(self, avaliacao):
        media = (self.__avaliacao + avaliacao) / self.__views
        self.__avaliacao = media

    def setViews(self, views):
        self.__views = views

    def setCurtidas(self, curtidas):
        self.__curtidas = curtidas

    def setReproduzindo(self, reproduzindo):
        self.__reproduzindo = reproduzindo