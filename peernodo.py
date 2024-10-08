import grpc
import torrent_pb2
import torrent_pb2_grpc
import socket
import uuid
from concurrent import futures 
import threading
import time

peer_files = []  # Lista de archivos del peer
tracker_channel = None
tracker_stub = None

# Obtener IP local automáticamente
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

# Conexión con el Web Server
def connect_to_web_server():
    local_ip = get_local_ip()
    with grpc.insecure_channel('54.159.93.33:50051') as web_server_channel:
        web_server_stub = torrent_pb2_grpc.TorrentServiceStub(web_server_channel)
        response = web_server_stub.GetTorrent(torrent_pb2.TorrentRequest(peer_ip=local_ip))
        tracker_ip = response.tracker_ip
        tracker_port = response.tracker_port
        print(f"Conectado al Web Server. Tracker IP: {tracker_ip}, Tracker Port: {tracker_port}")
        return tracker_ip, tracker_port

# Conexión con el Tracker
def connect_to_tracker(tracker_ip, tracker_port, peer_files):
    global tracker_channel, tracker_stub
    local_ip = get_local_ip()

    tracker_address = f"{tracker_ip}:{tracker_port}"
    tracker_channel = grpc.insecure_channel(tracker_address)
    tracker_stub = torrent_pb2_grpc.TorrentServiceStub(tracker_channel)

    file_list = [torrent_pb2.File(file_name=file['name'], file_size=file['size']) for file in peer_files]
    response = tracker_stub.RegisterPeer(torrent_pb2.PeerRequest(peer_ip=local_ip, files=file_list))

    print("Peer registrado con éxito:", response)

    if response.updated_files:
        update_peer_files(response.updated_files)

    print(f"Peer registrado con Tracker: {response.status}, IP: {local_ip}, Dirección del Tracker: {tracker_address}")

    for file in peer_files:
        file_name = file['name']
        file_size = int(file['size'])
        tracker_stub.UploadFile(torrent_pb2.UploadFileRequest(peer_ip=local_ip, file_name=file_name, file_size=file_size))
        print(f"Archivo '{file_name}' con tamaño {file_size} MB subido al Tracker.")

def update_peer_files(updated_files):
    global peer_files
    peer_files.clear()
    for file in updated_files:
        if not any(f['name'] == file.file_name for f in peer_files):
            peer_files.append({'name': file.file_name, 'size': file.file_size})
            print(f"Archivo '{file.file_name}' añadido a la lista del peer.")

# Desconexión del tracker
def disconnect_from_tracker():
    global tracker_channel, tracker_stub
    if tracker_stub:
        try:
            response = tracker_stub.UnregisterPeer(torrent_pb2.PeerRequest(peer_ip=get_local_ip()))
            print(f"Respuesta del tracker: {response.status}")
        except grpc.RpcError as e:
            print(f"Error desconectando del tracker: {e}")
        finally:
            tracker_channel.close()
            tracker_stub = None
            print("Peer desconectado del Tracker y canal cerrado.")
    else:
        print("No conectado al tracker.")

# Función de búsqueda
# def search_file():
#     if tracker_stub:
#         file_name = input("Nombre del archivo para obtener: ")
#         response = tracker_stub.GetFile(torrent_pb2.GetFileRequest(file_name=file_name))
        
#         if response.peers:  # Verifica si hay peers
#             print(f"Archivo '{file_name}' encontrado en los siguientes peers:")
#             peer_ips = []
#             for peer in response.peers:
#                 print(f"Archivo encontrado en el Peer con IP: {peer.peer_ip}")
#                 peer_ips.append(peer.peer_ip)
#             connection_menu(peer_ips)
#         else:
#             print("Archivo no encontrado.")
#     else:
#         print("No conectado al tracker.")

def search_file():
    if tracker_stub:
        file_name = input("Nombre del archivo para obtener: ")
        response = tracker_stub.GetFile(torrent_pb2.GetFileRequest(file_name=file_name))
        
        if response.peers:
            for peer in response.peers:
                peer_ip = peer.peer_ip
                print(f"Preguntando a {peer_ip} por el archivo '{file_name}'...")
                
                # Conectar al peer y solicitar el archivo
                with grpc.insecure_channel(f'{peer_ip}:50053') as channel:
                    peer_stub = torrent_pb2_grpc.PeerFileServiceStub(channel)
                    file_response = peer_stub.GetFile(torrent_pb2.GetFileRequest(file_name=file_name))
                    
                    print("Recibiendo archivo...")
                    if file_response.status == "Success":
                        print("Archivo recibido!")
                        # Aquí actualiza la lista del peer con el archivo recibido
                    else:
                        print("Error al recibir el archivo.")
                break  # Solo solicitamos a un peer por ahora
        else:
            print("Archivo no encontrado.")
    else:
        print("No conectado al tracker.")

# Menú de conexión a un peer
def connection_menu(peer_ips):
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Conectarse a un Peer")
        print("2. Volver al menú de búsqueda")
        option = input("Ingresa tu opción: ")

        if option == "1":
            connect_to_peer(peer_ips)
        elif option == "2":
            return
        else:
            print("Opción no válida. Intenta de nuevo.")

