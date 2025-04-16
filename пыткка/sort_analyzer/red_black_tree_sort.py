def red_black_tree_sort(arr):
    """Сортировка с использованием красно-черного дерева."""

    class Node:
        def __init__(self, data, color="RED"):
            self.data = data  # Данное значение узла
            self.color = color  # Цвет узла (по умолчанию красный)
            self.parent = None  # Родительский узел
            self.left = None  # Левый дочерний узел
            self.right = None  # Правый дочерний узел

    class RedBlackTree:
        def __init__(self):
            self.nil = Node(None, color="BLACK")  # "Нулевой" узел, используемый для замещения дочерних узлов
            self.root = self.nil  # Корень дерева инициализируется как "нулевой"

        def insert(self, data, comparisons):
            """Метод для вставки нового узла в красно-черное дерево."""
            node = Node(data)  # Создаем новый узел
            node.left = self.nil  # Устанавливаем левое дочернее пустое узел
            node.right = self.nil  # Устанавливаем правое дочернее пустое узел
            y = None  # Предыдущий узел
            x = self.root  # Начинаем с корня

            # Позиционируем новый узел на правильное место в дереве
            while x != self.nil:
                comparisons[0] += 1  # Увеличиваем счетчик сравнений
                y = x  # Сохраняем родителя текущего узла
                if node.data < x.data:
                    x = x.left  # Если новый узел меньше, переходим в левое поддерево
                else:
                    x = x.right  # Иначе — в правое поддерево

            node.parent = y  # Устанавливаем родителя для нового узла

            # Вставляем новый узел как дочерний
            if y is None:  # Если дерево было пустым
                self.root = node  # Новый узел становится корнем
            elif node.data < y.data:
                y.left = node  # Вставка в левую часть
            else:
                y.right = node  # Вставка в правую часть

            # Если новый узел - корень, окрашиваем его в черный
            if node.parent is None:
                node.color = "BLACK"
                return

            # Если родитель - корень, ничего не делаем
            if node.parent.parent is None:
                return

            # Коррегируем дерево после вставки
            self.fix_insert(node, comparisons)

        def fix_insert(self, k, comparisons):
            """Коррекция дерева после вставки для соблюдения свойств красно-черного дерева."""
            # Пока родитель узла красный, необходимо производить балансировку
            while k.parent is not None and k.parent.color == "RED":
                if k.parent == k.parent.parent.right:  # Если родитель - правый сын
                    u = k.parent.parent.left  # Дядя
                    if u.color == "RED":  # Если дядя красный
                        # Перекраска дяди и родителя в черный
                        k.parent.color = "BLACK"
                        u.color = "BLACK"
                        k.parent.parent.color = "RED"  # Красим дедушку в красный
                        k = k.parent.parent  # Поднимаемся к дедушке
                    else:
                        # Если узел - левый сын
                        if k == k.parent.left:
                            k = k.parent
                            self.right_rotate(k, comparisons)  # Правый поворот
                        k.parent.color = "BLACK"  # Перекрашиваем родителя в черный
                        k.parent.parent.color = "RED"  # Перекрашиваем дедушку в красный

                        self.left_rotate(k.parent.parent, comparisons)  # Левый поворот
                else:  # Если родитель - левый сын
                    u = k.parent.parent.right  # Дядя

                    if u.color == "RED":  # Если дядя красный
                        # Перекраска дяди и родителя в черный
                        k.parent.color = "BLACK"
                        u.color = "BLACK"
                        k.parent.parent.color = "RED"  # Красим дедушку в красный
                        k = k.parent.parent  # Поднимаемся к дедушке
                    else:
                        # Если узел - правый сын
                        if k == k.parent.right:
                            k = k.parent
                            self.left_rotate(k, comparisons)  # Левый поворот
                        k.parent.color = "BLACK"  # Перекрашиваем родителя в черный
                        k.parent.parent.color = "RED"  # Перекрашиваем дедушку в красный
                        self.right_rotate(k.parent.parent, comparisons)  # Правый поворот

                if k == self.root:  # Если мы вернулись на корень, выходим
                    break

            self.root.color = "BLACK"  # Устанавливаем цвет корня на черный

        def left_rotate(self, x, comparisons):
            """Левый поворот вокруг узла x."""
            y = x.right  # Сохраняем правого сына
            x.right = y.left  # Левый ребенок y становится правым ребенком x
            if y.left != self.nil:
                y.left.parent = x  # Обновляем родителя для левого ребенка y
                
            y.parent = x.parent  # Сохраняем родителя x
            if x.parent is None:  # Если x был корнем
                self.root = y  # y становится корнем
            elif x == x.parent.left:
                x.parent.left = y  # y становится левым ребенком
            else:
                x.parent.right = y  # y становится правым ребенком
            y.left = x  # x становится левым ребенком y
            x.parent = y  # Обновляем родителя для x

        def right_rotate(self, x, comparisons):
            """Правый поворот вокруг узла x."""
            y = x.left  # Сохраняем левого сына
            x.left = y.right  # Правый ребенок y становится левым ребенком x
            if y.right != self.nil:
                y.right.parent = x  # Обновляем родителя для правого ребенка y
                
            y.parent = x.parent  # Сохраняем родителя x
            if x.parent is None:  # Если x был корнем
                self.root = y  # y становится корнем
            elif x == x.parent.right:
                x.parent.right = y  # y становится правым ребенком
            else:
                x.parent.left = y  # y становится левым ребенком
            y.right = x  # x становится правым ребенком y
            x.parent = y  # Обновляем родителя для x

        def inorder_traversal(self):
            """Обход дерева в симметричном порядке (inorder)."""
            result = []  # Список для хранения отсортированных элементов
            
            def inorder_recursive(node):
                """Рекурсивная функция для обхода дерева."""
                if node != self.nil:  # Если узел не нулевой
                    inorder_recursive(node.left)  # Обход левого поддерева
                    result.append(node.data)  # Добавляем данные в результат
                    inorder_recursive(node.right)  # Обход правого поддерева
            
            inorder_recursive(self.root)  # Начинаем обход с корня
            return result  # Возвращаем отсортированные данные из дерева
    comparisons = [0]
    tree = RedBlackTree()
    for data in arr:
        tree.insert(data, comparisons)
    sorted_arr = tree.inorder_traversal()
    return sorted_arr, comparisons[0]