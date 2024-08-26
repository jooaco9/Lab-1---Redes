# Diseño de la Biblioteca `jsonrpc_redes`

## 1. Objetivo

El objetivo de esta biblioteca es permitir la comunicación RPC entre un cliente y un servidor utilizando JSON-RPC 2.0 sobre TCP.

## 2. Componentes Principales

### 2.1. Clase `Client`

# Responsabilidad:

# Gestionar la conexión TCP con el servidor y permitir que el cliente haga llamadas a procedimientos remotos de manera transparente.

# Metodos y Funcionalidades:

- **Método `connect(address, port)`**:

  - Establece una conexión TCP con el servidor en la dirección y puerto especificados.
  - Devuelve un objeto de conexión que permite hacer llamadas a procedimientos remotos.
  - Para establecer conexion se tiene que pedir la ip y puerto con (ip, port = client.gethost()) si es local
    y (ip, port = client.getpeer()) si no.
  - Creo un socket master con (master = socket.tcp())
  - Luego para conectarte al Servidor (client, err = master.connect(address, port))

- **Método `__getattr__(self,method_name:str,*args,notify = false) -> Callable`**:

  - Intercepta cualquier llamada a un método no definido explícitamente en la clase.
  - Permite crear dinámicamente métodos remotos en el cliente, basados en el nombre del método llamado.
  -

- **Método `__call__(self, *args, notify = false) -> Any`**:

  - Envía una solicitud JSON-RPC al servidor con los argumentos dados.
  - Para enviar con socket se usa (remain, err = client.send(data))
  - Si `notify=True`, envía una notificación (no espera respuesta).
  - Devuelve el resultado del procedimiento remoto, o None en el caso de una notificación.

- **Método `disconnect(self) -> None:`**:
  - Cierra la conexión TCP con el servidor.
  - para cerrar el socket se usa (client.close())

### 2.2. Clase `Server`

# Responsabilidad:

# Escuchar conexiones entrantes de clientes, procesar solicitudes JSON-RPC y ejecutar los procedimientos registrados en el servidor.

# Metodos y Funcionalidades:

- **Método `__init__(self, address: str, port: int):`**:

  - Inicializa el servidor, configurando la dirección IP y el puerto donde estará escuchando.
  - Para ello debe crear el socket con (master = socket.tcp()) y luego (master.bind(address, port))
  - Luego convertirlo en Servidor con (server = master.listen())

- **Método `add_method(proc) -> None`**:

  - Registra un procedimiento que el servidor puede ejecutar en respuesta a una solicitud JSON-RPC.
  - method debe ser una función que acepte argumentos y devuelva un resultado.

- **Método `serve(self) -> None:`**:

  - Inicia el servidor en modo bloqueante, esperando conexiones de clientes.
  - Utiliza hilos para manejar múltiples conexiones y solicitudes de manera concurrente.
  - Para cada conexión, llama a \_handle_client para procesar la solicitud.
  - Para esperar conexion de cliente se usa (client, err = server.accept())
  - y luego para crear un hilo (thread.new(function,parametro1,parametro2...))

- **Método `_handle_client(self, client_socket: socket.socket) -> None:`**:
  - Método interno que gestiona la interacción con un cliente específico.
  - Recibe solicitudes, ejecuta el procedimiento correspondiente, y envía la respuesta.
  - Para recibir la solicitud con socket se utiliza (data, err = client.receive())
    Y para enviar la respuesta (remain, err = client.send(data)).

### 3. Ejemplo de Uso

- # 3.1 Cliente:

  - conn = Client.connect('127.0.0.1', 8080)
  - result = conn.proc1(10, 20)
  - conn.disconnect()

- # 3.2 Servidor:

  - server = Server('0.0.0.0', 8080)
  - server.add_method(proc1)
  - server.add_method(proc2)
  - server.serve()

## 5. Detalles de Implementación

### 5.1. Formato de los Mensajes

- **Solicitud**: `{ "jsonrpc": "2.0", "method": "nombre_metodo", "params": [arg1, arg2], "id": 1 }`

  - "jsonrpc": "2.0" indica la versión del protocolo.
  - "method": "nombre_metodo" es el nombre del procedimiento remoto a ejecutar.
  - "params": ["arg1", "arg2"] contiene los parámetros que se enviarán al procedimiento remoto.
  - "id": 1 es un identificador único de la solicitud que permitirá al cliente asociar la respuesta con la solicitud correcta.

- **Respuesta**: `{ "jsonrpc": "2.0", "result": "resultado", "id": 1 }`

  - "result": "resultado" contiene el resultado de la ejecución del procedimiento remoto.
  - "id": 1 coincide con el identificador de la solicitud original.

- **Notificación**: `{ "jsonrpc": "2.0", "method": "nombre_metodo", "params": [arg1, arg2] }`
  - La notificación es similar a una solicitud, pero no incluye un "id", lo que indica que no se espera una respuesta.

# 6. Manejo del Transporte TCP

# 6.1. Cliente

        Conexión: Utiliza sockets TCP (socket.socket) para conectarse al servidor.
        Envío de Datos: Los mensajes JSON se convierten a formato string y se envían a través del socket.
        Recepción de Datos: El cliente lee la respuesta del servidor a través del socket y la convierte de JSON a un objeto Python.

# 6.2. Servidor

        Escucha: El servidor crea un socket que escucha conexiones en la dirección y puerto especificados.
        Aceptación de Conexiones: Cuando un cliente se conecta, se crea un nuevo hilo para manejar la comunicación con ese cliente.
        Manejo de Solicitudes: El servidor lee la solicitud JSON del cliente, ejecuta el procedimiento correspondiente, y envía la respuesta.

# 7. Manejo de Errores

# 7.1. Errores en el Cliente

        Errores de Conexión: Manejo de excepciones cuando no se puede conectar al servidor.
        Errores de Transmisión: Validar que los mensajes se envíen y reciban correctamente.

# 7.2. Errores en el Servidor

        Errores de Ejecución: Manejo de errores cuando un procedimiento no puede ejecutarse correctamente.
        Errores de Formato: Validar que las solicitudes JSON sean válidas y conformes a la especificación.

