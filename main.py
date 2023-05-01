### Зад.1. Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими методами для подсчета площади. Для классов нужно
# переопределить магические методы int(возвращает площадь) и str (возвращает информацию о фигуре).

# class Figure:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         return
#
#     def __int__(self):
#         print(f'Фигура: {self.name}')
#
#     def __str__(self):
#         print(f'Площадь: {self.area()}')
#
#
# class Rectangle(Figure):
#
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#         super().__init__('прямоугольник')
#
#     def area(self):
#         return self.lenght * self.width
#
#
# class Triangle(Figure):
#
#     def __init__(self, leg_1, leg_2):
#         self.leg_1, self.leg_2 = leg_1, leg_2
#         super().__init__('прямоугольный треугольник')
#
#     def area(self):
#         return self.leg_1 * self.leg_2 / 2
#
#
# class Circle(Figure):
#
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__('круг')
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# class Trapeze(Figure):
#     def __init__(self, top, base, height):
#         self.top = top
#         self.base = base
#         self.height = height
#         super().__init__('трапеция')
#
#     def area(self):
#         return (self.top + self.base) * self.height / 2
#
# r = Rectangle(20, 40)
# r.__int__()
# r.__str__()
# print('-----------------')
# c = Circle(20)
# c.__int__()
# c.__str__()
# print('-----------------')
# tr = Triangle(30, 40)
# tr.__int__()
# tr.__str__()
# print('-----------------')
# a = Trapeze(20, 30, 10)
# a.__int__()
# a.__str__()



### Зад.2. Создайте базовый класс Shape для рисования плоских фигур. Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника со сторонами,
# параллельными осям координат, и размерами этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о
# каждой из фигур.

class Shape:
    def __init__(self):
        self.shape_type = ''

    def Show(self):
        pass

    def Save(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'{shape.shape_type}')

    @staticmethod
    def Load(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__()
        self.x = x
        self.y = y
        self.side_length = side_length
        self.shape_type = 'Квадрат'

    def Show(self):
        print(f'{self.shape_type}. \nКоординаты верхнего левого угла: x = {self.x}, y = {self.y}, \n'
              f'длина стороны = {self.side_length}')


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape_type = 'Прямоугольник'

    def Show(self):
        print(f'{self.shape_type}. \nКоординаты верхнего левого угла: x = {self.x}, y = {self.y}, \n'
              f'Стороны: ширина = {self.width}, высота = {self.height}')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.shape_type = 'Окружность'

    def Show(self):
        print(f'{self.shape_type}. \nКоординаты центра: x = {self.x}, точка y = {self.y},\nрадиус = {self.radius}')

class Ellipse(Shape):
    def __init__(self, x, y, lenght, height):
        super().__init__()
        self.x = x
        self.y = y
        self.lenght = lenght
        self.height = height
        self.shape_type = 'Эллипс'

    def Show(self):
        print(f'{self.shape_type}. \nКоординаты верхнего угла описанного вокруг него прямоугольника:'
              f'x = {self.x}, y = {self.y}\n'
              f'стороны прямоугольника: {self.lenght}, {self.height}')

shapes = [Square(10, 10, 20), Rectangle(30, 30, 40, 50), Circle(60, 60, 30), Ellipse(10, 10, 20, 25)]
for shape in shapes:
    shape.Show()
    shape.Save(f'{shape.shape_type}.txt')


loaded_shapes = []

for shape_type in ['квадрат', 'прямоугольник', 'окружность', 'эллипс']:
    loaded_shapes.append(Shape.Load(f'{shape_type}.txt'))
print(loaded_shapes)