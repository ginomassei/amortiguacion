import mplcursors as mpl
import matplotlib.pyplot as plt
import numpy as np
from vlt import * 
from vla import *
from matplotlib.pyplot import figure
import pandas as pd


# ANSI Colours functions.
def print_red_text(string):
    red_text = '\033[31;1m'
    reset_text = '\033[m'

    print(red_text + string + reset_text)


def print_green_text(string):
    green_text = '\033[32;1m'
    reset_text = '\033[m'

    print(green_text + string + reset_text)


def print_blue_text(string):
    blue_text = '\033[34;1m'
    reset_text = '\033[m'
    print(blue_text + string + reset_text)


# Plot
def grafico(time, pos, vel, ace, lista, columns):
    # Graficos con ejes.
    fig = figure()
    fig.subplots_adjust(hspace=15)
    fig.suptitle("Analisis de vibración", fontsize=16)

    plt.subplot(3, 1, 1)
    plt.plot(time, pos, color="black", label="Posición")
    plt.axhline(y=0, color="red", linewidth=0.4)
    plt.axvline(x=0, color="red", linewidth=0.4)
    plt.ylabel("$X=f(t)$", fontsize=10)
    plt.grid(color="black", linestyle="-", linewidth=0.3)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time, vel, color="blue", label="Velocidad")
    plt.axhline(y=0, color="red", linewidth=0.4)
    plt.axvline(x=0, color="red", linewidth=0.4)
    plt.ylabel("$v=f(t)$", fontsize=10)
    plt.grid(color="black", linestyle="-", linewidth=0.3)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time, ace, color="orange", label="Aceleración")
    plt.axhline(y=0, color="red", linewidth=0.4)
    plt.axvline(x=0, color="red", linewidth=0.4)
    plt.xlabel("$Time$", fontsize=13)
    plt.ylabel("$a=f(t)$", fontsize=10)
    plt.grid(color="black", linestyle="-", linewidth=0.3)
    plt.legend()

    mpl.cursor()

    # Plot table.
    fig2, ax = plt.subplots()
    # Hide axes
    fig2.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    # Putting data on.
    df = pd.DataFrame(lista, columns=columns)
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    fig.tight_layout()  

    # Muestra los gráficos.
    plt.show()


def menu():
    option = -1
    while option != 0:
        print_red_text('Amortiguacion.')

        print('1 - Vibracion Libre de Traslacion.')
        print('2 - Vibracion Libre Amortiguada.')
        print('3 - Vibracion Forzada sin amortiguamiento.')
        print('4 - Vibracion Forzada de Estado estable.')
        print('5 - Vibracion forzada con amortiguamiento.')
        print('0 - Salir\n')

        option = int(input('Escriba el número del caso para resolver: '))

        if 0 < option < 5:

            k = float(input("Inserte el coeficiente elástica(N/m): "))
            m = float(input("Inserte la Masa del cuerpo(Kg): "))
            c = float(input("Inserte el coeficiente de amortiguamiento(N/(m/s)): "))
            time = np.linspace(0, int(input("Inserte Tiempo maximo: ")), 200)
            p = math.sqrt(k / m)
            n = (c / (2 * m))

            # --- Listas 
            pos = []  # Lista valores posicion
            vel = []  # Lista valores velocidad
            ace = []  # Lista valores aceleracion

            if option == 1:
                v0 = float(input("Inserte velocidad inicial: "))
                t0 = float(input("Inserte tiempo inicial: "))
                x0 = float(input("Inserte posición inicial: "))
                t, f, a = vibracion_libre_traslacion(v0, t0, x0, p, n, m, k, pos, vel, ace, time)

                columns = ("Periodo", "Frecuencia", "Amplitud")
                lista = [t, f, a]
                lista_b = [lista]

            elif option == 2:
                v0 = float(input("Inserte velocidad inicial: "))
                x0 = float(input("Inserte posición inicial: "))
                ccr, Tn, fn = vibracion_libre_amortiguada(v0, x0, p, n, m, k, pos, vel, ace, time)

                columns = ("Coeficiente critico", "Periodo natural", "Frecuencia natural")
                lista = [ccr, Tn, fn]
                lista_b = [lista]
            
            elif option == 3:
                pass  # TO DO
            elif option == 4:
                pass  # TO DO
            elif option == 5:
                pass  # TO DO
            
            # Plot
            grafico(time, pos, vel, ace, lista_b, columns)

        elif option == 0:
            print_blue_text('Fin del programa.')
            return
            
        else:
            print('Ingrese un número de opción válido.')


def main():
    menu()


if __name__ == "__main__":
    main()
