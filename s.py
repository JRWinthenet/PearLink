import socket
# Cria um socket para o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket a uma porta específica
server_socket.bind(("", 10020))

# Escuta a porta para conexões
server_socket.listen(1)
apelido = input("Digite seu apelido:")
recvapelido = ""
print("Esperando por conexões...")

# Aceita uma conexão de um cliente
client_socket, client_address = server_socket.accept()

print("Conexão estabelecida de: ", client_address)
recvapelido = client_socket.recv(1024).decode()
client_socket.send(apelido.encode())
# Envia e recebe dados do cliente
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"{recvapelido}: {data}")
    dataenv = input(f"<{apelido}>:")
    client_socket.send(dataenv.encode())

# Fecha o socket do cliente
client_socket.close()

# Fecha o socket do servidor
server_socket.close()
