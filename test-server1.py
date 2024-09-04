from jsonrpc_redes2 import Server
import math

def son_cadenas_iguales(cadena1, cadena2):
    """Verifica si dos cadenas son iguales."""
    if not isinstance(cadena1, str) or not isinstance(cadena2, str):
        return "Error: Ambos parámetros deben ser cadenas."
    return cadena1 == cadena2


def concatenar(cadena1, cadena2):
    return cadena1 + cadena2

def sumar(*args):
    return sum(args)

def potencia(base, exponente):
    return math.pow(base, exponente)

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(numero)

def factorialYmult(numero, multiplicador=1):
    """Calcula el factorial de un número y lo multiplica por un multiplicador opcional."""
    if numero < 0:
        return "Error: No se puede calcular el factorial de un número negativo"
    return math.factorial(numero) * multiplicador

server = Server(('localhost', 8080))
server.add_method(potencia)
server.add_method(raiz_cuadrada)
server.add_method(factorialYmult)
server.add_method(concatenar)
server.add_method(sumar)
server.add_method(son_cadenas_iguales)
server.serve()
