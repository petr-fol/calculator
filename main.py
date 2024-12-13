if __name__ == "main":
    from defs import from_dec, in_dec

    print("чтобы выйти из программы введите '0'\n")
    while True:

        a = int(input("в какой системе счисления ваше число?\n"))
        if a == 0:
            break
        b = int(input("в какую систему счисления перевести?\n"))
        if b == 0:
            break
        c = input("ваше число?\n")
        if c == 0:
            break

        num_notation = (2, 8, 10, 16)
        dec = int
        num = 0
        if a <= 36 and b <= 36:
            dec = c
            if a != 10:
                dec = in_dec(c, a)
            num = from_dec(dec, b)
        else:
            print("вы ввели систему счисления > 36, могут быть ошибки в вычислениях изза ограниченного алфавита")
            answer = input("продолжить: Enter\n")
            if answer is None:
                break
            else:
                dec = in_dec(c, a)
                num = from_dec(dec, b)

        print(num)
