from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.color = None

    def set_color(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass
