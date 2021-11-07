import sys, os.path
import win32com.client
import os
import json

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from crypt_data.crypt import Crypt_data
from import_data.import_data import Import

def import_data(crypto_data, key_des):
    cr_data = Crypt_data("")
    data = cr_data.decrypt_data_des(crypto_data, key_des)
    print("Decr_data: ", data)

    #imp = Import()
    #imp.import_data_to_db(data)

def receive_key():
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\key"
    queue=qinfo.Open(1, 0)   # Open a ref to queue to read(1)
    msg=queue.Receive()
    print("Label: ", msg.Label)
    key_des = msg.Body
    key_des = key_des
    print ("Body : ", key_des)
    queue.Close()
    return key_des

def receive_data():
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\data"
    queue=qinfo.Open(1, 0)   # Open a ref to queue to read(1)
    msg=queue.Receive()
    print("Label: ", msg.Label)
    crypto_data = json.loads(msg.Body)
    print ("Body : ", crypto_data)
    
    imp = Import()
    imp.import_data_to_db(crypto_data)
    queue.Close()
    return crypto_data    

if __name__ == '__main__':
    while True:
        try:
            data = receive_data()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)