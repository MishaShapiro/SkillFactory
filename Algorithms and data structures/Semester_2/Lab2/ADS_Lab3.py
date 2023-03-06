def umnojenie(mass: str, consta: float) -> list:
    res = []
    mass = [ord(i) for i in mass]
    for key in mass:
        res.append(int(len(mass) * ((key * consta) % 1)))
    return sum(res)

print("Умножение:")
string = "string"
print(string)
print("Хеш-код: ", umnojenie(string, 0.1))
string = "strige"
print(string)
print("Хеш-код: ", umnojenie(string, 0.1))

import math

'''Binary logic for md5 '''
F = lambda x, y, z: (x & y) | (~ x & z)
G = lambda x, y, z: (x & z) | (~ z & y)
H = lambda x, y, z: x ^ y ^ z
I = lambda x, y, z: y ^ (~ z | x)
'''end of binary logic for md 5'''

def func(x, y, z, i):
    if i == 0:
        return F(x, y, z)
    elif i == 1:
        return G(x, y, z)
    elif i == 2:
        return H(x, y, z)
    else:
        return I(x, y, z)

def copy_to_dict(dict_1):
    res = {}
    for i in dict_1.keys():
        res[i] = dict_1[i]
    return res

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):  # Перевод текста в биты
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def get64bit(num: int) -> str:  # Превращает длину исходной строки в 64 битное представление
    binary = bin(num)[2::]
    if len(binary) > 64:  # если в строке больше 2**64, то берутся только 64 младших бита
        binary = binary[len(binary) - 64::]
    else:
        while len(binary) < 64:
            binary = "0" + binary
        binary = binary[32::] + binary[:32:] # байты меняются по условию
    return binary

def step1(string):
    global len_string
    string = text_to_bits(string)
    len_string = len(string)
    res = "1"
    while len(res + string) % 512 != 448:
        res += "0"
    res += string
    return res


def step2(string):
    string += get64bit(len_string)
    return string


def step3():
    def inicialisation(values):
        res = ""
        for i in values:
            temp = bin(int(i, 16))[2::]
            res += "0" * (4 - len(temp)) + temp
        return res

    dict_1 = {"A": "01234567", "B": "89ABCDEF", "C": "FEDCBA98", "D": "76543210"}

    for i in dict_1.keys():
        dict_1[i] = inicialisation(dict_1[i])

    return dict_1

def step4(string, dict_1):
    T = [int(2 ** 32 * abs(math.sin(i + 1))) for i in range(64)]
    for block in range(len(string)//512):
        dict_2 = copy_to_dict(dict_1)
        X = []
        for round in range(0, 512, 32):
            X.append(string[(512*block) + round:(512*block) + round+32:])
        i_shum = 0
        for i in range(4):
            for k in range(len(X)):
                a, b, c, d = dict_2["A"][::], dict_2["B"][::], dict_2["C"][::], dict_2["D"][::]
                temp_bin = bin(int(b, 2) + (int(a, 2) + func(int(b, 2), int(c, 2), int(d, 2), i) + int(X[k], 2) + T[i_shum]))[2::]
                dict_2["B"] = temp_bin[len(temp_bin)-32:len(temp_bin):]
                dict_2["C"] = b
                dict_2["D"] = c
                dict_2["A"] = d
                i_shum += 1
        for i in dict_1.keys():
            dict_1[i] = bin(int(dict_1[i], 2) + int(dict_2[i], 2))[2:32:]
    return dict_1

string = "qwerty"
print(string)
string = step1(string)
string = step2(string)
dict_1 = step3()
dict_1 = step4(string, dict_1)
for i in dict_1.keys():
    print(hex(int(dict_1[i], 2))[2::].upper(), end="")
print("")

string = "qwerti"
print(string)
string = step1(string)
string = step2(string)
dict_1 = step3()
dict_1 = step4(string, dict_1)
for i in dict_1.keys():
    print(hex(int(dict_1[i], 2))[2::].upper(), end="")
print("")
