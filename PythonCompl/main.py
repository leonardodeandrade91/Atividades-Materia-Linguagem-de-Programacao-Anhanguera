from Pilha import *
from Aparelho import *

ray = Pilha("Rayovac")

ray.apresentacao()

controle = Aparelho(ray)

controle.ligado()

print(f"A carga da pilha é de {controle.getPl().getCarga()}%.")