class Color:
    def __init__(self, red, green, blue, name="unnamed"):
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue

    def to_i(self):
        return (self.red << 16) | (self.green << 8) | self.blue

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


green = Color(0, 255, 0, "colors.green")
red = Color(255, 0, 0, "colors.red")
blue = Color(0, 0, 255, "colors.blue")
indigo = Color(128, 0, 255, "colors.indigo")
yellow = Color(255, 255, 0, "colors.yellow")
lightyellow = Color(255, 102, 0, "colors.lightyellow")
orange = Color(255, 192, 0, "colors.orange")
purple = Color(255, 0, 255, "colors.purple")
white = Color(255, 255, 255, "colors.white")
gray = Color(25, 25, 25, "colors.gray")
black = Color(0, 0, 0, "colors.black")
