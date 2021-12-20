import os, sys
import grpc
import import_pb2_grpc as pb2_grpc
import import_pb2 as pb2
from config import config

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from import_data.get_data import get_data


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        conf = config()
        self.host = conf['gRPC']['host']
        self.server_port = conf['gRPC']['port']
        # instantiate a channel
        #self.channel = grpc.secure_channel('{}:{}'.format(self.host, self.server_port))

        if True:
            with open('cert/localhost/server.crt', 'rb') as f:
                options = (('grpc.ssl_target_name_override', "localhost"), ('grpc.default_authority', 'localhost'))
                creds = grpc.ssl_channel_credentials(f.read())
            self.channel = grpc.secure_channel('{}:{}'.format(self.host, self.server_port), credentials=creds, options=options)
            #self.channel = grpc.secure_channel('192.168.0.100:50051', credentials=creds, options=options)
        else:
            self.channel = grpc.secure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def send_data(self):
        """
        Client function to call the rpc for GetServerResponse
        """
        data = get_data()
        for row in data:
            request = pb2.Message(
                id = row['id'],
                user_id = row['user_id'],
                name = row['name'],
                email = row['email'],
                password = row['password'],
                role = row['role'],
                device_id = row['device_id'],
                device_name = row['device_name'],
                price = row['price'],
                rating = row['rating'],
                type_id = row['type_id'],
                type_name = row['type_name'],
                brand_id = row['brand_id'],
                brand_name = row['brand_name'],
                title = row['title'],
                description = row['description']
            )
            #message = pb2.Message(message=message)
            response = self.stub.GetServerResponse(request)
            if response.success:
                print("Успешно добавлено " + request.title)
        print("End")


if __name__ == '__main__':
    client = UnaryClient()
    client.send_data()