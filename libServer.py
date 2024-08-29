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
           
    def serve(self):
      # Configurar el socket para escuchar conexiones
      self.skt.listen()     
      print(f"Server escuchando en {self.host}:{self.port}")
      
      while True:
        client, addr = self.skt.accept()
        print(f"Conexion aceptada de {addr}")
        thread = threading.Thread(target=self.handle_client, args=(client,))
        thread.start()
       
    def add_method(self, method):
      name = method.__name__
      self.methods[name] = method
        
    def handle_client(self, client_socket):
      buffer = ""
      client_socket.settimeout(5)
      while True:
        
        buffer=""
        while not "}" in buffer:
          try:
            data = client_socket.recv(1024).decode("utf-8") 
            if not data:
              break
            buffer += data
          except Exception as e:    
            print(f"Error: {e}") 
            break
        
        if not data:
          break
        
        try:
          request = json.loads(buffer) 
          method = self.methods.get(request['method'])

          if method:
            try:
              result = method(*request['params']) 
              if 'id' in request:
                response = JSONRPC.create_response(result, request['id'])
            except TypeError as e:
              response = JSONRPC.invalid_params(request['id'], str(e))
          else:
            id = request.get('id')
            response = JSONRPC.method_not_found(request['id'] if id else None)
            
          if 'id' in request:
            client_socket.sendall(json.dumps(response).encode())
            
        except json.JSONDecodeError:
          response = JSONRPC.invalid_request()
          client_socket.sendall(json.dumps(response).encode())
          continue


