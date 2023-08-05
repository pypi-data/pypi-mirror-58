#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) Wed Oct 17 19:05:00 2018 Sinitca Alekandr <amsinitca@etu.ru, siniza.s.94@gmail.com>

Created on Wed Oct 17 19:05:00 2018
@author: Sinitca Alekandr <amsinitca@etu.ru, siniza.s.94@gmail.com>
"""

__author__ = 'Sinitca Alekandr'
__contact__ = 'amsinitca@etu.ru, siniza.s.94@gmail.com'
__copyright__ = 'Sinitca Alekandr'
__license__ = 'Proprietary'
__date__ = 'Wed Oct 17 19:05:00 2018'
__version__ = '0.2'

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # to import util
from tkinter import Tk, IntVar, StringVar
from tkinter import CENTER, HORIZONTAL, NORMAL, BOTH, DISABLED
from tkinter import Menu, Frame, Button, Label, Spinbox, Checkbutton
from tkinter import ttk
from tkinter.ttk import Scale
from tkinter import filedialog, simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import numpy as np
import argparse
import traceback
import appdirs, json
from pprint import pprint

from plugins.video_client import Video_Client
from widgets.status_bar import StatusBar
from dialogs.connect_dialog import ConnectDialog
from dialogs.summary_dialog import SummaryDialog
from config import ClientConfig

PADDING_SMALL = 4
PADDING_BIG = 8
APP_NAME = "automatic-behavior-analysis-client"
ELEM_TYPE_TK = 0
ELEM_TYPE_TTK = 1

class Video_GUI:
    def __init__(self, title, min_width, min_height, config):
        self._settings = self.read_settings()
        self._plugin_list = []
        self.root = Tk()
        self.root.title(title)
        # self.root.style = Style()
        # self.root.style.theme_use("clam")

        self.initialize_geometry(min_width, min_height)

        self._connected = False
        self._load_on_connect = None
        self._interactable_elements = []
        self._processing_mode = False

        self.root.config(menu=self.init_menu())
        self.root.protocol('WM_DELETE_WINDOW', self.close)

        self.main_frame = Frame(self.root) # root можно не указывать
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        column = 0
        self.button_frame = Frame(self.main_frame)

        def add_button(button, disabled=True):
            nonlocal column
            button.grid(row=0, column=column, sticky='ns')
            column += 1
            if disabled:
                button['state'] = 'disabled'
            self.register_interactable_element(button, ELEM_TYPE_TK)
            return button


        self.button_start = add_button(Button(self.button_frame, text="Start", command=self.button_start_clicked))
        self.button_upload = add_button(Button(self.button_frame, text="Upload", command=self.button_upload_clicked))
        self.button_process = add_button(Button(self.button_frame, text="Process", command=self.button_process_clicked))
        self.button_summary = add_button(Button(self.button_frame, text="Summary", command=self.button_summary_clicked))
        self.button_clear_cache = add_button(Button(self.button_frame, text="Clear cache", command=self.clear_cache))
        self.button_save_frame = add_button(Button(self.button_frame, text="Save frame", command=self.save_current_frame))

        self.sync_frames = IntVar()
        self.sync_frames.set(1)
        # self.checkbox_frameskip = add_button(Checkbutton(self.button_frame, text="Sync with server", variable=self.sync_frames))

        self.save_video = IntVar()
        self.checkbox_save_video = add_button(Checkbutton(self.button_frame, text="Save video", variable=self.save_video, command=self.toggle_save_video))

        self.sampling = IntVar()
        self.checkbox_sampling = add_button(Checkbutton(self.button_frame, text="Sample", variable=self.sampling, command=self.toggle_sampling))

        self.detect_motion = IntVar()
        self.detect_motion.set(self._settings.get('detect_motion', 1))
        self.checkbox_detect_motion = add_button(Checkbutton(self.button_frame, text="Apply filters", variable=self.detect_motion, command=self.toggle_motion_detection))

        self.limit_boxes = IntVar()
        self.limit_boxes.set(self._settings.get('limit_boxes', 1))
        self.checkbox_limit_boxes = add_button(Checkbutton(self.button_frame, text="Limit boxes", variable=self.limit_boxes, command=self.toggle_limit_boxes))

        self.inner_detection = IntVar()
        self.inner_detection.set(self._settings.get('inner_detection', 1))
        self.checkbox_inner_detection = add_button(Checkbutton(self.button_frame, text="Eye detection", variable=self.inner_detection, command=self.toggle_inner_detection))

        self.button_frame.columnconfigure(column, weight=1)
        column += 1 # Skip a column to create empty space in front of the frame indicator

        self.frame_indicator_label = add_button(Label(self.button_frame, text="Frame:"))
        self.frame_indicator_text = StringVar()
        self.frame_indicator = add_button(Spinbox(self.button_frame, command=self.frame_indicator_modified, textvariable=self.frame_indicator_text))
        self.frame_indicator.configure(width=10)

        self.button_frame.grid(row=0, column=0, sticky='wne')

        self.image_frame = Frame(self.main_frame, bg='black')
        self.image_panel = Label(self.image_frame, borderwidth=0, highlightthickness=0, bg='black')  # initialize image panel
        self.image_panel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.image_panel.bind('<Button-1>', self.video_clicked)
        self.image_panel.bind('<Button-2>', self.video_clicked)
        self.image_panel.bind('<Button-3>', self.video_clicked)
        # self.image_frame.pack(after=self.button_frame, pady=PADDING_SMALL, fill=BOTH, expand=True)
        self.image_frame.grid(row=1, column=0, pady=PADDING_SMALL, sticky='wnse')

        self._slider_disable_callback = False
        self.slider = Scale(self.main_frame, orient=HORIZONTAL, command=self.slider_moved)
        # self.slider = Scrollbar(self.main_frame, orient=HORIZONTAL, command=self.slider_moved)
        self.slider.state(['disabled'])
        # self.slider.pack(side=BOTTOM, fill=X)
        # self.slider.pack(fill=X)
        self.slider.grid(row=2, column=0, sticky='we')
        self.slider.bind('<ButtonPress>', self.slider_grabbed)
        self.slider.bind('<ButtonRelease>', self.slider_released)
        self.register_interactable_element(self.slider, ELEM_TYPE_TTK)
        self._bottom_margin = 150
        self._slider_captured = False

        self.status_bar = StatusBar(self.main_frame)
        # self.status_bar.pack(side=BOTTOM, fill=X, pady=(PADDING_BIG, 0))
        self.status_bar.grid(row=3, column=0, pady=(PADDING_BIG, 0), sticky='wse')

        self.main_frame.pack(padx=4, pady=4, fill=BOTH, expand=True)
        self.imgtk = None
        self.video_running = False
        self._was_running = False
        self._fps = 30
        self._frame_index = 0
        self._ready_for_next_frame = True
        self.root.update()
        self._window_width = self.root.winfo_width()
        self._window_height = self.root.winfo_height()
        print('Window dimensions: {}'.format((self._window_width, self._window_height)))
        self.root.bind('<Configure>', self.on_resize)
        self.status_bar.set_text("Ready")

        self.config = config
        if config.input_file:
            self._load_on_connect = config.input_file
        self._skip_frames = config.skip_frames
        self._sample_delta = self._settings.get('sample_delta', 10)
        config.limit_boxes = self._settings.get('limit_boxes', False)
        config.detect_motion = self._settings.get('detect_motion', True)
        config.inner_detection = self._settings.get('inner_detection', True)

        self._key_bindings = {
            '<space>': lambda event: self.button_start_clicked(),
            '.': lambda event: self.button_step_fw_clicked(),
            ',': lambda event: self.button_step_bk_clicked(),
            ']': lambda event: self.button_step_fw_clicked(self._skip_frames),
            '[': lambda event: self.button_step_bk_clicked(self._skip_frames),
            'g': lambda event: self.save_current_frame()
        }

    def on_resize(self, event):
        # print("Event: {} for {}, is_root: {}".format(event, event.widget, event.widget == self.root))
        if event.widget != self.root: return
        # print("Event: {}".format(event))
        self.root.update()
        if event.width != self._window_width or event.height != self._window_height:
            self._window_width = self.root.winfo_width()
            self._window_height = self.root.winfo_height()
            available_height = event.height - self._bottom_margin
            self.plugin_command('REFRESH_FRAME', available_height=available_height)

    def initialize_geometry(self, min_width, min_height):
        ws = self._settings.get('window') or {}
        width = ws.get('width') or max(self.root.winfo_screenwidth() // 2, min_width)
        height = ws.get('height') or max(self.root.winfo_screenheight() // 2, min_height)
        x = ws.get('x') or (self.root.winfo_screenwidth() - width) // 2
        y = ws.get('y') or (self.root.winfo_screenheight() - height) // 2
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def init_menu(self, menu=None):
        menu = menu or Menu(self.root)

        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="Open...", command=self.open_file_clicked, state=NORMAL if self._connected else DISABLED)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.close)

        servermenu = Menu(menu, tearoff=0)
        servermenu.add_command(label="Connect to remote server...", command=self.connect_remote_clicked)
        servermenu.add_command(label="Connect to localhost on default port", command=self.connect_local_clicked)
        servermenu.add_command(label="Send ping", command=self.send_ping, state=NORMAL if self._connected else DISABLED)

        configmenu = Menu(menu, tearoff=0)
        configmenu.add_command(label="Set max fps", command=self.set_max_fps)
        configmenu.add_command(label="Clear cache", command=self.clear_cache)
        configmenu.add_command(label="Set frameskip", command=self.set_frameskip)
        configmenu.add_command(label="Set sampling rate", command=self.set_sampling_rate)

        helpmenu = Menu(menu, tearoff=0)
        helpmenu.add_command(label="Help")
        helpmenu.add_command(label="About")

        menu.add_cascade(label="File", menu=filemenu)
        menu.add_cascade(label="Server", menu=servermenu)
        menu.add_cascade(label="Config", menu=configmenu)
        menu.add_cascade(label="Help", menu=helpmenu)
        return menu

    def set_image(self, image, frame_index, move_slider=False, preview=False, refresh=False):
        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(image)
        self.imgtk = ImageTk.PhotoImage(image=im)
        self._prev_index = self._frame_index
        self._frame_index = frame_index

        if self.slider and not self._slider_captured or move_slider:
            # self._slider_disable_callback = True
            # self.slider.set(frame_index)
            self.slider['value'] = frame_index
            # self.slider.set(frame_index/ 1000, frame_index/ 1000 + 0.1)
            # self._slider_disable_callback = False
            if self.sampling.get() and not preview and ((frame_index - self._prev_index) > self._sample_delta or frame_index == 0):
                self.save_current_frame()
        self.frame_indicator_text.set(frame_index)
        if not refresh:
            self._ready_for_next_frame = True

    def video_started(self, video_params, first_frame):
        # Configure UI elements after video data has been obtained
        print("Video parameters: {}".format(video_params))
        self.set_status("Opened video file: {}".format(video_params['filename']))
        self.update_video_size(video_params['width'], video_params['height'])
        self._frame_index = 0
        self._ready_for_next_frame = True
        self.slider.configure(from_=0, to=video_params['frame_count'] - 1)
        self.frame_indicator.configure(from_=0, to=video_params['frame_count'] - 1)
        self.set_image(first_frame, 0, True, True)
        self.show_image()
        self.set_element_state(True)
        self.enable_keybindings(True)

    def register_interactable_element(self, elem, elem_type):
        self._interactable_elements.append((elem, elem_type))

    def set_element_state(self, enabled, exceptions=None):
        for elem, elem_type in self._interactable_elements:
            if exceptions is not None and elem in exceptions: continue
            if elem_type == ELEM_TYPE_TK:
                elem['state'] = 'normal' if enabled else 'disabled'
            elif elem_type == ELEM_TYPE_TTK:
                elem.state(['!disabled' if enabled else 'disabled'])

    def enable_keybindings(self, enable):
        if enable:
            action = lambda key, func: self.root.bind(key, func)
        else:
            action = lambda key, func: self.root.unbind(key)

        for key, func in self._key_bindings.items():
            action(key, func)

    def handle_error(self, error):
        message = "Error: {}".format(error)
        print(message)
        traceback.print_exc()
        self.set_status(message)
        messagebox.showerror(title="Error", message=str(error))
        self.set_status("Ready")

    def after(self, ms, func, *args):
        if args and len(args) > 0:
            self.root.after(ms, func, args)
        else:
            self.root.after(ms, func)

    def set_status(self, text):
        self.status_bar.set_text(text)

    def show_image(self):
        self.image_panel.configure(image=self.imgtk, width=self.imgtk.width(), height=self.imgtk.height())  # show the image
        self.image_panel.image = self.imgtk

    def update_video_size(self, video_width, video_height):
        self.root.update()
        current_width = self.root.winfo_width()
        current_height = self.root.winfo_height()
        # if current_width < video_width or current_height < video_height:
        #     self.resize_and_center(max(current_width, video_width), max(current_height, video_height + 100))
        scale = (current_height - self._bottom_margin) / video_height
        print("Current height: {}, video height: {}, video scale: {}".format(current_height, video_height, scale))

    def request_next_frame(self, skip):
        # Don't need to sync - request next frame immediately
        if not self.sync_frames.get():
            self.plugin_command("NEXT_FRAME", skip=skip)
        # Need sync with server - request next frame only after receiving a response for the current frame
        elif self._ready_for_next_frame:
            self.plugin_command("NEXT_FRAME", skip=skip)
            self._ready_for_next_frame = False

    def request_frame(self, index):
        self.plugin_command("SEEK_FRAME", frame=index)
        if not self.video_running:
            self.request_next_frame(0)

    def video_loop(self):
        if self.imgtk is not None and self._ready_for_next_frame:
            self.show_image()
            if self.video_running:
                self.request_next_frame(self._skip_frames)
        self.root.after(int(1000/self._fps), self.video_loop)

    def set_max_fps(self):
        fps = simpledialog.askinteger("Max fps", "Input max fps. \n 1...80",
                                         minvalue=1,
                                         maxvalue=80,
                                         initialvalue=self._fps)
        if fps: self._fps = fps

    def set_frameskip(self):
        skip_frames = simpledialog.askinteger("", "Number of frames to skip between every processed frame",
                                         minvalue=0,
                                         initialvalue=self._skip_frames)
        if skip_frames: self._skip_frames = skip_frames

    def set_sampling_rate(self):
        sample_delta = simpledialog.askinteger("", "Number of frames to skip between saving samples",
                                         minvalue=0,
                                         initialvalue=self._sample_delta)
        if sample_delta:
            self._sample_delta = sample_delta
            self._settings['sample_delta'] = sample_delta

    def send_ping(self):
        self.plugin_command('PING')

    def received_ping_reply(self, reply):
        messagebox.showinfo("Server reply", str(reply))

    def connect(self, ip, port, server_type):
        self.set_status("Connecting to server...")
        self._connected = False
        self.root.config(menu=self.init_menu())
        self.plugin_command('CONNECT', ip=ip, port=port, server_type=server_type)

    def connect_remote_clicked(self):
        ip, port = ConnectDialog.show(
            "Please input the IP address and port of the server you want to connect to",
            self._settings.get('last_server_ip'),
            self._settings.get('last_server_port'))

        if ip and port:
            self._settings['last_server_ip'] = ip
            self._settings['last_server_port'] = port
            self.connect(ip, port, self.config.protocol)

    def connect_local_clicked(self):
        self.connect('127.0.0.1', self.config.port, self.config.protocol)

    def server_connected(self, hostname, port):
        self._connected = True
        self.root.config(menu=self.init_menu())
        self.set_status("Connected to {}:{}".format(hostname, port))
        filename = self._load_on_connect
        if filename:
            self._load_on_connect = None
            self.open_file(filename)

    def open_file_clicked(self):
        filename = filedialog.askopenfilename(initialdir=self._settings.get('last_open_dir', "./"),
                                              title="Select video",
                                              filetypes=(("Video files", "*.mp4"),
                                                         ("All files", "*.*")))
        if len(filename) > 0:
            self._settings['last_open_dir'] = os.path.dirname(filename)
            print("Opening file: {}".format(filename))
            self.open_file(filename)

    def open_file(self, filename):
        self.root.update()
        available_height = self.root.winfo_height() - self._bottom_margin
        self.plugin_command("SET_FILE", FileName=filename, available_height=available_height)
        self.button_start['text'] = "Start"
        self.video_running = False

    def button_summary_clicked(self):
        self.plugin_command("GET_SUMMARY", Handler=self.statistic_handler)

    def button_start_clicked(self):
        if self.video_running:
            self.pause_video()
        else:
            self.resume_video()

    def pause_video(self):
        self.video_running = False
        self.button_start['text'] = "Resume"

    def resume_video(self):
        self.video_running = True
        self.button_start['text'] = "Pause"

    def button_step_fw_clicked(self, skip=0, *args):
        if not self.imgtk: return
        self.pause_video()
        self.request_next_frame(skip)

    def button_step_bk_clicked(self, skip=0, *args):
        if not self.imgtk: return
        self.pause_video()
        self.request_frame(self._frame_index - 1 - skip)

    def video_clicked(self, event):
        self.plugin_command('VIDEO_CLICKED', event=event)

    def popup_object_menu(self, event, obj, frame_index):
        print("Object under mouse: {}".format(obj))
        self.set_dog_name_for_id(obj['id'], frame_index)
        # try:
        #     popup_menu = Menu(self.root, tearoff=0)
        #     popup_menu.add_command(label="Define name", command=lambda: self.set_dog_name_for_id(obj['id'], frame_index))
        #     popup_menu.tk_popup(event.x_root, event.y_root, 0)
        # finally:
        #     popup_menu.grab_release()

    def set_dog_name_for_id(self, dog_id, frame_index):
        name = simpledialog.askstring("Dog name", "Input the dog's name")
        if not name or not isinstance(name, str): return
        name = name.strip()
        if len(name) > 0:
            self.plugin_command('SET_OBJECT_NAME', id=dog_id, name=name, frame_index=frame_index)
            self.plugin_command('REFRESH_FRAME')

    def slider_grabbed(self, event):
        self._was_running = self.video_running
        self._slider_captured = True
        self.pause_video()

    def slider_released(self, event):
        self._slider_captured = False
        if self._was_running: self.resume_video()

    def slider_moved(self, position):
        if self._slider_disable_callback: return
        # print('Slider moved to position {}'.format(position))
        self.request_frame(round(float(position)))

    def frame_indicator_modified(self):
        try:
            value = int(self.frame_indicator_text.get())
        except Exception:
            return

        self.request_frame(value)

    def button_upload_clicked(self):
        self.plugin_command('BEGIN_UPLOAD')

    def upload_started(self, filename, total):
        self._uploading = True
        self.button_upload['state'] = 'disabled'
        self.set_status("Uploading '{}'...".format(filename))

    def upload_progress(self, filename, completed, total):
        percent = round(completed / total * 100) if total > 0 else float('nan')
        self.set_status("Uploading '{}'... {}%".format(filename, percent))

    def upload_finished(self, filename, success):
        self._uploading = False
        self.button_upload['state'] = 'normal'
        self.set_status("Ready")

    def button_process_clicked(self):
        if self._processing_mode:
            self.plugin_command('END_PROCESSING')
            self.button_process['text'] = "Process"
        else:
            self.pause_video()
            self.plugin_command('BEGIN_PROCESSING')
            self.button_process['text'] = "Stop"

    def processing_mode_status(self, event, **kwargs):
        if event == 'started':
            self._processing_mode = True
            self.set_element_state(False, {self.button_process})
        elif event == 'done':
            self._processing_mode = False
            self.set_element_state(True)
        elif event == 'progress':
            self.set_status("Processing: frame {} of {}".format(kwargs['frame_index'] + 1, kwargs['frame_count']))

    def clear_cache(self):
        self.plugin_command('CLEAR_CACHE')

    def save_current_frame(self):
        self.plugin_command('DUMP_FRAME')

    def toggle_save_video(self):
        print("Saving video enabled = {}".format(bool(self.save_video.get())))
        self.plugin_command('DUMP_VIDEO', enabled=bool(self.save_video.get()))

    def toggle_sampling(self):
        print("Sampling enabled = {}, delta = {}".format(bool(self.sampling.get()), self._sample_delta))

    def toggle_motion_detection(self):
        value = bool(self.detect_motion.get())
        self._settings['detect_motion'] = value
        print("Realtime filters enabled = {}".format(value))
        self.plugin_command('REALTIME_PROCESSING', enabled=value)

    def toggle_limit_boxes(self):
        value = bool(self.limit_boxes.get())
        self._settings['limit_boxes'] = value
        print("Box limit enabled = {}".format(value))
        self.plugin_command('BOX_LIMIT', enabled=value)

    def toggle_inner_detection(self):
        value = bool(self.inner_detection.get())
        self._settings['inner_detection'] = value
        print("Inner detection enabled = {}".format(value))
        self.plugin_command('INNER_DETECTION', enabled=value)

    def plugin_command(self, cmd, **kwargs):
        for p in self._plugin_list:
            try:
                p.command(cmd, **kwargs)
            except Exception as exception:
                self.handle_error(exception)

    @staticmethod
    def get_settings_filename():
        return os.path.join(appdirs.user_config_dir(APP_NAME, False), "settings.json")

    def save_settings(self, filename=None):
        self.root.update()
        settings = {
            'window': {
                'x': self.root.winfo_x(),
                'y': self.root.winfo_y(),
                'width': self.root.winfo_width(),
                'height': self.root.winfo_height()
            },
        }

        def write_if_exists(key):
            if key in self._settings:
                settings[key] = self._settings[key]

        write_if_exists('last_open_dir')
        write_if_exists('last_server_ip')
        write_if_exists('last_server_port')
        write_if_exists('sample_delta')
        write_if_exists('detect_motion')
        write_if_exists('limit_boxes')
        write_if_exists('inner_detection')

        filename = filename or self.get_settings_filename()
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(settings, file, indent=2, sort_keys=True)
            # from pprint import pprint
            # print("Wrote settings:")
            # pprint(settings, indent=2)

    def read_settings(self, filename=None):
        filename = filename or self.get_settings_filename()
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                settings = json.load(file)
                # from pprint import pprint
                # print("Loaded settings:")
                # pprint(settings, indent=2)
                return settings
        except:
            return {}

    def close(self):
        # print('Video_GUI::close()')
        self.save_settings()
        for p in self._plugin_list:
            p.close()
        self.video_running = False
        self.root.after(100, sys.exit(0))

    def statistic_handler(self, stat, video_path):
        video_id = os.path.splitext(os.path.basename(video_path))[0]
        SummaryDialog.show(stat, video_id)

    def add_plugin(self, plugin):
        self._plugin_list.append(plugin)
        plugin.run()

    def start(self):
        self.videoThread = threading.Thread(target=self.video_loop, args=())
        self.root.after(100, self.videoThread.start)
        self.root.mainloop()

def run_gui(config):
    """Start the client GUI"""
    gui = Video_GUI("Automatic Behavior Analysis", 320, 240, config)
    video_client = Video_Client(gui, config)
    gui.add_plugin(video_client)
    if config.auto_connect:
        video_client.start(config.ip, config.port, config.protocol)
    gui.start()

def main():
    """Application entry point"""
    config = ClientConfig(os.path.join(os.path.dirname(__file__), "config.json"))
    parser = argparse.ArgumentParser(description="Data analysis client")
    parser.add_argument('--ip', help="Server IP address or hostname", default=argparse.SUPPRESS)
    parser.add_argument('--port', help="Server port", type=int, default=argparse.SUPPRESS)
    parser.add_argument('--protocol', default=config.protocol, help="Server protocol", choices=['tcp', 'websocket'])
    parser.add_argument('--skip-frames', help="Skip (don't process) every k frames", default=0, type=int)
    parser.add_argument('--verbose', help="Show detailed debug messages", action='store_true')
    parser.add_argument('input_file', nargs='?', help="Input file")
    args = vars(parser.parse_args())
    config.update(args)
    config.auto_connect = 'ip' in args or 'port' in args or 'input' in args

    if config.auto_connect:
        print("Starting client for {}:{}".format(config.ip, config.port))
    else:
        print("Starting client")

    run_gui(config)

if __name__ == '__main__':
    main()