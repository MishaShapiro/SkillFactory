pit = [(4, 4), (7, 6), (1, 7)]

def remover(res):
    global pit
    res_1 = res[::]
    for i in res:
        if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
            res_1.remove(i)
        if i in pit:
            res_1.remove(i)
    return res_1

def finder_boira_muera(string, shablon):
    def if_find(shablon, shablon_strok): # проверка шаблона и подстроки по буквам от конца в начало (до первого отрицания)
        for i in range(len(shablon)-1, -1, -1):
            if shablon[i] != shablon_strok[i]:
                return False
        return True

    step = len(shablon) # начальное значение конца подстроки
    count = 0 # счётчик строк
    znach = ""
    while step <= len(string):
        if if_find(shablon, string[step-len(shablon):step:]): # если строки совпадают, подстрока двигается на 1 вправо
            count += 1
            step += 1
            znach += shablon
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
    return znach

def King_move(x, y):
    res = [(x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]
    res = remover(res)
    return res

def Peshka_move(x, y):
    res = remover([(x, y + 1)])
    return res

def Eleph_move(x, y):
    res1 = []
    res2 = []
    for i in range(-7, 8):
        if 0 <= x + i <= 7 and 0 <= y + i <= 7 and i != 0:
            res1.append((x + i, y + i))
            if i < 0 and (x + i, y + i) in pit:
                res1 = []
            if i > 0 and (x + i, y + i) in pit:
                break
    for i in range(-7, 8):
        if 0 <= x + i <= 7 and 0 <= y - i <= 7 and i != 0:
            res2.append((x + i, y - i))
            if i < 0 and (x + i, y - i) in pit:
                res2 = []
            if i > 0 and (x + i, y - i) in pit:
                break

    return remover(res1 + res2)

def Ladia_move(x, y):
    res1 = []
    res2 = []
    for i in range(-7, 8):
        if 0 <= x + i <= 7 and i != 0:
            res1.append((x + i, y))
        if i < 0 and (x + i, y) in pit:
            res1 = []
        if i > 0 and (x + i, y) in pit:
            break
    for i in range(-7, 8):
        if 0 <= y + i <= 7 and i != 0:
            res2.append((x, y + i))
        if i < 0 and (x, y + i) in pit:
            res2 = []
        if i > 0 and (x, y + i) in pit:
            break

    return remover(res1+res2)

def Ferz_move(x ,y):
    return Ladia_move(x, y) + Eleph_move(x, y)

def Knight_move(x, y):
    res = [(x + 1, y + 2), (x + 2, y + 1), (x + 1, y - 2), (x + 2, y - 1), (x - 1, y + 2), (x - 2, y + 1), (x - 1, y - 2), (x - 2, y - 1)]
    return remover(res)

def Figure_move(x, y, name):
    if name == 1:
        res = King_move(x, y)
    elif name == 2:
        res = Ferz_move(x, y)
    elif name == 3:
        res = Eleph_move(x, y)
    elif name == 4:
        res = Ladia_move(x, y)
    elif name == 5:
        res = Knight_move(x, y)
    elif name == 6:
        res = Peshka_move(x, y)
    return res

def figure_way(x1, y1, x2, y2, name):
    step = {}
    parents = {}
    step_i = 0
    while True:
        if step_i == 0:
            step[step_i] = Figure_move(x1, y1, name)
            parents[(x1, y1)] = step[step_i]
        else:
            for i in step[step_i - 1]:
                res = Figure_move(i[0], i[1], name)
                if not (step_i in step.keys()):
                    step[step_i] = res
                else:
                    step[step_i] += res
                parents[i] = res[::]
        if (x2, y2) in step[step_i]:
            break
        step_i += 1

    final_way = [(x2, y2)]

    while final_way[0] != (x1, y1):
        for i in parents.keys():
            k = parents[i]
            if (x2, y2) in parents[i]:
                final_way = [i] + final_way
                x2, y2 = i[0], i[1]
                break
    return final_way

print("1 Король, 2 Ферзь, 3 Слон, 4 Ладья, 5 Конь, 6 Пешка")

# name1 = int(input("Выберите фигуру 1: "))
# name2 = int(input("Выберите фигуру 2: "))
# x1, y1 = map(int, input("Введите начало для первой фигуры: ").split())
# x2, y2 = map(int, input("Введите конец для первой фигуры: ").split())
# x1_2, y1_2 = map(int, input("Введите начало для первой фигуры: ").split())
# x2_2, y2_2 = map(int, input("Введите конец для первой фигуры: ").split())

name1, name2 = 2, 2

x1, y1 = 0, 0
x2, y2 = 7, 7

x1_2, y1_2 = 1, 1
x2_2, y2_2 = 7, 7

way1 = figure_way(x1, y1, x2, y2, name1)
way2 = figure_way(x1_2, y1_2, x2_2, y2_2, name2)

print("Весь путь фигуры: ", way1)
print("Весь путь фигуры: ", way2)
k = ""
for i in way1:
    k += finder_boira_muera(str(way2), str(i))
print("Совпадают пути в:", k)

