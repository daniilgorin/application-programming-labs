import cv2
import matplotlib.pyplot as plt
import numpy as np


def get_hist(img: np.ndarray)->list:
    """
    Получает гистограмму для заданного изображения
    :param img: само изображение
    :return: гистограмма по данному изображению, которая будет использована в show_hist()
    """
    channels = cv2.split(img)
    histograms = []

    for channel in channels:
        hist = cv2.calcHist([channel], [0], None, [256], [0,256])
        histograms.append(hist)

    return histograms


def show_hist(hist: np.ndarray) -> None:
    """
    Выводит на экран гистограмму для каждого канала изображения
    :param hist: гистограммы по каждому каналу
    """
    colors = ['red', 'green', 'blue']
    plt.figure(figsize=(10,5))

    plt.title("Гистограмма изображения")
    plt.xlabel("Интенсивность пикселей")
    plt.ylabel("Частота")

    for i, hist in enumerate(hist):
        plt.plot(hist, color=colors[i], label=f'{colors[i].capitalize()} канал')
        plt.fill_between(range(256), hist.flatten(), color=colors[i], alpha = 0.5)

    plt.grid()
    plt.legend()
    plt.show()