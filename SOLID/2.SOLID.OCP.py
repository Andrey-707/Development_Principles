# SOLID

# Принципы дизайна, представленные Робертом Мартином.

# OCP - Open Closed Principle (принцип открытости / закрытости).

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Такой подход к фильтрации объектов является нарушением принципа 'OCP',
# поскольку при добавлении новой функциональности разработчик должен добавлять
# её через расширение, а не через модификацию.
# Кроме нарушения принципа 'OCP', такой подход так же не масштабируется, т.е.
# приводит к взрывной сложности. Фильтр по двум критериям приводит к трем
# методам. 2 --> 3 (C S CS)
# Фильтр по трем критериям (цвет, размер и вес) приводит к семи методам.
# 3 --> 7 (C W S CW SW CS CSW)
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# OCP = open for extension, closed for modification.
# Корпоративный шаблон Specification не нарушает принцип 'OCP'.

class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# здесь настраивается комбинатор фильтра
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        # Функция map применяет лямбда функцию ко всем аргументам.
        # Функция all вернет True в случае, когда все True.
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


# создадим несколько продуктов
apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

# поместим продукты в список
products = [apple, tree, house]

# используем 'old' подход, который нарушает принцип 'OCP'
pf = ProductFilter()

# напечатаем все зеленые продукты
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f'- {p.name} is green.')

# напечатаем все большие продукты
print('Large products (old):')
for p in pf.filter_by_size(products, Size.LARGE):
    print(f'- {p.name} is large.')

# ####################################################################################################
# используем 'new' подход, который НЕ нарушает принцип 'OCP'
bf = BetterFilter()

# напечатаем все зеленые продукты
print('Green products (new):')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f'- {p.name} is green.')

# напечатаем все большие продукты
print('Large products (new):')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f'- {p.name} is large.')

# исползуя комбинатор, найдем все большие и синие предметы
print('Large blue products (new):')
blue = ColorSpecification(Color.BLUE)
large_blue = AndSpecification(large, blue)
for p in bf.filter(products, large_blue):
    print(f'- {p.name} is large and blue.')
