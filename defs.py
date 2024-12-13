
def from_dec(a_str, b):
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

def in_dec(n, b):
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
    return result
