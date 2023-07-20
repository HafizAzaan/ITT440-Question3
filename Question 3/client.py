import socket

def get_user_input():
    while True:
        try:
            pressure_bar = float(input("Enter pressure in bar: "))
            return pressure_bar
        except ValueError:
            print("Invalid input. Please enter a valid pressure value.")

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.0.16'
    port = 12345

    try:
        client_socket.connect((host, port))
        pressure_bar = get_user_input()
        client_socket.sendall(str(pressure_bar).encode())
        atmosphere_standard = client_socket.recv(1024).decode()
        print("Received atmosphere-standard value from server:", atmosphere_standard)
    except ConnectionRefusedError:
        print("Error: The server is not running or unavailable.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    connect_to_server()
