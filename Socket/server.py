import os
import socket
import json
import sys

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from crypt_data.crypt import Crypt_data
from normalized_db_Postgres.create_db import create_tables
from import_data.get_data import get_data

if __name__ == '__main__':
    create_tables()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.bind(('', 55000))  # связываем сокет с портом, где он будет ожидать сообщения
    sock.listen(10)  # указываем сколько может сокет принимать соединений
    print('Сервер запущен')
    while True:
        conn, addr = sock.accept()  # начинаем принимать соединения
        print('connected:', addr)  # выводим информацию о подключении
        
        data = conn.recv(1024)  # принимаем данные от клиента, по 1024 байт
        data = get_data()
        print(data)
        data = json.dumps(data).encode('utf-8')
        
        conn.send(data)  # отправляем данные клиенту
    conn.close()  # закрываем соединение
