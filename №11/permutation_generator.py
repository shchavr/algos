def generate_permutations(elements):
    """
    Генерирует все перестановки заданного множества элементов.
    Реализовано рекурсивно.
    """
    if len(elements) == 0:
        return [[]]  # Пустое множество имеет одну перестановку - пустой список

    permutations = []
    for i in range(len(elements)):
        first_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        sub_permutations = generate_permutations(remaining_elements)

        for sub_permutation in sub_permutations:
            permutations.append([first_element] + sub_permutation)

    return permutations
