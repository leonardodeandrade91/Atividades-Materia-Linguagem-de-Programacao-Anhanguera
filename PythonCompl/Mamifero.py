from abc import ABC, abstractmethod

class Mamifero(ABC):
    @abstractmethod
    def lutar(self):
        pass

    def respirar(self):
        print("Eu Respiro!")

    def mamar(self):
        print("Eu Mamo!")