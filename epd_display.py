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
epd.init(0)
epd.Clear(0xFF, 0)



Himage2 = Image.new('L', (epd.height, epd.width), 0xFF)  # 255: clear the frame
bmp = Image.open("/home/epaper/test2.png")
bmp = bmp.rotate(90, PIL.Image.NEAREST, expand = 1)
bmp = bmp.resize((100, 100))
bmp2 = bmp.resize((100, 200))
#Himage2.paste(bmp, (280,0))
#Himage2.paste(bmp, (0,50))
#epd.display_4Gray(epd.getbuffer_4Gray(Himage2))
#time.sleep(5)

draw = ImageDraw.Draw(Himage2)
draw.rectangle((130, 20, 274, 56), 'black', 'black')
