import socket
import threading

ip = "0.0.0.0"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))

server.listen(5)

print(f"Ouvir {ip}: {port}")

def lidarCliente(cliente):
    pedido = cliente.recv(1024)

    print(f"Recebida: {pedido.decode()}")

    cliente.send(str.encode("ACK!"))

    cliente.close()

while True:
    clie, addr = server.accept()

    print(f"Conexão aceita a partir de {addr[0]}: {addr[1]}")

    lidClie = threading.Thread(target = lidarCliente, args = (clie,))

    lidClie.start()