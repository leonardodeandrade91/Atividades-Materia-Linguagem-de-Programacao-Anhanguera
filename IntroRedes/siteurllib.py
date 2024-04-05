import urllib.request

link = str(input("Coloque o link do site: "))

try:
    site = urllib.request.urlopen(link)
except urllib.error.URLError:
    print(f"O site {link} não está acessível no momento!")
else:
    print(f"Consegui acessar o site {link} com sucesso!")

    perg = str(input("Deseja mostrar o HTML do site? [S/N] ")).strip().upper()[0]

    if perg == "S":
        print(site.read().decode())