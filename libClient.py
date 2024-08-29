from socket import *
from jsonrpc import JSONRPC
import json

class Client:
  def __init__(self, function):
    pass
    
  def __call__(self, host, port):
    self.host = host
    self.port = port

    # Crear el socket TCP
    self.skt = socket(AF_INET, SOCK_STREAM)
    try:
      self.skt.connect((self.host, self.port))
      return self
    except ConnectionRefusedError:
      code = -32001
      message = "No se pudo establecer la conexion con el servidor"
      response = JSONRPC.create_error_response(code, message)
      print(response['error']['message'])
      

  def __getattr__(self, name):
    def method(*args,**kwargs):
      notify = kwargs.pop('notify', False)

      if notify:
          request = JSONRPC.create_notification(name, args)
      else:
          request = JSONRPC.create_request(name, args)
      
      self.skt.sendall(json.dumps(request).encode())

      if not notify:
        buff = ""

        while True:
          try:
            data = self.skt.recv(1024).decode()
            buff += data
          except Exception as e:
            print(f"Error: {e}")
            break
          
          try:
            response = json.loads(buff)
            break
          except json.JSONDecodeError:
            continue
        
        if('result' in response):
          return response['result']
        else:
          return response['error']['message']
        
      else:
        return 'ES NOTIFICACION'
      
    return method
    
  def close(self):
    self.skt.close()

@Client
def connect(host, port):
  pass
  
