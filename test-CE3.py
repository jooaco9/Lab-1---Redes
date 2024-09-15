from jsonrpc_redes import connect 
from jsonrpc_redes2 import ClientError 
import time
def test_client():
  # Este es el cliente de prueba que se ejecuta contra el
  # servidor de prueba en el módulo server.
  try:
    print('=======================================================================================')
    print('Iniciando pruebas de casos sin errores:\n')
    ip1 = '200.0.0.10'
    ip2 = '200.100.0.15'
    # ip1 = ip2 = 'localhost'
    try:
      connS1 = connect(ip1, 8080)
      connS2 = connect(ip2, 8080)
    except Exception as e:
      print('No se pudo conectar al servidor')
      print(e.code, e.message)
      if e.data is not None:
          print(e.data)  # Imprime data solo si existe
      return

    # Test de concatenar con kwargs
    result = connS1.concatenar(cadena1='Hola ', cadena2='Mundo')
    assert result == "Hola Mundo"
    print("Test de concatenar con kwargs completado.\n")

    # Test de metodo con mas de un valor de retorno de concatenar listas
    result1, result2 = connS2.concatenar_listas([1,2,3],[4,5,6])
    assert result1 == [1,2,3,4,5,6] 
    assert result2 == [4,5,6,1,2,3]
    print('Test de concatenar listas completada.\n')
    
    # Test de  echo
    result = connS2.echo('hola')
    assert result == 'hola'
    print('Test de echo completada.\n')

    # Test de sumar
    result = connS1.sumar(1,2, 3, 4, 5)
    assert result == 15
    print('Test de sumar completado.\n')

    # Test de notify activado
    result = connS2.echo('holi', notify = True)
    assert result == None
    print('Test de notify completada.\n')

    # Test de sumar con mas parametros
    result = connS1.sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert result == 55
    print('Segundo test de suma con 10 parámetros completado.\n')

    # Test de potencia
    result = connS1.potencia(3, 2)
    assert result == 9
    print('Test de potencia completado.\n') 

    # Test de greeting
    result = connS2.greeting()
    assert result == 'Buenos dias'
    print('Test de greeting completado.\n')

    # Test de crear usuario con todo
    result = connS1.crear_usuario('Juan', 30, 'Buenos Aires')
    assert result == 'Nombre: Juan Ciudad: Buenos Aires Edad: 30'
    print('Test de crear_usuario con todos los parámetros completado.\n')


    # Test con errors
    print('=======================================================================================')
    print('Pruebas de casos sin errores completadas.\n')
    print('=======================================================================================')
    print('Iniciando pruebas de casos con errores:\n')

    try:
      connS3 = connect(ip1, 8080)
      connS4 = connect(ip2, 8080)
      print('Conexion Establecida')
    except Exception as e:
      print('No se pudo conectar al servidor')
      print(e.code, e.message)
      if e.data is not None:
        print(e.data)  # Imprime data solo si existe
      return
    print('se conecta cons2')

    try:
      connS3.concatenar([1,2,3])
    except Exception as e:
      print('Llamada incorrecta de concatenar con menos parámetros. Genera excepción necesaria.')
      print(e.code, e.message, "\n")
    else:
      print('ERROR: No lanzó excepción.')

    # Test de error de llamar a un metodo inexistente
    try:
      connS3.error()
    except Exception as e:
      print('Llamada a método inexistente. Genera excepción necesaria.')
      print(e.code, e.message, "\n")
    else:
      print('ERROR: No lanzó excepción.')

    # Matar server 2 -> 200.100.0.15
    print("Matar servidor 200.100.0.15")
    time.sleep(15)

    try:
      connS4.echo("Muerto?")
    except Exception as e:
      print("Llamada a servidor desconectado. Genera excepción necesaria.")
      print(str(e), "\n")
    else:
      print('ERROR: No lanzó excepción.')

    # Test de error de llamar a un metodo con otro tipo de parametros
    try:
      connS3.sumar('a', 'b')
    except Exception as e:
      print('Llamada incorrecta de sumar tipo de parametros. Genera excepción necesaria.')
      print(e.code, e.message, "\n")
    else:
      print('ERROR: No lanzó excepción.')

    # Test de error de llamar a un metodo sin un parámetro y tipo incorrecto
    try:
      connS3.sumar('a')
    except Exception as e:
      print('Llamada incorrecta de sumar sin un parámetro y tipo. Genera excepción necesaria.')
      print(e.code, e.message, "\n")
    else:
      print('ERROR: No lanzó excepción.')

    # Test de error de conectarse a un servidor desconectado
    try:
      connS5 = connect('124.100.43.10', 8080)
    except Exception as e:
      print('No se pudo conectar al servidor')
      print(e.code, e.message)
      if e.data is not None:
        print(e.data)  # Imprime data solo si existe
      return

    print('=============================')
    print("Pruebas de casos con errores completadas.")
  except ClientError as e:
    print(f"Client error: {e.message}")

if __name__ == "__main__":
  test_client()