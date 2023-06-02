#Задание 1

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(root):
    result = []
    if root is None:
        return result

    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        # Добавляем детей текущего узла в стек в обратном порядке,
        # чтобы обеспечить правильный порядок обхода
        stack.extend(node.children[::-1])

    return result

#Задание 2

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def find_lca(root, node1, node2):
    if root is None or node1 is None or node2 is None:
        return None

    if root == node1 or root == node2:
        return root

    found_nodes = 0
    lca = None

    for child in root.children:
        child_lca = find_lca(child, node1, node2)
        if child_lca is not None:
            found_nodes += 1
            if found_nodes == 1:
                lca = child_lca
            elif found_nodes == 2:
                return root

    if found_nodes == 1:
        return lca

    return None

#Задание 3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root, sorted_list):
    if root is None:
        return

    inorder_traversal(root.left, sorted_list)
    sorted_list.append(root.value)
    inorder_traversal(root.right, sorted_list)

def update_tree(root, sorted_list):
    if root is None:
        return

    update_tree(root.left, sorted_list)
    root.value = sorted_list.pop(0)
    update_tree(root.right, sorted_list)

def sort_tree(root):
    if root is None:
        return

    sorted_list = []
    inorder_traversal(root, sorted_list)
    sorted_list.sort()
    update_tree(root, sorted_list)

#пример
# Создаем дерево
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Сортируем дерево
sort_tree(root)

# Проверяем отсортированность
def inorder_traversal(root):
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.value, end=' ')
    inorder_traversal(root.right)

inorder_traversal(root)


#Задание 4

def dfs(graph, vertex, visited, component):
    visited[vertex] = True
    component.append(vertex)

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def find_connected_components(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    components = []

    for vertex in range(num_vertices):
        if not visited[vertex]:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)

    return components

#пример

# Граф задан списком ребер
edges = [(0, 1), (0, 2), (1, 2), (3, 4)]

# Создаем граф в виде списка смежности
num_vertices = max(max(edge) for edge in edges) + 1
graph = [[] for _ in range(num_vertices)]

for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)

# Находим связные компоненты
components = find_connected_components(graph)

# Выводим результат
for component in components:
    print(component)

#Задание 5

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances




