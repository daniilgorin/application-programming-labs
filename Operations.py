import csv
import os
import shutil
from icrawler.builtin import GoogleImageCrawler


def crawler(keyword:str, folder:str)->None:
    """
    Скачивает изображения в указанную пaпку
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
    Создает аннотацию, куда записывается абсолютный и относительный путь к каждому изображению
    :param folder: Папка с изображениями
    :param csv_file: Имя файла с аннотацией
    """
    folder_path = os.path.join(os.getcwd(), folder)
    image_files = [f for f in os.listdir(folder_path)]

    with open(csv_file, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Absolute path", "Relative path"])

        for image_file in image_files:
            writer.writerow([os.path.join(folder_path, image_file), image_file])
