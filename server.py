import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 10025

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(HOST, PORT))

# Accept a connection
client_socket, client_address = server_socket.accept()
print('Connected to', client_address)

while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break
    print('Received:', data.decode())

    # Send a response back to the client
    message = input('Enter response: ')
    client_socket.sendall(message.encode())

# Close the connection
client_socket.close()
server_socket.close()
