# ------------------------ Imports ------------------------- #

from google.cloud import texttospeech
import fitz
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QDir
import os

# ------------------------ Class ------------------------- #

class Converter:
    def __init__(self, view):
        self.view = view
        self.chosen_file = ""
        self.new_mp3 = ""

    def choose_file(self):
        file_dialog = QFileDialog(self.view)
        file_dialog.setWindowTitle("PDF auswählen")
        file_dialog.setDirectory(QDir.homePath())
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.chosen_file = selected_files[0]
            filename = os.path.basename(self.chosen_file)
            self.view.file_name.setText(str(filename))

    def convert_pdf_to_audio(self):
        self.view.finished_converting.setText("Die Umwandlung kann ein paar Sekunde dauern.")
        def extract_text_from_pdf(pdf_path):
            text = ""
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text += page.get_text()

                return text
            
        # Text in einzelne Chunks aufteilen, um das Limit von 5000 Bytes pro Anfrage zu umgehen
        def split_text(text, max_bytes=4500):
            chunks = []
            current_chunk = ""

            for paragraph in text.split("\n"):
                paragraph = paragraph.strip()
                if not paragraph:
                    continue

                if len((current_chunk + paragraph).encode("utf-8")) > max_bytes:
                    chunks.append(current_chunk)
                    current_chunk = paragraph + "\n"
                else:
                    current_chunk += paragraph + "\n"

            if current_chunk:
                chunks.append(current_chunk)

            return chunks
            
        pdf_text = extract_text_from_pdf(str(self.chosen_file))
        client = texttospeech.TextToSpeechClient()

        voice = texttospeech.VoiceSelectionParams(
                language_code="de-DE", 
                name="de-DE-Wavenet-F",
                ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
            )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        all_audio = b""  # leere Bytefolge
        for chunk in split_text(pdf_text):  # jeder Textabschnitt unter 5000 Bytes
            synthesis_input = texttospeech.SynthesisInput(text=chunk)
            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            all_audio += response.audio_content  # hänge alle Audio-Bytes zusammen

        self.new_mp3 = all_audio
        self.view.finished_converting.setText("Umwandlung war erfolgreich.")

    def save_file(self):
        file_dialog = QFileDialog(self.view)
        file_dialog.setWindowTitle("Verzeichnis auswählen")
        file_dialog.setDirectory(QDir.homePath())
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        file_path, _ = file_dialog.getSaveFileName(self.view, "MP3 speichern unter", QDir.homePath(),
                                                "MP3 Datein (*.mp3)")
        
        if file_path:
            if not file_path.endswith(('.mp3')):
                file_path += '.mp3'
            try:
                with open(file_path, "wb") as audio_file:
                    audio_file.write(self.new_mp3)
                    print(f"Audio content written ti file {file_path}")
                self.view.finished_converting.setText("Die Datei wurde erfolgreich gespeichert.")
            except Exception as e:
                self.view.finished_converting.setText(f"Fehler beim Speichern der Datei: {str(e)}")
