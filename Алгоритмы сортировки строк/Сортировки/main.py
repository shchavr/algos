
import math
import random
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt  
from sort_analyzer import xml_parser, utils
from sort_analyzer.bubble_sort import bubble_sort
from sort_analyzer.quick_sort import quick_sort
from sort_analyzer.sort_tree_sort import sort_tree_sort
from sort_analyzer.insertion_sort import insertion_sort
from sort_analyzer.merge_sort import merge_sort
from sort_analyzer.heap_sort import heap_sort
from sort_analyzer.radix_sort import radix_sort
from sort_analyzer.red_black_tree_sort import red_black_tree_sort


class SortAnalyzer:
    """
    Класс для анализа алгоритмов сортировки строк.
    """
    def __init__(self, xml_file):
        """
        Конструктор класса.

        Args:
            xml_file (str): Путь к XML-файлу с планом экспериментов.
        """
        # Чтение экспериментов из указанного XML-файла
        self.experiments = xml_parser.read_experiments_from_xml(xml_file)
        
        # Определение словаря алгоритмов сортировки и их соответствующих реализаций
        self.algorithms = {
            "Bubble Sort": bubble_sort,
            "Quick Sort": quick_sort,
            "Sort Tree": sort_tree_sort,
            "Insertion Sort": insertion_sort,
            "Merge Sort": merge_sort,
            "Heap Sort": heap_sort,
            "Radix Sort": radix_sort,
            "Red-Black Tree Sort": red_black_tree_sort,
        }

    def analyze_algorithms(self):
        """
        Анализирует все алгоритмы сортировки и возвращает результаты в виде таблицы.

        Returns:
            list: Список кортежей (название алгоритма, сложность, коэффициент C).
        """
        results_table = []  # Инициализация списка для хранения результатов анализа
        print("Результаты экспериментов:\n")

        # Цикл по всем алгоритмам сортировки
        for name, algorithm in self.algorithms.items():
            print(f"Оценка для {name}:")  # Вывод имени алгоритма
            complexity, C, _ = self._estimate_complexity(name, algorithm, self.experiments)  # Оценка сложности
            print(f"  - Сложность: {complexity}")  # Вывод сложности
            print(f"  - Коэффициент C: {C:.6f}")  # Вывод коэффициента C
            results_table.append((name, complexity, C))  # Добавляем результаты в таблицу
            print("-" * 40)  # Разделительная линия

        return results_table  # Возвращаем таблицу результатов

    def print_results_table(self, results_table):
        """
        Выводит сравнительную таблицу результатов.

        Args:
            results_table (list): Список кортежей (название алгоритма, сложность, коэффициент C).
        """
        print("\nСравнительная таблица результатов:\n")
        print(f"{'Алгоритм':<20} {'Сложность':<15} {'Коэффициент C':<15}")
        print("-" * 50)  
        
        for name, complexity, C in results_table:
            print(f"{name:<20} {complexity:<15} {C:<15.6f}")  # Форматированный вывод результата


    def _estimate_complexity(self, algorithm_name, algorithm, experiments):
        """
        Оценивает сложность алгоритма и вычисляет коэффициент C.

        Args:
            algorithm_name (str): Название алгоритма сортировки
            algorithm (function): Функция алгоритма сортировки.
            experiments (list): Список экспериментов (структуры ExperimentData).

        Returns:
            tuple: (сложность, коэффициент C, результаты экспериментов).
        """
        results = []  # Инициализация списка для хранения результатов экспериментов
        for experiment in experiments:  # Проходим по всем экспериментам
            length = experiment.length  # Длина массива для эксперимента
            counts = experiment.counts  # Количество повторений эксперимента
            total_comparisons = 0  # Инициализируем счетчик сравнений для текущего эксперимента

            for _ in range(counts):  # Повторяем эксперимент указанное количество раз
                if algorithm_name == "Radix Sort":  # Проверка названия алгоритма
                    # Генерация случайных чисел для Radix Sort
                    data = [random.randint(0, 1000) for _ in range(length)]
                else:
                    # Генерация случайных строк для других алгоритмов
                    data = utils.generate_random_strings(length, 5)

                # Сортируем данные с использованием текущего алгоритма и получаем количество сравнений
                sorted_data, comparisons = algorithm(data.copy())
                total_comparisons += comparisons  # Суммируем все сравнения

            # Рассчитываем среднее количество сравнений для текущего эксперимента
            avg_comparisons = total_comparisons / counts
            results.append((length, avg_comparisons))  # Добавляем результат в список

        # Определяем коэффициент C и сложность с использованием метода наименьших квадратов (МНК)
        n_values = [length for length, _ in results]  # Извлечение длины массива из результатов
        f_values = [comparisons for length, comparisons in results]  # Извлечение среднем значений сравнений

        if algorithm_name == "Bubble Sort" or algorithm_name == "Insertion Sort":
            # Для O(N^2) алгоритмов
            sum_x2 = sum(x**4 for x in n_values)  # Сумма x^4 для МНК
            sum_y = sum(f_values)  # Сумма y
            sum_xy = sum(f_values[i] * n_values[i]**2 for i in range(len(f_values)))  # Сумма x^2*y
            C = sum_xy / sum_x2 if sum_x2 != 0 else 0  # Избежание деления на ноль
            complexity = "O(N^2)"  # Определение сложности

        elif algorithm_name == "Radix Sort":
            # Для O(kN), где k - средняя длина строки
            k = 5  # Предполагаем, что средняя длина равна 5
            sum_x = sum(n_values)  # Сумма x
            sum_y = sum(f_values)  # Сумма y
            sum_xy = sum(f_values[i] * n_values[i] for i in range(len(f_values)))  # Сумма x*y
            C = sum_xy / (k * sum_x) if sum_x != 0 else 0  # Избежание деления на ноль
            complexity = "O(kN)"  # Определение сложности

        else:  # Для всех остальных алгоритмов, предполагая O(N log N)
            log_values = [x * math.log2(x) if x > 0 else 0 for x in n_values]  # Обработка log2(0)
            sum_x2 = sum(x**2 for x in log_values)  # Сумма (x * log2(x))^2
            sum_y = sum(f_values)  # Сумма y
            sum_xy = sum(f_values[i] * log_values[i] for i in range(len(f_values)))  # Сумма (x * log2(x))*y
            C = sum_xy / sum_x2 if sum_x2 != 0 else 0  # Избежание деления на ноль
            complexity = "O(N log N)"  # Определение сложности

        return complexity, C, results  # Возвращаем сложность, коэффициент C и результаты экспериментов.


    def _test_sort_analyzer(self):
        """
        Тестирует класс SortAnalyzer.
        """
        # Создаем временный XML-файл для тестирования с заданным содержимым
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <experiments>
            <experiment Length="10" Counts="5"/>
            <experiment Length="20" Counts="5"/>
        </experiments>"""
        
        # Записываем тестовое содержимое в XML-файл
        with open("test_experiments.xml", "w") as f:
            f.write(xml_content)

        # Создаем экземпляр SortAnalyzer с указанием пути к тестовому XML-файлу
        analyzer = SortAnalyzer("test_experiments.xml")

        # Проверяем, что эксперименты прочитаны правильно
        assert len(analyzer.experiments) == 2  # Ожидаем, что было прочитано 2 эксперимента
        assert analyzer.experiments[0].length == 10  # Проверяем длину первого эксперимента
        assert analyzer.experiments[0].counts == 5  # Проверяем количество запусков первого эксперимента

        # Запускаем анализ алгоритмов и проверяем, что таблица результатов не пуста
        results_table = analyzer.analyze_algorithms()
        assert len(results_table) > 0  # Ожидаем, что результаты были получены

        # Выводим таблицу результатов (для ручной визуальной проверки)
        analyzer.print_results_table(results_table)

        print("Все тесты пройдены") 

    def generate_best_array(self, length):
        """Генерирует лучший случайный массив (уже отсортированный)"""
        arr = list(range(length))  # Создает список от 0 до length-1
        return arr  

    def generate_random_array(self, length):
        """Генерирует случайный массив."""
        arr = [random.randint(0, length) for _ in range(length)]  # Создает массив из случайных чисел в диапазоне от 0 до length
        return arr  

    def generate_worst_array(self, length):
        """Генерирует худший случайный массив (отсортированный в обратном порядке)"""
        arr = list(range(length, 0, -1))  # Создает список от length до 1 (обратный порядок)
        return arr  

    def sort_array(self, sort_type, arr):
        """Выполняет сортировку массива."""
        comparisons = 0  # Инициализация счетчика сравнений
        # Выполняем сортировку в зависимости от заданного типа
        if sort_type == "bubble":
            arr, comparisons = bubble_sort(arr)
        elif sort_type == "quick":
            arr, comparisons = quick_sort(arr)
        elif sort_type == "sort_tree":
            arr, comparisons = sort_tree_sort(arr)
        elif sort_type == "insertion":
            arr, comparisons = insertion_sort(arr)
        elif sort_type == "merge":
            arr, comparisons = merge_sort(arr)
        elif sort_type == "heap":
            arr, comparisons = heap_sort(arr)
        elif sort_type == "radix":
            arr, comparisons = radix_sort(arr)
        elif sort_type == "red_black_tree":
            arr, comparisons = red_black_tree_sort(arr)
        
        return arr, comparisons  


    def create_charts(self, res_dict):  
        """Создает графики для каждого алгоритма."""

        for sort_name in res_dict.keys():
            plt.figure(figsize=(12, 8))  
            plt.title(f"Сортировка: {sort_name}")  # Заголовок 
            plt.xlabel("Длина массива")  #  оси X
            plt.ylabel("Количество операций")  # оси Y
            plt.grid(True)  # Включаем сетку 

            # Для каждого случая (лучший, случайный, худший) создаем графики
            for case in ["best", "random", "worst"]:
                x_values = []  # Список для хранения значений длины массива
                y_values = []  # Список для хранения значений количества операций
                for len_array, operations in res_dict[sort_name].items():  # Проходим по результатам текущего алгоритма
                    for i, ops in enumerate(operations[case]):  # Проходим по операциям для данного случая
                        x_values.append(len_array)  # Добавляем длину массива
                        y_values.append(ops)  # Добавляем количество операций

                # Построение графика 
                plt.plot(x_values, y_values, marker='o', linestyle='', label=f"{sort_name} ({case})")

            plt.legend()  # Добавляем легенду для графика
            plt.savefig(f"{sort_name}_chart.png")  
            plt.show()  


    def save_results_to_xml(self, res_dict):  
        """Сохраняет результаты в XML файл."""
        root = ET.Element("results")  # Создаем корневой элемент XML

        # Проходим по каждому алгоритму и его результатам
        for sort_name, sizes in res_dict.items():
            sort_element = ET.SubElement(root, "sort", {"name": sort_name})  # Создаем элемент для алгоритма
            for len_array, cases in sizes.items():  # Проходим по длинам массивов
                size_element = ET.SubElement(sort_element, "size", {"length": str(len_array)})  # Элемент для размера массива
                for case, operations in cases.items():  # Проходим по каждому случаю
                    case_element = ET.SubElement(size_element, "case", {"type": case})  # Элемент для случая
                    for op in operations:  # Проходим по операциям
                        ET.SubElement(case_element, "operation").text = str(op)  # Добавляем элемент для операции

        # Создаем дерево элементов и сохраняем его в XML-файл
        tree = ET.ElementTree(root)  
        tree.write("results.xml", encoding="utf-8", xml_declaration=True)  # Сохранение дерева в файл
        print("Результаты успешно сохранены в results.xml")  # Сообщение о завершении


class Program:
    def __init__(self, analyzer, config_file="config.xml"):  # Добавлено: analyzer
        """Конструктор класса Program, принимающий анализатор и файл конфигурации."""
        self.analyzer = analyzer  # Сохраняет переданный анализатор
        self.config_file = config_file  # Сохраняет путь к файлу конфигурации
        self.config = self.load_config()  # Загружает конфигурацию из XML файла
        self.res_dict = {}  # Инициализирует словарь для хранения результатов

    def load_config(self):
        """Загружает конфигурацию из XML файла."""
        try:
            tree = ET.parse(self.config_file)  # Парсинг XML файла конфигурации
            root = tree.getroot()  # Получение корневого элемента

            config = {}  # Инициализация словаря для конфигурации
            # Извлечение типов сортировки из XML
            config["SortTypes"] = [el.text for el in root.findall("./SortTypes/SortType")]
            # Извлечение размеров массивов из XML
            config["ArraySizes"] = [int(el.text) for el in root.findall("./ArraySizes/ArraySize")]
            # Извлечение количества повторений из XML
            config["RepeatCount"] = int(root.find("./RepeatCount").text)

            return config  # Возвращает загруженную конфигурацию
        except FileNotFoundError:
            print(f"Ошибка: Файл конфигурации {self.config_file} не найден.")  # Обработка ошибки отсутствия файла
            exit()  # Завершение программы
        except ET.ParseError:
            print(f"Ошибка: Некорректный XML формат в файле {self.config_file}.")  # Обработка ошибки формата
            exit()  # Завершение программы

    def run(self):
        """Основной метод для запуска анализа и построения графиков."""
        # Проходим по каждому алгоритму сортировки из конфигурации
        for sort_name in self.config["SortTypes"]:
            self.res_dict[sort_name] = {}  # Инициализация словаря для результата текущего алгоритма
            # Проходим по размерам массивов из конфигурации
            for len_array in self.config["ArraySizes"]:
                self.res_dict[sort_name][len_array] = {}  # Инициализация словаря для текущего размера массива

                # Обработка лучшего случая
                self.res_dict[sort_name][len_array]["best"] = []  # Инициализация для лучшего случая
                best_array = self.analyzer.generate_best_array(len_array)  # Генерация лучшего случая
                _, best_comparisons = self.analyzer.sort_array(sort_name, best_array)  # Сортировка лучшего массива
                self.res_dict[sort_name][len_array]["best"].append(best_comparisons)  # Сохранение числа операций

                # Обработка случайного случая
                self.res_dict[sort_name][len_array]["random"] = []  # Инициализация для случайного случая
                for _ in range(self.config["RepeatCount"]):  # Повторяем заданное количество раз
                    random_array = self.analyzer.generate_random_array(len_array)  # Генерация случайного массива
                    _, random_comparisons = self.analyzer.sort_array(sort_name, random_array)  # Сортировка
                    self.res_dict[sort_name][len_array]["random"].append(random_comparisons)  # Сохранение числа операций

                # Обработка худшего случая
                self.res_dict[sort_name][len_array]["worst"] = []  # Инициализация для худшего случая
                worst_array = self.analyzer.generate_worst_array(len_array)  # Генерация худшего случая

                _, worst_comparisons = self.analyzer.sort_array(sort_name, worst_array)  # Сортировка
                self.res_dict[sort_name][len_array]["worst"].append(worst_comparisons)  # Сохранение числа операций

        # После обработки всех алгоритмов создаем графики и сохраняем результаты в XML
        self.analyzer.create_charts(self.res_dict)  # Создание графиков для результатов
        self.analyzer.save_results_to_xml(self.res_dict)  # Сохранение результатов в XML файл


if __name__ == "__main__":
    xml_file = "experiments.xml"  
    # Создадим файл experiments.xml если его нет
    try:
        with open(xml_file, "r") as f:
            pass  # Проверяем, существует ли файл
        
    except FileNotFoundError:  # Если файл не найден
        with open(xml_file, "w") as f:
            # Записываем содержимое в новый файл
            f.write("""<?xml version="1.0" encoding="UTF-8"?>
        <experiments>
            <experiment Length="100" Counts="50"/>
            <experiment Length="200" Counts="50"/>
            <experiment Length="400" Counts="50"/>
            <experiment Length="800" Counts="25"/>
            <experiment Length="1600" Counts="25"/>
            <experiment Length="3200" Counts="10"/>
        </experiments>""")
    # Создаем экземпляр SortAnalyzer с указанием файла
    analyzer = SortAnalyzer(xml_file)
    results_table = analyzer.analyze_algorithms()  # Запускаем анализ алгоритмов
    analyzer.print_results_table(results_table)  # Печатаем таблицу результатов

    program = Program(analyzer)  # Создаем экземпляр Program с анализатором
    program.run()  

    print("\nГотово")
