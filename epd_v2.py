import sys
import os
import logging
from waveshare_epd import epd3in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import PIL


class DisplayManager(): 
    def __init__(self, display_mode = 0, color = 0xFF): 
        self.display_mode = display_mode
        self.color = color
        self.epd =  epd3in7.EPD()

        self.init_display()
        self.clear_display()

    ''' Wrappers for epd methods'''
    def clear_display(self):
        self.epd.Clear(self.color, self.display_mode)
        logging.info("Display clear")

    def init_display(self):
        self.epd.init(self.display_mode)
        logging.info("Display Init")

epd = DisplayManager()

epd.init_display()
epd.clear_display()

