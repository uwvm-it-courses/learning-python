# https://www.w3schools.com/python/python_datatypes.asp

x = "Hello World"
print(type(x),  x)

x = 20
print(type(x),  x)

x = 20.5
print(type(x),  x)

x = 1j
print(type(x),  x)

x = ["apple", "banana", "cherry"]
print(type(x),  x)

x = ("apple", "banana", "cherry")
print(type(x),  x)

x = range(6)
print(type(x),  x)

x = {"name" : "John", "age" : 36, "family": [{"name": "Ivasya", "age" : 36}, {"name": "Ivasya", "age" : 36}, {"name": "Ivasya", "age" : 36}]}
print(type(x),  x)

x = {"apple", "banana", "cherry"}
print(type(x),  x)

x = frozenset({"apple", "banana", "cherry"})
print(type(x),  x)

x = True
print(type(x),  x)

x = False
print(type(x),  x)

x = b"Hello"
print(type(x),  x)

x = bytearray(5)
print(type(x),  x)

x = memoryview(bytes(5))
print(type(x),  x)


# Setting the Specific Data Type
print("\n####################################################################\n")
print("####################   Explicit types   #############################")
print("\n####################################################################\n")

x = str("Hello World")
print(type(x),  x)

x = int(20)
print(type(x),  x)


x = float(20.5)
print(type(x),  x)

x = complex(1j)
print(type(x),  x)

x = list(("apple", "banana", "cherry"))
print(type(x),  x)

x = tuple(("apple", "banana", "cherry"))
print(type(x),  x)

x = range(6)
print(type(x),  x)

x = dict(name="John", age=36)
print(type(x),  x)

x = set(("apple", "banana", "cherry"))
print(type(x),  x)

x = frozenset(("apple", "banana", "cherry"))
print(type(x),  x)

x = bool(5)
print(type(x),  x)
x = bool(1)
print(type(x),  x)
x = bool(-1)
print(type(x),  x)

x = bool(0)
print(type(x),  x)

x = bytes(5)
print(type(x),  x)

x = bytearray(5)
print(type(x),  x)

x = memoryview(bytes(5))
print(type(x),  x)
