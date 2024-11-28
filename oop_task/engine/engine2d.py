from oop_task.constants import DEFAULT_COLOR


class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = DEFAULT_COLOR

    def set_color(self, color):
        self.current_color = color

    def add_shape(self, shape):
        shape.set_color(self.current_color)
        self.canvas.append(shape)

    def draw(self):
        for shape in self.canvas:
            shape.draw()
        self.canvas.clear()
