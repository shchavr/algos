from permutation_generator import generate_permutations
from utils import print_matrix

class AssignmentProblem:
    """
    Представляет задачу о назначениях.
    """
    def __init__(self, cost_matrix):
        """
        Конструктор.

        Args:
            cost_matrix: Матрица стоимостей (список списков). cost_matrix[i][j] 
            - стоимость назначения работника i на задачу j.
        """
        self.cost_matrix = cost_matrix
        self.num_workers = len(cost_matrix)
        self.num_tasks = len(cost_matrix[0]) if self.num_workers > 0 else 0
    
        if self.num_workers != self.num_tasks:
            raise ValueError("Матрица стоимостей должна быть квадратной (число работников должно быть равно числу задач).")

    def solve(self):
        """
        Решает задачу о назначениях с помощью переборного алгоритма.

        Returns:
            tuple: (минимальная стоимость, оптимальное назначение)
                   Оптимальное назначение - это список, где assignment[i] - задача, назначенная работнику i.
        """
        workers = list(range(self.num_workers)) # индексы работников 
        task_permutations = generate_permutations(workers) 

        min_cost = float('inf')  
        best_assignment = None

        for assignment in task_permutations:
            current_cost = 0 # стоимость 
            for worker, task in enumerate(assignment):
                current_cost += self.cost_matrix[worker][task]

            if current_cost < min_cost:
                min_cost = current_cost
                best_assignment = assignment

        return min_cost, best_assignment

    def calculate_cost(self, assignment):
        """
        Вычисляет стоимость заданного назначения.
        """
        cost = 0
        for worker, task in enumerate(assignment):
            cost += self.cost_matrix[worker][task]
        return cost


