import cv2
import matplotlib.pyplot as plt
import numpy as np


def get_hist(img: np.ndarray)->np.ndarray:
    """
    Получает гистограмму для заданного изображения
    :param img: само изображение
    :return: гистограмма по данному изображению, которая будет использована в show_hist()
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.calcHist(gray_img, [0], None, [256], [0, 256])


def show_hist(hist: np.ndarray)->None:
    """
    Выводит на экран готовую гистограмму
    :param hist: гистограмма, полученная в функции get_hist()
    """
    plt.figure(figsize=(10,5))

    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность пикселей')
    plt.ylabel('Частота')
    plt.xlim([0, 256])


    plt.plot(hist, color="black")
    plt.fill_between(range(256), hist.flatten(), color='black', alpha=0.5)
    plt.grid()

    plt.show()