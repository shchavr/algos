from assignment_problem import AssignmentProblem
from utils import print_matrix

def main():
    print("=" * 60)
    print("Лабораторная работа №11: Задача о назначениях")
    print("Переборный комбинаторный алгоритм")
    print("=" * 60)

    cost_matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]

    print("\nИсходные данные:")
    print("Матрица стоимостей:")
    print_matrix(cost_matrix)

    problem = AssignmentProblem(cost_matrix)
    min_cost, best_assignment = problem.solve()

    print("\nРезультаты решения:")
    print("-" * 60)
    print(f"Минимальная суммарная стоимость назначений: {min_cost}")
    print("\nОптимальное назначение:")
    for worker, task in enumerate(best_assignment):
        print(f"  Работник {worker+1} назначается на задачу {task+1}")

    print("-" * 60)
    print("Конец работы.")

if __name__ == "__main__":
    main()
