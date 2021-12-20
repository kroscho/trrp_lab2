import grpc
from concurrent import futures
import os, sys
import import_pb2_grpc as pb2_grpc
import import_pb2 as pb2 
from config import config

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from import_data.import_data import Import

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        imp = Import()
        f = False

        id = request.id
        user_id = request.user_id
        name = request.name
        email = request.email
        password = request.password
        role = request.role
        device_id = request.device_id
        device_name = request.device_name
        price = request.price
        rating = request.rating
        type_id = request.type_id
        type_name = request.type_name
        brand_id = request.brand_id
        brand_name = request.brand_name
        title = request.title
        description = request.description

        row = {'id': id, 'user_id':user_id, "name":name, "email":email, "password":password, "role":role, "device_id":device_id,
                "device_name":device_name, "price": price, "rating": rating, "type_id":type_id, "type_name":type_name, 
                "brand_id":brand_id, "brand_name":brand_name, "title":title, "description":description}
        print(row)
        f = imp.import_data_to_db(row)
        result = {'success': f}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    with open('gRPC/cert/localhost/server.key', 'rb') as f:
        private_key = f.read()
    with open('gRPC/cert/localhost/server.crt', 'rb') as f:
        certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain), ))
    conf = config()
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_secure_port('[::]:{}'.format(conf['grpc']['port']), server_credentials)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()