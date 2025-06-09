from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal, QThread, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, 
    QPalette, QPixmap, QRadialGradient, QTransform, QCloseEvent)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy, QProgressBar, QMessageBox,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget, QLayout, QGridLayout, QCheckBox, QDialog, QDialogButtonBox, QFrame)
from threading import Timer
from asset_finder import get_path, get_batch_path
import subprocess, json, os, sys, platform, http.client
import datetime, humanize, pyperclip
import constants

REQ_NAME = "Pulse%20Extreme"
REQ_VER = "1.0"
REQ_OWNER_ID = "5yiNVzEtid"

file_dir = os.path.expandvars(r'%LOCALAPPDATA%\PulseExtreme')
file_name = r'\save_state.json'

def get_save_data() -> dict:
    if os.path.exists(file_dir + file_name):
        with open(file_dir + file_name, "r") as f:
            content = f.read()
            if content: # File not empty
                data = json.loads(content)
                if isinstance(data, dict):
                    return data
    return {}

def dump_save_data(data) -> None:
    if not os.path.exists(file_dir):
        os.make_dirs(file_dir)
    
    with open(file_dir + file_name, "w") as f:
        json.dump(data, f)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow) -> None:
        # ================
        # Qt Designer Dump
        # ================
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 515)
        MainWindow.setWindowIcon(QIcon(get_path("icon_logo")))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebarLayout = QVBoxLayout()
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        
        self.logoLayout = QHBoxLayout()
        self.logoLayout.setObjectName(u"logoLayout")
        self.label_2 = QLabel(self.sidebar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(get_path("corner_logo")))
        self.label_2.setScaledContents(True)

        self.logoLayout.addWidget(self.label_2)

        self.titleLabel = QLabel(self.sidebar)
        self.titleLabel.setObjectName(u"titleLabel")

        self.logoLayout.addWidget(self.titleLabel)


        self.sidebarLayout.addLayout(self.logoLayout)

        self.categories = QVBoxLayout()
        self.categories.setSpacing(2)
        self.categories.setObjectName(u"categories")
        self.categories.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.sidebarLayout.addLayout(self.categories)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.sidebarLayout.addItem(self.verticalSpacer)

        self.LicenseBtn = QPushButton(self.sidebar)
        self.LicenseBtn.clicked.connect(self._on_license_clicked)
        self.LicenseBtn.setObjectName(u"LicenseBtn")

        self.sidebarLayout.addWidget(self.LicenseBtn)

        self.verticalLayout_2.addLayout(self.sidebarLayout)


        self.horizontalLayout.addWidget(self.sidebar)

        self.content = QWidget(self.centralwidget)
        self.content.setObjectName(u"content")
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topbar = QWidget(self.content)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setMinimumSize(QSize(0, 50))
        self.topbar.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.topbar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.restore_btn = RoundedButton(self.topbar)
        self.restore_btn.clicked.connect(self._on_create_restore_clicked)
        self.restore_btn.setObjectName(u"restore_btn")
        #self.searchbar = QHBoxLayout()
        #self.searchbar.setObjectName(u"searchbar")
        #self.searchIcon = QLabel(self.topbar)
        #self.searchIcon.setObjectName(u"searchIcon")
        #self.searchIcon.setMinimumSize(QSize(30, 30))
        #self.searchIcon.setMaximumSize(QSize(30, 30))
        #self.searchIcon.setPixmap(QPixmap(u"icons/search.png"))
        #self.searchIcon.setScaledContents(True)

        #self.searchbar.addWidget(self.searchIcon)

        #self.searchBox = QLineEdit(self.topbar)
        #self.searchBox.setObjectName(u"searchBox")
        #self.searchBox.setMinimumSize(QSize(200, 0))

        #self.searchbar.addWidget(self.searchBox)


        self.horizontalLayout_3.addWidget(self.restore_btn)

        self.horizontalSpacer = QSpacerItem(280, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.selectAllBtn = RoundedButton(self.topbar)
        self.selectAllBtn.clicked.connect(self._on_select_all_clicked)
        self.selectAllBtn.setObjectName(u"selectAllBtn")

        self.horizontalLayout_3.addWidget(self.selectAllBtn)


        self.verticalLayout_3.addWidget(self.topbar)

        self.mainarea = QStackedWidget(self.content)
        self.mainarea.setObjectName(u"mainarea")

        self.verticalLayout_3.addWidget(self.mainarea)

        self.footer = QWidget(self.content)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 100))
        self.footer.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.checkout = QScrollArea(self.footer)
        self.checkout.setObjectName(u"checkout")
        self.checkout.setMinimumSize(QSize(300, 0))
        self.checkout.setMaximumSize(QSize(300, 16777215))
        self.checkout.setWidgetResizable(True)
        self.checkout.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.checkout.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.checkout_items = {}

        self.checkoutWidget = QWidget()
        self.checkoutWidget.setObjectName(u"checkoutWidget")
        self.checkoutWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.checkoutLayout = QVBoxLayout()
        
        self.checkoutWidget.setLayout(self.checkoutLayout)
        
        self.checkout.setWidget(self.checkoutWidget)

        self.horizontalLayout_4.addWidget(self.checkout)

        self.horizontalSpacer_2 = QSpacerItem(403, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.applyButton = RoundedButton(self.footer)
        self.applyButton.clicked.connect(self._on_apply_clicked)
        self.applyButton.setObjectName(u"applyButton")

        self.horizontalLayout_4.addWidget(self.applyButton)


        self.verticalLayout_3.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.content)

        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # =====================
        # Setup sidebar buttons
        # =====================
        self.category_buttons = []
        for title in constants.CATEGORIES:
            catButton = CategoryButton(title)
            self.categories.addWidget(catButton)
            self.category_buttons.append(catButton)
            catButton.categoryChosen.connect(self._on_category_chosen)
        
        # ==============================
        # Create pages for each category
        # ==============================
        self.category_pages = {}
        i = 0
        for category, page in constants.TWEAKS.items():
            option_categories = {"none": []} # String: Array(OptionToggle)
            # Place options into page categories
            for option, attributes in page.items():
                # Make toggle
                toggle = OptionToggle(option, category)
                toggle.tweakToggled.connect(self._on_tweak_toggle)
                # Add to page category
                if "category" in attributes:
                    if attributes["category"] in option_categories:
                        option_categories[attributes["category"]].append(toggle)
                    else:
                        option_categories[attributes["category"]] = [toggle]
                else:
                    option_categories["none"].append(toggle)
            
            content_widgets = {}
            # Create grid layouts and add options
            for page_category in option_categories.keys():
                # Create grid layout
                layout = QGridLayout()
                layout.setSpacing(10)
                # Add options to grid layout
                x = 0
                y = 0
                for toggle in option_categories[page_category]:
                    layout.addWidget(toggle, y, x)
                    layout.setRowStretch(i, 0)
                    x += 1
                    if x > 2:
                        y+= 1
                        x = 0
                # Create grid widget
                content_widgets[page_category] = QWidget()
                content_widgets[page_category].setLayout(layout)
                content_widgets[page_category].setObjectName(category)

            # Create spacing widget
            spacing = QWidget()
            spacing.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # Create VBox to add grids & labels into
            full_widget = QWidget()
            full_widget.setLayout(QVBoxLayout())
            full_widget.setObjectName(category)
            # Add to VBox
            for page_category, content_widget in content_widgets.items():
                if page_category != "none":
                    full_widget.layout().addWidget(QLabel(page_category))
                full_widget.layout().addWidget(content_widget)
            full_widget.layout().addWidget(spacing)
            # Add to stacked widget
            self.mainarea.addWidget(full_widget)
            self.category_pages[i] = full_widget
            i += 1
        # Default to first 
        self.mainarea.setCurrentIndex(0)
        self.category_buttons[0].setChecked(True)
        # Load tweaks
        self._load_tweaks()
    # setupUi

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Pulse Extreme", None))
        self.LicenseBtn.setText(QCoreApplication.translate("MainWindow", u"License", None))
        #self.searchIcon.setText("")
        self.selectAllBtn.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.restore_btn.setText(QCoreApplication.translate("restore_btn", u"Create Restore Point", None))
    

    def _load_tweaks(self) -> None:
        data = get_save_data()
        if not data:
            return
        # Update toggles
        if ("applied" in data) and (isinstance(data["applied"], list) and (len(data["applied"]) > 0)):
            for item in self._get_option_toggles(False, data["applied"]):
                item.set_applied()
                # Remove from checkout & unselect
                self._delete_checkout_item(item.text())
            
    # Gets all OptionToggles with matching names (or all OptionToggles if no names are given)
    def _get_option_toggles(self, current_page = True, names = []) -> list[QCheckBox]:
        output = []
        # Get current page layout (or all page layouts)
        if current_page:
            layouts = [self.category_pages[self.mainarea.currentIndex()].layout()]
        else:
            layouts = [page.layout() for page in self.category_pages.values()]
        # Get all QGridLayouts in page
        for layout in layouts:
            for i in range(layout.count()):
                grid = layout.itemAt(i).widget().layout()
                if isinstance(grid, QGridLayout):
                    # Get all OptionToggles in grid
                    for j in range(grid.count()):
                        item = grid.itemAt(j).widget()
                        if (isinstance(item, OptionToggle)) and (not names or item.text() in names):
                            output.append(item)
        return output

    # Delete a QLabel from checkout panel given str name
    def _delete_checkout_item(self, item_name) -> None:
        for i in range(self.checkoutLayout.count()):
            label = self.checkoutLayout.itemAt(i)
            if label != None and isinstance(label.widget(), QLabel):
                label = label.widget()
                if label.name == item_name:
                    self.checkoutLayout.removeWidget(label)
                    label.deleteLater()
                    self.checkout_items.pop(item_name)

    # Signal
    def _on_select_all_clicked(self) -> None:
        for item in self._get_option_toggles():
            item.set_checked(True)

    # Signal
    def _on_category_chosen(self, title) -> None:
        # Uncheck other sidebar buttons
        for child in self.category_buttons:
            if child.text() != title:
                child.setChecked(False)
        # Change page
        for index, page in self.category_pages.items():
            if page.objectName() == title:
                self.mainarea.setCurrentIndex(index)
    
    # Signal
    def _on_create_restore_clicked(self) -> None:
        filepath = get_batch_path(constants.RESTORE_POINT)
        p = subprocess.Popen(filepath, shell=True)

    # Signal
    def _on_tweak_toggle(self, checked, applied, name, category) -> None:
        if checked:
            self.checkoutLayout.addWidget(CheckoutLabel(name, applied), alignment=Qt.AlignTop)
            self.checkout_items[name] = category
        else:
            self._delete_checkout_item(name)
    
    # Signal
    def _on_apply_clicked(self) -> None:
        # run process
        if self.checkout_items:
            # Start dialog
            dialog = ApplyDialog(self.checkout_items)
            dialog.exec()
            # Dialog over
            self._load_tweaks()
    
    # Signal
    def _on_license_clicked(self) -> None:
        dialog = LicenseCheckDialog()
        #dialog.setParent(self)
        dialog.exec()
        
