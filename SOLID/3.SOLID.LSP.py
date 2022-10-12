# SOLID

# Принципы дизайна, представленные Робертом Мартином.

# LSP - Liskov Substitution Principle (принцип подстановки Барбары Лисков).

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height


# Создание производного класса нарушает принцип 'LSP'.

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # Проблема здесь! Функция работает только с Rectangle!
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


# rectangle 3x5
rect = Rectangle(3, 5)
print(rect)
use_it(rect)  # OUT: Expected an area of 30, got 30

# square 5x5
sq = Square(5)
print(sq)
use_it(sq)  # OUT: Expected an area of 50, got 100
