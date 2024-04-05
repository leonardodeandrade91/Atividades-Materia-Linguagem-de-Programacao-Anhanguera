import sys
import dns.resolver

try:
    dominio = str(input("Insira o nome ou IP do domínio: "))
except:
    print("O domínio é inválido!")
    sys.exit(1)

try:
    arquivo = open("wordlist.txt")
    linhas = arquivo.read().splitlines()
except:
    print("Arquivo não encontrado ou inválido!")
    sys.exit(1)

for l in linhas:
    subdominio = l + "." + dominio

    try:
        respostas = dns.resolver.resolve(subdominio, "a")

        for res in respostas:
            print(f"{subdominio} - {res}")
    except:
        pass