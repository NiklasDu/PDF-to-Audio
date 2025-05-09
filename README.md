# PDF-to-Audio

Ein Python-Projekt, das eine grafische Benutzeroberfläche (GUI) bereitstellt, um PDF-Dateien in Audio umzuwandeln. Das Projekt verwendet **PyQt6** für die GUI und unterstützt die Verarbeitung von PDF-Dateien.

## Features

- **Splash Screen**: Zeigt ein Logo beim Start der Anwendung.
- **GUI**: Eine benutzerfreundliche Oberfläche, die mit PyQt6 erstellt wurde.
- **PDF-Verarbeitung**: (Geplant oder implementiert) Konvertiert PDF-Inhalte in Audio.

## Voraussetzungen

Zusätzlich zu den genannten Abhängigkeiten wird ein Google-Konto benötigt, um die entsprechenden Google-Dienste zu nutzen. Die Authentifizierung und Einrichtung erfolgt über die Google CLI. Stelle sicher, dass du Folgendes erledigst:

1. **Google-Konto erstellen**:
   - Besuche [https://accounts.google.com/](https://accounts.google.com/) und erstelle ein Konto, falls du noch keines hast.

2. **Google Cloud CLI installieren**:
   - Lade die Google Cloud CLI herunter und installiere sie, falls sie noch nicht installiert ist. Folge der Anleitung hier: [Google Cloud CLI installieren](https://cloud.google.com/sdk/docs/install).

3. **Google CLI einrichten**:
   - Melde dich mit deinem Google-Konto an:
     ```bash
     gcloud auth login
     ```
   - Initialisiere die Google CLI, um ein Projekt auszuwählen oder zu erstellen:
     ```bash
     gcloud init
     ```
     Während dieses Prozesses wirst du aufgefordert:
     - Ein Google Cloud-Projekt auszuwählen oder ein neues zu erstellen.
     - Die Standardregion für dein Projekt festzulegen.

4. **Google Cloud API aktivieren**:
   - Aktiviere die benötigte API (z. B. Google Text-to-Speech API) für dein Projekt:
     ```bash
     gcloud services enable texttospeech.googleapis.com
     ```

5. **API-Berechtigungen überprüfen**:
   - Stelle sicher, dass die aktivierte API mit deinem Projekt verknüpft ist:
     ```bash
     gcloud services list
     ```

## Verwendung

1. Stelle sicher, dass du über die Google CLI angemeldet bist und dein Projekt installiert ist:
   ```bash
   gcloud auth login
   gcloud init
   
2. Starte die Anwendung:
    ```bash
    python main.py

3. Die Anwendung zeigt zunächst einen Splash Screen und öffnet dann das Hauptfenster.


## Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/NiklasDu/PDF-to-Audio.git
   cd PDF-to-Audio/pdf-to-audio

2. **Virtuelle Umgebung erstellen (optional, empfohlen)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Für Mac/Linux

3. **Abhängigkeiten installieren**:
    ```bash
    pip install -r requirements.txt

3. **Assets sicherstellen**: 
    Stelle sicher, dass die Datei assets/logo.png im Ordner pdf-to-audio/assets/ vorhanden ist.


## Abhängigkeiten
Die Abhängigkeiten sind in der Datei requirements.txt definiert. Hier sind die wichtigsten:

- PyQt6: Für die GUI.
- PyMuPDF: Für die PDF-Verarbeitung.

