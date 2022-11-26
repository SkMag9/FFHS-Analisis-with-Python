#
#   Semesterarbeit AnPy - Abgabe 3
#
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d as interp


def punkte_spline():
    # Spline Funktion durch zufällig gewählte Punkte
    # Punkte
    x = np.array([6,  8, 12, 16, 18, 24])
    y = np.array([6, 10,  8, 12,  4, 14])

    # Lineare Splines
    lin_spline = interp(x, y)

    # Kubische Splines
    cub_spline = interp(x, y, kind="cubic")

    # Splines aufzeigen
    line = np.linspace(6, 24, num=100, endpoint=True)
    plt.plot(x, y, "rx", line, lin_spline(line), "-", line, cub_spline(line), "g--")

    plt.legend(["Punkte", "linear", "kubisch"], loc="lower left")
    plt.show()


def curve_spline_drei():
    # Kurve
    x = np.arange(-1, 1, 0.001)
    y = 1/(1+50*x**2)
    plt.plot(x, y, "-b")

    # Punkte auf Kurve
    punkte_x = np.arange(-1, 1, 0.5)
    punkte_y = 1/(1+50*punkte_x**2)
    plt.plot(punkte_x, punkte_y, "rx")

    # Kubische Splines
    cub_spline = interp(punkte_x, punkte_y, kind="cubic")
    line = np.linspace(-.5, .5, num=100)
    plt.plot(line, cub_spline(line), "--")
    plt.legend(["Kurve", "Punkte", "kubisch 3 Punkte"], loc="upper left")
    plt.show()


def curve_spline_sieben():
    # Kurve
    x = np.arange(-1, 1, 0.001)
    y = 1/(1+50*x**2)
    plt.plot(x, y, "-b")

    # Punkte auf Kurve
    punkte_x = np.arange(-1, 1, 0.25)
    punkte_y = 1/(1+50*punkte_x**2)
    plt.plot(punkte_x, punkte_y, "rx")

    # Kubische Splines
    cub_spline = interp(punkte_x, punkte_y, kind="cubic")
    line = np.linspace(-0.74, 0.74, num=100)
    plt.plot(line, cub_spline(line), "--")
    plt.legend(["Kurve", "Punkte", "kubisch 7 Punkte"], loc="upper left")
    plt.show()


def curve_spline_siebzehn():
    # Kurve
    x = np.arange(-1, 1, 0.001)
    y = 1 / (1 + 50 * x ** 2)
    plt.plot(x, y, "-b")

    # Punkte auf Kurve
    punkte_x = np.arange(-1, 1, 0.1)
    punkte_y = 1 / (1 + 50 * punkte_x ** 2)
    plt.plot(punkte_x, punkte_y, "rx")

    # Kubische Splines
    cub_spline = interp(punkte_x, punkte_y, kind="cubic")
    line = np.linspace(-0.8, 0.8, num=100)
    plt.plot(line, cub_spline(line), "--")

    plt.legend(["Kurve", "Punkte", "kubisch 17 Punkte"], loc="upper left")
    plt.show()


def main():
    punkte_spline()
    curve_spline_drei()
    curve_spline_sieben()
    curve_spline_siebzehn()


if __name__ == '__main__':
    main()
