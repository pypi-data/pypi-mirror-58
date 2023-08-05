import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSlot, pyqtSignal

'''
This file contains classes for statistics.
Those class are later used on the GUI
'''


class StatisticItemWidget(QtWidgets.QWidget):
    """This widget displays real-time stats using labels """
    nameChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super(StatisticItemWidget, self).__init__(parent)
        self.id = None
        self.name = None

        # create needed labels for the widget
        self._id = QtWidgets.QLabel()
        self._state = QtWidgets.QLabel()
        self._pos_x = QtWidgets.QLabel()
        self._pos_y = QtWidgets.QLabel()
        self._name_label = QtWidgets.QLabel()
        self._space = QtWidgets.QLabel()

        # create and add action to button
        self._name_line_edit = QtWidgets.QLineEdit()
        self._name_button = QtWidgets.QPushButton("Set name")
        self._name_button.clicked.connect(self.nameEdit)

        # give names to different labels
        self._id.setText("ID: ")
        self._state.setText("STATE: ")
        self._pos_x.setText("POS X: ")
        self._pos_y.setText("POS Y: ")
        self._name_label.setText("NAME: ")

        # creating an HBOX and adding button elements to it
        self.textQHBoxLayout = QtWidgets.QHBoxLayout()
        self.textQHBoxLayout.addWidget(self._name_label)
        self.textQHBoxLayout.addWidget(self._name_line_edit)
        self.textQHBoxLayout.addWidget(self._name_button)

        # creating a VBOX and adding all elements to the VBOX
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textQVBoxLayout.addWidget(self._id)
        self.textQVBoxLayout.addWidget(self._state)
        self.textQVBoxLayout.addWidget(self._pos_x)
        self.textQVBoxLayout.addWidget(self._pos_y)
        # adding the HBOX to the VBOX
        self.textQVBoxLayout.addLayout(self.textQHBoxLayout)
        self.textQVBoxLayout.addWidget(self._space)

        self.setLayout(self.textQVBoxLayout)

    def setStatistic(self, dog, name):
        """
        sets the labels to display the stats results

        Args:
            dog: dictionary of real-time stats normalized
            name: String of dog name

        """
        if dog:
            self.id = dog.get('id')

            self._id.setText("ID: " + str(dog.get('id')))
            self._state.setText("STATE: " + str(dog.get('state')))
            self._pos_x.setText(
                "POS X: " + str(round(dog.get('x1'), 3)) + " " + str(round(dog.get('x2'), 3)))
            self._pos_y.setText(
                "POS Y: " + str(round(dog.get('y1'), 3)) + " " + str(round(dog.get('y2'), 3)))
            self._name_label.setText("NAME: ")
            self._name_line_edit.setText(name)
        else:
            self.id = None
            self.name = None

            self._id.setText("ID: ")
            self._state.setText("STATE: ")
            self._pos_x.setText("POS X: ")
            self._pos_y.setText("POS Y: ")
            self._name_label.setText("NAME: ")
            self._name_line_edit.setText("")

    def clearRtStatistic(self):
        self._id.setText("ID: ")
        self._state.setText("STATE: ")
        self._pos_x.setText("POS X: ")
        self._pos_y.setText("POS Y: ")
        self._name_label.setText("NAME: ")

    @pyqtSlot()
    def nameEdit(self):
        """ edits the name of the dog """

        self.name = self._name_line_edit.text()
        if self.name != "":
            self.nameChanged.emit(self.name)


