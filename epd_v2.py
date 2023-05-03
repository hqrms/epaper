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

    def update_display(self, board):
        self.epd.display_4Gray(self.epd.getbuffer_4Gray(board))

    def display_sleep(self):
        self.epd.sleep()

class DrawingBoard():
    def __init__(self, height = 480, width = 280, color = 0xFF): 
        self.height = height
        self.width = width
        self.color = color 
        self.greyscale = "L"
        self.board = Image.new(self.greyscale, (self.height, self.width), self.color)

    def paste_image(self, image, position):
        x,y = position
        self.board.paste(image, (x,y))

class FontManager():
    def __init__(self, size = 24):
        self.size = size 
        self.font_path = '/home/epaper/OpenSans-Regular.ttf'
        self.font = ImageFont.truetype(self.font_path, self.size)

    def draw_font(self, board):
        draw = ImageDraw.Draw(board)
        draw.text((10, 0), 'Hello World', font = self.font, fill = 0)

        
epd = DisplayManager()
canvas = DrawingBoard()
font = FontManager()

epd.init_display()
epd.clear_display()

img = Image.open("/home/epaper/test2.png")
img = img.rotate(90, PIL.Image.NEAREST, expand = 1)
img = img.resize((200, 100))

canvas.paste_image(img, [280,0])
epd.update_display(canvas.board)

# Partial update test

partial_epd = DisplayManager(1)

font.draw_font(canvas.board)
epd.update_display(canvas.board)
epd.display_sleep()
