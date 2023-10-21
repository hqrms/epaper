import os
import sys
from waveshare_epd import epd3in7
from PIL import Image,ImageDraw,ImageFont

class DisplayManager(): 
    def __init__(self):
        self.width = 280
        self.height = 480
        self.font_size = 18
        self.font = ImageFont.truetype(os.path.join("component library", 'Font.ttc'), self.font_size)

        # "L" = Greyscale image channel
        self.canvas = Image.new(
                                    'L', 
                                    (self.height, self.width),
                                    0xFF
                                )
        
        self.canvas_board = ImageDraw.Draw(self.canvas)

    def init_display(self, partial=False):
        self.epd = epd3in7.EPD()

    def draw_text(self, position, text, is_filled=0):
        self.canvas_board.text(
            (position[0], position[1]), 
            text, 
            font = self.font, 
            fill = is_filled
        )

    def sleep_display(self):
        self.epd.sleep()

    def clear_display(self, color=0xFF):
        self.epd.Clear(color, 0)

    
    def generate_text_array(self):
        lines = round(self.width / self.font_size)
        cols  = round(self.height / self.font_size)
        return lines,cols

    