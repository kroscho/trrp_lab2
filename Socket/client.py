import socket
import os, sys
import json
import time
from config import config

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from crypt_data.crypt import Crypt_data
from normalized_db_Postgres.create_db import create_tables
from import_data.import_data import Import


def main():
    conf = config()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    #sock.connect(('192.168.0.103', 55000))  # подключемся к серверному сокету
    sock.connect((conf['socket']['host'], int(conf['socket']['port'])))  # подключемся к серверному сокету
    sock.send(bytes('size', encoding = 'UTF-8'))  # отправляем сообщение

    #data = b""
    data = []
    buff_size = 1024
    check_size = 50

    while True:
        part = sock.recv(buff_size)  # читаем ответ от серверного сокета частями по 1024 байта
        time.sleep(0.1)
        print(len(part))
        print(part)
        if len(part) < check_size:
            break
        else:
            data.append(json.loads(part.decode('utf-8')))

    # отправляем данные в нормализованную бд построчно  
    imp = Import()
    create_tables()
    for d in data:
        imp.import_data_to_db(d)

    sock.close()  # закрываем соединение

if __name__ == '__main__':
    main()