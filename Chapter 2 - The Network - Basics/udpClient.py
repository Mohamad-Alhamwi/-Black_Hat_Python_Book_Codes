#!/bin/python3

import socket
import sys

target_host = "127.0.0.1"
target_port = 80

try:
    # Create a UDP-socket object.
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

except socket.error as error_message: 
    # Print out the error message.
    print (f"Error creating socket: {error_message}") 

    # Unsuccessful termination.
    sys.exit(1) 

try:
    # Encode the string into bytes and end the server some data.
    client.sendto("AAABBBCCC".encode(), (target_host, target_port))

except socket.error as error_message:  
    # Print out the error message.
    print (f"Error sending data: {error_message}") 
    
    # Unsuccessful termination.
    sys.exit(1) 

try:
    # Receive both the data and the details of the remote host and port.
    data, add = client.recvfrom(4096)

except socket.error as error_message:  
    # Print out the error message.
    print (f"Error receiving data: {error_message}") 
    
    # Unsuccessful termination.
    sys.exit(1)

# Print out the response data after decoding it from bytes to a string.
print(data.decode('utf-8'))

# Close the socket connection.
client.close()