import re
import sys
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
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")
        sys.exit(1)


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
        return "Имена не найдены"

    counter = Counter(names)
    most_common_name, _ = counter.most_common(1)[0]
    return most_common_name


def main():
    """
    Главная функция для чтения файла, извлечения имен и поиска наиболее частого имени.
    """
    if len(sys.argv) < 2:
        print("Ошибка: Укажите название файла в аргументах командной строки.")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_file(file_name)
    names = extract_names(data)
    most_common_name = find_most_common_name(names)

    print(f"Наиболее часто встречающееся имя: {most_common_name}")


if __name__ == '__main__':
    main()
