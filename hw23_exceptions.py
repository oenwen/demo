operation = input('Введите операцию в польской нотации (одно арифметическое действие с положительными числами) ')
symbols = operation.split()

try:
    assert len(symbols) == 3
    try:
        operator = symbols[0]
        assert operator in ['+', '-', '*', '/']
        try:
            a = int(symbols[1])
            b = int(symbols[2])
            if operator == '+':
                print(a + b)
            elif operator == '-':
                print(a - b)
            elif operator == '/':
                try:
                    print(a / b)
                except:
                    b == 0
                    print('Деление на 0 не приветствуется')
            elif operator == '*':
                print(a * b)
        except ValueError:
            print('Необходимо ввести два числа')
    except AssertionError:
        print(operator, 'не является арифметическим оператором')

except AssertionError:
    print('Количество символов не равно 3')
