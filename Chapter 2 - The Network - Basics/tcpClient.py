#!/bin/python3

import socket
import sys

target_host = "127.0.0.0"
target_port = 80

try:
    # Create a TCP-socket object.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as error_message: 
    # Print out the error message.
    print (f"Error creating socket: {error_message}") 

    # Unsuccessful termination.
    sys.exit(1) 

try:
    # Connect the client to the server.
    client.connect((target_host, target_port))

except socket.gaierror as error_message:
    # Print out the error message.  
    print (f"Error connecting to the server (address-related error): {error_message}") 
    
    # Unsuccessful termination.
    sys.exit(1) 

except socket.error as error_message:  
    # Print out the error message.
    print (f"Connection error: {error_message}") 
    
    # Unsuccessful termination.
    sys.exit(1) 

try:
    # Encode the string into bytes and end the server some data.
    client.send("GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n".encode())

except socket.error as error_message:  
    # Print out the error message.
    print (f"Error sending data: {error_message}") 
    
    # Unsuccessful termination.
    sys.exit(1) 

try:
    # Receive some data back.
    response = client.recv(4096)

except socket.error as error_message:  
    # Print out the error message.
    print (f"Error receiving data: {error_message}") 
    
    # Unsuccessful termination.
    sys.exit(1)

# Print out the response after decoding it from bytes to a string.
print(response.decode('utf-8'))

# Close the socket connection.
client.close()