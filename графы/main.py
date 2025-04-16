from graph import Graph
from bron_kerbosch import bron_kerbosch
from input_output import read_graph_from_file, input_graph_manually, generate_random_graph, print_clique
from visualization import visualize_graph


def main():
    """
    Основная функция программы.
    """
    while True:
        print("\nВыберите способ ввода данных:")
        print("1. Ввести граф вручную")
        print("2. Загрузить граф из файла Graph.txt")
        print("3. Сгенерировать случайный граф")
        print("4. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            graph = input_graph_manually()
        elif choice == "2":
            graph = read_graph_from_file()
        elif choice == "3":
            try:
                num_vertices = int(input("Введите количество вершин: "))
                num_edges = int(input("Введите количество рёбер: "))
                graph = generate_random_graph(num_vertices, num_edges)
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите целые числа.")
                graph = None
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте ещё раз.")
            continue

        if graph:
            print("Граф:")
            print(graph)
            clique = bron_kerbosch(graph)
            print_clique(clique)
            visualize_graph(graph, clique)


if __name__ == "__main__":
    main()
