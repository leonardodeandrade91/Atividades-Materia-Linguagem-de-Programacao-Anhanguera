import socket

serv = str(input("Digite o link ou IP do servidor: "))

portas = (20, 21, 22, 25, 43, 53, 80, 110, 143, 443, 465, 587, 993, 995)

for p in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.settimeout(0.5)

    codigo = cliente.connect_ex((serv, p))

    if codigo == 0:
        sit = "aberta"
    else:
        sit = "fechada"

    print(f"A porta {p} de {serv} está {sit}.")