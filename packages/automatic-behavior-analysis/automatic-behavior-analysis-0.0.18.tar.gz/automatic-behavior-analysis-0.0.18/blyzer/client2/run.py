#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import argparse
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
# to import from this project without instalation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

import base_plugin
from gui.client_main_gui import Client_GUI

def main():
    """Application entry point"""
    parser = argparse.ArgumentParser(description="Data analysis client")

    parser.add_argument('input_file', nargs='?', help="Input file")
    args = vars(parser.parse_args())
    app = QApplication(sys.argv)
    gui = Client_GUI("Automatic Behavior Analysis", 320, 240, args)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
