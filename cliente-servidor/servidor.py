import socket
import threading

# Función para manejar la comunicación con un cliente
def manejar_cliente(cliente, direccion):
    print("Conexión establecida desde:", direccion)

    # Enviar el primer paso del saludo
    cliente.sendall("Paso 1: Hola".encode())
    # Recibir la confirmación del cliente
    respuesta = cliente.recv(1024)
    print("Respuesta del cliente:", respuesta.decode())

    # Enviar el segundo paso del saludo
    cliente.sendall("Paso 2: ¿Cómo estás?".encode())
    # Recibir la confirmación del cliente
    respuesta = cliente.recv(1024)
    print("Respuesta del cliente:", respuesta.decode())

    # Enviar el tercer paso del saludo
    cliente.sendall("Paso 3: ¡Hasta luego!".encode())

    # Cerrar la conexión con el cliente
    cliente.close()

# Configurar el servidor
host = 'localhost'
port = 12345

# Crear el socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
servidor.bind((host, port))

# Escuchar conexiones entrantes
servidor.listen(5)
print("Esperando conexiones...")

# Ciclo infinito para aceptar conexiones y crear subprocesos para manejar cada cliente
while True:
    # Aceptar la conexión entrante
    cliente, direccion = servidor.accept()

    # Crear un subproceso para manejar la comunicación con el cliente
    subproceso = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
    subproceso.start()

