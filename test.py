class Letter:
    # 3) створити змінну класу __count.
    __count = 0

    # 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
    def __init__(self, text):
        self.__text = text

    def __str__(self):
        return f'{self.__dict__}'


def get_text(self):
    return self.__text


def set_text(self, text):
    self.__text = text


def cnt(self):
    self.__count += 1
    return self.__count


# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount


# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
let1 = Letter('abcd')
let1.cnt()
print(let1.count)
let2 = Letter('abcd')
print(let2)
