# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start, finish):
    real_start = start
    real_finish = finish
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    path = [real_finish]

    if real_start == real_finish:
        path = [real_start]
    else:
        while True:
            finish = parent[finish]
            if finish == -1:
                path = f'No path'
                break
            if real_start == finish:
                path.append(real_start)
                path.reverse()
                break
            path.append(finish)
    return f'From {real_start} to {real_finish}. Path: "{path}", cost: {cost[real_finish]}'


st = int(input('Старт (0-7): '))
fin = int(input('Финиш (0-7): '))
if 0 <= st < 8 and 0 <= fin < 8:
    print(dijkstra(g, st, fin))
else:
    print('Некорректный ввод')
