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



Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
bmp = Image.open("/home/epaper/test.png")
Himage2.paste(bmp, (200,50))
epd.display_4Gray(epd.getbuffer_4Gray(Himage2))
time.sleep(5)