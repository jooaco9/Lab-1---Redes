from jsonrpc_redes2 import Server

# Metodos del server
def suma(x, y):
  return x + y

def resta(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

# Inicializacion del server
server = Server(('localhost', 8080))
server.add_method(suma)
server.add_method(resta)
server.add_method(multiplicar)
server.serve()

