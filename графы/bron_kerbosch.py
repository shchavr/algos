def bron_kerbosch(graph):
    """
    Алгоритм Брона-Кербоша для поиска максимальной клики.
    """
    def find_clique(R, P, X, max_clique):
        """
        Рекурсивная функция для поиска клик.
        """
        if not P and not X:
            if len(R) > len(max_clique[0]):
                max_clique[0] = R[:]  # обновляем

            return

        for v in P[:]:  # Создаем копию P для итерации
            find_clique(
                R + [v],
                [neighbor for neighbor in P if neighbor in graph.get_neighbors(v)],
                [neighbor for neighbor in X if neighbor in graph.get_neighbors(v)],
                max_clique
            )
            P.remove(v)  # Удаляем v из P
            X.append(v)

    max_clique = [[]]  # Используем список, чтобы можно было изменять изнутри рекурсии
    find_clique([], list(range(graph.num_vertices)), [], max_clique)
    return max_clique[0]
