import datetime
import pandas as pd
import numpy as np
import os
import copy
from client2.tools.vid_analysis import Rt_vienna_analysis
from Blyzer.common.settings import BlazesSettings

def frame2time(start_time, frame_number, fps):
    """
    returns the time of the frame
    Args:
        start_time: start time of the video
        frame_number: number of frame
        fps: video fps

    Returns:timestamp

    """
    p_ms = int(1000 / fps) * frame_number
    return start_time + pd.Timedelta(np.timedelta64(p_ms, 'ms'))


def filename2time(filename):
    """
    03_20171108201654.mp4
    """
    filename = os.path.basename(filename)
    filename = os.path.basename(filename).split('.')[0][3:]
    time = None
    try:
        time = pd.Timestamp(filename)
    except Exception:
        time = "20000101000000"
    return time


class FrameAnnotation:
    def __init__(self):
        self.frame_index = -1  # Номер кадра
        self.objects = {}  # Ключ -- id


class StatisticHolder:
    """
    The class responsible for storing and processing video annotations
    """

    def __init__(self, file_name, fps):
        """
        File name in date-time format
        Args:
            file_name: video filename
            fps: video fps
        """
        self.annotation_buffer = {}
        self.file_name = file_name
        self.fps = fps
        self._default_name = None
        self.video_time = filename2time(file_name)
        self._rt_vienna_analysis = None

    def set_default_name(self, name):
        self._default_name = name

    def get_all_annotations(self):
        return self.annotation_buffer.copy()

    def add_frame_annotation(self, annotation):
        """
        adds annotation to the annotation_buffer

        {
            'dogs': [
                {
                    'y2': 0.3626135289669037,
                    'category': 'dog',
                    'x2': 0.3295483887195587,
                    'y1': 0.07861500978469849,
                    'state': 'awake',
                    'id': 0,
                    'children': None,
                    'rate': 0.9999867677688599,
                    'x1': 0.15095321834087372
                },
                {
                    'y2': 0.4441756308078766,
                    'category': 'dog',
                    'x2': 0.3256682753562927,
                    'y1': 0.10957882553339005,
                    'state': 'awake',
                    'id': 1,
                    'children': None,
                    'rate': 0.9537808895111084,
                    'x1': 0.12371381372213364
                },
                {
                    'y2': 0.5296827554702759,
                    'category': 'dog',
                    'x2': 0.30304935574531555,
                    'y1': 0.201608344912529,
                    'state': 'awake',
                    'id': 2,
                    'children': None,
                    'rate': 0.9105631113052368,
                    'x1': 0.11796851456165314
                }
            ],
            'frame_index': 6,
            'status': 'ok',
            'event': 'load_image'
        }
        """
        fa = FrameAnnotation()
        annotation = copy.deepcopy(annotation)

        fa.frame_index = annotation['frame_index']

        # dogs detected on the frame added to the annotation_buffer
        for o in annotation['dogs']:
            fa.objects[o['id']] = copy.deepcopy(o)
        self.annotation_buffer[fa.frame_index] = fa

        # Наследуем значения из предыдущего фрейма
        # TODO: скорректировать на случай пропуска фреймов

        try:  # if known name, update all objects to have this name
            for k in self.annotation_buffer[annotation['frame_index']].objects.keys():
                if self._default_name is not None:
                    self.annotation_buffer[annotation['frame_index']].objects[k]['name'] = self._default_name

                # TODO what happens here
                if k in self.annotation_buffer[annotation['frame_index'] - 1].objects.keys():
                    src = self.annotation_buffer[int(annotation['frame_index']) - 1].objects[k]['name']
                    self.annotation_buffer[annotation['frame_index']].objects[k]['name'] = src
        except:
            pass

        self._rt_vienna_analysis.add_frame_annotation(annotation)

    def set_object_name(self, n_frame, id, name):
        """
        Set a name for the object. Name is automatically distributed
        to adjacent frames

        Args:
            n_frame: frame number
            id: object id
            name: string of dog name
        """

        self.annotation_buffer[n_frame].objects[id]['name'] = name

        # Spread the name in adjacent frames
        p_frame = n_frame
        try:
            while id in self.annotation_buffer[p_frame].objects.keys():  # spreads to previous frames
                self.annotation_buffer[p_frame].objects[id]['name'] = name
                p_frame -= 1
        except:
            pass  # Дошли до конца файла

        p_frame = n_frame + 1
        try:
            while id in self.annotation_buffer[p_frame].objects.keys():  # spreads to next frames
                self.annotation_buffer[p_frame].objects[id]['name'] = name
                p_frame += 1
        except:
            pass  # Дошли до конца файла

    def get_object_name(self, n_frame, id):
        """
        Gets the object name
        Args:
            n_frame: frame number
            id: id of the object

        Returns: name of the object

        """
        try:
            name = self.annotation_buffer[n_frame].objects[id]['name']
        except KeyError:
            name = ""
        return name

    def get_unnamed_objects_position(self):
        """
        Returns: list of frames (numbers) with objects without names

        """
        frame_list = []
        for annot in self.annotation_buffer.values():
            try:
                for obj in annot.objects.values():
                    obj['name']
            except:
                frame_list.append(annot.frame_index)
        return frame_list

    def get_all_names(self):
        """
        Returns: all names assigned to objects
        """
        name_list = []
        for key, annot in self.annotation_buffer.items():
            for n_obj, obj in annot.objects.items():
                try:
                    if obj['name'] not in name_list:
                        name_list.append(obj['name'])
                except:
                    pass
        return name_list

    def get_history_by_object_name(self, name):
        """
        gets all stats saved of a specific object
        Args:
            name: object name

        Returns: DataFrame of object history

        """
        if name not in self.get_all_names():
            return None

        columns = ['DateTime',
                   'y1',
                   'y2',
                   'x1',
                   'x2',
                   'state',
                   'rate',
                   'moving_rate',
                   'total_moving']
        history = pd.DataFrame(columns=columns)

        # get all objects and check there name
        for annot in self.annotation_buffer.values():
            for obj in annot.objects.values():
                try:
                    if obj['name'] == name:  # collect data of specific object
                        d = {
                            'DateTime': frame2time(self.video_time, annot.frame_index, self.fps),
                            'y1': obj['y1'],
                            'y2': obj['y2'],
                            'x1': obj['x1'],
                            'x2': obj['x2'],
                            'state': obj['state'],
                            'rate': obj['rate'],
                            'moving_rate': obj['moving_rate'],
                            'total_moving': obj['total_moving']}
                        data = pd.DataFrame(d, columns=columns, index=[annot.frame_index])
                        history = history.append(data)
                except Exception as e:
                    print(e)
        return history

    def save_all_history(self):
        """
        saves all objects history to csv file
        """
        for name in self.get_all_names():
            history = self.get_history_by_object_name(name)
            p = os.path.dirname(self.file_name)
            filename = os.path.basename(self.file_name).split('.')[0]
            fp = os.path.join(p, name + '_' + filename + ".csv")
            history.to_csv(fp)

    def custom_frame_decorator(self, image, response):
        if self._rt_vienna_analysis is None:
            self._rt_vienna_analysis = Rt_vienna_analysis(image, self.fps)

        if BlazesSettings().getParam("show_trajectory", True):
            self._rt_vienna_analysis.decorate_frame_with_trajectory(image, int(response['frame_index']))
        return image

    def create_heatmap(self, frame):
        return self._rt_vienna_analysis.decorate_frame_with_heatmap(frame)

    def create_full_trajectory(self, frame):
        return self._rt_vienna_analysis.decorate_frame_with_trajectory(frame, duration='All')

    def get_statistics(self):
        return self._rt_vienna_analysis.get_statistics()
