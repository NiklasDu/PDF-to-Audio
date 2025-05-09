# ------------------------ Imports ------------------------- #
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, QPushButton
from constants import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QMediaPlayer
from utils.converter import Converter

# ------------------------ Class ------------------------- #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDFonix")
        self.ui_setup()

    def ui_setup(self):
        self.converter = Converter(self)

        self.logo_label = QLabel(self)
        pixmap_logo = QPixmap("pdf-to-audio/assets/logo.png")
        scaled_logo = pixmap_logo.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo_label.setPixmap(scaled_logo)
        self.logo_label.setFixedHeight(100)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.title_text = QLabel("Verwandel deine PDF zu einer Audio Datei.")
        self.title_text.setObjectName("title_text")
        self.title_text.setFixedHeight(50)
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.add_pdf_btn = QPushButton("PDF auswählen")
        self.add_pdf_btn.setFixedHeight(42)
        self.add_pdf_btn.setFixedWidth(200)
        self.add_pdf_btn.clicked.connect(self.converter.choose_file)

        self.file_name = QLabel("Noch keine Datei ausgewählt.")
        self.file_name.setObjectName("file_name")
        self.file_name.setFixedHeight(50)
        self.file_name.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.convert_pdf_btn = QPushButton("Umwandeln zu MP3")
        self.convert_pdf_btn.setFixedHeight(42)
        self.convert_pdf_btn.setFixedWidth(200)
        self.convert_pdf_btn.clicked.connect(self.converter.convert_pdf_to_audio)

        # Zu Media Player umwandeln später
        self.finished_converting = QLabel("-")
        self.finished_converting.setObjectName("finished_converting")
        self.finished_converting.setFixedHeight(50)
        self.finished_converting.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.save_mp3_btn = QPushButton("MP3 speichern")
        self.save_mp3_btn.setFixedHeight(42)
        self.save_mp3_btn.setFixedWidth(200)
        self.save_mp3_btn.clicked.connect(self.converter.save_file)        

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.addWidget(self.title_text)
        layout.addWidget(self.add_pdf_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.file_name)
        layout.addWidget(self.convert_pdf_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.finished_converting)
        layout.addWidget(self.save_mp3_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        container = QWidget()
        container.setLayout(layout)

        self.setFixedSize(QSize(750, 600))

        self.setCentralWidget(container)

        # ----------------------- Styling ------------------------- #

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {BACKGROUND_COLOR};
                color: {TEXT_COLOR};
                font-family: "Helvetica Neue", "Arial", sans-serif;
                font-size: 15px;
            }}

            QPushButton {{
                background-color: {BUTTON_BACKGROUND};
                color: {BUTTON_TEXT_COLOR};
                border-radius: 10px;
                padding: 10px 20px;
                font-weight: bold;
                border: none;
            }}

            QPushButton:hover {{
                background-color: {HIGHLIGHT_COLOR};
            }}

            QPushButton:pressed {{
                background-color: {CLICKED_COLOR};
                padding-top: 11px;
                padding-bottom: 9px;
            }}

            QLabel#title_text {{
                font-size: 24px;
                font-weight: bold;
            }}

            QLabel#file_name, QLabel#finished_converting {{
                font-size: 16px;
            }}
        """)