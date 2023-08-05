from PyQt5.QtCore import Qt, QObject
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QLabel, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtGui import QImage
from abc import abstractmethod
from video2nnMediaSource import Video2nnMediaSource
from statistic_item_widget import StatisticItemWidget, SummaryStatisticItemWidget
from statistic_holder import StatisticHolder
from summary_widget import SummaryWidget

import base_plugin
import cv2
import os
import glob

"""
File contains plugins for dogs
"""


class SleepDogPlugin(base_plugin.BasePlugin):
    """ Sleeping dog plugin """

    setVideoSrc = pyqtSignal(str)

    def __init__(self, config=None, parent=None):
        super().__init__(config=config, parent=parent)

        self._MAX_OBJECTS = 2

        self._current_viewed_frame = None

        self._rt_statistic_widget = QListWidget()
        self._summary_statistic_widget = QListWidget()

        self.status_bar = None

        self._statistic_holder = None
        self._default_name = None
        self._video_queue = []

        # создание объекта виджета статистики и его установка в QListWidget
        self._statistic_items = []
        for i in range(self._MAX_OBJECTS):
            self._statistic_items.append(StatisticItemWidget())  # create real-time stats object
            myQListWidgetItem = QListWidgetItem(self._rt_statistic_widget)  # create a list to contain real-time widget item
            myQListWidgetItem.setSizeHint(self._statistic_items[i].sizeHint())  # update the size
            self._rt_statistic_widget.addItem(myQListWidgetItem)  # add the the widget to the list
            self._rt_statistic_widget.setItemWidget(myQListWidgetItem, self._statistic_items[i])   # connecting item to the object
            self._statistic_items[i].nameChanged.connect(self.nameChanged)

        # creating summery statistic
        self._summary_statistic_item = SummaryStatisticItemWidget()
        myQListWidgetItem = QListWidgetItem(self._summary_statistic_widget) # creating item for the Q list
        myQListWidgetItem.setSizeHint(self._summary_statistic_item.sizeHint())# set size
        self._summary_statistic_widget.addItem(myQListWidgetItem) # adding the item to the list
        self._summary_statistic_widget.setItemWidget(myQListWidgetItem, self._summary_statistic_item) # connecting item to the object

    def set_status_bar(self, status_bar):
        self.status_bar = status_bar

    def set_menu(self, root_menu):
        """ setting the actions to the menu """
        self._plugin_menu = root_menu.addMenu("Analysis")
        action = self._plugin_menu.addAction("Preview basic stats")
        action.triggered.connect(self.preview_basic_stats_clicked)

        action = self._plugin_menu.addAction("Save all statistic")
        action.triggered.connect(self.save_all_statistic)

        action = root_menu.addAction("Go to unnamed objects")
        action.triggered.connect(self.go_to_unnamed_obj)

    def preview_basic_stats_clicked(self):
        try:
            base = os.path.basename(self._current_file)
            name = os.path.splitext(base)[0]
            self.summaryWidget = SummaryWidget(name=name)
            heatmap = self._statistic_holder.create_heatmap(self._video_preview)
            heatmap = self._statistic_holder.create_full_trajectory(heatmap)
            self.summaryWidget.set_heatmap(heatmap)
            basic_statisic = self._statistic_holder.get_statistics()
            self.summaryWidget.set_report(basic_statisic)
            self.summaryWidget.show()
        except AttributeError:
            QMessageBox.warning(None, "Basic statistic", "Have not statistics", QMessageBox.Cancel)


    def save_all_statistic(self):
        try:
            self._statistic_holder.save_all_history()
        except:
            pass

    def go_to_unnamed_obj(self):
        unnamed_obj_list = self._statistic_holder.get_unnamed_objects_position()
        if unnamed_obj_list:
            next_unnamed_obj_list = list(filter(lambda x: x > self._current_viewed_frame, unnamed_obj_list))
            if len(next_unnamed_obj_list) > 0:
                self._media_source.changePosition(next_unnamed_obj_list[0])
            else:
                self._media_source.changePosition(unnamed_obj_list[0])

    def update_rt_statistic(self, pos):
        """
        updates real-time stats of the widgets
        Args:
            pos: frame number on the video
        """
        dogs = self._statistic_holder.annotation_buffer[pos].objects

        for stat_widget in self._statistic_items:
            stat_widget.clearRtStatistic()

        for dog in dogs.values():
            dog_id = dog.get('id')
            if dog_id >= self._MAX_OBJECTS:
                continue
            name = self._statistic_holder.get_object_name(pos, dog_id)
            self._statistic_items[dog_id].setStatistic(dog, name)

    def process_file(self, filename):
        vidcap = cv2.VideoCapture(filename)
        if not vidcap.isOpened():
            raise RuntimeError("Invalid file format")

        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        success, image = vidcap.read()
        if success:
            self._video_preview = image.copy()
        else:
            self._video_preview = None

        vidcap.release()

        self._current_file = filename
        self.setVideoSrc.emit(filename)
        self.status_bar.showMessage(filename)

        self._statistic_holder = StatisticHolder(filename, fps)
        self._statistic_holder.set_default_name(self._default_name)

        self._media_source.add_custom_frame_decorator(self._statistic_holder.custom_frame_decorator)

        for stat_widget in self._statistic_items:
            stat_widget.clearRtStatistic()

        self._summary_statistic_item.clearSummaryStatistic()

    @pyqtSlot(str)
    def nameChanged(self, name):
        sender = self.sender()
        if sender.id != None:
            self._statistic_holder.set_object_name(self._current_viewed_frame, sender.id, name)

    @abstractmethod
    def get_media_source_processor(self):
        self._media_source = Video2nnMediaSource(self._config)
        self._media_source.onNewFrameAnnotation.connect(self.add_frame_annotation)
        self._media_source.changePixmap.connect(self.frameChanged)
        self._media_source.newStatisticData.connect(self.add_frame_annotation)
        self._media_source.onEndOfFile.connect(self.onEndOfFile)
        self.setVideoSrc.connect(self._media_source.set_source)

        return self._media_source

    @abstractmethod
    def get_rt_statistic_widget(self):
        return self._rt_statistic_widget

    @abstractmethod
    def get_summary_statistic_widget(self):
        return self._summary_statistic_widget

    @pyqtSlot(dict)
    def add_frame_annotation(self, summary):
        """
        На этом уровне должно сохраняться соответствие введенного имени/индекса
        в виджете статистики и собакам на кадрах. При необходимости обновляться и
        распространяться (вперед и назад до момента отсутствия объектов в кадре) при смене.
        Также необходимо подготовить данные для сохранения статистики.
        """
        self._statistic_holder.add_frame_annotation(summary)
        self._summary_statistic_item.setSummaryStatistic(summary)

    @pyqtSlot(int, QImage)
    def frameChanged(self, position, image):
        """

        """
        # TODO: Обновление содержимого виджетов статистики
        self._current_viewed_frame = position
        self.update_rt_statistic(position)

    @pyqtSlot(str)
    @abstractmethod
    def onOpenFile(self, filename):
        if not os.path.exists(filename):
            raise RuntimeError("File does not exist: '{}'".format(filename))

        if not os.path.isfile(filename):
            raise RuntimeError("'{}' is not a file".format(filename))

        self._default_name = None
        self.process_file(filename)

    @pyqtSlot()
    def onEndOfFile(self):
        print("End of file")
        self.save_all_statistic()
        self._process_next_video()

    def _process_next_video(self):
        try:
            next_file = self._video_queue.pop()
            print(next_file)
            self.process_file(next_file)
        except IndexError:
            print("End of task")

    @pyqtSlot(str)
    @abstractmethod
    def onOpenFolder(self, foldername):
        if not os.path.exists(foldername):
            raise RuntimeError("Folder does not exist: '{}'".format(foldername))

        if not os.path.isdir(foldername):
            raise RuntimeError("'{}' is not a folder".format(foldername))

        self._default_name = None #"Atila"  # TODO: get name from config
        self._video_queue = glob.glob(os.path.join(foldername, "") + "*.mp4")  # TODO: get extension from config
        self._process_next_video()
