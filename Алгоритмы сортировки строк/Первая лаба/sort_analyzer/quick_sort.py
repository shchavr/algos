# def insertion_sort(arr, low, high):
#     """Сортировка вставками для малых подмассивов."""
#     comparisons = 0
#     for i in range(low + 1, high + 1):
#         key = arr[i]
#         j = i - 1
#         while j >= low and arr[j] > key:
#             comparisons += 1
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             j -= 1
#         if j >= low: # Final comparison that fails the `while` loop
#             comparisons += 1
#         arr[j + 1] = key
#     return comparisons


# def quick_sort(arr):
#     """Быстрая сортировка (итеративная) - с Insertion Sort и медианой из трех."""
#     comparisons = 0
#     n = len(arr)
#     if n <= 1:
#         return arr, comparisons

#     stack = [(0, n - 1)]  # Используем стек для имитации рекурсии
#     INSERTION_THRESHOLD = 10  # Порог для использования Insertion Sort

#     while stack:
#         low, high = stack.pop()

#         if low < high:
#             # Если размер подмассива мал, используем Insertion Sort
#             if high - low + 1 < INSERTION_THRESHOLD:
#                 comparisons += insertion_sort(arr, low, high) #Increment comparison
#                 continue

#             # Выбор опорного элемента: медиана из трех
#             mid = (low + high) // 2
#             if arr[low] > arr[mid]:
#                 arr[low], arr[mid] = arr[mid], arr[low]
#             if arr[low] > arr[high]:
#                 arr[low], arr[high] = arr[high], arr[low]
#             if arr[mid] > arr[high]:
#                 arr[mid], arr[high] = arr[high], arr[mid]

#             # Перемещаем опорный элемент (медиану) в конец
#             arr[mid], arr[high] = arr[high], arr[mid]


#             pi, comps = partition_optimized2(arr, low, high)  # Используем оптимизированный partition
#             comparisons += comps  # Обновляем счетчик comparisons

#             # Оптимизация: обрабатываем меньший подмассив первым
#             if (pi - low) < (high - pi):
#                 stack.append((pi + 1, high))
#                 stack.append((low, pi - 1))
#             else:
#                 stack.append((low, pi - 1))
#                 stack.append((pi + 1, high))

#     return arr, comparisons


# def partition_optimized2(arr, low, high):
#     """Разбиение массива (partition) - с учетом опорного элемента."""
#     i = (low - 1)
#     pivot = arr[high]
#     comparisons = 0  # Локальный счетчик сравнений для partition

#     j = low
#     while j < high:
#         comparisons += 1  # Увеличиваем счетчик сравнений
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#         j += 1

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1, comparisons  # Возвращаем pi и comparisons


def quick_sort(arr):
    """Быстрая сортировка (итеративная) - оптимизированная версия."""
    
    comparisons = 0 
    n = len(arr)  
    
    if n <= 1:  # Если массив пустой или содержит один элемент, он уже отсортирован
        return arr, comparisons  # Возвращаем массив и 0 сравнений

    stack = [(0, n - 1)]  # Инициализируем стек для хранения диапазонов (low, high)

    while stack:  
        low, high = stack.pop()  # Извлекаем последний диапазон для обработки

        if low < high:  # Проверяем, что есть более одного элемента для сортировки
            pi, comps = partition_optimized(arr, low, high)  # Получаем индекс опорного элемента и количество сравнений
            comparisons += comps  # Обновляем общий счетчик сравнений

            # Оптимизация: обрабатываем меньший подмассив первым для уменьшения использования стека
            if (pi - low) < (high - pi):
                stack.append((pi + 1, high))  # Сначала добавляем правую часть
                stack.append((low, pi - 1))  # Затем левую
            else:
                stack.append((low, pi - 1))  # Сначала добавляем левую часть
                stack.append((pi + 1, high))  # Затем правую

    return arr, comparisons 


def partition_optimized(arr, low, high):
    """Разбиение массива (partition)."""
    
    i = (low - 1)  # Индекс для меньшего элемента; начинается до low
    pivot = arr[high]  # Опорный элемент выбранный из правого конца массива
    comparisons = 0  # Локальный счетчик сравнений для partition

    j = low  # Инициализируем j, чтобы просмотреть массив с low до high
    
    while j < high:  
        comparisons += 1
        if arr[j] <= pivot:  # Если текущий элемент меньше или равен опорному
            i += 1  # Увеличиваем индекс для меньшего элемента
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы, чтобы отсортировать

        j += 1  # Переходим к следующему элементу

    # Меняем местами опорный элемент с первым элементом, который больше опорного
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons  # Возвращаем индекс опорного элемента и счетчик сравнений
