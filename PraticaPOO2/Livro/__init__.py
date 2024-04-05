from Pessoa import Pessoa
from Publicacao import Publicacao

class Livro(Publicacao):
    __titulo = ""
    __autor = ""
    __totPaginas = 0
    __pagAtual = 0
    __aberto = False
    __leitor = None

    def detalhes(self):
        print(f"Livro {self.__titulo} escrito por {self.__autor}.")

        if self.__aberto == True:
            print("O livro está aberto!")
            print(f"Páginas: {self.__totPaginas}, página atual {self.__pagAtual}.")
            print(f"Sendo lido por {self.__leitor.getNome()}.")
            print(f"De idade de {self.__leitor.getIdade()} anos.")
            print(f"E de sexo {self.__leitor.getSexo()}.")
        else:
            print("O livro está fechado no momento!")

    def abrir(self):
        self.__aberto = True

    def fechar(self):
        self.__aberto = False

    def folhear(self, p):
        if self.getAberto() == True:
            if p > self.__totPaginas:
                self.setPagAtual(self.getTotPaginas())
            elif p < 0:
                self.setPagAtual(0)
            else:
                self.__pagAtual = p

    def avancarPag(self):
        if self.getAberto() == True:
            if self.getPagAtual() < self.getTotPaginas():
                self.setPagAtual(self.getPagAtual() + 1)

    def voltarPag(self):
        if self.getAberto() == True:
            if self.getPagAtual() > 0:
                self.setPagAtual(self.getPagAtual() - 1)

    def __init__(self, titulo, autor, totPaginas, leitor):
        self.__titulo = titulo
        self.__autor = autor
        self.__totPaginas = totPaginas
        self.__leitor = leitor
        self.__aberto = False
        self.__pagAtual = 0

    def __del__(self):
        del self.__leitor

        print("Objeto Livro Destruído!")

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getTotPaginas(self):
        return self.__totPaginas

    def getPagAtual(self):
        return self.__pagAtual

    def getAberto(self):
        return self.__aberto

    def getLeitor(self):
        return self.__leitor

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setTotPaginas(self, totPaginas):
        self.__totPaginas = totPaginas

    def setPagAtual(self, pagAtual):
        self.__pagAtual = pagAtual

    def setAberto(self, aberto):
        self.__aberto = aberto

    def setLeitor(self, leitor):
        self.__leitor = leitor