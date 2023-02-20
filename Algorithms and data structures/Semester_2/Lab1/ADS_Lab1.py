import timeit
import time

def simple_nums(num): # поиск простых чисел
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def naiv_finder(string, shablon):
    count = 0
    for i in range(0, len(string)-len(shablon)+1): # проход по индексам строки от 0 до длины минус шаблон
        s = string[i:i+len(shablon):] # отрезок строки
        if shablon == string[i:i+len(shablon):]: # проверка совпадения строки с шаблоном
            count += 1
    return count

def finder_rabina_karpa(string, shablon):
    count = 0
    def hash_finder(power_string, shablon): # высчитывание хеша подстроки
        Hash = 0
        for i in range(len(shablon)): # сумма всех элементов
            Hash += int(shablon[i]) * len(power_string) ** (len(shablon) - i - 1) # элементы длины строки
        return Hash
    power_string = list(sorted(set(string)))
    shablon_hash = hash_finder(power_string, shablon) # хеш шаблона
    for i in range(0, len(string) - len(shablon) + 1):
        step_hash = hash_finder(power_string, string[i:i + len(shablon):]) # хеш подстроки
        if step_hash == shablon_hash:
            count += 1
    return count

def finder_boira_muera(string, shablon):
    def if_find(shablon, shablon_strok): # проверка шаблона и подстроки по буквам от конца в начало (до первого отрицания)
        for i in range(len(shablon)-1, -1, -1):
            if shablon[i] != shablon_strok[i]:
                return False
        return True

    step = len(shablon) # начальное значение конца подстроки
    count = 0 # счётчик строк
    while step <= len(string):
        if if_find(shablon, string[step-len(shablon):step:]): # если строки совпадают, подстрока двигается на 1 вправо
            count += 1
            step += 1
        else: # если строка не совпадает, то начинается поиск последнего символа подстроки в шаблоне
            new_step = 0 # временный счётчик
            for i in range(len(shablon)-2, -1, -1):
                if string[step - 1] == shablon[i]: # если символ найден, шабблон двигается до совпадающих символов
                    new_step = (len(shablon) - i) - 1
                    break
                else: # если символ не найден, шаблон двигается за последний символ подстроки
                    new_step += 1
            step += new_step # обновление движения
            if len(shablon) == 1: # Для значений с шаблоном 1 (Так как new_step всегда остаётся 0)
                step += 1
    return count

def prefix_func(string): #Префикс-функция
    mass = [0] # итоговый массив значений
    for i in range(2, len(string)+1): # проход по всем префиксам строки
        counter = 0 # итоговое значение для текущего префикса
        string_prefix = string[0:i:] # текущий префикс
        for j in range(1, i): # проход по всем префиксам, суффискам текущего префикса строки
            pre_prefix = string[0:j:] # текущий префикс текущего префикса строки
            pre_suffix = string[len(string_prefix)-j:len(string_prefix):] # текущий суфикс текущего префикса строки
            if pre_suffix == pre_prefix: # проверка эевиваленции
                counter = len(pre_prefix) # обновление итогового значения
        mass.append(counter)
    return mass

def finder_kunta_morrisa_pratta(string, shablon):
    prefix_shablon = prefix_func(shablon) # нахождение префикс-функции для шаблона
    step = 0
    count = 0
    while step + len(shablon) <= len(string): # проход по всей строке
        new_step = 1
        for i in range(len(shablon)): # проход по символам подстроки
            if shablon[i] == string[i + step]: # сравнение с шаблоном
                new_step += 1
            else: # если нет, то отнятие индекса префикс-функции по формуле
                new_step -= prefix_shablon[i]
                break
        if new_step - 1 == len(shablon): # опредлеление совпадения с шаблоном
            new_step = 1
            count += 1
        step += new_step
    return count



mass = [i for i in range(2, 500) if simple_nums(i)] # массив простых чисел

string = "".join(map(str, mass)) # строка простых чисел

shablon = str(input("Введите искомую строку: "))

print(naiv_finder(string, shablon))
print(finder_rabina_karpa(string, shablon))
print(finder_boira_muera(string, shablon))
print(finder_kunta_morrisa_pratta(string, shablon), "По формуле")

slovar = {}

maxi, maxi_count = 0, 0

for i in range(10, 100): # поиск количества i (двухзначных чисел) в строке string
    slovar[i] = naiv_finder(string, str(i))
    if maxi < int(slovar[i]):
        maxi_count = 1
        maxi = int(slovar[i])
    elif maxi == int(slovar[i]):
        maxi_count += 1

print(maxi, maxi_count) # максимальное число повторений, количество максимальных повторений

print(slovar)
def comprasion():
    t0 = time.perf_counter()

    for i in range(100):
        naiv_finder(string, shablon)
    t1 = time.perf_counter()
    print('%.8f sec naive' % ((t1-t0)/100))

    t0 = time.perf_counter()

    for i in range(100):
        finder_rabina_karpa(string, shablon)
    t1 = time.perf_counter()
    print('%.8f sec hash karp' % ((t1-t0)/100))

    t0 = time.perf_counter()

    for i in range(100):
        finder_boira_muera(string, shablon)
    t1 = time.perf_counter()
    print('%.8f sec mur' % ((t1-t0)/100))

    t0 = time.perf_counter()

    for i in range(100):
        finder_kunta_morrisa_pratta(string, shablon)
    t1 = time.perf_counter()
    print('%.8f sec morrisa pratta' % ((t1-t0)/100))

comprasion()

