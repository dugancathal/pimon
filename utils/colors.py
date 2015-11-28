class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def to_i(self):
        return (self.red << 16) | (self.green << 8) | self.blue

green = Color(0, 255, 0)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
yellow = Color(255, 255, 0)
purple = Color(255, 0, 255)
white = Color(255, 255, 255)
black = Color(0, 0, 0)
