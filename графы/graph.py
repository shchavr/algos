class Graph:
    """
    Представление графа в виде списка смежности.
    """

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        """
        Добавляет ребро в граф.
        """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Граф неориентированный

    def get_neighbors(self, vertex):
        """
        Возвращает список соседей вершины.
        """
        return self.adj_list[vertex]

    def __str__(self):
        """
        Возвращает строковое представление графа.
        """
        s = ""
        for i in range(self.num_vertices):
            s += f"{i}: {self.adj_list[i]}\n"
        return s
