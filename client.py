from jsonrpc_redes2 import connect 

conn = connect('localhost', 8080)
if conn:

  print("Conexión exitosa.")

  # si es notificacion poner -> notify = true
  print(conn.resta(9, 6, notify = False))
  print(conn.resta(9, 19, notify = False))
  print(conn.hola(4, 3, notify = True))
  try:
    print(conn.multiplicar(notify = False))  
  except Exception as e:
    print('error')
  try:
    print(conn.suma(23, 7, notify = False))
  except Exception as e:
    print('error') 
  try:  
    print(conn.multipliar(3, -1, notify=True))
  except Exception as e:
    print('error')
  try:
    print(conn.suma(9, 9, 9,))
  except Exception as e:
    print('error')
  conn.close()
  print("Cerrando conexión...")