from socket import *
import sys  # In order to terminate the program

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 9090  # You can change this to any port above 1024
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # The server can listen for one connection at a time
print('The server is ready to receive on port', serverPort)

while True:  # Loop to keep the server running
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Accepts incoming connection
    print(f"Connection successful from {addr}")  # Print the connection address

    try:
        # Receive the HTTP request from the client
        message = connectionSocket.recv(1024).decode()  # Receive the message and decode it
        print(f"Received message: {message}")  # Print the received message
        
        if len(message.split()) > 1:  # Check if there is a valid request
            filename = message.split()[1]  # Get the requested filename
            f = open(filename[1:], 'r')  # Open the file (skip the leading '/')
            outputdata = f.read()  # Read the content of the file
            f.close()

            # Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Send the content of the requested file to the client
            connectionSocket.send(outputdata.encode())
            print(f"Served file: {filename[1:]}")  # Print the name of the served file
        else:
            raise IOError  # Trigger the error handling if the request is invalid

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        # Print an error message in the terminal
        print("404 Not Found: The requested file was not found.")

    finally:
        connectionSocket.close()  # Close client socket
        break  # Exit the loop after processing the first request

# Close the server socket
serverSocket.close()
sys.exit() # Terminate the program after closing the server
