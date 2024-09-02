class ClientError(Exception):
    """Excepción base para errores del cliente."""
    def __init__(self, code, message, *args):
        self.code = code
        self.message = message
        super().__init__(self.message, *args)

class lanzarExcepcion(Exception):
    def __init__(self, code, message, *args):
        self.code = code
        self.message = message
        self.data = args  # Puedes usar esto para pasar datos adicionales si es necesario
        super().__init__(message)  # Pasar el mensaje a la clase base Exception

