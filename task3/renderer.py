class Renderer:
    def render(self, shape: str):
        raise NotImplementedError("Метод render повинен бути реалізований у підкласах.")


class VectorRenderer(Renderer):
    def render(self, shape: str):
        print(f"Drawing {shape} as vector graphics")


class RasterRenderer(Renderer):
    def render(self, shape: str):
        print(f"Drawing {shape} as pixels")
