# PDF-to-Audio

Ein Python-Projekt, das eine grafische Benutzeroberfläche (GUI) bereitstellt, um PDF-Dateien in Audio umzuwandeln. Das Projekt verwendet **PyQt6** für die GUI und unterstützt die Verarbeitung von PDF-Dateien.

## Features

- **Splash Screen**: Zeigt ein Logo beim Start der Anwendung.
- **GUI**: Eine benutzerfreundliche Oberfläche, die mit PyQt6 erstellt wurde.
- **PDF-Verarbeitung**: (Geplant oder implementiert) Konvertiert PDF-Inhalte in Audio.

## Voraussetzungen

Stelle sicher, dass die folgenden Abhängigkeiten installiert sind:

- Python 3.9 oder höher
- PyQt6
- PyMuPDF (für die PDF-Verarbeitung)

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

## Verwendung
1. Starte die Anwendung:
    ```bash
    python main.py

2. Die Anwendung zeigt zunächst einen Splash Screen und öffnet dann das Hauptfenster.

## Abhängigkeiten
Die Abhängigkeiten sind in der Datei requirements.txt definiert. Hier sind die wichtigsten:

PyQt6: Für die GUI.
PyMuPDF: Für die PDF-Verarbeitung.

Installiere sie mit:
    ```bash
    pip install -r requirements.txt

