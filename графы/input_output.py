from graph import Graph
import random
    

def read_graph_from_file(filename="Graph.txt"):
    """
    Читает граф из файла.
    """
    try:
        with open(filename, "r") as f:
            num_vertices = int(f.readline().strip())
            num_edges = int(f.readline().strip())
            graph = Graph(num_vertices)
            for _ in range(num_edges):
                u, v = map(int, f.readline().strip().split())
                graph.add_edge(u, v)
            return graph
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None
    except ValueError:
        print(f"Ошибка в формате файла {filename}.")
        return None


def input_graph_manually():
    """
    Вводит граф вручную.
    """
    try:
        num_vertices = int(input("Введите количество вершин: "))
        num_edges = int(input("Введите количество рёбер: "))
        graph = Graph(num_vertices)
        print("Введите рёбра (каждое в отдельной строке, например, '0 1'):")
        for _ in range(num_edges):
            u, v = map(int, input().split())
            graph.add_edge(u, v)
        return graph
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целые числа.")
        return None

def generate_random_graph(num_vertices, num_edges):
    """
    Генерирует случайный граф.
    """
    if num_edges > num_vertices * (num_vertices - 1) // 2:
        print("Слишком много рёбер для данного количества вершин.")
        return None

    graph = Graph(num_vertices)
    edges_added = 0
    while edges_added < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v and v not in graph.get_neighbors(u):  # Проверяем, что ребра нет
            graph.add_edge(u, v)
            edges_added += 1
    return graph

def print_clique(clique):
    """
    Выводит клику.
    """
    print("Максимальная клика:", clique)
