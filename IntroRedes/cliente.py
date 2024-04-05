import socket

host = "127.0.0.1"
port = 9999

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host, port))

cliente.send(str.encode("GET / HTTP / 1.1 \r \nHost: google.com \n\r\n"))

resposta = cliente.recv(4096)

print(resposta.decode())