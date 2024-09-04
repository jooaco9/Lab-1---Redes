from jsonrpc_redes2 import Server
import math

def concatenar(cadena1, cadena2):
    return cadena1 + cadena2

def sumar(a1, a2, *args):
    return a1 + a2 + sum(args)

def potencia(base, exponente):
    return math.pow(base, exponente)

server = Server(('localhost', 8080))
server.add_method(potencia)
server.add_method(concatenar)
server.add_method(sumar)
server.serve()
