from Livro import Livro
from Pessoa import Pessoa

p = list()
l = list()

p.append(Pessoa("Sérgio", 22, "M"))
p.append(Pessoa("Maria", 31, "F"))

l.append(Livro("Python Básico", "José da Silva", 300, p[0]))
l.append(Livro("POO com Python", "Maria de Souza", 500, p[0]))
l.append(Livro("Python Avançado", "Ana Paula", 800, p[1]))

l[2].abrir()
l[2].folhear(305)
l[2].avancarPag()
l[2].detalhes()

del p
del l