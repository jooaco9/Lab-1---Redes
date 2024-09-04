from jsonrpc_redes2 import connect 
from jsonrpc_redes2 import ClientError 
import time
def test_client():
    # Este es el cliente de prueba que se ejecuta contra el
    # servidor de prueba en el módulo server.
    try:
        print('=============================')
        print('Iniciando pruebas de casos sin errores.')
        #ip = 200.0.0.10
        try:
            connS1 = connect('localhost', 8080)  
        except Exception as e:
            print('No se pudo conectar al servidor')
            print(e.code, e.message)
            if e.data is not None:
                print(e.data)  # Imprime data solo si existe
            return
        
        value = 'Testing!'
        result = connS1.echo(value)
        assert result == value
        print('Test simple completado.')
        
        result = connS1.echo(message='No response!', notify = False)
        assert result == 'No response!'
        print('Test de notificación completado.')
        result = connS1.echo_concat('a', 'b', 'c', 'd')
        assert result == 'abcd'
        print('Test de múltiples parámetros completado')

        result = connS1.echo_concat(msg1='a', msg2='b', msg3='c', msg4='d')
        assert result == 'abcd'
        print('Test de múltiples parámetros con nombres completado')
        
        result = connS1.echo(message=5)
        assert result == 5
        print('Otro test simple completado.')
        
        result = connS1.summa(1, 2, 3, 4, 5)
        assert result == 15
        print('Test de suma completado.')

        result = connS1.summa(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        assert result == 55
        print('Segundo test de suma con 10 parámetros completado')
        print('=============================')
        print('Pruebas de casos sin errores completadas.')
        print('=============================')
        print('Iniciando pruebas de casos con errores.')


        try:
            connS2 = connect('localhost', 8080)
        except Exception as e:
            print('No se pudo conectar al servidor')
            print(e.code, e.message)
            if e.data is not None:
                print(e.data)  # Imprime data solo si existe
            return
        
        try:
            connS2.echo()
        except Exception as e:
            print('Llamada incorrecta sin parámetros. Genera excepción necesaria.')
            print(e.code, e.message)
        else:
            print('ERROR: No lanzó excepción.')
            
        try:
            connS2.foobar(5, 6)
        except Exception as e:
            print('Llamada a método inexistente. Genera excepción necesaria.')
            print(e.code, e.message)
        else:
            print('ERROR: No lanzó excepción.')

        try:
            connS2.echo_concat('a', 'b', 'c')
        except Exception as e:
            print('Llamada incorrecta genera excepción interna del servidor.')
            print(e.code, e.message)
        else:
            print('ERROR: No lanzó excepción.')

        try:
            connS2.echo_concat('a', msg2='b', msg3='c', msg4='d')
        except Exception as e:
            print('Llamada incorrecta genera excepción en el cliente.')
            print(e)
        else:
            print('ERROR: No lanzó excepción.')
            
        connS2.close()
        connS1.close()

        print('=============================')
        print("Pruebas de casos con errores completadas.")
    except ClientError as e:
        print(f"Client error: {e.message}")

if __name__ == "__main__":
    test_client()