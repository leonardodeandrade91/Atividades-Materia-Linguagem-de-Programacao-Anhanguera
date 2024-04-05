from abc import ABC, abstractmethod

class AcoesVideo(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def like(self):
        pass