from jsonrpc_redes2 import Server

def es_cadena_numerica(cadena):
    """Verifica si una cadena representa un número."""
    return cadena.isdigit()


def concatenar_listas(lista1, lista2):
    """Concatena dos listas de cadenas."""
    return lista1 + lista2

def echo(message):
    """Devuelve el mismo mensaje que se recibio."""
    return message

server = Server(('localhost', 8082))

server.add_method(echo)
server.add_method(concatenar_listas)
server.add_method(es_cadena_numerica)
server.serve()
