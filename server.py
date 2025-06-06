#!/bin/python3
# Server
import socket
import os

ip = "0.0.0.0"
porto = 5000

print("Server a ligar...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, porto))

s.listen(20)

print("Server Ligado!")

while True:
    c, addr = s.accept()

    hostname = os.popen("cat /etc/hostname").read()
    ip = os.popen("ip a show wlo1 | grep inet | head -n 1 | cut -c10-21").read()
    ram = os.popen('free -m | awk \'/Mem:/ {printf "%dMiB / %dMiB (%.0f%%)\\n", $3, $2, $3/$2 * 100}\'').read()
    uptime = os.popen("uptime -p | cut -c4-").read()
    resposta = f""" Servidor: {hostname}--------------------------------
 IP: {ip} RAM: {ram} Uptime: {uptime}--------------------------------
"""
    c.sendall(resposta.encode())
