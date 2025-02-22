# Secure Chat System

## 📌 Project Overview
This project is a **Secure Chat System** that ensures **private and encrypted communication** between users using **Fernet encryption**. It provides both **Command-Line Interface (CLI)** and **Graphical User Interface (GUI)** options for user flexibility. The system protects against **Man-in-the-Middle (MITM) attacks, eavesdropping, and unauthorized access**, making it a reliable tool for secure messaging.

## 🔥 Features
✅ **End-to-End Encryption** – Messages are encrypted using **Fernet encryption** to ensure confidentiality.  
✅ **Real-Time Communication** – Enables instant messaging between multiple clients.  
✅ **Multi-Client Support** – The server handles multiple concurrent user connections using **socket programming and threading**.  
✅ **Dual Interface** – Supports both **CLI and GUI** clients.  
✅ **Logging and Monitoring** – The server keeps logs of connected clients and encrypted messages.  

## 🚀 Technologies Used
- **Python** (Core Programming Language)
- **Cryptography (Fernet Encryption)** – Ensures secure message transmission.
- **Socket Programming** – Facilitates real-time client-server communication.
- **Threading** – Manages multiple client connections simultaneously.
- **Tkinter** – Provides a user-friendly GUI interface.

## 🛠 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
 git clone https://github.com/yourusername/secure-chat-system.git
 cd secure-chat-system
```
### **2️⃣ Create a Virtual Environment**
```sh
 python -m venv secure_chat_env  
```
Activate the environment:  
- **Windows:** `secure_chat_env\Scripts\activate`
- **Mac/Linux:** `source secure_chat_env/bin/activate`

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Server**
```sh
python server.py
```

### **5️⃣ Run the Clients**
- **CLI Client:**
```sh
python cli_client.py
```
- **GUI Client:**
```sh
python gui_client.py
```

## 📜 Project Structure
```
secure-chat-system/
│-- server.py         # Server handling multiple clients
│-- cli_client.py     # Command-Line Interface Client
│-- gui_client.py     # Graphical User Interface Client
│-- encryption.py     # Handles encryption & decryption
│-- requirements.txt  # Required dependencies
│-- README.md         # Project Documentation
```

## 🖥️ Live Demonstration
📌 Run **server.py** and then execute **CLI or GUI clients** to establish a secure chat session.

- **Example Encrypted Message Transmission:**
  ```sh
  User1: Hello, how are you?
  Encrypted: gAAAAABkl...
  User2 (Decrypted): Hello, how are you?
  ```

## 🛠 Future Enhancements
✅ **Multi-Factor Authentication (MFA)** – Strengthen user authentication.
✅ **Improved Scalability** – Optimize server performance for large user bases.
✅ **Logging & Monitoring Systems** – Detect suspicious activities.
✅ **Performance Optimization** – Reduce encryption-decryption latency.

## 👨‍💻 Author
**Bini Manandhar**  
**BSc (Hons) in Ethical Hacking and Cybersecurity**  
**Softwarica College**  

## 📜 License
This project is licensed under the **MIT License** – feel free to modify and improve it!

## 🌟 Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork and submit a pull request. 🚀
