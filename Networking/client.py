import socket

HOST = '10.5.1.144'    
PORT = 4444      
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))
with open('myUpload.txt', 'rb') as file_to_send:
    for data in file_to_send:
        socket.sendall(data)
print 'end'
socket.close()
