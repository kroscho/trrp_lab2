import win32com.client
import os
import sys, os.path
import json

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)
print(path_dir)

from import_data.get_data import get_data

def send_data(data):
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    #computer_name = os.getenv('COMPUTERNAME')
    computer_name = 'LAPTOP-OIJPISIU'
    computer_ip = '192.168.0.100'
    #qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\data"
    qinfo.FormatName="direct=tcp:"+computer_ip+"\\PRIVATE$\\data"
    queue=qinfo.Open(2,0) # Open a ref to queue

    msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
    msg.Label="Data"
    msg.Body = data
    print("Body: ", msg.Body)
    msg.Send(queue)
    queue.Close()

def send_key(key):
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    #qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\key"
    computer_ip = '192.168.0.105'
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
        d = json.dumps(d)
        send_data(d)