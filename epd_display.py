import sys
import os
import logging
from waveshare_epd import epd3in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

epd = epd3in7.EPD()
logging.info("init and Clear")
epd.init(0)
epd.Clear(0xFF, 0)

img= Image.open(r"/home/epaper/test.png")
epd.display_4Gray(epd.getbuffer_4Gray(Himage))
