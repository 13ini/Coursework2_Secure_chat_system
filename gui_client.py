import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import socket
import threading
from encryption import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 12345
client_socket = None

def connect_to_server():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        messagebox.showinfo("Success", "Connected to the server!")
        threading.Thread(target=receive_messages, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

def send_message():
    message = msg_entry.get()
    if message and client_socket:
        encrypted_message = encrypt_message(message)
        print(f"Encrypted message sent: {encrypted_message}")  # Show encrypted message
        client_socket.send(encrypted_message)
        chat_box.insert(tk.END, f"You: {message}\n")
        msg_entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break
            print(f"Encrypted message received: {encrypted_msg}")  # Show encrypted message
            decrypted_msg = decrypt_message(encrypted_msg)
            chat_box.insert(tk.END, f"Friend: {decrypted_msg}\n")
        except:
            break

def quit_app():
    if client_socket:
        client_socket.close()
    root.destroy()

root = tk.Tk()
root.title("Secure Chat System")
root.geometry("600x500")

bg_image = Image.open("background.jpg")  
bg_image = bg_image.resize((600, 500))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

chat_box = scrolledtext.ScrolledText(root, width=50, height=15, bg="white")
chat_box.pack(pady=10)

msg_entry = tk.Entry(root, width=40)
msg_entry.pack(pady=5)

send_btn = tk.Button(root, text="Send", command=send_message, bg="green", fg="white")
send_btn.pack(pady=5)

connect_btn = tk.Button(root, text="Connect", command=connect_to_server, bg="blue", fg="white")
connect_btn.pack(pady=5)

quit_btn = tk.Button(root, text="Quit", command=quit_app, bg="red", fg="white")
quit_btn.pack(pady=5)

root.mainloop()