# Popup that opens when applying tweaks
class ApplyDialog(QDialog):
    reportStart = Signal()
    
    def __init__(self, items):
        super().__init__()
        self.setObjectName("ApplyWindow")
        self.setWindowTitle("Applying Tweaks...")
        self.setWindowIcon(QIcon(get_path("icon_logo")))
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        #self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedWidth(300)
        border_rad = 0
        if platform.release() == "11":
            border_rad = 6 # Adjust for rounded corners on windows 11
        style_str = """
            * {
                color: white;
            }
            QDialog {
                background-color: #222;
                border: 2px solid white; 
                border-width: 0px 1px 1px 1px;
                border-bottom-left-radius: %dpx;
                border-bottom-right-radius: %dpx;
            }
            QProgressBar {
                background-color: #fff;
                border: 2px solid gray;
                min-height: 20px;
                max-height: 20px;
            }
            QProgressBar::chunk {
                background-color: #dc6acf;
                width: 10px;
                margin: 0px;     
            }
        """ % (border_rad, border_rad)
        self.setStyleSheet(style_str)

        self.num_tweaks = 0
        self.applied_tweaks = []
        self.errorReport = []
        self.items = items
        self.thread_working = True
        self.saved = False # avoid saving multiple times
        self.reportStart.connect(self._show_report)
        # Create layout & widgets
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(15, 15, 10, 15)

        self.topMessage = QLabel("Applying (0/" + str(len(items)) + ")")
        self.topMessage.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        topFont = QFont("Roboto-Medium", 12)
        topFont.setBold(True)
        self.topMessage.setFont(topFont)

        self.progressLabel = QLabel()
        self.progressLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, len(items))
        self.progressBar.setTextVisible(False)
        self.progressBar.setMinimumHeight(20)

        self.barTopSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.barBottomSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.dialogBtn = (QDialogButtonBox.Cancel)
        self.buttonBox = QDialogButtonBox(self.dialogBtn)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setStyleSheet("background: gray;")
        self.buttonBox.clicked.connect(self._save_and_close)
        # Add widgets to layout
        self.mainLayout.addWidget(self.topMessage)
        self.mainLayout.addWidget(self.progressLabel)
        self.mainLayout.addItem(self.barTopSpacer)
        self.mainLayout.addWidget(self.progressBar)
        self.mainLayout.addItem(self.barBottomSpacer)
        self.mainLayout.addWidget(self.buttonBox)
        self.setLayout(self.mainLayout)
        
        
        # Create worker thread
        self.work_thread = QThread()
        self.worker = ApplyWorker(items)
        self.worker.moveToThread(self.work_thread)
        # Connect signals
        self.work_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.work_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self._on_finished)
        self.work_thread.finished.connect(self.work_thread.deleteLater)
        self.worker.tweakStart.connect(self._on_tweak_started)
        self.worker.tweakDone.connect(self._on_tweak_finished)
        # start thread
        self.work_thread.start()
    

    def _is_tweak_repeatable(self, tweak_name) -> bool:
        for category in constants.TWEAKS:
            if tweak_name in constants.TWEAKS[category]:
                if "repeatable" in constants.TWEAKS[category][tweak_name]:
                    return True
                else:
                    return False
        return False

    # call _show_report through signal to stay on main thread
    def _start_report(self) -> None:
        self.reportStart.emit()
        

    def _show_report(self) -> None:
        # Get number of errors
        numErrors = 0
        errorLabels = []
        errorLayout = QVBoxLayout()
        for name in self.errorReport:
            errorLabels.append(QLabel("• " + name))
            numErrors += 1
        for label in errorLabels:
            errorLayout.addWidget(label)
        self.mainLayout.insertLayout(2, errorLayout)
        # Clean old layout
        self.progressBar.hide()
        self.topMessage.setText("Tweaks Applied!")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Close") # "Cancel" to "Close"
        # Create new layout
        if numErrors == 0:
            self.progressLabel.setText("Success!")
        elif numErrors == 1:
            self.progressLabel.setText("An error occured applying tweak:")
        else:
            self.progressLabel.setText("Errors occured applying tweaks:")

    # Signal
    def _on_tweak_started(self, tweak_name) -> None:
        self.progressLabel.setText(tweak_name)

    # Worker signal (when tweak succeeds / fails)
    def _on_tweak_finished(self, success, tweak_name) -> None:
        # Report tweak fail / success
        if success:
            self.applied_tweaks.append(tweak_name)
        else:
            self.errorReport.append(tweak_name)
        # Update progress
        self.num_tweaks += 1
        self.topMessage.setText("Applying (" + str(self.num_tweaks) + "/" + str(len(self.items)) + ")")
        self.progressBar.setValue(self.num_tweaks)
        
    # Worker signal
    def _on_finished(self) -> None:
        self.thread_working = False
        self.progressLabel.setText("Finished!")
        # Show report after short wait
        wait_timer = Timer(0.7, self._start_report) 
        wait_timer.start()


    def closeEvent(self, event: QCloseEvent) -> None:
        self._save_and_close()

    # Save updates & close dialog
    def _save_and_close(self) -> None:
        if self.saved:
            return
        if self.thread_working:
            self.topMessage.setText("Stopping process...")
            self.progressLabel.setText("(Program will temporarily freeze)")
            self.progressBar.hide()
            QApplication.processEvents()
            self.work_thread.quit()
            self.work_thread.wait()
            self.thread_working = False
        # Create directory
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # Create save data
        save_data = {"applied": self.applied_tweaks}

        # Add existing data to new save data
        old_data = get_save_data()
        if ("applied" in old_data) and (isinstance(old_data["applied"], list)) and (len(old_data["applied"]) > 0):
            for tweak_name in old_data["applied"]:
                if tweak_name not in save_data["applied"]:
                    save_data["applied"].append(tweak_name)
        if "license" in old_data:
            save_data["license"] = old_data["license"]

        # Save to file
        dump_save_data(save_data)
        self.saved = True
        self.close()

