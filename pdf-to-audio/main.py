# ------------------------ Imports ------------------------- #

from gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, Qt

# ------------------------ Splash Class ------------------------- #

class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

# ------------------------ Program Loop ------------------------- #

app = QApplication([])

pixmap = QPixmap("pdf-to-audio/assets/logo.png").scaled(
            400, 400, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
            )
splash = SplashScreen(pixmap)
splash.show()

QTimer.singleShot(2000, splash.close)


window = MainWindow()

QTimer.singleShot(2000, window.show)

app.exec()