class SummaryStatisticItemWidget(QtWidgets.QWidget):
    """ a widget which displays the summery of the stats """

    def __init__(self, parent=None):
        super(SummaryStatisticItemWidget, self).__init__(parent)
        # setting stats
        self._total_frames = 0
        self._frames_with_dogs = 0
        self._frames_with_dog_1 = 0
        self._frames_with_dog_1_asleep = 0
        self._frames_with_dog_2 = 0
        self._frames_with_dog_2_asleep = 0

        # setting VBOX and labels for storing the stats
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self._total_frames_w = QtWidgets.QLabel()
        self._frames_with_dogs_w = QtWidgets.QLabel()
        self._frames_with_dog_1_w = QtWidgets.QLabel()
        self._frames_with_dog_1_asleep_w = QtWidgets.QLabel()
        self._frames_with_dog_2_w = QtWidgets.QLabel()
        self._frames_with_dog_2_asleep_w = QtWidgets.QLabel()

        # giving names to the labels
        self._total_frames_w.setText("TOTAL FRAME: ")
        self._frames_with_dogs_w.setText("FRAMES WITH DOGS: ")
        self._frames_with_dog_1_w.setText("FRAMES WITH DOG 1: ")
        self._frames_with_dog_1_asleep_w.setText("FRAMES WITH DOG 1 ASLEEP: ")
        self._frames_with_dog_2_w.setText("FRAMES WITH DOG 2: ")
        self._frames_with_dog_2_asleep_w.setText("FRAMES WITH DOG 2 ASLEEP: ")

        # adding labels to the VBOX
        self.textQVBoxLayout.addWidget(self._total_frames_w)
        self.textQVBoxLayout.addWidget(self._frames_with_dogs_w)
        self.textQVBoxLayout.addWidget(self._frames_with_dog_1_w)
        self.textQVBoxLayout.addWidget(self._frames_with_dog_1_asleep_w)
        self.textQVBoxLayout.addWidget(self._frames_with_dog_2_w)
        self.textQVBoxLayout.addWidget(self._frames_with_dog_2_asleep_w)

        self.setLayout(self.textQVBoxLayout)

    def setSummaryStatistic(self, data):
        """
        Using real-time stats for:

        1) counting the amount of frames
        2) counting the amount of frames that contain a dog.
        3) counting the amount of frames containing a specific dog
        4) counting the amount of frames on which the specific dog is sleeping

        The results are displayed on the labels

        Args:
            data: list of dictionaries, each dictionary contains real-time stats of dog

        Returns:

        """

        self._total_frames += 1  # count frames
        dogs = data.get('dogs')
        if dogs:
            self._frames_with_dogs += 1   # count frame with dog

            dog_id = dogs[0].get('id')
            dog_state = dogs[0].get('state')
            if dog_id == 0:
                self._frames_with_dog_1 += 1   # count specific dog
                if dog_state == 'sleep':
                    self._frames_with_dog_1_asleep += 1  # count of the is sleeping
            elif dog_id == 1:
                self._frames_with_dog_2 += 1
                if dog_state == 'sleep':
                    self._frames_with_dog_2_asleep += 1
            if len(dogs) == 2:
                dog_id = dogs[1].get('id')
                dog_state = dogs[1].get('state')
                if dog_id == 0:
                    self._frames_with_dog_1 += 1
                    if dog_state == 'sleep':
                        self._frames_with_dog_1_asleep += 1
                elif dog_id == 1:
                    self._frames_with_dog_2 += 1
                    if dog_state == 'sleep':
                        self._frames_with_dog_2_asleep += 1

        # display stats on the labels
        self._total_frames_w.setText("TOTAL FRAME: " + str(self._total_frames))
        self._frames_with_dogs_w.setText(
            "FRAMES WITH DOGS: " + str(self._frames_with_dogs))
        self._frames_with_dog_1_w.setText(
            "FRAMES WITH DOG 1: " + str(self._frames_with_dog_1))
        self._frames_with_dog_1_asleep_w.setText(
            "FRAMES WITH DOG 1 ASLEEP: " + str(self._frames_with_dog_1_asleep))
        self._frames_with_dog_2_w.setText(
            "FRAMES WITH DOG 2: " + str(self._frames_with_dog_2))
        self._frames_with_dog_2_asleep_w.setText(
            "FRAMES WITH DOG 2 ASLEEP: " + str(self._frames_with_dog_2_asleep))

    def clearSummaryStatistic(self):
        self._total_frames = 0
        self._frames_with_dogs = 0
        self._frames_with_dog_1 = 0
        self._frames_with_dog_1_asleep = 0
        self._frames_with_dog_2 = 0
        self._frames_with_dog_2_asleep = 0

        self._total_frames_w.setText("TOTAL FRAME: ")
        self._frames_with_dogs_w.setText("FRAMES WITH DOGS: ")
        self._frames_with_dog_1_w.setText("FRAMES WITH DOG 1: ")
        self._frames_with_dog_1_asleep_w.setText("FRAMES WITH DOG 1 ASLEEP: ")
        self._frames_with_dog_2_w.setText("FRAMES WITH DOG 2: ")
        self._frames_with_dog_2_asleep_w.setText("FRAMES WITH DOG 2 ASLEEP: ")
