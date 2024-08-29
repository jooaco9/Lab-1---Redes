from libClient import *

conn = connect('localhost', 8080)
if conn:

  print("Conexión exitosa.")

  # si es notificacion poner -> notify = true
  print(conn.resta(9, 6, notify = False))
  print(conn.resta(9, 19, notify = False))
  print(conn.hola(4, 3, notify = True))
  print(conn.multiplicar(notify = False))
  print(conn.suma(23, 7, notify = False))
  print(conn.multipliar(3, -1, notify=True))
  print(conn.suma(9, 9, 9,))
  conn.close()
  print("Cerrando conexión...")
