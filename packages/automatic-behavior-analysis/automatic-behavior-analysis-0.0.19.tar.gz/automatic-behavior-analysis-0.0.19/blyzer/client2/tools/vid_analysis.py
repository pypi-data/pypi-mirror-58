import math
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
import Vienna_lines_screens as vls
import csv
import glob

from Blyzer.common.settings import BlazesSettings

FPS = 30
Vienna_Width = 1280
Vienna_Height = 720


def get_fps_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps


class Rt_vienna_analysis():
    """
    Warning!!! Class can work only with one object
    """

    def __init__(self, sample_frame, fps):
        self._trajectory = []
        self._last_detected_index = 0

        self._total_distance = 0

        self._fps = fps


        self._frame_width = sample_frame.shape[1]
        self._frame_height = sample_frame.shape[0]

        if str(BlazesSettings().getParam('project', "Vienna")).lower() == 'Vienna':
            environment_settings = vls.get_data(sample_frame)
            self._center_x = environment_settings[0]
            self._center_y = environment_settings[1]
            self._TL_left = environment_settings[2]
            self._BR_left = environment_settings[3]
            self._TL_right = environment_settings[4]
            self._BR_right = environment_settings[5]

        self._heatmap = np.zeros(sample_frame.shape[:2])

        self._object_of_interests = []

    def add_object_of_interests(self, objects):
        self._object_of_interests.append(objects)

    def get_average_distances(self):
        """
            What is the avarage distance between the object we are detecting, and an object of interst
        """
        average_distance = np.zeros(len(self._object_of_interests))
        objects_position = np.array(self._object_of_interests)

        for position in self._trajectory:
            distance = np.add(objects_position, -1 * np.array(position))
            distance = np.linalg.norm(distance, 1)
            average_distance += distance
        average_distance /= len(self._trajectory)
        return average_distance

    def get_distance(self):
        return self._total_distance

    def add_frame_annotation(self, annotation):
        frame_index = annotation["frame_index"]
        while frame_index < len(self._trajectory):
            self._trajectory.append(None)

        if len(annotation["dogs"]) > 0:
            observable_object = annotation["dogs"][0]
            x = (observable_object['x1'] +
                 observable_object['x2'])*self._frame_width / 2
            y = (observable_object['y1'] +
                 observable_object['y2'])*self._frame_height / 2
            self._save_point(frame_index, x, y)

            if self._last_detected_index != frame_index - 1:
                self._interpolate_between(
                    self._last_detected_index, frame_index)

            # Increment distance. Can be applicable only for linear interpolation
            a = np.array(self._trajectory[frame_index])
            b = np.array(self._trajectory[self._last_detected_index])
            self._total_distance += np.linalg.norm(b-a)

            self._last_detected_index = frame_index
        else:
            self._trajectory.append(None)

    def decorate_frame_with_heatmap(self, frame, n_row=18, n_collumn=32, transparency=0.5):
        heatmap = self.get_heatmap(n_row, n_collumn, True)
        y_step = int(frame.shape[0] / n_row)
        x_step = int(frame.shape[1] / n_collumn)
        output = frame.copy()
        for x in range(n_collumn):
            for y in range(n_row):
                x1 = x*x_step
                x2 = (x+1)*x_step
                y1 = y*y_step
                y2 = (y+1)*y_step
                r = heatmap[y][x]
                overlay = frame.copy()
                cv2.rectangle(overlay, (x1, y1), (x2, y2), (255, 0, 0), -1)
                transp = transparency * (r)
                cv2.addWeighted(overlay, transp, output,
                            1 - transp, 0, output)
        frame = output
        return frame

    def decorate_frame_with_trajectory(self, frame, index=-1, duration=None, thickness=3):
        if self._trajectory is None:
            return frame

        if duration is None:
            duration = self._fps * 3
        if str(duration).lower() == 'All'.lower():
            duration = len(self._trajectory)
        if duration > len(self._trajectory):
            duration = len(self._trajectory)

        pts = self._trajectory[index-int(duration):index]
        pts = list(filter(None, pts))
        pts = np.array(pts)
        pts = pts[pts != np.array(None)]
        pts = np.reshape(pts, (pts.shape[0]//2, 2))
        cv2.polylines(frame, np.int32([pts]), False, (0, 0, 255), thickness)
        return frame

    def get_heatmap(self, n_row=18, n_collumn=32, is_norm=True):
        heatmap = np.zeros((n_row, n_collumn), dtype=np.int64)
        y_step = int(self._frame_height / n_row)
        x_step = int(self._frame_width / n_collumn)
        for x in range(n_collumn):
            for y in range(n_row):
                x1 = x*x_step
                x2 = (x+1)*x_step
                y1 = y*y_step
                y2 = (y+1)*y_step
                hm_crop = self._heatmap[y1:y2, x1:x2]
                s = np.sum(hm_crop)
                heatmap[y][x] = s

        if is_norm:
            hm_max = np.amax(heatmap)
            heatmap = heatmap / hm_max
        return heatmap

    def get_average_speed(self):
        return self._total_distance / self._fps


    def get_statistics(self):
        """
        Collect ant return dictinary with basic statistics
        """
        stats = {}
        stats['Total distance'] = self._total_distance
        stats['Average speed'] = self.get_average_speed()
        return stats

    def _save_point(self, i, x, y):
        x = int(x)
        y = int(y)
        if i == len(self._trajectory):
            self._trajectory.append((x, y))
        else:
            self._trajectory[i] = (x, y)
        self._heatmap[y][x] += 1

    def _interpolate_between(self, index_1, index_2, method='linear'):
        # Make method unsensible to index sequence
        if index_2 < index_1:
            index_1, index_2 = index_2, index_1
        if index_1 == index_2:
            return

        try:
            y_start, x_start = self._trajectory[index_1]
        except TypeError:
            y_start, x_start = self._trajectory[index_2]
        y_end, x_end = self._trajectory[index_2]
        length = index_2 - index_1

        x = np.linspace(x_start, x_end, length, endpoint=False)
        y = np.linspace(y_start, y_end, length, endpoint=False)

        for i, x_i, y_i in zip(range(index_1, index_2), x, y):
            self._save_point(i, y_i, x_i)

    def get_quartiles_times(self):
        top_left_samples = np.sum(
            self._heatmap[0:self._center_x, 0:self._center_y])
        top_right_samples = np.sum(
            self._heatmap[self._center_x:self._frame_width, 0:self._center_y])
        bottom_left_samples = np.sum(
            self._heatmap[0:self._center_x, self._center_y:self._frame_height])
        bottom_right_samples = np.sum(
            self._heatmap[self._center_x:self._frame_width, self._center_y:self._frame_height])
        quartiles_time = [top_left_samples, top_right_samples,
                          bottom_left_samples, bottom_right_samples]
        quartiles_time /= self._fps
        return quartiles_time


class vid_info:
    def __init__(self, name, dir_path='/home/liel/Documents/scripts/Vienna_split_video/',  width=Vienna_Width, height=Vienna_Height):
        self.name = name
        self.width = width
        self.height = height
        self.video_name = self.name + '.mp4'
        self.json_name = self.name + '.json'
        self.dir_path = dir_path
        self.csv_file_path = self.dir_path + 'final.csv'
        self.json_path = self.dir_path + self.json_name
        self.video_path = self.dir_path + self.video_name
        self.fps = self.get_fps()
        self.img = vls.get_image(self.video_path, 1)
        # data = X axis of Horizontal separation line, Y axis of vertical separation, left screen
        self.data = vls.get_data(self.img)
        # Top-Left Coordinates, left screen Bottom-Right Coordinates, right screen Top-Left Coordinates,
        # right screen Bottom-Right Coordinates.
        self.center_list = []
        self.acc = 0

    def get_fps(self):
        cap = cv2.VideoCapture(self.video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        return fps

    def set_acc(self):
        cap = cv2.VideoCapture(self.video_path)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        cap.release()
        self.acc = len(self.center_list) / frame_count * 100

    def get_dog_center_list(self, width=Vienna_Width, height=Vienna_Height):
        frame = -1
        with open(self.json_path, 'r') as f:
            datastore = json.load(f)
        for k in range(0, len(datastore["frame_annotations"])):
            frame += 1
            try:
                dog = datastore["frame_annotations"][str(frame)]["dogs"][0]
            except:
                k -= 1
                continue
            self.center_list.append(
                (((dog['x1'] + dog['x2'])*width / 2), ((dog['y1'] + dog['y2'])*height / 2)))
        self.set_acc()

    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0])*(point1[0] - point2[0]) + (point1[1] - point2[1])*(point1[1] - point2[1]))

    def dog_screens_distance(self, dog_center, screen1, screen2):
        return self.distance(dog_center, screen1), self.distance(dog_center, screen2)

    def in_rect(self, obj_center_point, TL_point, BR_point):
        return (TL_point[0] < obj_center_point[0] < BR_point[0] and TL_point[
            1] < obj_center_point[1] < BR_point[1])

    def time_in_rect(self, rect_TL, rect_BR):
        """
        :param path: full path to json file
        :param rect_TL: top-left corner
        :param rect_BR: bottom-right corner
        :return: number of seconds that the object was inside the marked area
        """
        count = 0
        for k in range(0, len(self.center_list)):
            if in_rect(self.center_list[k], rect_TL, rect_BR):
                count += 1
        return float(count) / self.fps

    def init_blue(self, arr):
        for x in range(0, self.height):
            for y in range(0, self.width):
                arr[x][y] = [0, 0, 255]
        return arr

    def create_heatmap(self):
        heatmap = np.zeros((self.height, self.width, 3), np.uint8)
        heatmap = self.init_blue(heatmap)
        for k in range(0, len(self.center_list)):
            heatmap[int(self.center_list[k][1])][int(
                self.center_list[k][0])][2] = 0
            heatmap[int(self.center_list[k][1])][int(
                self.center_list[k][0])][0] += 100
            heatmap = self.add_to_neighbors(heatmap, int(self.center_list[k][1]), int(self.center_list[k][0]),
                                            self.height, self.width, 50)
        cv2.imwrite(self.name + "- Heat map.jpg", heatmap)

    def trajector(self):
        blue = np.zeros((self.height, self.width, 3), np.uint8)
        blue = self.init_blue(blue)
        img = blue
        out = cv2.VideoWriter(self.name + "- Trajectory.mp4", cv2.VideoWriter_fourcc(*'MP4V'), FPS,
                              (self.width, self.height))
        for k in range(0, len(self.center_list)):
            img[int(self.center_list[k][1])][int(
                self.center_list[k][0])][2] = 0  # set pixel to black
            img[int(self.center_list[k][1])][int(
                self.center_list[k][0])][0] = 255  # set pixel to red
            img = self.add_to_neighbors(img, int(self.center_list[k][1]), int(self.center_list[k][0]), self.height,
                                        self.width, 255)
            for a in range(int(self.center_list[k][0]) - 1, int(self.center_list[k][0]) + 2):
                for b in range(int(self.center_list[k][1]) - 1, int(self.center_list[k][1]) + 2):
                    self.add_to_neighbors(
                        img, b, a, self.height, self.width, 255)
            out.write(img)
        out.release()

    def get_avg_distance(self):
        TL_left = self.data[2]
        BR_left = self.data[3]
        TL_right = self.data[4]
        BR_right = self.data[5]
        avg_left = 0
        avg_right = 0
        left_center = (TL_left[0] + BR_left[0])/2, (TL_left[1] + BR_left[1])/2
        right_center = (TL_right[0] + BR_right[0]) / \
            2, (TL_right[1] + BR_right[1]) / 2
        for k in range(0, len(self.center_list)):
            avg_left += self.distance(self.center_list[k], left_center)
            avg_right += self.distance(self.center_list[k], right_center)
        avg_left /= len(self.center_list)
        avg_right /= len(self.center_list)
        return avg_left, avg_right

    def add_to_neighbors(self, arr, x, y, height, width, val):
        if 1 < x < width and 1 < y < height:
            for a in range(x - 1, x + 2):
                for b in range(y - 1, y + 2):
                    if a == x and y == b:
                        continue
                    arr[a][b][2] = 0  # 0 blue in rgb
                    arr[a][b][0] += val  # increase red in rgb
        return arr

    def get_quartiles_times(self):
        center_x = self.data[0]
        center_y = self.data[1]
        top_left = ((0, 0), (center_x, center_y))
        top_right = ((center_x, 0), (self.width, center_y))
        bottom_left = ((0, center_y), (center_x, self.height))
        bottom_right = ((center_x, center_y), (self.width, self.height))
        quartiles_time = [0, 0, 0, 0]  # same order as above
        quartiles_access = [0, 0, 0, 0]
        last_quartile = [False, False, False, False]

        for k in range(0, len(self.center_list)):
            if self.in_rect(self.center_list[k], top_left[0], top_left[1]):
                quartiles_time[0] += 1
                if not last_quartile[0]:
                    for j in range(len(last_quartile)):
                        last_quartile[j] = False
                    last_quartile[0] = True
                    quartiles_access[0] += 1

            elif self.in_rect(self.center_list[k], top_right[0], top_right[1]):
                quartiles_time[1] += 1
                if not last_quartile[1]:
                    for j in range(len(last_quartile)):
                        last_quartile[j] = False
                    last_quartile[1] = True
                    quartiles_access[1] += 1

            elif self.in_rect(self.center_list[k], bottom_left[0], bottom_left[1]):
                quartiles_time[2] += 1
                if not last_quartile[2]:
                    for j in range(len(last_quartile)):
                        last_quartile[j] = False
                    last_quartile[2] = True
                    quartiles_access[2] += 1

            elif self.in_rect(self.center_list[k], bottom_right[0], bottom_right[1]):
                quartiles_time[3] += 1
                if not last_quartile[3]:
                    for j in range(len(last_quartile)):
                        last_quartile[j] = False
                    last_quartile[3] = True
                    quartiles_access[3] += 1

        for quar in range(len(quartiles_time)):
            quartiles_time[quar] /= self.fps  # so we get results in seconds.
        return quartiles_time, quartiles_access

    def make_analysis(self):

        print("analyzing " + self.name)

        quar_time, quar_access = self.get_quartiles_times()
        check = 0
        for time in quar_time:
            check += time
        if check <= 25:
            print("Too short.", check)
            return self.name
        avg_dis = self.get_avg_distance()
        self.create_heatmap()
        self.trajector()
        final_results = [self.name.split('_')[0], self.name.split('_')[2], self.name.split('_')[4], quar_time[0], quar_time[1],
                         quar_time[2],
                         quar_time[3], quar_access[0], quar_access[1], quar_access[2], quar_access[3], avg_dis[0],
                         avg_dis[1],
                         self.name + "- Heat map.jpg", self.name + " - Trajectory.mp4", self.name + ".json", str(self.acc) + "%"]
        with open(r'final.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(final_results)
        return 0


def main():
    """
    #analyzing a whole dir example
    #make sure to change path in class init func as well:
    #########################################################################
    error_list = [] # for
    dir_path = '/home/liel/Documents/scripts/Vienna_split_video/'
    vid_list = glob.glob(dir_path + "*.mp4")
    for x in range(len(vid_list)):
        vid_list[x] = vid_list[x].split("/")[-1].split(".")[0]
    vid_list.sort()
    for name in vid_list:
        name = name.split("/")[-1].split(".")[0]
        analyze = vid_info(name, dir_path)
        analyze.get_dog_center_list()
        if analyze.make_analysis():
            error_list.append(name)
    print(error_list)   # analyze all dir
    #########################################################################
    """

    """
    #analyzing one video
    #make sure to change path in class init func:
    #########################################################################
    a = vid_info('Aeden_session_1_trial_1')
    a.get_dog_center_list()
    a.make_analysis()  # 1 file
    #########################################################################
    """


def tst_heatmap():
    sample_frame = np.random.randint(255, size=(1080, 1920, 3))
    sample_frame[:, 960, :] = 0
    sample_frame[540, :, :] = 0
    fps = 30
    instance = Rt_vienna_analysis(sample_frame, fps)
    instance._heatmap = np.random.randint(10, size=(1080, 1920))
    instance._heatmap[:540, :] *= 2
    hm = instance.get_heatmap()
    plt.imshow(hm)
    plt.show()
    instance.decorate_frame_with_heatmap(sample_frame)
    plt.imshow(sample_frame)
    plt.show()


if __name__ == '__main__':
    tst_heatmap()
    # main()
