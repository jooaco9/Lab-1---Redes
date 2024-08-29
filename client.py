from libClient import *

conn = connect('localhost', 8080)
if conn:

  print("Conexión exitosa.")

  # si es notificacion poner -> notify = true
  print(f"Resultado de la resta 9 - 6 = {conn.resta(9, 6, notify = False)}")
  print(f"Resultado de la resta 9 - 19 = {conn.resta(9, 19, notify = False)}")
  print(f"Resultado de la multiplicacion 9 * 9 = {conn.multiplicar(9, 9, notify = False)}")
  print(f"Resultado de la suma 23 + 7 = {conn.suma(23, 7, notify = False)}")
  conn.close()
  print("Cerrando conexión...")
