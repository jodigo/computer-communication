#import socket module
from socket import *
import sys # In order to terminate the program

serverPort = 85
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Server running on port:',serverPort)

while True:
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)
        print("Message 0:",message.split()[0])
        print("Message 1:",message.split()[1])
        filename = message.split()[1]
        print("Filename: ",filename,'||',filename[1:])
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)
        #Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        connectionSocket.send(outputdata.encode())
  
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close() 
    except IOError:
        #Send response message for file not found
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
        print('\nHTTP/1.1 404 Not Found\n\n'.encode())
#Close client socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data