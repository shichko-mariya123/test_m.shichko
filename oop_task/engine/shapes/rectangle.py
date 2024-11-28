from oop_task.engine.shapes.base_shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        print(
            f"Drawing Rectangle: top-left=({self.x}, {self.y}), width={self.width}, height={self.height}, color={self.color}"
        )