# Función para conectarse a un peer
def connect_to_peer(peer_ips):
    if not peer_ips:
        print("No hay peers disponibles para conectarse.")
        return
    
    print("\nPeers disponibles para conectarse:")
    for i, ip in enumerate(peer_ips):
        print(f"{i+1}. {ip}")
    
    try:
        choice = int(input("Selecciona el número del Peer con el que deseas conectarte: "))
        if 1 <= choice <= len(peer_ips):
            peer_ip = peer_ips[choice - 1]
            print(f"Conectando al Peer con IP: {peer_ip}...")
            # Aquí puedes agregar la lógica para conectarte al peer
            print("Archivo entregado.")  # Simulación de entrega de archivo
        else:
            print("Selección no válida. Intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

# Servidor gRPC
class TorrentService(torrent_pb2_grpc.TorrentServiceServicer):
    def GetFile(self, request, context):
        print(f"Solicitud recibida para el archivo: {request.file_name}")
        response = torrent_pb2.GetFileResponse()
        # Aquí debes agregar la lógica para manejar la solicitud de archivo
        # Simulamos que encontramos un peer
        response.peers.add(peer_ip=get_local_ip())  # Ejemplo de peer encontrado
        return response

# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     torrent_pb2_grpc.add_TorrentServiceServicer_to_server(TorrentService(), server)
#     server.add_insecure_port('[::]:50053')
#     server.start()
#     print("Servidor gRPC escuchando en el puerto 50053...")
#     try:
#         while True:
#             time.sleep(86400)  # Mantener el servidor corriendo
#     except KeyboardInterrupt:
#         server.stop(0)

# Clase para manejar las solicitudes de otros peers
class PeerFileService(torrent_pb2_grpc.PeerFileServiceServicer):
    def GetFile(self, request, context):
        file_name = request.file_name
        print(f"Solicitud del peer con IP {context.peer()} busca archivo {file_name}...")
        
        # Simula la entrega del archivo
        time.sleep(2)  # Simula un retraso en la entrega
        print("Entregando archivo...")
        
        time.sleep(2)  # Simula un retraso en la entrega
        print("Archivo Entregado")
        
        # Aquí deberías implementar la lógica para enviar el archivo real
        return torrent_pb2.UploadFileResponse(status="Success", file_name=file_name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    torrent_pb2_grpc.add_PeerFileServiceServicer_to_server(PeerFileService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Servidor de archivos del peer escuchando en el puerto 50053...")
    server.wait_for_termination()

def run():
    server_thread = threading.Thread(target=serve)
    server_thread.start()
    tracker_ip, tracker_port = connect_to_web_server()  # Conectar al Web Server
    
    global tracker_channel, tracker_stub
    tracker_channel = None
    tracker_stub = None

    while True:
        print("\nMenu:")
        print("1. Conectar al Tracker")
        print("2. Agregar archivo a la lista del peer")
        print("3. Eliminar archivo de la lista del peer")
        print("4. Ver Lista del Peer")
        print("5. Salir")

        choice = input("Ingresa tu opción: ")

        if choice == '1':
            connect_to_tracker(tracker_ip, tracker_port, peer_files)
            
            while True:
                print("\nMenú del Tracker:")
                print("1. Buscar archivo")
                print("2. Salir del Tracker")

                tracker_choice = input("Ingresa tu opción: ")

                if tracker_choice == '1':
                    search_file()  # Buscar un archivo en el tracker
                elif tracker_choice == '2':
                    disconnect_from_tracker()
                    break
                else:
                    print("Opción inválida. Por favor elige una opción válida.")

        elif choice == '2':
            file_name = input("Ingresa el nombre del archivo a agregar: ")
            if any(file['name'] == file_name for file in peer_files):
                print(f"El archivo '{file_name}' ya existe en la lista del peer.")
            else:
                while True:
                    file_size_input = input("Ingrese el tamaño del archivo en MB: ")
                    if file_size_input.isdigit():
                        file_size = int(file_size_input)
                        peer_files.append({'name': file_name, 'size': file_size})
                        print(f"Archivo '{file_name}' con tamaño {file_size} MB agregado a la lista del peer.")
                        break
                    else:
                        print("Error: Solo valores numéricos son permitidos. Intente nuevamente.")

        elif choice == '3':
            file_name = input("Ingresa el nombre del archivo a eliminar: ")
            file_to_remove = None
            for file in peer_files:
                if file['name'] == file_name:
                    file_to_remove = file
                    break
            
            if file_to_remove:
                peer_files.remove(file_to_remove)
                print(f"Archivo '{file_name}' eliminado de la lista del peer.")
            else:
                print(f"El archivo '{file_name}' no está en la lista.")

        elif choice == '4':
            if peer_files:
                print("\nLista de archivos del peer:")
                for file in peer_files:
                    print(f"- {file['name']} (Size: {file['size']})")
            else:
                print("No tienes archivos en la lista del peer.")
                
        elif choice == '5':
            print("Saliendo...")
            if tracker_stub:
                disconnect_from_tracker()
            break

        else:
            print("Opción inválida. Por favor elige una opción válida.")

if __name__ == '__main__':
    run()