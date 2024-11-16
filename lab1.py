import re
import argparse
from collections import Counter
from typing import List


def read_file(file_name: str) -> List[str]:
    """
    Читает файл и возвращает список строк.

    :param file_name: Название файла для чтения.
    :return: Список строк из файла.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Ошибка: Файл '{file_name}' не найден.") from e


def extract_names(data: List[str]) -> List[str]:
    """
    Извлекает имена из списка строк, используя регулярные выражения.

    :param data: Список строк, представляющих содержимое файла.
    :return: Список имен.
    """
    name_pattern = re.compile(r'Имя: (\w+)')
    names = []

    for line in data:
        match = name_pattern.search(line)
        if match:
            names.append(match.group(1))
    return names


def find_most_common_name(names: List[str]) -> str:
    """
    Находит наиболее часто встречающееся имя.

    :param names: Список имен.
    :return: Наиболее часто встречающееся имя.
    """
    if not names:
        raise ValueError("Ошибка: Имена не найдены в данных.")

    counter = Counter(names)
    most_common_name, _ = counter.most_common(1)[0]
    return most_common_name


def main():
    """
    Главная функция для чтения файла, извлечения имен и поиска наиболее частого имени.
    """
    parser = argparse.ArgumentParser(description="Поиск наиболее часто встречающегося имени в файле.")
    parser.add_argument('file_name', type=str, help="Название файла для анализа")
    args = parser.parse_args()

    try:
        data = read_file(args.file_name)
        names = extract_names(data)
        most_common_name = find_most_common_name(names)
        print(f"Наиболее часто встречающееся имя: {most_common_name}")
    except (FileNotFoundError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    main()
