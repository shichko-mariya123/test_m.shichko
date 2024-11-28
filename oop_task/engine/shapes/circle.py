from oop_task.engine.shapes.base_shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle: center=({self.x}, {self.y}), radius={self.radius}, color={self.color}")
