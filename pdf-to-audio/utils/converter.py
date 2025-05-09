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
        def extract_text_from_pdf(pdf_path):
            text = ""
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text += page.get_text()

                return text
            
        def text_too_long(text):
            byte_length = len(text.encode("utf-8"))
            print(f"Textlänge in Bytes: {byte_length}")
            if byte_length > 5000:
                print("⚠️ Achtung: Text ist zu lang für die Google Text-to-Speech API (Limit: 5000 Bytes).")
                return True
            else:
                print("✅ Text ist innerhalb des erlaubten Bereichs.")
                return False

        pdf_text = extract_text_from_pdf(str(self.chosen_file))

        if text_too_long(pdf_text):
            self.view.finished_converting.setText("Die Datei ist zu groß. Bitte wähle eine Datei unter 5000 Zeichen.")
        else:
            self.view.finished_converting.setText("Die Umwandlung kann ein paar Sekunde dauern.")
            client = texttospeech.TextToSpeechClient()

            synthesis_input = texttospeech.SynthesisInput(text=pdf_text)
            voice = texttospeech.VoiceSelectionParams(
                language_code="de-DE", 
                name="de-DE-Wavenet-F",
                ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )

            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            self.new_mp3 = response.audio_content
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
