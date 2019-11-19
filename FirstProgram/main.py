import re

print("My magical Calculator")
print("Type 'quit' to exit")
previous = 0
run = True


def performMath():
    global run
    equation = input("Enter equation:")
    if equation == "quit":
        run = False
    else:
        print("You Typed:", equation)


while run:
    performMath()
