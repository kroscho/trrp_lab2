import os, sys
import socket
import json
import time
from config import config

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from import_data.get_data import get_data

if __name__ == '__main__':
    conf = config()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаем сокет
    sock.bind(('', int(conf['socket']['port']))) # связываем сокет с портом, где он будет ожидать сообщения
    sock.listen(10) # указываем сколько может сокет принимать соединений
    print('Сервер запущен')
    while True:
        conn, addr = sock.accept() # начинаем принимать соединения
        print('connected:', addr) # выводим информацию о подключении
        data = conn.recv(1024) # принимаем данные от клиента, по 1024 байт
        data = get_data()
        data.append({'data': 'end'})
        #print(data)
        size_data = len(data)
        item = 0
        while item < size_data:
            part = json.dumps(data[item]).encode('utf-8')
            print(part)
            conn.send(part) # отправляем данные клиенту
            time.sleep(0.1)
            item += 1
    conn.close() # закрываем соединение