# Создать класс File:
# -он должен принимать любое количество уникальных имен файлов но не меньше 2-х
# -создать метод который будет проверять существуют ли эти файлы, если нет то создать их
# -создать метод который принимает текст и выводит список файлов (записать текст в выбранный файл)
# -создать метод который выводит список файлов, и при выборе, выводит содержимое в консоль
# -создать метод который даёт возможность выбрать два файла и меняет их содержимое местами
l = []


class File:

    def __init__(self):
        self.__list = []

    def add(self, file_name):
        self.__list.append(file_name)
        self.__list = list(set(self.__list))
        return self.__list

    def check(self):
        for i in self.__list:
            # print(self.__list)
            open(i, "w+")

    def wright(self, text):
        print('List of files')
        for i in self.__list:
            print(i)
        choice = input('select a file: ')
        print(choice)
        f1 = open(choice, 'w')
        f1.write(text)
        f1.close()
        f1 = open(choice, 'r')
        f = f1.read()
        print(f)

    def show_text(self):
        print('List of files')
        for i in self.__list:
            print(i)
        choice = input('select a file for showing: ')
        print(choice)
        f1 = open(choice, 'r')
        f = f1.read()
        print(f)

    def replace(self):
        print('List of files')
        for i in self.__list:
            print(i)
        choice1 = input('select first file: ')
        print(choice1)
        f1 = open(choice1, 'r')
        f = f1.read()
        print(f)
        choice2 = input('select second file: ')
        print(choice2)
        f2 = open(choice2, 'r')
        t = f2.read()
        print(t)

        new_text = open(choice1, 'w')
        new_text.write(t)
        new_text.close()
        new_text = open(choice1, 'r')
        nw = new_text.read()
        print(nw)
        new_text1 = open(choice2, 'w')
        new_text1.write(f)
        new_text1.close()
        new_text1 = open(choice2, 'r')
        nw1 = new_text1.read()
        print(nw1)


file_list = File()
f1 = file_list.add('text3.txt')
print(f1)
f2 = file_list.add('text1.txt')
print(f2)
f3 = file_list.add('text1.txt')
print(f3)
file_list.check()

file_list.wright('ABCDEFG')
file_list.wright('1234567')

file_list.show_text()
file_list.show_text()

file_list.replace()

file_list.show_text()
file_list.show_text()
