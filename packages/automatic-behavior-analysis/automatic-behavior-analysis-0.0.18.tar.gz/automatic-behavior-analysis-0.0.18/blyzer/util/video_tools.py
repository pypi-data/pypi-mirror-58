import os
import cv2
from analitics.summary import get_object_name
from Blyzer.common.settings import BlazesSettings


class VideoSaver:
    """ A class that writes video to a file """
    def __init__(self, path, fps, width, height):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # TODO: put video output format into the config file
        print("VideoSaver.__init__: fourcc: {}, fps: {}, width: {}, height: {}".format(fourcc, fps, width, height))
        self.writer = cv2.VideoWriter(path, fourcc, fps, (width, height))

    @staticmethod
    def create(config:BlazesSettings, output_dir, base_filename, vidcap):
        """
        Creates a class of VideosSaver and adds parameters to it

        Args:
            config: output folder path
            output_dir: folder which the written video will be saved
            base_filename: filename
            vidcap: video capture object

        Returns:

        """
        output_dir = output_dir
        path = os.path.join(output_dir, "{}-output.{}".format(base_filename, config.getParam("video_extension")))
        # print("Output video path:", path)
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return VideoSaver(path, fps, width, height)

    def add_frame(self, image):
        self.writer.write(image)

    def close(self):
        self.writer.release()


class FrameDecorator:
    def __init__(self, config:BlazesSettings):
        r = lambda color: list(reversed(color[:3])) + color[3:]
        self._color_unknown = r(config.getParam("color_unknown"))
        self._color_by_state = {'awake': r(config.getParam("color_awake")), 'sleep': r(config.getParam("color_sleep"))}
        self._max_boxes = config.getParam("max_detection_targets")
        self._limit_boxes = config.getParam('limit_boxes', True)
        self._font = cv2.FONT_HERSHEY_SIMPLEX
        self._text_y_offset = 7
        self._skeleton = config.getParam("skeleton")

        self._show_state = config.getParam("show_state", False)
        self._show_name = config.getParam("show_name", False)
        self._show_rate = config.getParam("show_rate", True)
        self._show_type = config.getParam("show_type", True)

        self._text_format = ""
        if self._show_name:
            self._text_format += "[{name}]"
        if self._show_type:
            self._text_format +=  " {type}"
        if self._show_state:
            self._text_format +=  "-{state}"
        if self._show_rate:
            self._text_format += " {rate:.2%}"


    @staticmethod
    def resize_image(image, scale):
        im_height, im_width, *_ = image.shape
        return cv2.resize(image, (round(im_width * scale), round(im_height * scale)))

    def set_box_limit(self, limit_enabled, max_boxes):
        self._limit_boxes = limit_enabled
        self._max_boxes = max_boxes

    def decorate(self, image, response, object_names={}, draw_children=False):
        # print("Image width: {}, image height: {}".format(im_width, im_height))
        im_height, im_width, *_ = image.shape

        items = response['dogs']
        if self._limit_boxes:
            items = items[:self._max_boxes]

        for item in items:
            xmin = int(im_width * item['x1'])
            ymin = int(im_height * item['y1'])
            xmax = int(im_width * item['x2'])
            ymax = int(im_height * item['y2'])
            name = get_object_name(object_names, item['id'])
            color = self._color_by_state.get(item['state'], self._color_unknown)
            text = self._text_format.format(name=name, type=item['category'], state=item['state'], rate = item['rate'])
            image = self.draw_item(image, xmin, ymin, xmax, ymax, item, color, 3, text, 0.4)
            if not draw_children: continue
            children = item.get('children')
            if children is None: continue
            image = self.draw_children(image, xmin, ymin, xmax, ymax, children, color)

        return image

    def draw_children(self, image, parent_xmin, parent_ymin, parent_xmax, parent_ymax, children, parent_color):
        width = abs(parent_xmax - parent_xmin)
        height = abs(parent_ymax - parent_ymin)

        for item in children:
            xmin = int(width * item['x1']) + parent_xmin
            ymin = int(height * item['y1']) + parent_ymin
            xmax = int(width * item['x2']) + parent_xmin
            ymax = int(height * item['y2']) + parent_ymin
            # color = self._color_by_state.get(item['state'], self._color_unknown)
            # text = "{}-{}: {:.2g}".format(item['category'], item['state'], item['rate'])
            text = item['category']
            image = self.draw_item(image, xmin, ymin, xmax, ymax, item, parent_color, 2, text, 0.3)
            # image = self.draw_item(image, xmin, ymin, xmax, ymax, item, parent_color, None, 0.3)
        return image

    def draw_item(self, image, xmin, ymin, xmax, ymax, item, color, thickness, text, text_size):
        image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, thickness)
        if text is None: return image

        text_x = xmin
        text_y = ymin - self._text_y_offset

        if text_y < 10:
            text_y = ymax + self._text_y_offset * 2

        # return cv2.putText(image, text, (text_x, text_y), self._font, text_size, (255, 255, 255), 1, cv2.LINE_AA)
        return cv2.putText(image, text, (text_x, text_y), self._font, text_size, (52, 211, 152), 1, cv2.LINE_AA)

def test():
	pass

def show_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
