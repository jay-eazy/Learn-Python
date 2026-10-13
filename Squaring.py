# The print function, once used, does not get "saved" in the computer
# The return key allows the computer to remember a certain input
# You only need to define it in able for it to remember
# x ** x is another way to do exponents
# pow (x.y) is another way to do exponents

def square_question():
    x = int((input("What number do you want to square")))
    print(square(x))

def square(n):
    return n * n

square_question()