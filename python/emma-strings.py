def price ():
    a = input()
    price = " Ціна родукту: {}"
    print(price.format(a))

price()

def word ():
    print('Введіть текст: ')
    b = str(input())
    text = "\t {} \n".format(b)
    print(text)

    import re
    pattern = r'\W'
    results = re.findall(pattern, b)
    print('no' if results else 'yes')
          
word()

def number():
    print("Введіть ціле число: ")
    n = int(input())
    n = '%05i'%n
    print("{}".format(n))

    print("Введіть ціле число: ")
    n = int(input())
    print('%05i'%n)

    print("Введіть ціле число: ")
    n = int(input())
    print("{0:05.0f}".format(n))

number()
