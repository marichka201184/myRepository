def decor(func):
    def wrap():

        return func().replace('_', ' ')
    return wrap

@decor
def pr():
    return 'Hello_boss_!!!'


print(pr())
