# Instrucciones para la Ejecución Local

Para ejecutar el sistema de manera local, seguir los siguientes pasos:

## Configuración de los Servidores

1. En los archivos `test-SE1.py` y `test-SE2.py`, cambia la dirección IP a `localhost`:
   - Reemplaza la IP actual por `localhost` en ambos archivos.
   
2. En el archivo `test-SE2.py`, cambiar el puerto en el que se levanta:
   - Elegir un puerto diferente al que utiliza `test-SE1.py`.

## Configuración de los Clientes

1. En los archivos `test-CE1.py`, `test-CE2.py` y `test-CE3.py`, realiza las siguientes modificaciones:
   - Comenta las siguientes líneas:
     ```python
     ip1 = '200.0.0.10'
     ip2 = '200.100.0.15'
     ```
   - Descomenta la línea correspondiente a `localhost`:
     ```python
     # ip1 = ip2 = 'localhost'
     ```

2. En donde se utiliza la variable `ip2`, actualizar el puerto para que coincida con el puerto configurado en `test-SE2.py`.

## Ejecución del Sistema

1. Inicia los servidores:
   - Ejecuta primero `test-SE1.py` y luego `test-SE2.py` para que ambos servidores estén escuchando.

2. Ejecuta el cliente:
   - Una vez que los servidores estén activos, ejecutar cualquiera de los clientes (`test-CE1.py`, `test-CE2.py` o `test-CE3.py`), según lo que desees probar.
