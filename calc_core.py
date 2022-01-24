from calc_integer import CalcInteg
from calc_fraction import Fraction


def letter(input_text):
    for symb in input_text:
        if 65 <= ord(symb) <= 90 or 97 <= ord(symb) <= 122:
            return True
    return False


def check_type(number):
    if '.' in number:
        return CalcInteg(float(number))
    else:
        return CalcInteg(int(number))


def check_dot(number):
    if '.' in number:
        return True
    else:
        return False


def check_zero(number):
    if number == 0:
        return True
    else:
        return False


def sum_integer(number1, number2):
    return check_type(number1) + check_type(number2)


def sub_integer(number1, number2):
    return check_type(number1) - check_type(number2)


def mul_integer(number1, number2):
    return check_type(number1) * check_type(number2)


def truediv_integer(number1, number2):
    return check_type(number1) / check_type(number2)


def pow_integer(number1, degree):
    return check_type(number1) ** degree


def sum_fraction(numerator1, denominator1, numerator2, denominator2):
    return Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2)


def sub_fraction(numerator1, denominator1, numerator2, denominator2):
    return Fraction(numerator1, denominator1) - Fraction(numerator2, denominator2)


def mul_fraction(numerator1, denominator1, numerator2, denominator2):
    return Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2)


def truediv_fraction(numerator1, denominator1, numerator2, denominator2):
    return Fraction(numerator1, denominator1) / Fraction(numerator2, denominator2)


def pow_fraction(numerator, denominator, degree):
    return Fraction(numerator, denominator) ** degree
