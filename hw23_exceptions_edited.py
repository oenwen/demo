operation = input('Введите операцию в польской нотации (одно арифметическое действие с положительными числами) ')
symbols = operation.split()

class CountUserError(Exception):
    pass

try:
    if len(symbols) != 3:
        raise CountUserError()
    operator = symbols[0]
    assert operator in ['+', '-', '*', '/']
    a = int(symbols[1])
    b = int(symbols[2])
    if operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)
    elif operator == '/':
        try:
            print(a / b)
        except ZeroDivisionError:
            print('Деление на 0 не приветствуется')
    elif operator == '*':
        print(a * b)

except ValueError:
    print('Необходимо ввести два числа')
except AssertionError:
    print(operator, 'не является арифметическим оператором')
except CountUserError:
    print('Количество символов не равно 3')
