import socket

# Configurar el cliente
host = 'localhost'
port = 12345

# Crear el socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
cliente.connect((host, port))

# Recibir el primer paso del saludo
paso1 = cliente.recv(1024)
print("Servidor dice:", paso1.decode())

# Enviar una confirmación al servidor
cliente.sendall("Paso 1 recibido".encode())

# Recibir el segundo paso del saludo
paso2 = cliente.recv(1024)
print("Servidor dice:", paso2.decode())

# Enviar una confirmación al servidor
cliente.sendall("Paso 2 recibido".encode())

# Recibir el tercer paso del saludo
paso3 = cliente.recv(1024)
print("Servidor dice:", paso3.decode())

# Enviar una confirmación al servidor
cliente.sendall("Paso 3 recibido".encode())

# Cerrar la conexión
cliente.close()
