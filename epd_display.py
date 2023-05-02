import sys
import os
import logging
from waveshare_epd import epd3in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import PIL

epd = epd3in7.EPD()
logging.info("init and Clear")
epd.init(1)
epd.Clear(0xFF, 1)



Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
bmp = Image.open("/home/epaper/test2.png")
bmp = bmp.rotate(90, PIL.Image.NEAREST, expand = 1)
bmp = bmp.resize((100, 100))
bmp2 = bmp.resize((100, 200))
#Himage2.paste(bmp, (280,0))
#Himage2.paste(bmp, (0,50))
#epd.display_4Gray(epd.getbuffer_4Gray(Himage2))
#time.sleep(5)

draw = ImageDraw.Draw(Himage2)
while True:
   draw.rectangle((10, 10, 120, 50), fill = 255)
   time.sleep(3)
   draw.rectangle((10, 10, 120, 50), fill = 255)
