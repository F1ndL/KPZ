from renderer import VectorRenderer, RasterRenderer
from shape import Circle, Square, Triangle


def main():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    print("Використовуємо VectorRenderer:")
    circle = Circle(vector_renderer)
    square = Square(vector_renderer)
    triangle = Triangle(vector_renderer)
    circle.draw()
    square.draw()
    triangle.draw()

    print("\nВикористовуємо RasterRenderer:")
    circle = Circle(raster_renderer)
    square = Square(raster_renderer)
    triangle = Triangle(raster_renderer)
    circle.draw()
    square.draw()
    triangle.draw()


if __name__ == "__main__":
    main()
