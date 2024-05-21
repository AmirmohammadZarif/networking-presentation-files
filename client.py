import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 10025

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print('Connected to server')

while True:
    # Send data to the server
    message = input('Enter message: ')
    client_socket.sendall(message.encode())

    # Receive a response from the server
    data = client_socket.recv(1024)
    print('Received:', data.decode())

# Close the connection
client_socket.close()
