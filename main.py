from math import factorial

from defs import from_dec, in_dec, translator, calculator, count_combination


def main():

    while True:
        print("выберите действие:")
        print("0. выйти ")
        print("1. калькулятор чисел")
        print("2. перевод чисел в разные системы")
        print("3. вычисление факториала")
        main_f = input()

        if main_f.isdigit():
            main_f = int(main_f)
        else:
            continue

        if main_f == 0:
            break
        elif main_f == 1:
            result = calculator()
            if result is not None:
                print(result)
        elif main_f == 2:
            result = translator()
            if result is not None:
                print(result)
        elif main_f == 3:
            result = count_combination()
            if result is not None:
                print(result)
if __name__ == "__main__":
    main()