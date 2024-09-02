from libClientExceptions import *
from socket import *
from jsonrpc import JSONRPC
import json

class Client:
  def __init__(self, function):
    pass
    
  # Call
  def __call__(self, host, port):
    self.host = host
    self.port = port

    # Crear el socket TCP
    self.skt = socket(AF_INET, SOCK_STREAM)
    try:
      self.skt.connect((self.host, self.port))
      return self
  
    # Error al no poder conectarse
    except ConnectionRefusedError as e:
      code = -32001
      message = "Connection Refused"
      data = str(e)
     # response = JSONRPC.create_error_response(code, message, data=str(e))
     # print(f"{response['error']['message']} -> {response['error']['data']}")

    except TimeoutError as e:
      code = 10060
      message = "timeout"
      data = str(e)
     # response = JSONRPC.create_error_response(code, message, data=str(e))
    #  print(f"{response['error']['message']} -> {response['error']['data']}")    
    except gaierror as e:
      code = 11001
      message = "getaddrinfo failed"
      data = ''
    #  response = JSONRPC.create_error_response(code, message, data=str(e))
    #  print(f"{response['error']['message']} -> {response['error']['data']}")
    
    raise lanzarExcepcion(code,message,data)

  # getattr 
  def __getattr__(self, name):
    def method(*args,**kwargs):
      notify = kwargs.pop('notify', False)
      args = list(args) + list(kwargs.values())
      # Verificacion de notificacion para crear request o notificacion
      if notify:
          request = JSONRPC.create_notification(name, args)
      else:
          request = JSONRPC.create_request(name, args)
      
      # Se manda la request
      self.skt.sendall(json.dumps(request).encode())

      if not notify:
        buff = ""

        # Recibir response
        while not "}" in buff:
          try:
            data = self.skt.recv(1024).decode()
            if not data:
              break
            buff += data
          except Exception as e:
            print(f"Error: {e}")
            break 

        try:
          response = json.loads(buff) # deserialización
        except json.JSONDecodeError:
          response = JSONRPC.invalid_request()
          error_message = response['error']['message']
          error_data = response['error'].get('data')
          code = response['error']['code']
          raise lanzarExcepcion(code, error_data,error_message)
        #ENDWHILE

        # Verificacion de si es respuesta con resultado o si es un error
        if('result' in response):
          return response['result']
        else:
          error_message = response['error']['message']
          error_data = response['error'].get('data')
          code = response['error']['code']
          raise lanzarExcepcion(code, error_message,error_data)

      else:
        return 
      
    return method
    
  def close(self):
    self.skt.close()

@Client
def connect(host, port):
  pass
  
