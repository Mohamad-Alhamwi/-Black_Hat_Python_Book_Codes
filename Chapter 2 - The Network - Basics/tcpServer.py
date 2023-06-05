#!/bin/python3

import sys
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# Define a function to hundle the client socket object.
def handle_client(client_socket):
    # Print out what the client sends after decoding it from bytes to a string.
    request = client_socket.recv(1024)
    print(f"[*] Received: {request.decode('utf-8')}")

    # Encode the string into bytes and send back a packet to the client.
    client_socket.send("ACK!".encode())

    # Close the connection with the client.
    client_socket.close()

try:
    # Create a TCP-socket object.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as error_message: 
    # Print out the error message.
    print (f"Error creating socket: {error_message}") 

    # Unsuccessful termination.
    sys.exit(1) 

try:
    # Pass in the IP address and the port we want the server to listen on.
    server.bind((bind_ip, bind_port))

except socket.error as error_message: 
    # Print out the error message.
    print (f"Error binding the IP and the port: {error_message}") 

    # Unsuccessful termination.
    sys.exit(1)

# Start listening with a maximum backlog of 5 connections.
server.listen(5)

# Print out listening information.
print (f"[*] Listening on {bind_ip}:{bind_port}\n")

# Put the server into its main loop and wait for an incoming connection.
while True:
    try:
        # Receive the client socket, and the remote connection details.
        client,addr = server.accept()
        # Print out the received connection information.
        print (f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        # Create a new thread to handle each incoming connection.
        client_handler = threading.Thread(target = handle_client, args = (client,))
        # start the thread to handle the client connection.
        client_handler.start()

    except KeyboardInterrupt:
        # Closing down gracefully in response to a user action.
        print("\nKeyboard interrupt received, shutting down.")
        server.close()
        sys.exit(0)

    except Exception as e:
        # Print out the error message.
        print("An error occurred: ", error_message)
        # Keep the server running and wait for new connections.
        continue