from drobi import drobi
from digit import digit


def main():
    while True:
        que = input('Вычисления будут для дробных числех? введите [Y/N]:')

        if que == 'N' or que == 'n':
            digit()

        elif que == 'Y' or que == 'y':
            drobi()

        else:
            continue

        answer = input('Продолжить? [Y/N]: ')
        if answer == 'N' or answer == 'n':
            break
        elif answer == 'Y' or answer == 'y':
            continue
        else:
            print("Выбран неверный символ, программа завершена")
            break
