import xml.etree.ElementTree as ET  
from .experiment_data import ExperimentData  
def read_experiments_from_xml(xml_file):
    """
    Читает план экспериментов из XML-файла.

    Args:
        xml_file (str): Путь к XML-файлу.

    Returns:
        list: Список экспериментов (структуры ExperimentData).
    """
    try:
        tree = ET.parse(xml_file)  # Парсинг XML-файла, создание дерева элементов
        root = tree.getroot()  # Получение корневого элемента XML
        experiments = []  
        
        # Поиск всех узлов "experiment" в корневом элементе
        for element in root.findall("experiment"):
            # Извлечение атрибутов Length и Counts из узла "experiment"
            length = int(element.get("Length"))  # Преобразование значения Length в целое число
            counts = int(element.get("Counts"))  # Преобразование значения Counts в целое число
            
            # Создаем экземпляр ExperimentData и добавляем его в список экспериментов
            experiments.append(ExperimentData(length, counts))
        
        return experiments 
    
    except FileNotFoundError:
        # Обработка исключения в случае, если файл не найден
        print(f"Ошибка: Файл не найден: {xml_file}")
        return []  
    
    except ET.ParseError:
        # Обработка исключения для некорректного XML-файла
        print(f"Ошибка: Некорректный XML-файл: {xml_file}")
        return []  
