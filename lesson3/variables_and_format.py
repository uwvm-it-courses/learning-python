#https://www.w3schools.com/python/python_variables.asp
print("hello!")

# Whitespaces are matter
if 5 > 2:
  print("Five is greater than two!")

x = 4 # x is of type int
print(x)

x = "Sally" # x is now of type str
print(x)

x = 'John' # x is now of type str, same as ""
print(x)

# # Variable names
# # A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# # A variable name must start with a letter or the underscore character
# # A variable name cannot start with a number
# # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# # Variable names are case-sensitive (age, Age and AGE are three different variables)
#

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Output
x = "awesome"
print("Python is " + x)


# Format
a = 9.99
price = "Ціна родукту: {}"
print(price.format(a))

x = "Python is "
y = "awesome"
z =  x + y
print(z)

## Format
for i in range(65, 112):
    print("ASCII code: %d, char: %c" % (i,i))


# Global variables

print("###########################Global variables##################################")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
print("\n###########################################################################\n")

# Global and local
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

print("###########################Global & local variables##################################")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print("\n###########################################################################\n")

print("########################### Global keyword (makes the variable global)##################################")

## The global Keyword
## BAD PATTERN!
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
print("\n###########################################################################\n")


## BAD PATTERN!
print("########################### Global keyword (makes the variable global and change x) ##################")

x = "awesome"

def myfunc():
  global x
  x = "fantastic"


print("Python is " + x + "(бо ми ще не викликали myfunc())")
# x досі "awesome"

myfunc()

# x після виклику  став "fantastic"

print("Python is " + x)
print("\n###########################################################################\n")
