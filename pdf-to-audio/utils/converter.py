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

    def choose_file(self):
        file_dialog = QFileDialog(self.view)
        file_dialog.setWindowTitle("PDF auswählen")
        file_dialog.setDirectory(QDir.homePath())
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.view.chosen_file = selected_files[0]
            filename = os.path.basename(self.view.chosen_file)
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

        pdf_text = extract_text_from_pdf(str(self.view.chosen_file))

        if text_too_long(pdf_text):
            self.view.finished_converting.setText("Die Datei ist zu groß. Bitte wähle eine Datei unter 5000 Zeichen.")
        else:
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

            with open("output.mp3", "wb") as out:
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')
            self.view.finished_converting.setText("Umwandlung war erfolgreich.")

    def save_file(self):
        pass