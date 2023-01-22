import time
import socket
numeroes = input("Digite o ip:")
# Cria um socket para o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket ao servidor
server_address = (f"{numeroes}", 10020)
client_socket.connect(server_address)

# Envia e recebe dados do servidor
print("Conectado")
apelido = input("Digite seu apelido:")
client_socket.send(apelido.encode())
recvapelido = ""
recvapelido = client_socket.recv(1024).decode()
while True:
    data = input(f"<{apelido}>: ")
    if not data:
        break
    client_socket.send(data.encode())
    data = client_socket.recv(1024).decode()
    print(f"{recvapelido}: {data}")

# Fecha o socket do cliente
client_socket.close()
