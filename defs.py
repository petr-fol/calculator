
def from_dec(a_str, b) -> str:
    """
    :param a_str: число в 10 системе
    :param b: система исчисления в которую мы переводим число
    :return: str new_num
    """
    new_num_list = []
    # oct_notation = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    a = int(a_str)
    while a > 0:
        ost = a % b
        new_num_list.append(str(ost))
        num = a // b
        print(f"{a} / {b} = {num}  {ost}")
        a = num
    if b >= 11:
        for i, char in enumerate(new_num_list):
            char_int = int(char)
            if char_int >= 10:
                new_num_list[i] = chr(char_int + 55)

    new_num = ''.join(new_num_list)
    new_num = new_num[::-1]
    return new_num

def in_dec(n, b) -> int:
    """
    n = число переводимое в 10 систему
    b = основание системы
    :return: int в десятичной системе
    сейчас функция не правильно преобразовывает 2 систему в другие
    """
    n_str = str(n)
    result = 0

    # преобразовываем в десятичное число
    for i, char in enumerate(reversed(n_str)):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char.upper()) - 55 # преобразовываем букву в число А = 10 и тд
        if value >= b:
            raise ValueError(f"цифра {char} не может быть в системе с основанием {b}")
        result += value * (b ** i)
        print(f"{result} = {value} * {b}^{i}")
    return result

def translator():
    print("для выхода из переводчика введите 0")

    a = input("в какой системе счисления ваше число?\n")
    if a.isdigit():
        a = int(a)
        if a == 0:
            return
    else: return

    b = input("в какую систему счисления перевести?\n")
    if b.isdigit():
        b = int(b)
        if b == 0:
            return
    else: return
    c = input("ваше число?\n")
    if c.isdigit():
        c = int(c)
        if c == 0:
            return
    else: return


    if a <= 36 and b <= 36:
        dec = c
        if a != 10:
            dec = in_dec(c, a)
        num = from_dec(dec, b)

    else:
        print("вы ввели систему счисления > 36, могут быть ошибки в вычислениях изза ограничений алфавита")

        dec = in_dec(c, a)
        num = from_dec(dec, b)

        return num

    return num

def calculator():
    a = input("в какой системе счисления первое число?\n")
    if a.isdigit():
        a = int(a)
        if a == 0:
            return
    else:
        return

    b = input("в какой системе счисления второе число?\n")
    if b.isdigit():
        b = int(b)
        if b == 0:
            return
    else:
        return

    c = input("первое число?\n")
    if c.isdigit():
        c = int(c)
        if c == 0:
            return
    else:
        return

    d = input("второе число?\n")
    if d.isdigit():
        d = int(d)
        if d == 0:
            return
    else:
        return

    e = input("в какой системе счисления вывести число?\n")
    if e.isdigit():
        e = int(e)
        if e == 0:
            return
    else:
        return
    print("выберите действие для чисел: + - * /")
    operation = input()
    first = in_dec(c, a)
    second = in_dec(d, b)
    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        result = first / second
    else: return

    result = from_dec(result, e)
    return result

