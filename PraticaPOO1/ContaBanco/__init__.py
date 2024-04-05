class ContaBanco:
    numConta = 0
    __tipo = ""
    __dono = ""
    __saldo = 0
    __status = False

    def estadoAtual(self):
        print("-" * 20)
        print(f"Conta: {self.getNumConta()}")
        print(f"Tipo: {self.getTipo()}")
        print(f"Dono: {self.getDono()}")
        print(f"Saldo: {self.getSaldo()}")
        print(f"Status: {self.getStatus()}")

    def abrirConta(self, t):
        self.setTipo(t)
        self.setStatus(True)

        if t == "CC":
            self.setSaldo(50)
        elif t == "CP":
            self.setSaldo(150)

        print("Conta aberta com sucesso!")

    def fecharConta(self):
        if self.getSaldo() > 0:
            print(f"A conta ainda tem dinheiro, não podemos fechá-la!")
        elif self.getSaldo() < 0:
            print(f"A conta está em débito, não podemos fechá-la!")
        else:
            self.setStatus(False)
            print(f"A conta de {self.getDono()} foi encerrada com sucesso!")

    def depositar(self, v):
        if self.getStatus():
            self.setSaldo(self.getSaldo() + v)
            print(f"Depósito de R${v:.2f} autorizado na conta de {self.getDono()}!")
        else:
            print("Conta Fechada ou Inexistente!")

    def sacar(self, v):
        if self.getStatus():
            if self.getSaldo() >= v:
                self.setSaldo(self.getSaldo() - v)
                print(f"Saque de R${v:.2f} autorizado na conta de {self.getDono()}!")
            else:
                print("Saldo insuficiente para saque!")
        else:
            print("Essa conta tá fechada ou não existe!")

    def pagarMensal(self):
        if self.getTipo() == "CC":
            v = 12
        elif self.getTipo() == "CP":
            v = 20

        if self.getStatus():
            self.setSaldo(self.getSaldo() - v)
            print(f"Mensalidade de R${v:.2f} debitada da conta de {self.getDono()}.")
        else:
            print("Problemas na conta, não podemos cobrar.")

    def __init__(self):
        self.setSaldo(0)
        self.setStatus(False)
        print("Conta criada com sucesso!")

    def __del__(self):
        print("Objeto ContaBanco Destruído!")

    def getNumConta(self):
        return self.numConta

    def getTipo(self):
        return self.__tipo

    def getDono(self):
        return self.__dono

    def getSaldo(self):
        return self.__saldo

    def getStatus(self):
        return self.__status

    def setNumConta(self, numConta):
        self.numConta = numConta

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setDono(self, dono):
        self.__dono = dono

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def setStatus(self, status):
        self.__status = status