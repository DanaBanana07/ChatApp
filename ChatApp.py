import socket
import threading

host = '0.0.0.0'
port = 8080

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat!'.encode('utf-8'))
            aliases.remove(alias)
            break

def recieve():
    while True:
        #starting a connection
        client, addres = server.accept()
        print(f'connection from {str(addres)}')

        #creating a new client
        client.send('Name:'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)

        print(f'The client alias is {alias}')
        broadcast(f'{alias} has joined the chat!'.encode('utf-8'))
        client.send('Connection to chat confirmed!'.encode('utf-8'))

        #creating and starting a thread
        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()

print('server is running!')
recieve()

