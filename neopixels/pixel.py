class Pixel:
    def __init__(self, index, color):
        self.index = index
        self.color = color
        self.old_color = color

    def set_color(self, new_color):
        self.old_color = self.color
        self.color = new_color

    def red(self):
        return self.color.red

    def green(self):
        return self.color.green

    def blue(self):
        return self.color.blue
