import unittest
from sort_analyzer import xml_parser
from sort_analyzer.experiment_data import ExperimentData
from main import SortAnalyzer

class TestSortAnalyzer(unittest.TestCase):
    """Класс тестов для анализа сортировок, наследованный от unittest.TestCase."""

    def test_read_experiments_from_xml(self):
        """Тест для проверки функции чтения экспериментов из XML-файла."""
        # Создаем временный XML-файл для тестирования с заданным содержимым
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <experiments>
            <experiment Length="10" Counts="5"/>
            <experiment Length="20" Counts="5"/>
        </experiments>"""
        
        # Запись тестового содержимого в временный XML-файл
        with open("test_experiments.xml", "w") as f:
            f.write(xml_content)

        # Читаем эксперименты из XML-файла с помощью функции
        experiments = xml_parser.read_experiments_from_xml("test_experiments.xml")
        
        # Проверяем, что было прочитано 2 эксперимента
        self.assertEqual(len(experiments), 2)
        # Проверяем, что атрибут length первого эксперимента равен 10
        self.assertEqual(experiments[0].length, 10)
        # Проверяем, что атрибут counts первого эксперимента равен 5
        self.assertEqual(experiments[0].counts, 5)

    def test_sort_analyzer(self):
        """Тест для проверки корректности работы SortAnalyzer."""
        # Создаем временный XML-файл для тестирования
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <experiments>
            <experiment Length="10" Counts="5"/>
            <experiment Length="20" Counts="5"/>
        </experiments>"""
        
        # Запись тестового содержимого в временный XML-файл
        with open("test_experiments.xml", "w") as f:
            f.write(xml_content)

        # Создаем экземпляр SortAnalyzer с путем к тестовому XML-файлу
        analyzer = SortAnalyzer("test_experiments.xml")

        # Проверяем, что эксперименты были правильно прочитаны
        self.assertEqual(len(analyzer.experiments), 2)
        self.assertEqual(analyzer.experiments[0].length, 10)
        self.assertEqual(analyzer.experiments[0].counts, 5)

        # Запускаем анализируемость алгоритмов и получаем таблицу результатов
        results_table = analyzer.analyze_algorithms()
        # Проверяем, что таблица результатов не пуста, что означает успешный анализ
        self.assertGreater(len(results_table), 0)

if __name__ == '__main__':
    unittest.main()
