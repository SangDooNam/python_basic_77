


# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def parse_input(user_input):
    
    while True:
        user_input = input('>>> ')
        if user_input == 'quit':
            break
        lst_input = user_input.split()
        if len(lst_input) != 3:
            raise MathematicalError('Input does not consist of three elements')
        if lst_input[1] not in ['+', '-']:
            raise MathematicalError('Invalid operator. Can only use "+" or "-"')
        try:
            result = calculate(float(lst_input[0]), lst_input[1], float(lst_input[2]))
            print(result)
        except ValueError:
            raise MathematicalError('The first and third input value must be numbers')


def calculate(n1, op, n2):

    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2


# print(parse_input('1 + 1'))
