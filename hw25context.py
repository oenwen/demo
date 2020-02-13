import contextlib
import datetime

@contextlib.contextmanager

def my_open(path):
    date1 = datetime.datetime.now()
    try:
        file = open(path, encoding = 'utf8')
        yield file

    finally:
        counter = 0
        for line in file:
            if 'Наташ' in line and 'Пьер' in line:
                counter += 1
        print(f'В романе "Война и мир" "Пьер" и "Наташа" встречаются в одном абзаце {counter} раз(а)')
        date2 = datetime.datetime.now()
        print(f'время запуска кода: {date1}')
        print(f'время окончания кода: {date2}')
        print(f'время выполнения кода: {date2 - date1}')
        file.close()

if __name__ == '__main__':
    with my_open('warandpeace.txt') as file:
        pass
