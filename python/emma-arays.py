
def numbers() :
    number = [1, 2, 3, 4, 5]
    print('На скільки розширити')
    a = int(input())
    print('Масив 1')
    for i in range (a) :
        i = int(number[-1]) + 1
        number.append(i)
    for i in range(len(number)):
        print('Елемент 1:',[i], number[i])
    print('Масив 2')
    number_new = [i * 2 for i in number]
    for i in range(len(number_new)):
        print('Елемент 2:', [i], number_new[i])
    
numbers ()