# Works in a seperate thread & updates progress to ApplyDialog
class ApplyWorker(QObject): 
    finished = Signal()
    tweakStart = Signal(str) # name
    tweakDone = Signal(bool, str) # success, name

    def __init__(self, items):
        super().__init__()
        self.items = items


    def run(self) -> None:
        for name, category in self.items.items():
            # Report progress
            self.tweakStart.emit(name)
            # Open file
            tweak = constants.TWEAKS[category][name]
            filepath = get_batch_path(tweak['batch'])
            print(filepath)
            if filepath.endswith("reg"):
                # Registry edit
                print("applying .reg file")
                p = subprocess.Popen(['regedit.exe', '/s', filepath], shell=True, stdout = subprocess.PIPE)
            else:
                print("applying .bat file")
                # Batch file
                p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
            # Return result
            stdout, stderr = p.communicate()
            if p.returncode == 0:
                self.tweakDone.emit(True, name)
            else:
                print(p.returncode)
                self.tweakDone.emit(False, name)

        self.finished.emit()

# Popup that opens on startup
class StartupLicenseDialog(QDialog):
    sessionid = "" # KeyAuth session
    license = ""
    expiry = ""

    def __init__(self):
        super().__init__()
        self.setObjectName("LicenseWindow")
        self.setWindowTitle("License")
        self.setWindowIcon(QIcon(get_path("license_key")))
        
        # Create layout & widgets
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(10, 10, 10, 10)

        self.topMessage = QLabel("Enter your license key to continue. A license key can be purchased at (link)")
        self.topMessage.setWordWrap(True)
        #self.topMessage.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        topMessageFont = QFont("Roboto-Light", 10)
        self.topMessage.setFont(topMessageFont)

        self.topSpacer = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.licenseLabel = QLabel("License Key:")
        self.licenseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        licenseLabelFont = QFont("Roboto-Medium", 12)
        licenseLabelFont.setBold(True)
        self.licenseLabel.setFont(licenseLabelFont)
        
        self.licenseBox = QLineEdit()
        self.licenseBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.licenseBox.setMaximumWidth(250)
        self.licenseBox.setPlaceholderText("XXXXX-XXXXX-XXXXX")
        licenseBoxLayout = QHBoxLayout() # Layout for centering licenseBox
        licenseBoxLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        licenseBoxLayout.addWidget(self.licenseBox)

        self.bottomSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.lineBreak = QFrame()
        self.lineBreak.setFrameShape(QFrame.Shape.HLine)
        self.lineBreak.setFrameShadow(QFrame.Shadow.Sunken)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Apply)

        nextButton = self.buttonBox.button(QDialogButtonBox.Apply)
        nextButton.clicked.connect(self._on_next_pressed)
        nextButton.setText("Next")

        cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)
        cancelButton.clicked.connect(self._on_cancel_pressed)

        # Make next button default
        cancelButton.setDefault(False)
        cancelButton.setAutoDefault(False)
        nextButton.setDefault(True)
        nextButton.setAutoDefault(True)
        
        # Add widgets to layout
        self.mainLayout.addWidget(self.topMessage)
        self.mainLayout.addItem(self.topSpacer)
        self.mainLayout.addWidget(self.licenseLabel)
        self.mainLayout.addLayout(licenseBoxLayout)
        self.mainLayout.addItem(self.bottomSpacer)
        self.mainLayout.addWidget(self.lineBreak)
        self.mainLayout.addWidget(self.buttonBox)
        self.setLayout(self.mainLayout)

        # Set window size
        self.adjustSize()
        size_hint = self.sizeHint()
        self.setFixedSize(350, size_hint.height())
    

    def _on_next_pressed(self, button) -> None:
        if self.verify_license(self.licenseBox.text()):
            # Add license to existing data (if there's a file already)
            data = get_save_data()
            data["license"] = self.licenseBox.text()
            # Save to file
            dump_save_data(data)
            # Continue to main program
            self.accept()
        else:
            QMessageBox.warning(self, "License Verification Failed", "The provided key could not be validated. Please try again.")
    
    # Used in main.py to skip this dialog on init
    def verify_saved_license(self) -> bool:
        save_data = get_save_data()
        if "license" in save_data:
            saved_license = save_data["license"]
        else:
            saved_license = ""
        
        if saved_license and self.verify_license(saved_license):
            return True
        return False

    # Check license with KeyAuth, Sets static variables
    def verify_license(self, license) -> bool:
        # Initialize with GET request
        conn = http.client.HTTPSConnection("keyauth.win")
        conn.request("GET", f'/api/1.3/?type=init&ver={REQ_VER}&name={REQ_NAME}&ownerid={REQ_OWNER_ID}', '', {})
        res = conn.getresponse()
        data = res.read()
        init_res = json.loads(data.decode())
        if 'success' in init_res and init_res["success"] == True:
            # Login with key
            print(f'Attempting to login (key: {license})')
            self.sessionid = init_res['sessionid']
            conn.request("GET", f'/api/1.3/?type=license&key=KEYAUTH-{license}&sessionid={self.sessionid}&name={REQ_NAME}&ownerid={REQ_OWNER_ID}', '', {})
            res = conn.getresponse()
            data = res.read()
            login_res = json.loads(data.decode())
            print(login_res)
            if 'success' in login_res and login_res["success"] == True:
                # Set static variables
                StartupLicenseDialog.license = license
                if "subscriptions" in login_res["info"] and len(login_res["info"]["subscriptions"]) > 0:
                    expiry = login_res["info"]["subscriptions"][0]["expiry"]
                    if int(expiry) < 100_000_000: # Account for lifetime licenses
                        StartupLicenseDialog.expiry = expiry
                # Return
                conn.close()
                return True
            else:
                if 'message' in login_res:
                    # TODO: Use message in error popup
                    print(login_res['message'])
                print("Failed to login")
        else:
            # Initialization failed
            print("failed to initialize")
        conn.close()
        return False
    

    def _on_cancel_pressed(self) -> None:
        self.reject()

