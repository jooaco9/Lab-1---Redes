from jsonrpc_redes import Server
import math
import time
def concatenar(cadena1, cadena2):
  """Concatena dos cadenas de texto."""
  return cadena1 + cadena2

def sumar(a1, a2, *args):
  """Suma n numeros. Puede recibir desde 2 hasta n numeros."""
  return a1 + a2 + sum(args)

def potencia(base, exponente):
  """Calcula la potencia de un numero."""
  return math.pow(base, exponente)

def crear_usuario(nombre, edad=None, ciudad="Montevideo"):
  nomCiu = f"Nombre: {nombre} Ciudad: {ciudad}" 
  if edad:
    return nomCiu + f" Edad: {edad}"
  return nomCiu
#ip = '200.0.0.10'

def hacer_tiempo():
  time.sleep(10)
  return '10 segundos'

server = Server(('localhost', 8080))
server.add_method(potencia)
server.add_method(hacer_tiempo)
server.add_method(concatenar)
server.add_method(sumar)
server.add_method(crear_usuario)
server.serve()
