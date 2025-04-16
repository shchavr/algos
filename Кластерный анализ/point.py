class Point:
    """
    Представляет точку на плоскости.
    """
    def __init__(self, x, y):
        """
        Конструктор.
        """
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """
        Вычисляет расстояние до другой точки.
        """
        return self.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def sqrt(self, number):
        """
        Вычисляет квадратный корень числа методом Герона (итерационным методом).
        """
        if number < 0:
            raise ValueError("Нельзя извлечь квадратный корень из отрицательного числа")

        if number == 0:
            return 0

        guess = number  # Начальное приближение 
        precision = 0.00001  # Заданная точность

        while True:
            new_guess = 0.5 * (guess + number / guess) 
            if abs(new_guess - guess) < precision:
                return new_guess
            guess = new_guess

