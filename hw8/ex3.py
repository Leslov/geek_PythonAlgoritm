# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import sample


def generate_graph(n):
    letters = [chr(x) for x in range(ord('A'), ord('Z'))][:n]
    if n > len(letters):
        raise Exception(f'Число вершин для генерации графа не может быть больше, чем {len(letters)}')
    graph = {}
    for i in range(n):
        new_node = letters[i]
        graph[new_node] = set()
    for key in graph.keys():
        i = letters.index(key)
        vals = letters[i - 1:i]
        for val in vals:
            graph[val].add(key)
            graph[key].add(val)

    return graph


def checkout_graph(graph, node_name, checked_nodes=[]):
    for node in graph[node_name]:
        if node not in checked_nodes:
            checked_nodes.append(node)
            checkout_graph(graph, node, checked_nodes)


graph = generate_graph(10)
print(graph)
checked_nodes = []
checkout_graph(graph, 'A', checked_nodes)
print(checked_nodes)
