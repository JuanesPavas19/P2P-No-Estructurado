#Tópicos Especiales en Telemática


Estudiante(s): Juan Jose Velez Orozco, jjvelezo@eafit.edu.co, Juan Esteban Pavas, jepavase@eafit.edu.co

Profesor: JUAN CARLOS MONTOYA MENDOZA, jcmontoyay@eafit.edu.co

# Reto N1. Aplicaciones P2P

## 1. Breve descripción de la actividad

Este proyecto desarrolla un sistema de comunicación Peer-to-Peer (P2P) no estructurado utilizando gRPC para la transferencia de archivos entre peers. Cada peer puede actuar como cliente y servidor, permitiendo registrar y buscar archivos dentro de la red, así como descargar archivos directamente de otros peers.

### 1.1. Aspectos cumplidos o desarrollados de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Conexion entre webserver y redirecion al tracker.
- Manejo de registros en tracker.
- Tracker registra los archivos de cada peer en la red.
- Tracker permite la búsqueda de archivos en la red.
- Tracker se encarga de gestionar Fragmentación.
- Tracker encraga de gestionar replicación de archivos.
- Tracker asume la tarea de consistencia en la red.
- Los peers pueden preguntar a otros peers por el archivo (Comunicación directa)
- Manejo de Concurrencia en la red.
- Manejor de Varias Solicitudes al Tiempo.
- Uso de gRPC para la comunicación.



### 1.2. Aspectos NO cumplidos o desarrollados de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- La replicacion se hace al azar (no por disponibilidad o geografia).
- No se guardan archivos en el tiempo (falta de persistencia).
- Manejo de archivos duplicados básico.
- Intento de desarrollo en Java.
- Manejo IDs.


## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

<Descripción de la arquitectura del sistema, patrones de diseño utilizados y cualquier práctica relevante aplicada en el desarrollo del proyecto.>

## 3. Descripción del ambiente de desarrollo y técnico

### Lenguaje de programación y herramientas utilizadas:
- Python 3.X
- gRPC 1.38.X
- Librerías: grpcio, grpcio-tools, socket (solo para conseguir la IP), futures, threading

### Como se compila y ejecuta:

- En AWS, se debe crear un entorno virtual y ejecutar:
'python3 -m venv venv
source venv/bin/activate
pip install grpcio grpcio-tools'

- Para compilar y ejecutar se debe poner:
'nano tracker.py/webserver'
nano torrent.proto'
'python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. torrent.proto'
Correr en cada PC: python torrent.py/webserver.py/peernodo.py

### Detalles técnicos y configuración de parámetros del proyecto:

- El web server escucha el puerto 50051, El tracker escucha el puerto 50052, entre peers escichan el peurto 50053.
- Los parametros de replicación y fragmentacion se pueden configurar.

### Estructura de directorios y archivos importantes del proyecto:

/
|-- tracker.py
|-- peernodo.py
|-- webserver.py
|-- torrent_pb2.py
|-- torrent_pb2_grpc.py
|-- torrent.proto


## 4. Descripción del ambiente de EJECUCIÓN (en producción)

### IP o nombres de dominio en nube o en la máquina servidor:

- La IP varia segun el momento que se ejecute la instancia (es variable).

### Como se lanza el servidor:

'python3 -m venv venv
source venv/bin/activate
pip install grpcio grpcio-tools
nano tracker.py/webserver
nano torrent.proto'
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. torrent.proto'
 python torrent.py/webserver.py/peernodo.py'

### Mini guía de usuario:

<Instrucciones breves sobre cómo un usuario final utilizaría el software o la aplicación.>

## 5. Otra información relevante para esta actividad.

<Incluya cualquier otra información que considere relevante para comprender o utilizar el proyecto.>

# Referencias:

- [Nombre del sitio o autor](URL)
- [Nombre del sitio o autor](URL)
- [URL de donde se tomó información para desarrollar este proyecto]