import socket
import os, sys
import json

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from crypt_data.crypt import Crypt_data
from import_data.import_data import Import

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 55000))  # подключемся к серверному сокету
sock.send(bytes('give me data, please', encoding = 'UTF-8'))  # отправляем сообщение

data = b""
buff_size = 1024

while True:
    part = sock.recv(buff_size)  # читаем ответ от серверного сокета частями по 1024 байта
    data = b"".join([data, part])
    if len(part) < buff_size:
        break

# отправляем данные в нормализованную бд построчно
data = json.loads(data.decode('utf-8'))   
imp = Import()

for d in data:
    imp.import_data_to_db(d)

sock.close()  # закрываем соединение

