from PyQt5.QtCore import Qt, QObject
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QLabel
from abc import abstractmethod
from Blyzer.client2.gui.videowidget import MediaSource
from PreprocessedMediaSource import PreprocessedMediaSource
from NNPreprocessedMediaSource import NNProcessedMediaSource



"""
This file contains definitions of client2 plugins.
Plugins are classes which add features to the client2 GUI
"""

class BasePlugin(QObject):
    """
    Defines methods which every plugin should contain
    For creating a new plugin for client you need to extend this class
    """
    def __init__(self, config=None, parent=None):
        super().__init__(None)
        self._config = config

    @abstractmethod
    def get_media_source_processor(self):
        return None

    @abstractmethod
    def get_rt_statistic_widget(self):
        return None

    @abstractmethod
    def get_summary_statistic_widget(self):
        return None

    @pyqtSlot(str)
    @abstractmethod
    def onOpenFile(self, filename):
        pass

    @pyqtSlot(str)
    @abstractmethod
    def onOpenFolder(self, foldername):
        pass

class SimplePlugin(BasePlugin):
    def __init__(self, config=None, parent=None):
        super().__init__(config=config, parent=parent)

    @abstractmethod
    def get_media_source_processor(self):
        return PreprocessedMediaSource()

    @abstractmethod
    def get_rt_statistic_widget(self):
        return QLabel()

    @abstractmethod
    def get_summary_statistic_widget(self):
        return QLabel()

class SimplePreprocessPlugin(BasePlugin):
    @abstractmethod
    def get_media_source_processor(self):
        return PreprocessedMediaSource()

    @abstractmethod
    def get_rt_statistic_widget(self):
        return QLabel()

    @abstractmethod
    def get_summary_statistic_widget(self):
        return QLabel()

class SimpleNNPreprocessPlugin(BasePlugin):
    def __init__(self, config=None, parent=None):
        super().__init__(config=config, parent=parent)

    @abstractmethod
    def get_media_source_processor(self):
        return NNProcessedMediaSource(self._config)

    @abstractmethod
    def get_rt_statistic_widget(self):
        return QLabel()

    @abstractmethod
    def get_summary_statistic_widget(self):
        return QLabel()
