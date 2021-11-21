import configparser
import os, sys

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

def config():
    parser = configparser.ConfigParser()  # создаём объекта парсера
    filename='settings.ini'
    parser.read(filename)  # читаем конфиг
    
    return parser