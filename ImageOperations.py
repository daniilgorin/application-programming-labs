import cv2
import matplotlib.pyplot as plt
import numpy as np


def print_size(img: np.ndarray)->None:
    """
    Выводит в консоль данные о текущей высоте и ширине изображения
    :param img: изображенния данные о котором необходимо получить
    """
    height, width = img.shape[:2]
    print(f"Высота изображения: {height} \nШирина изображения: {width}")


def resize_image(img: np.ndarray, h:int, w:int, save_path: str)->np.ndarray:
    """
    Изменяет размер изображения на новые заданные параметры
    :param img: само изображение
    :param h: новая высота изображения
    :param w: новая ширина изображения
    :param save_path: путь, где новое изображение будет сохранено
    """
    resized_img = cv2.resize(img,(w,h))
    cv2.imwrite(save_path, resized_img)
    return cv2.imread(save_path)


def show_images(img:np.ndarray, save_path: str)->None:
    """
    Выводит на экран 2 изображения: исходное и измененное
    :param img: исходное изображение
    :param save_path: путь где хранится измененное изображение
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    res = cv2.imread(save_path)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10,10))

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(res)
    plt.axis('off')

    plt.show()
