import re

print("My magical Calculator")
print("Type 'quit' to exit")
previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = eval(str(previous))

    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-z.,:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
