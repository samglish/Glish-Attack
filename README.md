# Glish-Attack
### Voici le plan du script client (victime) qu’on va créer :
🔁 Fonctions de base
* Connexion reverse shell
* Exécution de commandes shell
🎥 Surveillance
📸 Capture webcam (photo)
🎬 Capture vidéo (10 sec)
🎙️ Enregistrement audio (10 sec via micro)
⌨️ Espionnage
⌨️ Keylogger en fond
💾 Exfiltration de fichiers
📁 Navigation et lecture de fichiers

### On va utiliser :

```bash
pip install opencv-python sounddevice scipy pynput
```
* Webcam	`cv2` (OpenCV)
* Microphone	`sounddevice, scipy.io.wavfile`
* Keylogger	`pynput`
* Transfert fichier	`base64, open()`
