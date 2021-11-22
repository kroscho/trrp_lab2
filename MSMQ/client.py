import sys, os.path
import win32com.client
import os
import json
from config import config
from crypt_data.crypt import decrypt

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from import_data.import_data import Import

conf = config()

def receive_key():
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\" + conf['msmq']['name_key']
    queue=qinfo.Open(1, 0)   # Open a ref to queue to read(1)
    msg=queue.Receive()
    #print("Label: ", msg.Label)
    key_des = msg.Body
    key_des = key_des
    print("Key : ", key_des)
    queue.Close()
    return key_des

def receive_data(password):
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    #print("comp_name: ", computer_name)
    qinfo.FormatName="direct=os:"+ computer_name+"\\PRIVATE$\\" + conf['msmq']['name_data']
    queue=qinfo.Open(1, 0)   # Open a ref to queue to read(1)
    msg=queue.Receive()
    #print("Label: ", msg.Label)
    crypto_data = json.loads(msg.Body)
    #print("Data : ", crypto_data)
    crypto_data = json.loads(decrypt(crypto_data, password).decode('utf-8'))
    print("data: ", crypto_data)
    print()
    imp = Import()
    imp.import_data_to_db(crypto_data)
    queue.Close()
    return crypto_data    

if __name__ == '__main__':
    while True:
        try:
            password = receive_key()
            print(password)
            data = receive_data(password)
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)