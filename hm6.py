# Создать класс File:
# -он должен принимать любое количество уникальных имен файлов но не меньше 2-х
# -создать метод который будет проверять существуют ли эти файлы, если нет то создать их
# -создать метод который принимает текст и выводит список файлов (записать текст в выбранный файл)
# -создать метод который выводит список файлов, и при выборе, выводит содержимое в консоль
# -создать метод который даёт возможность выбрать два файла и меняет их содержимое местами
class File:
    def __init__(self, x, y):
        self.list = [x, y]

    def get_file(self):
        return self.list

    def __add__(self, other):
        return f'{self.__dict__} : {other.__dict__}'

    def add(self, file_name):
        self.list.append(file_name)
        return self.list


file_list = File('text.txt', 'text2.txt')
print(file_list)
print(file_list.get_file())
file_list.add('text3.txt')
print(file_list.get_file())
file_list.add('text1.txt')
print(file_list.get_file())


def check(files):
    for i in files:
        open(i, "w+")


check(file_list.get_file())


def wright(text, l):
    for i in l:
        print(i)
    choice = input('select a file: ')
    print(choice)
    f1 = open(choice, 'w')
    f1.write(text)
    f1.close()
    f1 = open(choice, 'r')
    f = f1.read()
    print(f)


wright('ABCDEFG', file_list.get_file())
