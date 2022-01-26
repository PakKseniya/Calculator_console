from calc_core import check_dot, pow_fraction, check_zero, truediv_fraction, mul_fraction, sub_fraction, \
    sum_fraction, letter


def drobi():
    operation = input("Введите операцию(*, /, -, +, ** - возведение в степень): ")

    if operation == '**':
        while True:
            a = input('Введите числитель дроби: ')
            b = input('Введите знаменатель дроби: ')
            c = input('Введите степень: ')
            if check_dot(a) or check_dot(b) or check_dot(c) or letter(a) or letter(b) or letter(c):
                print('Ошибка!Введено вещественное число или буква')
                continue
            else:
                a = int(a)
                b = int(b)
                c = int(c)
                break

        print('Результат = ', pow_fraction(a, b, c))

    elif operation == '*' or operation == '-' or operation == '+' or operation == '/':
        while True:
            a = input('Введите числитель 1-ой дроби: ')
            b = input('Введите знаменатель 1-ой дроби: ')
            c = input('Введите числитель 2-ой дроби: ')
            d = input('Введите знаменатель 2-ой дроби: ')

            if check_dot(a) or check_dot(b) or check_dot(c) or check_dot(d) or letter(a) or letter(b) or letter(c) or \
                    letter(d):
                print('Ошибка!Введено вещественное число или буква')
                continue

            if check_zero(int(b)) or check_zero(int(d)):
                print('На ноль делить нельзя!')
                continue

            else:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                break

        if operation == '/':

            print('Результат = ', truediv_fraction(a, b, c, d))
        elif operation == '*':
            print('Результат = ', mul_fraction(a, b, c, d))
        elif operation == '-':
            print('Результат = ', sub_fraction(a, b, c, d))
        elif operation == '+':
            print('Результат = ', sum_fraction(a, b, c, d))
        else:
            print('Неверно введена арифмитичская операция')

    else:
        print('Неверно введен оператор!')
