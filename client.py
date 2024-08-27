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
    except Exception as e:
      print(f"Error: {e}")

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
    
@Client
def connect(host, port):
  pass
  
conn = connect('localhost', 8080)
if conn:
    print("Conexión exitosa.")
  # #SI ES NOTIFICACION PONER notify = true
  #   print(f"Resultado de la resta 9 - 6 = {conn.restas(9, 6,notify = False)}")
else:
    print("Conexión fallida.")
