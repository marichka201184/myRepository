class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.age} '

    def __repr__(self):
        return f'{self.name} - {self.age} '


class Cinderella(Human):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def __repr__(self):
        return f'Name-{self.name} Age- {self.age} Size-{self.size}'


l = [Cinderella('Anna', 20, 37), Cinderella('Kate', 25, 35), Cinderella('Ira', 19, 36)]

print(l)


class Prince(Human):
    def __init__(self, name, age, size_c):
        super().__init__(name, age)
        self.size_c = size_c

    def __repr__(self):
        return f'Name-{self.name} Age- {self.age} Size of Cinderella-{self.size_c}'

    def find(self, list):
        for i in list:
            if i.size == self.size_c:
                print(f'It is my cinderella - {i.name}')
                break


prince = Prince('Vova', 30, 35)
print(prince)

prince.find(l)