from defs import from_dec, in_dec, translator


def main():

    while True:
        print("выберите действие:")
        print("0. выйти ")
        print("1. калькулятор чисел")
        print("2. перевод чисел в разные системы")
        main_f = input()

        if main_f.isdigit():
            main_f = int(main_f)
        else:
            continue

        if main_f == 0:
            break
        elif main_f == 1:
            pass
        elif main_f == 2:
            result = translator()
            if result is not None:
                print(result)
        else: continue

if __name__ == "__main__":
    main()