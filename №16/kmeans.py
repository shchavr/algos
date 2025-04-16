import random
from point import Point
from utils import calculate_mean_point

class KMeans:
    """
    Реализует алгоритм K-средних.
    """
    def __init__(self, points, k):
        """
        Конструктор.

        Args:
            points: Список точек для кластеризации (Point объекты).
            k: Количество кластеров.
        """
        self.points = points
        self.k = k
        self.centroids = self.initialize_centroids()
        self.clusters = {}

    def initialize_centroids(self):
        """
        Инициализирует центроиды случайным образом, выбирая k случайных точек из набора данных.
        """
        return random.sample(self.points, self.k)

    def assign_points_to_clusters(self):
        """
        Назначает каждую точку ближайшему центроиду.
        """
        self.clusters = {i: [] for i in range(self.k)} # Очищаем кластеры на каждой итерации

        for point in self.points:
            closest_centroid_index = self.find_closest_centroid(point)
            self.clusters[closest_centroid_index].append(point)

    def find_closest_centroid(self, point):
        """
        Находит индекс ближайшего центроида к данной точке.
        """
        min_distance = float('inf')
        closest_centroid_index = -1

        for i, centroid in enumerate(self.centroids):
            distance = point.distance_to(centroid)
            if distance < min_distance:
                min_distance = distance
                closest_centroid_index = i

        return closest_centroid_index

    def update_centroids(self):
        """
        Пересчитывает центроиды как среднее значение точек в каждом кластере.
        """
        for i in range(self.k):
            if self.clusters[i]:  # Обработка случая пустого кластера
                self.centroids[i] = calculate_mean_point(self.clusters[i])
            else:
                # Если кластер пустой, перемещаем центроид в случайную точку
                self.centroids[i] = random.choice(self.points)  # Или можно сгенерировать новую случайную точку

    def run(self, max_iterations=100):
        """
        Запускает алгоритм K-средних.

        Args:
            max_iterations: Максимальное количество итераций.
        """
        for _ in range(max_iterations):
            old_centroids = [Point(c.x, c.y) for c in self.centroids] # Создаем копию центроидов для сравнения
            self.assign_points_to_clusters()
            self.update_centroids()

            # Проверка сходимости:  Если центроиды не изменились, алгоритм сошелся.
            if all(self.centroids[i].distance_to(old_centroids[i]) == 0 for i in range(self.k)):
                print("Алгоритм сошелся!")
                break
        else:
            print("Алгоритм не сошелся после {} итераций.".format(max_iterations))

    def get_clusters(self):
        """
        Возвращает кластеры.
        """
        return self.clusters

    def get_centroids(self):
        """
        Возвращает центроиды.
        """
        return self.centroids
