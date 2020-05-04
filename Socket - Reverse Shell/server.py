
import socket
import sys

def make_socket():
    try:
        global host
        global port 
        global stark
        host = ''
        port = 9989
        stark = socket.socket()
    except socket.error as err:
        print(err)


def bind_starky():
    try:
        global host
        global port 
        global stark

        print(f'Starky Is Enabled -- {str(port)}')
        stark.bind((host,port))
        stark.listen(3)
        
    except socket.error as err:
        print('Not Binded Trying again' + err)
        bind_starky()


def starky_accept():
    new_connection , new_address = stark.accept()
    print(f'starky connected --> {new_connection}@{new_address}')
    with open('ConnectionLogger.txt','a') as logger:
        logger.write(f'\tNew Connection\nName = {new_connection}\nAddress = {new_address}\n\n')
    sender(new_connection)
    new_connection.close()


def sender(new_connection):
    while True:
        cmd = input()
        if cmd == 'qstarky':
            print('Quiting....')
            new_connection.close()
            stark.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            new_connection.send(str.encode(cmd))
            response = str(new_connection.recv(1024),'utf-8')
            print(response, end='')

def main():
    make_socket()
    bind_starky()
    starky_accept()

main()