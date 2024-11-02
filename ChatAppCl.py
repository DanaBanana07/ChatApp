import socket
import threading

alias = input('Enter your name: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

def recieve_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error connecting to server')
            client.close()
            break

def send_messages():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))
        
recieve_thread = threading.Thread(target=recieve_messages)
recieve_thread.start()
send_thread = threading.Thread(target=send_messages)
send_thread.start()




