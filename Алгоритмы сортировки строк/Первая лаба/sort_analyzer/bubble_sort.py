def bubble_sort(arr):
    """Пузырьковая сортировка."""
    
    # Инициализация счетчика сравнений
    comparisons = 0
    
    # Получаем длину входного массива
    n = len(arr)
    
    # Внешний цикл: проходим по всем элементам массива
    for i in range(n):
        # Внутренний цикл: сравниваем соседние элементы
        for j in range(0, n - i - 1):
            # Увеличиваем счетчик сравнений
            comparisons += 1
            
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Возвращаем отсортированный массив и количество сравнений
    return arr, comparisons
