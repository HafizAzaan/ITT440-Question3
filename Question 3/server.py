import socket

def convert_to_atmosphere(pressure_bar):
    # Conversion from bar to atmosphere-standard (1 bar = 0.986923 atmospheres)
    return pressure_bar * 0.986923

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.0.16'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, port))

    while True:
        conn, addr = server_socket.accept()
        print("Connected to client:", addr)

        try:
            data = conn.recv(1024)
            pressure_bar = float(data.decode())
            atmosphere_standard = convert_to_atmosphere(pressure_bar)
            response = "{:.2f}".format(atmosphere_standard).encode()
            conn.sendall(response)
        except ValueError:
            conn.sendall("Invalid input. Please provide a valid pressure value.".encode())

        conn.close()

if __name__ == "__main__":
    start_server()
