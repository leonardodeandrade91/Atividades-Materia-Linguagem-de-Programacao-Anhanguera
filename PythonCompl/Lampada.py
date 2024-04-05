class Lampada:
    __preco = 9.50
    __acesa = False

    @staticmethod
    def custo():
        print("A lâmpada custa R${:.2f}.".format(Lampada.__preco))

    @staticmethod
    def acender():
        print("A lâmpada está acesa!")
        Lampada.__acesa = True

    @staticmethod
    def apagar():
        print("A lâmpada está apagada!")
        Lampada.__acesa = False