# Popup that opens from "License" button in main program
class LicenseCheckDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("LicenseCheckWindow")
        self.setWindowTitle("License")
        self.setWindowIcon(QIcon(get_path("license_key")))
        
        # Create layout & widgets
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(10, 10, 10, 10)

        self.topSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.licenseLabel = QLabel() 
        self.licenseLabel.setText("Your license:\n" + StartupLicenseDialog.license)
        self.licenseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        licenseLabelFont = QFont("Roboto-Medium", 12)
        licenseLabelFont.setBold(True)
        self.licenseLabel.setFont(licenseLabelFont)
        
        self.expireLabel = QLabel()
        self.expireLabel.setText(self.format_expiry_time())
        self.expireLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.bottomSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.lineBreak = QFrame()
        self.lineBreak.setFrameShape(QFrame.Shape.HLine)
        self.lineBreak.setFrameShadow(QFrame.Shadow.Sunken)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Open | QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)

        logOutButton = self.buttonBox.button(QDialogButtonBox.Ok)
        logOutButton.setText("Sign out")
        logOutButton.clicked.connect(self._on_logout_pressed)

        copyButton = self.buttonBox.button(QDialogButtonBox.Open)
        copyButton.setText("Copy To Clipboard")
        copyButton.clicked.connect(self._on_copy_pressed)

        continueButton = self.buttonBox.button(QDialogButtonBox.Cancel)
        continueButton.setText("Continue")
        continueButton.clicked.connect(self._on_continue_pressed)

        # Add widgets to layout
        self.mainLayout.addItem(self.topSpacer)
        self.mainLayout.addWidget(self.licenseLabel)
        self.mainLayout.addWidget(self.expireLabel)
        self.mainLayout.addItem(self.bottomSpacer)
        self.mainLayout.addWidget(self.lineBreak)
        self.mainLayout.addWidget(self.buttonBox)
        self.setLayout(self.mainLayout)

        # Set window size
        self.adjustSize()
        size_hint = self.sizeHint()
        self.setFixedSize(400, size_hint.height())

 
    def _on_logout_pressed(self) -> None:
        # Remove saved license
        save_data = get_save_data()
        if "license" in save_data:
            del save_data["license"]
            dump_save_data(save_data)
        # Close program
        # TODO: Make program reset to license key window
        sys.exit()
    

    def _on_copy_pressed(self) -> None:
        pyperclip.copy(StartupLicenseDialog.license)


    def _on_continue_pressed(self) -> None:
        self.close()


    def format_expiry_time(self) -> str:
        if StartupLicenseDialog.expiry:
            # Temporary license
            expiry = datetime.datetime.fromtimestamp(int(StartupLicenseDialog.expiry))
            now = datetime.datetime.now()
            relative_time = humanize.naturaltime(now - expiry)
            date = expiry.strftime(r"%Y/%m/%d")
            return f'Expires {relative_time} ({date})'
        else:
            return "(Lifetime)"
        

