class All_money:

    def __init__(self, money):
        self.money = money
        self.sorted_cost= []
        self.sorted_money = []
        mass = [i.cost for i in self.money]
        self.sorted_cost = sorted(mass, reverse=True)
        for i in self.sorted_cost:
            for j in self.money:
                if i == j.cost:
                    self.sorted_money.append(j)

    def finder(self, task):
        res = {}
        if task > sum([i.cost * i.count for i in self.sorted_money]):
            print("Сликом большая сдача")
            return None
        else:
            for i in self.sorted_money:
                temp_count = 0
                while task >= i.cost and i.count > 0:
                    task -= i.cost
                    i.count -= 1
                    temp_count += 1
                res[i] = temp_count
                if task == 0:
                    for j in res.keys():
                        if res[j] != 0:
                            print("{0} монет {1} с номиналом {2}".format(res[j], j.get_money_name(), j.cost))
                    return None
        print("Невозможно дать сдачу")


class Money:

    def __init__(self, cost, count):
        self.cost = cost
        self.count = count

    def get_money_name(self):
        for k, v in globals().items():
            if v is self:
                return k
a, b = map(int, input("Ввдеите номинал монет и их количество через пробел: ").split(" "))
S1 = Money(a, b)
a, b = map(int, input("Ввдеите номинал монет и их количество через пробел: ").split(" "))
S2 = Money(a, b)
a, b = map(int, input("Ввдеите номинал монет и их количество через пробел: ").split(" "))
S3 = Money(a, b)
all_m = All_money([S1, S2, S3])
all_m.finder(int(input("Введите сумму, которую нужно выдать: ")))
