#  Створити клас rectangle
# 1) об'єкт приймає два параметри - дві сторони х у
# 2) описати методи арифметичні
#   + сума площин двок об'єктів
#   - різниця площин
# 3) логічні оператори:
#   == повертає true якщо рівні по площині
#   != якщо не рівні
#   >, < відповідно
# 4) len() - сума сторін

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def len(self):
        return self.x + self.y


rectangle1 = Rectangle(5, 4)
rectangle2 = Rectangle(3, 2)

print(rectangle1.area());
print(rectangle2.area());


def sum(a, b):
    return a + b


s = sum(rectangle1.area(), rectangle2.area())
print(s)


def diff(a, b):
    return a - b


d = diff(rectangle1.area(), rectangle2.area())
print(d)


def comp(a, b):
    if a == b:
        print('True')
    elif a != b:
        print('False')
    if a > b:
        print('a>b')
    else:
        print('a<b')


comp(rectangle1.area(), rectangle2.area())

l = rectangle1.len()
l2 = rectangle2.len()

print(l)
print(l2)

# ######################################################################
l = []


# 2)Створити клас Letter
class Letter:
    # 3) створити змінну класу __count.
    __count = 0

    def __init__(self, text):
        self.__text = text
        Letter.__count += 1

    # 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    # 7) має бути метод який записує в наш ліст текст з нашої змінної __text
    def add(self, l):
        l.append(self.__text)
        return l

    # 5) при створені об'єкта __count має збільшуватися на 1
    # 6) має бути метод(метод класу) для виводу __сount

    @classmethod
    def cnt(cls):
        print(f'cont: {cls.__count}')


let1 = Letter('abcd')
print(let1.get_text())
let1.set_text('ABCD')
print(let1.get_text())
let1.add(l)
print(l)
let2 = Letter('k')
let2.set_text('EFGH')
print(let2.get_text())
let2.add(l)
print(l)
Letter.cnt()
