from jsonrpc_redes2 import Server
import math

def concatenar(cadena1, cadena2):
    """Concatena dos cadenas de texto."""
    return cadena1 + cadena2

def sumar(a1, a2, *args):
    """Suma n numeros. Puede recibir desde 2 hasta n numeros."""
    return a1 + a2 + sum(args)

def potencia(base, exponente):
    """Calcula la potencia de un numero."""
    return math.pow(base, exponente)

server = Server(('localhost', 8080))
server.add_method(potencia)
server.add_method(concatenar)
server.add_method(sumar)
server.serve()
