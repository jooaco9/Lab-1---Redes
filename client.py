from socket import *
from jsonrpc import JSONRPC
import json

class Client:
  def __init__(self,function):
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
    def method(*args):
      request = JSONRPC.create_request(name, args)
      self.skt.sendall(json.dumps(request).encode())
      
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

      return response['result']
    return method
    
@Client
def connect(host, port):
  pass
  
conn = connect('localhost', 8080)
if conn:
    print("Conexión exitosa.")
    print(conn.resta(9, 6))

else:
    print("Conexión fallida.")
