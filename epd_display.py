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


Himage = Image.new('L', (epd.height, epd.width), 0xFF)  # 0xFF: clear the frame
draw = ImageDraw.Draw(Himage)
draw.text((10, 0), 'hello world', font = font24, fill = 0)
draw.text((10, 20), '3.7inch e-Paper', font = font24, fill = 0)
draw.rectangle((10, 110, 154, 146), 'black', 'black')
draw.text((10, 110), u'微雪电子', font = font36, fill = epd.GRAY1)
draw.text((10, 150), u'微雪电子', font = font36, fill = epd.GRAY2)
draw.text((10, 190), u'微雪电子', font = font36, fill = epd.GRAY3)
draw.text((10, 230), u'微雪电子', font = font36, fill = epd.GRAY4)
draw.line((20, 50, 70, 100), fill = 0)
draw.line((70, 50, 20, 100), fill = 0)
draw.rectangle((20, 50, 70, 100), outline = 0)
draw.line((165, 50, 165, 100), fill = 0)
draw.line((140, 75, 190, 75), fill = 0)
draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
draw.rectangle((80, 50, 130, 100), fill = 0)
draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
epd.display_4Gray(epd.getbuffer_4Gray(Himage))
time.sleep(5)
