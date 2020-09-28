def my_function(*kids):
    for name in kids:
        print(name)
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
my_function("Emil", "Tobias", "Linus", "Vanya", "Vasya", "Svitlana", "Bogdana")


def my_function(**kid):
  print(kid["age"])
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes", age = 34)

def mult(a,b,c):
    res = a*b*c
    print("res: ", res)
    return res

v1 = mult(1,2,3)
v2 = mult(v1, 4, 5)
print(v2)

name = input('What is your name? ')

print(name)

upper_name = name.upper()
name = name.upper()
print(upper_name)


def greeting(arg1, arg2):
    name1 = "Creat " + arg1
    name2 = "Sant " + arg2
    print("Hello, ", name1, " and ", name2)


greeting("Svitlana", "Bogdana")
greeting("Svitlana1", "Bogdana1")
greeting("Vanya", "Vasya")

name1 = "Anna"
name2 = "Vasyl"
greeting(name1, name2)
greeting(name2, name1)

xx = "Petro"
yy = "Oksana"
greeting(xx, yy)
greeting("Vanya", "Vasya")


