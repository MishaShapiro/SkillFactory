def Thief(N,M,K,items):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_weight = 0
    total_value = 0
    # пробуем взять каждый предмет в порядке убывания ценности
    for i in range(N):
        # если вес всех взятых предметов превысил M*K, то выходим из цикла
        if total_weight >= M * K:
            break
        # если вес текущего предмета не превышает K и его можно взять,
        # то добавляем его к списку взятых предметов и обновляем суммарный вес и ценность
        if items[i][0] <= K and total_weight + items[i][0] <= M * K:
            total_weight += items[i][0]
            total_value += items[i][1]
    return total_value
items = [(3, 5), (7, 9), (2, 3), (4, 6), (6, 8)]
print(Thief(5,4,6,items))