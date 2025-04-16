class Image:
    """
    Класс для представления изображения в формате PPM.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(255, 255, 255) for _ in range(width)] for _ in range(height)]  # Изначально все пиксели белые

    def set_pixel(self, x, y, color):
        """
        Устанавливает цвет пикселя по координатам (x, y).
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def save_ppm(self, filename):
        """
        Сохраняет изображение в файл в формате PPM.
        """
        with open(filename, 'w') as f:
            f.write(f'P3\n{self.width} {self.height}\n255\n')  

            for row in self.pixels:
                for r, g, b in row:
                    f.write(f'{r} {g} {b} ')
                f.write('\n')
