
#Спосіб 1
while 1:
    a = input("Введіть ціле число: ")
    try:
        a = int(a)
        break
    except ValueError:
        print('Ви ввели {}, введіть число'.format(type(a)))

# Спосіб 2

def number (a):
    print("Введіть ціле число: ",a)
    if type (a) == int:
        print(a)
    else:
        print('Ви ввели ', type(a))

number('gfdr')

#Функція поділу чисел

def division (a, b):
    while 2:
        if b == 0:
            print("Знаменник дорівнює 0")
            return
        if type(a) not in (float, int) or type(b) not in (float, int):
            print("Ви ввели :", type(a), type(b), "Введіть числа")
            return
        else:
            c = a/b
            print(a,'/', b, '=', c)
        break

division(10, 5)

def number(a):
    a = int(a)
    print(bin(a), oct(a), hex(a))
number(25)
