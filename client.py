#!/bin/python3
import socket
import time
import os

ip = "docker-server"
porto = 5000

while True:
    # try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, porto))

        # Receber os dados
        dados = s.recv(1024).decode()

        os.system("clear")
        print(dados)

        s.close()
        time.sleep(1)
    # except ConnectionRefusedError:
    #     print("Servidor não disponível. A tentar novamente em 5 segundos...")
    #     time.sleep(5)
