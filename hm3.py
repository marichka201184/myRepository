# - створити функцію яка виводить ліст
l = [3, 4, 5, 6, 7, 89]


def func():
    print(l)


func()


# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def func_min(a, b, c):
    print(a, b, c)
    st1 = []
    st1.append(a)
    st1.append(b)
    st1.append(c)
    print("min value element : ", min(st1))
    return min(st1)


func_min(2, 3, 4)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def func_max(a, b, c):
    print(a, b, c)
    st1 = []
    st1.append(a)
    st1.append(b)
    st1.append(c)
    print("max value element : ", max(st1))
    return max(st1)


func_min(2, 3, 4)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def func_min_max(*args):
    print(max(*args))
    return min(*args)


f1 = func_min_max(2, 3, 4, 5)
print(f1)


# - створити функцію яка повертає найбільше число з ліста
def func_max_l(l):
    print(max(l))
    return max(l)


l = [4, 7, 8, 9]
f1 = func_max_l(l)
print(f1)


# - створити функцію яка повертає найменьше число з ліста

def func_min_l(l):
    print(min(l))
    return min(l)


l = [4, 7, 8, 9]
f1 = func_min_l(l)
print(f1)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def func_sum(l):
    print(sum(l))
    return sum(l)


l = [4, 7, 8, 9]
f1 = func_sum(l)
print(f1)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def func_avg(l):
    print(sum(l) / len(l))
    return sum(l) / len(l)


l = [4, 7, 8, 9]
f1 = func_avg(l)
print(f1)


# -функція: def pr(): return 'Hello_boss_!!!'
#  написати декоратор який замінює нижні підчеркування на пробіли і повертає це значення
def decor(func):
    def wrap():

        return func().replace('_', ' ')
    return wrap

@decor
def pr():
    return 'Hello_boss_!!!'


print(pr())
