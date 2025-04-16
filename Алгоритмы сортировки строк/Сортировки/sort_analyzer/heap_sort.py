def heap_sort(arr):
    """Пирамидальная сортировка с итеративным heapify и линейным построением кучи."""
    comparisons = 0  # Счетчик сравнений
    n = len(arr)  # Длина входного массива

    def sift_down(arr, start, end):
        """Итеративный heapify (sift-down)."""
        nonlocal comparisons  # Используем внешнюю переменную для подсчета сравнений
        root = start  # Начинаем с корня поддерева
        while True:
            child = 2 * root + 1  # Индекс левого ребенка
            if child > end:  # Если нет детей, выходим из цикла
                break
            
            # Если правый ребенок существует и больше левого
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1  # Переходим к правому ребенку
            
            comparisons += 1  # Увеличиваем счетчик сравнений
            
            # Если корень меньше дочернего элемента, меняем их местами
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child  # Переходим к следующему уровню
                
            else:
                break  # Если корень больше или равен дочернему, выходим

    # Строим кучу 
    for start in range(n // 2 - 1, -1, -1):
        sift_down(arr, start, n - 1)

    # Извлекаем элементы из кучи и сортируем
    for end in range(n - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]  # Перемещаем корень в конец
        sift_down(arr, 0, end - 1)  # Восстанавливаем кучу

    return arr, comparisons  # Возвращаем отсортированный массив и количество сравнений


