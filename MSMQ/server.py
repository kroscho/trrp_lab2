import win32com.client
import os
import sys, os.path
import json
from config import config 

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from crypt_data.crypt import encrypt, decrypt
from import_data.get_data import get_data

conf = config()
password = conf['crypt']['password']

def send_data(data):
    #computer_name = os.getenv('COMPUTERNAME')
    #computer_name = 'LAPTOP-OIJPISIU'
    #qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\data"

    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_ip = conf['msmq']['host']
    qinfo.FormatName="direct=tcp:"+computer_ip+"\\PRIVATE$\\" + conf['msmq']['name']
    queue=qinfo.Open(2,0) # Open a ref to queue

    msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
    msg.Label="Data"
    msg.Body = data
    print("Body: ", msg.Body)
    msg.Send(queue)
    queue.Close()

def send_key(key):
    #computer_name = os.getenv('COMPUTERNAME')
    #qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\key"
    
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_ip = conf['msmq']['host']
    qinfo.FormatName="direct=tcp:"+computer_ip+"\\PRIVATE$\\key"
    queue=qinfo.Open(2,0) # Open a ref to queue
    msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
    msg.Label="Key"
    msg.Body = key
    print("В send Body: ", msg.Body)
    msg.Send(queue)
    queue.Close()


if __name__ == '__main__':
    #create_tables()
    data = get_data()
    for d in data:
        #d = json.dumps(d)
        encrypted_part = encrypt(d, password)
        print(encrypted_part)
        print()
        send_key(password)
        send_data(json.dumps(encrypted_part))
        