#
#   Semesterarbeit AnPy - Abgabe 2
#
import matplotlib.pyplot as plt
import numpy as np


def funktion():
    x = np.arange(-10, 10, 0.01)
    y = x ** 2

    plt.plot(x, y)

    plt.title("Funktionsgraph für x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()


def mehrere_funktionen():
    x = np.arange(-10, 10, 0.01)
    y = x ** 2
    plt.plot(x, y, label="x^2")

    y = np.abs(x * 5)
    plt.plot(x, y, label="x*|5|")

    plt.title("Funktionsgraphen für x^2 und x*|5|")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend(loc="upper center")
    plt.show()


def balken():
    x = np.array(["A", "B", "C", "D", "E"])
    y = np.array([3, 13, 29, 11, 9])

    plt.bar(x, y)
    plt.show()


def torte():
    data = np.array([3, 13, 29, 11, 9])
    data_labels = np.array(["Apples", "Blueberries", "Cherries", "Dandelions", "Eucalyptus"])
    data_explode = np.array([0, 0.2, 0, 0, 0])

    plt.pie(data, labels=data_labels, explode=data_explode)
    plt.show()


def histogramm():
    x = np.random.normal(170, 10, 200)

    plt.hist(x)
    plt.show()


def main():
    funktion()
    mehrere_funktionen()
    balken()
    torte()
    histogramm()


if __name__ == '__main__':
    main()
