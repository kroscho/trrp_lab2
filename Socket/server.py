#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import os, sys
import socket
import json
from config import config

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from crypt_data.crypt import encrypt, decrypt
from import_data.get_data import get_data

if __name__ == '__main__':
    conf = config()
    password = conf['crypt']['password']

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаем сокет
    sock.bind(('', int(conf['socket']['port']))) # связываем сокет с портом, где он будет ожидать сообщения
    sock.listen(10) # указываем сколько может сокет принимать соединений
    print('Сервер запущен')

    i = 0
    while True:
        conn, addr = sock.accept() # начинаем принимать соединения
        print('connected:', addr) # выводим информацию о подключении
        message = conn.recv(1024) # принимаем данные от клиента, по 1024 байт
        print(message)

        data = get_data()
        #encrypted_data = encrypt(data, password)
        size_data = len(data)
        #encrypted_data = json.dumps(encrypted_data).encode('utf-8')
        #print(encrypted_data)
       
        if message.decode('utf-8') == "password":
            conn.send(password.encode('utf-8'))
        elif message.decode('utf-8') == "count":
            conn.send(str(size_data).encode('utf-8'))
        elif message.decode('utf-8') == "size":
            print("size")
            encrypted_data = encrypt(data[i], password)
            conn.send(str(len(json.dumps(encrypted_data).encode('utf-8'))).encode('utf-8'))
        else:
            encrypted_data = encrypt(data[i], password)
            conn.send(json.dumps(encrypted_data).encode('utf-8'))
            i += 1

            if i == size_data:
                i = 0
            '''
            data = get_data()
            data.append({'data': 'end'})
            #print(data)
            size_data = len(data)
            item = 0
            while item < size_data:
                #part = json.dumps(data[item]).encode('utf-8')
                encrypted_part = encrypt(data[item], password)
                print(encrypted_part)
                #encrypted_part = (json.loads(decrypt(encrypted_part, password).decode('utf-8')))
                print()
                conn.send(json.dumps(encrypted_part).encode('utf-8')) # отправляем данные клиенту
                time.sleep(0.3)
                item += 1
            '''
    conn.close() # закрываем соединение