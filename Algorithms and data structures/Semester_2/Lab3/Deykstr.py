def matrix(string):
    mass = [-1 for i in range(11)]
    for i in string:
        mass[int(i.split(":")[0])-1] = int(i.split(":")[1])
    return mass

files = open("USA_States.txt")
mass = files.read().split("\n")
mass1 = []
for i in mass:
    mass1.append([i.split(" ")[0], i.split(" ")[1], i.split(" ")[2::]])

graph_matrix = []
for i in range(11):
    graph_matrix.append(matrix(mass1[i][2]))

d = {i: 9999 for i in range(len(graph_matrix))}
d[0] = 0

tree = [0]

while True:
    visited = {}
    for i in range(len(graph_matrix)):
        if i not in tree and graph_matrix[i][tree[-1]] != -1:
            d[i] = min(d[i], d[tree[-1]] + graph_matrix[i][tree[-1]])
            visited[i] = d[i]
    if len(visited) == 0:
        break
    tree.append(min(visited.keys()))

print(d)
