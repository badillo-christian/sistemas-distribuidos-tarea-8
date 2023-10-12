import socket

def servidor():
    host = '127.0.0.1'
    puerto = 12345

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen(1)
    print(f"El servidor está escuchando en {host}:{puerto}")
    n = 1
    cliente_socket, cliente_direccion = servidor_socket.accept()
    print(f"Conexión entrante desde {cliente_direccion}")

    archivo_nombre = 'archivo_grande_recibido.bin'
    with open(archivo_nombre, 'wb') as archivo:
        while True:
            datos = cliente_socket.recv(1048576)
            if not datos:
                break
            archivo.write(datos)
            print("Reciboendo en pedacitos de 1MB, pedacito #" + str(n))
            n=n+1

    print("Archivo recibido y guardado.")
    cliente_socket.close()
    servidor_socket.close()

if __name__ == '__main__':
    servidor()
