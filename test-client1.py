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
    
    # Test de concatenar simple
    result = connS1.concatenar('a', 'b')
    assert result == 'ab'
    print('Test de concatenar simple')
    
    result = connS1.sumar(1, 2, 3, 4, 5)
    assert result == 15
    print('Test de sumar completado.')

    result = connS1.sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert result == 55
    print('Segundo test de suma con 10 parámetros completado')

    result = connS1.potencia(3, 2)
    assert result == 9
    print('Test de potencia completado.') 

    try:
      connS3 = connect('localhost', 8082)  
      connS4 = connect('localhost', 8082)
    except Exception as e:
      print('No se pudo conectar al servidor')
      print(e.code, e.message)
      if e.data is not None:
        print(e.data)  # Imprime data solo si existe
      return
    
    result = connS3.es_cadena_numerica('123')
    assert result 
    print('Test de cadena numerica completada')

    result = connS4.concatenar_listas([1,2,3],[4,5,6])
    assert result == [1,2,3,4,5,6]
    print('Test de concatenar listas completada')

    result = connS3.echo('hola}')
    assert result == 'hola}'
    print('Test de echo completada')

    result = connS4.echo('holi', notify = True)
    assert result == None
    print('Test de notify completada')

    print('=============================')
    print('Pruebas de casos sin errores completadas.')
    print('=============================')
    print('Iniciando pruebas de casos con errores.')

    try:
      connS2 = connect('localhost', 8080)
      print('Conexion Establecida')
    except Exception as e:
      print('No se pudo conectar al servidor')
      print(e.code, e.message)
      if e.data is not None:
        print(e.data)  # Imprime data solo si existe
      return
        
    try:
      connS2.concatenar()
    except Exception as e:
      print('Llamada incorrecta de concatenar sin parámetros. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.error()
    except Exception as e:
      print('Llamada a método inexistente. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    
    try:
      connS2.concatenar('a')
    except Exception as e:
      print('Llamada incorrecta de concatenar sin un parámetro. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.sumar()
    except Exception as e:
      print('Llamada incorrecta de sumar sin parámetros. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.sumar(1)
    except Exception as e:
      print('Llamada incorrecta de sumar sin un parámetro. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.sumar('a', 'b')
    except Exception as e:
      print('Llamada incorrecta de sumar tipo de parametros. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.sumar('a')
    except Exception as e:
      print('Llamada incorrecta de sumar sin un parámetro y tipo. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.potencia()
    except Exception as e:
      print('Llamada incorrecta de potencia sin parámetros. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    try:
      connS2.potencia('a')
    except Exception as e:
      print('Llamada incorrecta tipo de parametro. Genera excepción necesaria.')
      print(e.code, e.message)
    else:
      print('ERROR: No lanzó excepción.')

    connS2.close()
    connS1.close()
    connS3.close()
    connS4.close()

    print('=============================')
    print("Pruebas de casos con errores completadas.")
  except ClientError as e:
    print(f"Client error: {e.message}")

if __name__ == "__main__":
  test_client()