from jsonrpc_redes2 import Server
import sys
import time

def test_server():
    # Este método es un ejemplo de cómo se puede usar el servidor.
    # Se inicia un servidor en el puerto 8080 y se añaden dos métodos
    
    host, port = 'localhost', 8080
    
    def echo(message):
        return message
        
    def summa(*args):
        return sum(args)

    def echo_concat(msg1, msg2, msg3, msg4):
        return msg1 + msg2 + msg3 + msg4
        
    server = Server((host, port))
    server.add_method(echo)
    server.add_method(summa)
    server.add_method(echo_concat)
    #server_thread = threading.Thread(target=server.serve)
    #server_thread.daemon = True
    #server_thread.start()
    server.serve()

    #print ("Servidor ejecutando: %s:%s" % (host, port))
    
if __name__ == "__main__":
    test_server()