import math

class Constants:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.half_width = width // 2
        self.half_height = height // 2
        self.pixel = math.ceil(width / 1920)
        self.fps = 144
        self.running = True
        self.state = 0
        self.font_size = 30*self.pixel
        self.padding = 40*self.pixel