#int - numbers/integers (+ - * / %)
# floats - a number with a decimal
# percent is modulo/ taking the remainder of a division

x = float(input("What is x?"))
y = float(input("What is y?"))
# We can nest functions in other functions
# we do the int/float function because the input function always converts input into string

z= round(x/y,3)

print(z)

#print(f"{z:,}")
# notice how this is an f string

# The round function rounds a float, which turns it into an int
# round(number [. ndigits])
#Brackets [] are optional things


