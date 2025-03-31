from math import factorial as f
def get_var(text) -> int:
    a = input(text)
    if a.isdigit():
        a = int(a)
        return a
    else:
        return 0

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
    a = get_var("в какой системе счисления ваше число?\n")
    b = get_var("в какую систему счисления перевести?\n")
    c = get_var("ваше число?\n")


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
    a = get_var("в какой системе счисления первое число?\n")
    b = get_var("в какой системе счисления второе число?\n")
    c = get_var("первое число?\n")
    d = get_var("второе число?\n")
    e = get_var("в какой системе счисления вывести число?\n")
    
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

def count_combination():
    n = get_var("общее количество\n")
    k = get_var("количество для одного варианта комбинаций\n")
    result = int(f(n)/(f(k)*f((n-k))))
    return result
