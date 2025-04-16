import matplotlib.pyplot as plt
import math

def visualize_graph(graph, clique, filename="graph.png"):
    """
    Визуализирует граф и выделяет максимальную клику
    """

    num_vertices = graph.num_vertices
    # Определяем координаты вершин по кругу
    positions = {}
    for i in range(num_vertices):
        angle = 2 * math.pi * i / num_vertices
        x = math.cos(angle)
        y = math.sin(angle)
        positions[i] = (x, y)

    plt.figure(figsize=(8, 8))
    plt.axis('off')  # Убираем оси

    # Рисуем ребра
    for u in range(num_vertices):
        for v in graph.get_neighbors(u):
            if u < v:  # Чтобы не рисовать ребро дважды
                x1, y1 = positions[u]
                x2, y2 = positions[v]
                if u in clique and v in clique:
                    plt.plot([x1, x2], [y1, y2], color='red', linewidth=2)  # Ребро клики
                else:
                    plt.plot([x1, x2], [y1, y2], color='skyblue', linewidth=1)  # Обычное ребро

    # Рисуем вершины
    for i in range(num_vertices):
        x, y = positions[i]
        if i in clique:
            plt.plot(x, y, 'ro', markersize=15)  # Вершина клики
        else:
            plt.plot(x, y, 'bo', markersize=10, color = 'skyblue') # Обычная вершина
        plt.text(x, y, str(i), ha='center', va='center', fontsize=12, color='black') # Подпись вершины

    plt.savefig(filename)
    plt.show()