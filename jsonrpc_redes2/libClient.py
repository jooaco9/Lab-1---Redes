from socket import *
from .jsonrpc import JSONRPC
import json

class lanzarExcepcion(Exception):
  def __init__(self, code, message, *args):
    self.code = code
    self.message = message
    self.data = args  # Puedes usar esto para pasar datos adicionales si es necesario
    super().__init__(message)  # Pasar el mensaje a la clase base Exception

class ClientError(Exception):
  def __init__(self, message,*args):
    self.code = 10054
    self.message = message
    self.data = args
    super().__init__(message)  # Pasar el mensaje a la clase base Exception

class Client:
  def __init__(self, function):
    pass
    
  # Call
  def __call__(self, host, port):
    self.host = host
    self.port = port

    self.skt = socket(AF_INET, SOCK_STREAM)
    try:
      self.skt.connect((self.host, self.port)) 
      self.skt.close()
      # Crear el socket TCP
      return self    # Error al no poder conectarse
    except ConnectionRefusedError as e:
      code = -32001
      message = "Connection Refused"
      data = str(e)

    except TimeoutError as e:
      code = 10060
      message = "timeout"
      data = str(e)

    except gaierror as e:
      code = 11001
      message = "getaddrinfo failed"
      data = ''

    except OSError as e:
      code = 101
      message = "getaddrinfo failed"
      data = ''

    raise lanzarExcepcion(code,message,data)    

  # getattr 
  def __getattr__(self, name):
    #Me conecto con el servidor
    error = True
    self.skt = socket(AF_INET, SOCK_STREAM)
    try:
      self.skt.connect((self.host, self.port))
      error = False
    # Error al no poder conectarse
    except ConnectionRefusedError as e:
      code = -32001
      message = "Connection Refused"
      data = str(e)

    except TimeoutError as e:
      code = 10060
      message = "timeout"
      data = str(e)
 
    except gaierror as e:
      code = 11001
      message = "getaddrinfo failed"
      data = ''

    except OSError as e:
      code = 101
      message = "getaddrinfo failed"
      data = ''
    if error:
      raise lanzarExcepcion(code,message,data)
    
    #Llamo al metodo
    def method(*args,**kwargs):
      notify = kwargs.pop('notify', False)
      if(args and kwargs):  
        response = JSONRPC.internal_error()
        error_message = response['error']['message']
        error_data = response['error'].get('data')
        code = response['error']['code']
        raise lanzarExcepcion(code, error_message, error_data)
      
      if(kwargs):
        args = kwargs
        
      # Verificacion de notificacion para crear request o notificacion
      if notify:
          request = JSONRPC.create_notification(name, args)
      else:
          request = JSONRPC.create_request(name, args)
      
      # Se manda la request
      try:
        self.skt.sendall(json.dumps(request).encode())
      except ConnectionResetError as e: 
        raise ClientError("Connection was reset by the server.",str(e))

      if not notify:
        buff = ""

        # Recibir response
        self.skt.settimeout(2) # Setteo de timeout
        while buff.count("{") != buff.count("}") or buff.count("{") < 1 or buff[-1] != "}":
          try:
            data = self.skt.recv(1024).decode()
            if not data:
              break
            buff += data
          except Exception as e:
            break
        

        try:
          response = json.loads(buff) # deserialización
          print(f"RESPONSE: {response}")
        except json.JSONDecodeError:
          response = JSONRPC.invalid_request()
          error_message = response['error']['message']
          error_data = response['error'].get('data')
          code = response['error']['code']
          raise lanzarExcepcion(code, error_message, error_data)
        #ENDWHILE

        # Verificacion de si es respuesta con resultado o si es un error
        if('result' in response):
          return response['result']
        else:
          error_message = response['error']['message']
          error_data = response['error'].get('data')
          code = response['error']['code']
          raise lanzarExcepcion(code, error_message, error_data)

      else:
        return 
      
    return method
    
  def close(self):
    self.skt.close()

@Client
def connect(host, port):
  pass
  
