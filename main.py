import argparse
import cv2

import ImageOperations
import Hist


def create_parser()->tuple:
    """
    Получает от пользователя путь до изображения, путь для сохранения преобразованного изображения,
    новые размер и ширину для преобразованного изображения
    :return: Кортеж состоящий из пути до изображения, пути сохранения результата, новых высоты и ширины изображения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("img",type=str,help="path to the image")
    parser.add_argument("save_path", type=str, help="path where result will be saved")
    parser.add_argument("new_height", type=int, help="new height for the image")
    parser.add_argument("new_width", type=int, help="new width for the image")
    args=parser.parse_args()
    return args.img, args.save_path, args.new_height, args.new_width


def main():
    try:
        image, save_path, new_height, new_width = create_parser()

        img = cv2.imread(image)
        cv2.imshow("Image", img)

        ImageOperations.print_size(img)
        Hist.show_hist(Hist.get_hist(img))

        #Измененные размеры изображения
        result = ImageOperations.resize_image(img, new_height, new_width, save_path)
        ImageOperations.print_size(result)

        ImageOperations.show_images(img, save_path)
    except Exception as e:
        print(f'Ошибка при доступе к директории: {e}')


if __name__ == "__main__":
    main()