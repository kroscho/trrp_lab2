#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import socket
import os, sys
import json
import time
from config import config

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from crypt_data.crypt import decrypt
from normalized_db_Postgres.create_db import create_tables
from import_data.import_data import Import

conf = config()

def get_password():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    #sock.connect(('192.168.0.103', 55000))  # подключемся к серверному сокету
    sock.connect((conf['socket']['host'], int(conf['socket']['port'])))  # подключемся к серверному сокету
    sock.send(bytes('password', encoding = 'UTF-8'))  # отправляем сообщение

    buff_size = 2048

    password = sock.recv(buff_size)  # читаем ответ от серверного сокета частями по 1024 байта
    print("password: ", password)
    password = password.decode('utf-8')
    sock.close()  # закрываем соединение
    return password

def get_size_data(type):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    #sock.connect(('192.168.0.103', 55000))  # подключемся к серверному сокету
    sock.connect((conf['socket']['host'], int(conf['socket']['port'])))  # подключемся к серверному сокету
    sock.send(bytes(type, encoding = 'UTF-8'))  # отправляем сообщение

    buff_size = 1024

    size = sock.recv(buff_size)  # читаем ответ от серверного сокета частями по 1024 байта
    print(type, int(size.decode('utf-8')))
    size = int(size.decode('utf-8'))
    sock.close()  # закрываем соединение
    return size

def get_data(password, count):
    
    data = []
    item = 0
    for item in range(count):
        # получаем размер строки
        size = get_size_data('size')

        # получаем саму строку с ее размером
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
        sock.connect((conf['socket']['host'], int(conf['socket']['port'])))  # подключемся к серверному сокету

        sock.send(bytes('data', encoding = 'UTF-8'))  # отправляем сообщение
        
        buff_size = size
        part = sock.recv(buff_size)  # читаем ответ от серверного сокета частями
        print(part)    
        part = json.loads(part.decode('utf-8'))
        #data.append(json.loads(part.decode('utf-8')))
        data.append(json.loads(decrypt(part, password).decode('utf-8')))

    print(data)
    # отправляем данные в нормализованную бд построчно  
    imp = Import()
    create_tables()
    for d in data:
        imp.import_data_to_db(d)

    sock.close()  # закрываем соединение

def main():
    password = get_password()
    count = get_size_data('count')
    get_data(password, count)

if __name__ == '__main__':
    main()