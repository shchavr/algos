import random
from point import Point
from kmeans import KMeans
from utils import visualize_clusters_matplotlib  

def main():
    print("=" * 60)
    print("Лабораторная работа №16: Кластерный анализ методом K-средних")
    print("Реализация алгоритма K-средних")
    print("=" * 60)

    # Генерация случайных точек
    num_points = 30
    points = [Point(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_points)]

    k = 3

    kmeans = KMeans(points, k)
    kmeans.run() 

    # результаты
    clusters = kmeans.get_clusters()
    centroids = kmeans.get_centroids()

    print("\nРезультаты кластеризации:")
    print("-" * 60)
    for i, cluster in clusters.items():
        print(f"Кластер {i+1}:")
        print(f"  Центроид: {centroids[i]}")
        print(f"  Точки: {cluster}")
        print("-" * 60)

    print("\nВизуализация кластеров на изображении:")
    visualize_clusters_matplotlib(clusters, centroids, "clusters.png") 

    print("=" * 60)
    print("Конец работы.")


if __name__ == "__main__":
    main()
