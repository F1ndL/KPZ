from renderer import Renderer

class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError("Метод draw повинен бути реалізований у підкласах.")


class Circle(Shape):
    def draw(self):
        self.renderer.render("Circle")


class Square(Shape):
    def draw(self):
        self.renderer.render("Square")


class Triangle(Shape):
    def draw(self):
        self.renderer.render("Triangle")
