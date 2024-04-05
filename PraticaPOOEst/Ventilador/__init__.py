class Ventilador:
    __ligado = False
    __velocidade = 0

    @staticmethod
    def ligar(vel):
        Ventilador.__ligado = True

        if vel < 1:
            vel = 1
        elif vel > 3:
            vel = 3

        Ventilador.__velocidade = vel

        print(f"O ventilador está ligado, na velocidade de {Ventilador.__velocidade}.")

    @staticmethod
    def desligar():
        Ventilador.__velocidade = 0
        Ventilador.__ligado = False

        print("O ventilador está desligado!")

    @staticmethod
    def getLigado():
        return Ventilador.__ligado

    @staticmethod
    def getVelocidade():
        return Ventilador.__velocidade

    @staticmethod
    def setLigado(ligado):
        Ventilador.__ligado = ligado

    @staticmethod
    def setVelocidade(velocidade):
        Ventilador.__velocidade = velocidade