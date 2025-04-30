from ui import Ui_MainWindow, StartupLicenseDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtGui import QFontDatabase
from asset_finder import get_path
import sys


class Dashboard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pulse Extreme")
    
    def show(self):
        dialog = StartupLicenseDialog()
        if dialog.exec() == QDialog.Accepted:
            super().show()
        else: # QDialog.Rejected
            # TODO: close program
            print("Valid license missing")
            sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Dashboard()
    # Load stuff
    QFontDatabase.addApplicationFont(get_path("roboto_light"))
    QFontDatabase.addApplicationFont(get_path("roboto_medium"))

    with open(get_path("style"), "r") as file:
        style = file.read()
    app.setStyleSheet(style)
    # Run
    window.show()
    sys.exit(app.exec())