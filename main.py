import re


print('Not Too Scientific Calculator')
print('Type QUIT to Exit')

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input('Enter Equation:')
    else:
        equation = input(str(previous))

    if equation == 'quit'.lower():
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)



while run:
    perform_math()
