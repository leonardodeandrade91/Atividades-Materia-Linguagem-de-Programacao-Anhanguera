from ContaBanco import ContaBanco

p1 = ContaBanco()
p2 = ContaBanco()

p1.abrirConta("CC")
p1.setNumConta(1111)
p1.setDono("Jubileu")

p2.abrirConta("CP")
p2.setNumConta(2222)
p2.setDono("Creuza")

p1.depositar(300)
p2.depositar(500)

p2.sacar(100)

p1.pagarMensal()
p2.pagarMensal()

p1.estadoAtual()
p2.estadoAtual()

del p1
del p2