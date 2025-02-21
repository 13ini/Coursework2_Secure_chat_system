import socket
import threading
from encryption import decrypt_message

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345

clients = []  # List to store client connections

# Broadcast messages to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Handle individual client connection
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(client_socket)
    
    while True:
        try:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break
            
            decrypted_msg = decrypt_message(encrypted_msg)
            print(f"[{addr}] Encrypted: {encrypted_msg}")
            print(f"[{addr}] Decrypted: {decrypted_msg}")
            
            # Broadcast message to others
            broadcast(encrypted_msg, client_socket)
        except Exception as e:
            print(f"[ERROR] {addr}: {e}")
            break

    print(f"[DISCONNECTED] {addr} left.")
    clients.remove(client_socket)
    client_socket.close()

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[LISTENING] Server running on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    start_server()
