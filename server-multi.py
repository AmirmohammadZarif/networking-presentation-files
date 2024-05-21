import socket
import threading

# Define host and port
HOST = '127.0.0.1'
PORT = 10025

# Function to handle client connections
def handle_client(client_socket, client_address):
    print('Connected to', client_address)

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        print('Received from {}: {}'.format(client_address, data.decode()))

        # Send a response back to the client
        message = input('Enter response: ')
        client_socket.sendall(message.encode())

    # Close the connection
    print('Client {} disconnected'.format(client_address))
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print('Server is listening on {}:{}'.format(HOST, PORT))

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
