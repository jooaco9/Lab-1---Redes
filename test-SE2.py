from jsonrpc_redes2 import Server

def es_cadena_numerica(cadena):
  """Verifica si una cadena representa un número."""
  return cadena.isdigit()

def concatenar_listas(lista1, lista2):
  """Concatena dos listas de cadenas."""
  return lista1 + lista2, lista2 + lista1

def echo(message):
  """Devuelve el mismo mensaje que se recibio."""
  return message

def greeting():
  return "Buenos dias"

server = Server(('localhost', 8082))

server.add_method(echo)
server.add_method(concatenar_listas)
server.add_method(es_cadena_numerica)
server.add_method(greeting)
server.serve()





