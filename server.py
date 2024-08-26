import threading
import json
from jsonrpc import JSONRPC
from socket import *

class Server:
    def __init__(self, host, port ):
        self.host = host
        self.port = port
        self.methods = {}

        # Crear el socket TCP
        self.skt = socket(AF_INET, SOCK_STREAM)
        
        # Enlazar el socket a la dirección y puerto 
        self.skt.bind((self.host ,self.port))
        # Configurar el socket para escuchar conexiones
           
    def serve(self):
      self.skt.listen()     # PREGUNTAR SI TIENE QUE IR EN CONSTRUCTOR O ESTA BIEN
      print(f"Server escuchando en {self.host}:{self.port}")
      while True:
        client, addr = self.skt.accept()
        print(f"Acepto coneccion de {addr}")
        thread = threading.Thread(target=self.handle_client, args=(client,))
        thread.start()
        #thread.join() Tendria que ir?? 
       
    def add_method(self, name, method):
      self.methods[name] = method
        
    def handle_client(self, client_socket):
      buffer = ""
      while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")  
            if not data:  
                break     # NO TIENE SETNIDO PQ SI ES VACIO
            buffer += data
        except Exception as e:    
            print(f"Error: {e}") 
            break

        try:
          request = json.loads(buffer) 
          break       
        except json.JSONDecodeError:
            continue
    
      method = self.methods.get(request['method'])
      if method:
        result = method(*request['params']) #ver donde queda el metodo
        response = JSONRPC.create_response(result, request['id'])
      else:
        response = {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": request['id']}
      
      client_socket.sendall(json.dumps(response).encode())    
      client_socket.close()   

def suma(x, y):
  return x + y

def resta(x, y):
  return x - y

server = Server('localhost', 8080)
server.add_method('suma', suma)
server.add_method('resta', resta)
server.serve()