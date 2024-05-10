from Video import Video
from Gafanhoto import Gafanhoto
from Visualizacao import Visualizacao

v = list()

v.append(Video("Aula 1 de POO"))
v.append(Video("Aula 12 de Python"))
v.append(Video("Aula 15 de HTML"))

print(v[0].toString())

g = list()

g.append(Gafanhoto("Jubileu", 22, "M", "Jubi"))
g.append(Gafanhoto("Creuza", 12, "F", "Creuzita"))

print(g[0].toString())

vis = list()

vis.append(Visualizacao(g[0], v[2]))
vis.append(Visualizacao(g[0], v[1]))

vis[0].avaliar()
vis[1].avaliarPorc(85.0)

print(vis[0].toString())
print(vis[1].toString())

del v
del g
del vis
