import threading
import json
from .jsonrpc import JSONRPC
from socket import *
import time
class Server:
    
    # Constructor
    def __init__(self, address ):
      self.host,self.port = address
      self.methods = {}

      # Crear el socket TCP
      self.skt = socket(AF_INET, SOCK_STREAM)
      
      # Enlazar el socket a la dirección y puerto 
      self.skt.bind((self.host ,self.port))
      self.abierto = True
    # Arrancar el server
    def serve(self):
      # Configurar el socket para escuchar conexiones
      self.skt.listen()   
      print(f"Server escuchando en {self.host}:{self.port}")
      serverAbierto = True
      self.skt.settimeout(None)
      try:
        while serverAbierto:
          try:
            client, addr = self.skt.accept()
            print(f"Conexion aceptada de {addr}")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.daemon = True
            thread.start()
          except TimeoutError:
            continue
          except Exception:
            continue
      except KeyboardInterrupt:
        serverAbierto = False
        self.abierto = False
        self.shutdown()
        return
        
    # Agregar metodos 
    def add_method(self, method,name = None):
      if name:
        self.name = name
      else:
        self.name = method.__name__

      self.methods[self.name] = method

    # Manejar el cliente 
    def handle_client(self, client_socket):
        buffer = ""
        client_socket.settimeout(None) # Setteo de timeout
        primeraVez = True
        while buffer.count("{") != buffer.count("}") or buffer.count("{") < 1 or buffer[-1] != "}":
          data = ''        
          # Recibir request
          try:
            data = client_socket.recv(1024).decode("utf-8") 
            if(primeraVez):
              primeraVez = False
              client_socket.settimeout(3)

            if not data:
              break
            buffer += data

          except Exception as e:    
            break

        try:
          request = json.loads(buffer) # Deserialización
          print(f"REQUEST: {request}")
          method = self.methods.get(request['method']) # Obtener metodo

          if method:
            try:
              if 'params' in request:
                if isinstance(request['params'], dict):
                  result = method(**request['params'])
                else:
                  result = method(*request['params']) # Aplicar metodo
              else:
                  result = method()
              if 'id' in request:
                  response = JSONRPC.create_response(result, request['id'])

            except TypeError as e:
              if 'id' in request:
                response = JSONRPC.invalid_params(request['id'], str(e)) # Error de parametros
          else:
            id = request.get('id')
            response = JSONRPC.method_not_found(request['id'] if id else None) # Error de metodo no encontrado
          if 'id' in request:
            try:
              client_socket.sendall(json.dumps(response).encode())
            except ConnectionResetError as e:
              print(f"Error: {e}") 
        # Error de formato JSON
        except json.JSONDecodeError:
          response = JSONRPC.invalid_request()
          try:
            client_socket.sendall(json.dumps(response).encode())
          except ConnectionResetError as e:
            print(f"Error: {e}") 
            return
          
        client_socket.close()

    def shutdown(self):
      print('El socket Servidor se cerro')
      self.skt.close()




