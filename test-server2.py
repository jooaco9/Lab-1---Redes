from jsonrpc_redes2 import Server

def es_cadena_numerica(cadena):
    """Verifica si una cadena representa un número."""
    if not isinstance(cadena, str):
        return "Error: El parámetro debe ser una cadena."
    return cadena.isdigit()


def concatenar_listas(lista1, lista2):
    """Concatena dos listas de cadenas."""
    if not all(isinstance(i, str) for i in lista1 + lista2):
        return "Error: Todos los elementos deben ser cadenas."
    return lista1 + lista2


def concatenar_cadenas(*args):
    """Concatena todas las cadenas proporcionadas."""
    if not all(isinstance(arg, str) for arg in args):
        return "Error: Todos los parámetros deben ser cadenas."
    return ''.join(args)

def unir_listas(lista, *args, **kwargs):
    """Une la lista proporcionada con elementos adicionales y argumentos nombrados."""
    if not isinstance(lista, list):
        return "Error: El primer parámetro debe ser una lista."
    lista.extend(args)
    lista.append(kwargs)
    return lista

#ejemplo resultado = unir_listas([1, 2], 3, 4, a=5, b=6)
#        print(resultado)  # [1, 2, 3, 4, {'a': 5, 'b': 6}]


server = Server(('localhost', 8080))

server.add_method(unir_listas)
server.add_method(concatenar_cadenas)
server.add_method(concatenar_listas)
server.add_method(es_cadena_numerica)
server.serve()