class OptionToggle(QCheckBox):
    tweakToggled = Signal(bool, bool, str, str) # pressed, already applied, name, category
    applied = False

    def __init__(self, text, category):
        super().__init__(text)
        self.category = category
        self.clicked.connect(self._on_click)
        self.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url("{get_path("toggle_on")}");
            }}
            QCheckBox::indicator:unchecked {{
                image: url("{get_path("toggle_off")}");
            }}
        """)
    

    def set_checked(self, check = True) -> None:
        if check and not self.isChecked():
            self.setChecked(True)
            self._on_click(True)
        elif not check and self.isChecked():
            self.setChecked(False)
            self._on_click(False)
    
    
    def set_applied(self) -> None:
        self.setChecked(False)
        self.applied = True
        # Darken toggle & text
        self.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url('{get_path("toggle_on_disabled")}');
            }}
            QCheckBox::indicator:unchecked {{
                image: url('{get_path("toggle_off_disabled")}');
            }}
            QCheckBox {{
                color: #a3a3a3;
            }}
        """)
    

    def _on_click(self, pressed) -> None:
        self.tweakToggled.emit(pressed, self.applied, self.text(), self.category)


class CheckoutLabel(QLabel):
    def __init__(self, text, applied):
        super().__init__(text)
        self.name = text
        if applied:
            self.setText("+  " + self.name + " (already applied)")
        else:
            self.setText("+  " + self.name)
        self.setStyleSheet("color: black;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWordWrap(True)

# Sidebar button
class CategoryButton(QPushButton):
    categoryChosen = Signal(str)

    def __init__(self, title):
        super().__init__(title)
        self.setIcon(QIcon(get_path(title)))
        self.setIconSize(QSize(21, 21))
        self.setCheckable(True)
        self.clicked.connect(self._on_click)
    
    def _on_click(self, pressed) -> None:
        if pressed:
            self.categoryChosen.emit(self.text())
        else:
            self.setChecked(True)


class RoundedButton(QPushButton):
    def resizeEvent(self, event):
        super().resizeEvent(event)
        radius = min(self.width(), self.height()) // 2
        self.setStyleSheet(f"border-radius: {radius}px;")