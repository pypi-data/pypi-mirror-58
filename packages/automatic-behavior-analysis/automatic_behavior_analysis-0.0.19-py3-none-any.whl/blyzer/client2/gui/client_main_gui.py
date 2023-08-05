import sys
import os
import appdirs
import json
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow
from PyQt5.QtWidgets import QMenuBar, QMenu, QFileDialog, QLabel, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSizePolicy, QGridLayout

# to import from this project without instalation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import base_plugin
from videowidget import VideoWidget
from client.config import ClientConfig
from Blyzer.common.settings import BlazesSettings
from Blyzer.client2.gui.about_widget import AboutWidget

DEFAULT_SETTING_FILE_NAME = "settings.json"
APP_NAME = "automatic-behavior-analysis-client"


class Client_GUI(QMainWindow):
    onOpenFile = pyqtSignal(str)
    onOpenFolder = pyqtSignal(str)

    def __init__(self, title, min_width, min_height, args):
        super().__init__()

        self.config = BlazesSettings()

        self._title = title  # type:String
        self._min_width = min_width
        self._min_height = min_height

        self.initUI()
        self.setAttribute(Qt.WA_DeleteOnClose, True)


    def initUI(self):
        """constructs the GUI  """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle(self._title)

        ### creating the menu ###
        self._menu_bar = self.menuBar()

        self._menu_file = self._menu_bar.addMenu("File")
        action = self._menu_file.addAction("Open file")
        action.triggered.connect(self.open_file_clicked)

        action = self._menu_file.addAction("Open folder")
        action.triggered.connect(self.open_folder_clicked)

        self._menu_file.addSeparator()

        action = self._menu_file.addAction("Exit")
        action.triggered.connect(self.exit_clicked)

        self._menu_plugin = self._menu_bar.addMenu("Processing")

        self._menu_help = self._menu_bar.addMenu("Help")
        self._menu_help.addSeparator()
        action = self._menu_help.addAction("About")
        action.triggered.connect(self.about_clicked)

        ### create status bar ###

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready')

        # Load plugin and components from it
        self._plugin = self.load_plugin()
        self.mediasrc = self._plugin.get_media_source_processor()
        self._rtStatisticWidget = self._plugin.get_rt_statistic_widget()
        self._summaryStatisticWidget = self._plugin.get_summary_statistic_widget()

        ws = self.config.getParam('window', {})
        q = QDesktopWidget().availableGeometry()  # Get screen size

        ### Основные виджеты ###
        self._main_widget = QWidget()
        self._main_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        ### creating video widget ###
        self._videoview = VideoWidget(media_source=self.mediasrc, parent=self)
        self._videoview.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        ### setting layout of the GUI window ###
        self._gridLayout = QGridLayout()
        self._gridLayout.setSpacing(5)

        ### adding widgets to the layout ###
        self._gridLayout.addWidget(self._videoview, 0, 0, -1, 10)
        self._gridLayout.addWidget(QLabel("Realtime statistic"), 0, 10, 1, 1)
        self._gridLayout.addWidget(self._rtStatisticWidget, 1, 10, 10, 3)
        self._gridLayout.addWidget(QLabel("Summary statistic"), 11, 10, 1, 1)
        self._gridLayout.addWidget(self._summaryStatisticWidget, 12, 10, 10, 3)

        self._main_widget.setLayout(self._gridLayout)
        self.setCentralWidget(self._main_widget)

        # Set main windows geometry
        width = ws.get('width') or max(q.width() // 2, self._min_width)
        height = ws.get('height') or max(q.height() // 2, self._min_height)
        x = ws.get('x') or (q.width() - width) // 2
        y = ws.get('y') or (q.height() - height) // 2
        self.setGeometry(x, y, width, height)

        # Show gui
        self.show()

    def load_plugin(self):
        """
        loads plugin features to the GUI.
        type of plugin decided according to config
        """
        plugin = None
        if self.config.getParam("media_source_type") == 'simpleCam':
            plugin = base_plugin.SimplePlugin(self.config)
        elif self.config.getParam("media_source_type") == 'nnCam':
            plugin = base_plugin.SimpleNNPreprocessPlugin(self.config)
        elif self.config.getParam("media_source_type") == 'nnVideo':
            from Blyzer.client2.dog_plugin import SleepDogPlugin
            plugin = SleepDogPlugin(self.config)
            plugin.set_status_bar(self.status_bar)
            plugin.set_menu(self._menu_plugin)

        self.onOpenFile.connect(plugin.onOpenFile)
        self.onOpenFolder.connect(plugin.onOpenFolder)
        return plugin

    @pyqtSlot()
    def open_folder_clicked(self):
        """
        Обработчик нажатия на открыть папку
        """
        folderName = QFileDialog.getExistingDirectory(
            self, "Select Folder", self.config.getParam('last_open_dir', "./"))
        self.open_folder(folderName)

    @pyqtSlot()
    def open_file_clicked(self):
        """
        Обработчик нажатия на открыть файл
        """
        fileName = QFileDialog.getOpenFileName(self, "Open Video",
                                               self.config.getParam(
                                                   'last_open_dir', "./"),
                                               "Video files (*.mp4) ;; All files (*.*)")[0]
        if len(fileName) > 0:
            self.config.setParam('last_open_dir', os.path.dirname(fileName), force=True)
            print("Opening file: {}".format(fileName))
            self.open_file(fileName)

    @pyqtSlot()
    def about_clicked(self):
        #TODO: call help widget
        self.aboutWidget = AboutWidget()
        self.aboutWidget.show()

    @pyqtSlot()
    def exit_clicked(self):
        QCoreApplication.instance().quit()

    def open_file(self, filename):
        self.onOpenFile.emit(filename)

    def open_folder(self, foldername):
        self.onOpenFolder.emit(foldername)

    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle('Exit')
        msg.setText(
            'Did you save the statistics? (to save the statistics, give the dogs names and click on the "Save statistic" button)')
        no = msg.addButton(
            'No', QMessageBox.NoRole)
        yes = msg.addButton(
            'Yes', QMessageBox.YesRole)
        msg.setDefaultButton(yes)
        msg.exec_()
        msg.deleteLater()
        if msg.clickedButton() is yes:
            self.deleteLater()
            QApplication.closeAllWindows()
            event.accept()
        else:
            event.ignore()
