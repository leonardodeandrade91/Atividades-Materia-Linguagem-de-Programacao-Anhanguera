from abc import ABC, abstractmethod

class Publicacao(ABC):
    @abstractmethod
    def detalhes(self):
        pass

    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def fechar(self):
        pass

    @abstractmethod
    def folhear(self, p):
        pass

    @abstractmethod
    def avancarPag(self):
        pass

    @abstractmethod
    def voltarPag(self):
        pass