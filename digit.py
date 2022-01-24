from calc_core import check_dot, pow_integer, truediv_integer, mul_integer, sub_integer, sum_integer, letter


def digit():
    operation = input("Введите операцию(*, /, -, +, ** - возведение в степень): ")

    if operation == '**':
        while True:
            a = input('Введите число: ')
            if letter(a):
                print('Ошибка!Введена буква!')
            else:
                break
        while True:
            degree = input('Введите степень: ')
            if check_dot(degree) or letter(degree):
                print('Ошибка!Степень не может быть вещественным числом или буквой')
                continue
            else:
                degree = int(degree)
                break

        print('Результат = ', pow_integer(a, degree))

    else:
        while True:
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            if letter(a) or letter(b):
                print("Ошибка!Введена буква")

            else:
                break

        if operation == '/':
            print('Результат = ', truediv_integer(a, b))
        elif operation == '*':
            print('Результат = ', mul_integer(a, b))
        elif operation == '-':
            print('Результат = ', sub_integer(a, b))
        elif operation == '+':
            print('Результат = ', sum_integer(a, b))
        else:
            print('Неверно введена арифмитичская операция')
