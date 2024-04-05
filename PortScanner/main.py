import socket

serv = str(input("Coloque o link ou IP do site: "))

portas = (20, 21, 22, 23, 25, 43, 53, 67, 68, 80, 110, 135, 137, 138, 139, 143, 433, 443, 445, 465, 587, 993, 995, 1039, 1040, 3050, 3306, 5432, 8080)

print("-=" * 30)

for p in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    codigo = cliente.connect_ex((serv, p))

    if codigo == 0:
        sit = "aberta"
    else:
        sit = "fechada"

    print(f"A porta {p} de {serv} está {sit}.")

print("-=" * 30)