import argparse

import Operations
import ImageIterator

def create_parser()->tuple:
    """
    Пользавaтель вводит ключевое слово, папку, куда будут сохраняться изображения, и названия csv файла для аннотации
    :return: Кортеж состоящий из ключевого слова, папки с изображениями и имени файла аннотации
    """
    parser=argparse.ArgumentParser()
    parser.add_argument("word", type=str, help="the key word for uploading images")
    parser.add_argument("save_folder", type=str, help="folder where images will be saved")
    parser.add_argument("csv_file", type=str, help="csv file with annotation")
    args=parser.parse_args()
    return args.word, args.save_folder, args.csv_file


def main():
    try:
        key_word, folder, annotation = create_parser()
        print(key_word, folder, annotation)
        Operations.crawler(key_word, folder)
        Operations.create_annotation(folder, annotation)

        for row in ImageIterator.ImageIterator(annotation):
            print(row)
    except Exception as e:
        print(f"Ошибка при доступе к дирректории: {e} ")

if __name__ == "__main__":
    main()
