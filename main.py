from ui import Ui_MainWindow, StartupLicenseDialog, REQ_NAME, REQ_OWNER_ID
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtGui import QFontDatabase
from asset_finder import get_path
import sys, http.client

sessionid = ""

class Dashboard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pulse Extreme")
    
    def show(self):
        dialog = StartupLicenseDialog()
        if dialog.verify_saved_license() or dialog.exec() == QDialog.Accepted:
            super().show()
        else: # QDialog.Rejected, or window was closed
            print("Valid license missing")
            sys.exit(0)
        global sessionid
        sessionid = dialog.sessionid
      

if __name__ == '__main__':
    try:
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
    except:
        print("Program exiting due to exception")
    finally:
        # Logout of keyauth
        if sessionid:
            print("logging out...")
            conn = http.client.HTTPSConnection("keyauth.win")

            conn.request("GET", f'/api/1.3/?type=logout&sessionid={sessionid}&name={REQ_NAME}&ownerid={REQ_OWNER_ID}')
            # Testing
            #res = conn.getresponse()
            #data = res.read()
            #print(data.decode())

