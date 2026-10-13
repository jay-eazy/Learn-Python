# def - define
# Scope - a variable that is only defined inside whatever it is inside
def hello():
    name = input("Enter your first and last name: ")
    name = name.title().strip()
    first, *last = name.split()
    print("Hello, ", end="")
    print(first)

hello()
