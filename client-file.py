import socket

def cliente():
    host = '127.0.0.1'
    puerto = 12345

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, puerto))
    n = 1
    archivo_nombre = 'archivo_grande_a_enviar.bin'
    with open(archivo_nombre, 'rb') as archivo:
        while True:
            datos = archivo.read(1048576)
            if not datos:
                break
            cliente_socket.send(datos)
            print("Enviando en pedacitos de 1MB, pedacito #" + str(n))
            n=n+1

    print("Archivo enviado")
    cliente_socket.close()

if __name__ == '__main__':
    cliente()
