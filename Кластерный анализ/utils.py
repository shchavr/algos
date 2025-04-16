from point import Point
import matplotlib.pyplot as plt  

def calculate_mean_point(points):
    """
    Вычисляет среднюю точку (центроид) для списка точек.
    """
    if not points:
        return None 

    x_sum = sum(point.x for point in points)
    y_sum = sum(point.y for point in points)
    return Point(x_sum / len(points), y_sum / len(points))


def visualize_clusters_matplotlib(clusters, centroids, filename="clusters.png"):
    """
    Визуализирует кластеры с помощью matplotlib.
    """
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'cyan']  

    plt.figure(figsize=(8, 6)) 

    for i, cluster in clusters.items():
        color = colors[i % len(colors)]
        x = [point.x for point in cluster]
        y = [point.y for point in cluster]
        plt.scatter(x, y, color=color, label=f"Кластер {i+1}")  # точки кластера

    centroid_x = [centroid.x for centroid in centroids]
    centroid_y = [centroid.y for centroid in centroids]
    plt.scatter(centroid_x, centroid_y, marker='x', s=100, color='black', label="Центроиды")  # центроиды крестиками

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Кластеризация методом K-средних")
    plt.legend()  
    plt.grid(True)  
    plt.savefig(filename)
    plt.show() 
    print(f"Изображение сохранено в {filename}")
