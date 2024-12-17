import argparse
import os
import csv
import shutil
from icrawler.builtin import GoogleImageCrawler

import ImageIterator

def create_parser()->tuple:
    """
    Пользователь вводит ключевое слово, папку, куда будут сохраняться изображения, и названия csv файла для аннотации
    :return: Кортеж состоящий из ключевого слова, папки с изображениями и имени файла аннотации
    """
    parser=argparse.ArgumentParser()
    parser.add_argument("word", type=str, help="the key word for uploading images")
    parser.add_argument("save_folder", type=str, help="folder where images will be saved")
    parser.add_argument("csv_file", type=str, help="csv file with annotation")
    args=parser.parse_args()
    return args.word, args.save_folder, args.csv_file


def crawler(keyword:str, folder:str)->None:
    """
    Скачивает изображения в указанную папку
    :param keyword: Ключевое слово для скачивания изображений
    :param folder: Папка для хранения изображений
    """
    if os.path.exists(folder):
        shutil.rmtree(folder)
    else:
        os.mkdir(folder)
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder})
    google_crawler.crawl(keyword=keyword, max_num=100)

def create_annotation(folder:str, csv_file:str)->None:
    """
    Создает аннотацию, куда  записывается абсолютный и относительный путь к каждому изображению
    :param folder:  Папка с изображениями
    :param csv_file: Имя файла с аннотацией
    """
    folder_path = os.path.join(os.getcwd(), folder)
    image_files = [f for f in os.listdir(folder_path)]

    with open(csv_file, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Absolute path", "Relative path"])

        for image_file in image_files:
            writer.writerow([os.path.join(folder_path, image_file), image_file])


def main():
    try:
        key_word, folder, annotation = create_parser()
        print(key_word, folder, annotation)
        crawler(key_word, folder)
        create_annotation(folder, annotation)
        for row in ImageIterator.ImageIterator(annotation):
            print(row)
    except Exception as e:
        print(f"Ошибка  при доступе к дирректории: {e} ")

if __name__ == "__main__":
    main()
