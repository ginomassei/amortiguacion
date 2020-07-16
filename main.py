import numpy as np
from vlt import *
from vla import *
from vfsa import *
from vfca import *
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
def grafico(time, pos, vel, ace, lista, columns: list, title: list):
    # Graficos con ejes.
    fig = plt.figure()
    fig.subplots_adjust(hspace=0)
    fig.suptitle("Analisis de vibración: {}".format(title), fontsize=16)

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

    mplcursors.cursor()

    # Plot table.
    fig2, ax = plt.subplots()
    # Hide axes
    fig2.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    # Putting data on.
    df = pd.DataFrame(lista, columns=columns)
    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', colLoc="center", rowLoc="center", cellLoc="center")
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    the_table.scale(1.2, 1.2)

    # Muestra los gráficos.
    plt.show()

def menu():
    global lista_b, columns, title
    option = -1
    while option != 0:
        print_blue_text('Simulador de oscilaciones')

        print('1 - Vibración Libre de Traslacion.')
        print('2 - Vibración Libre Amortiguada.')
        print('3 - Vibración Forzada sin amortiguamiento.')
        print('4 - Vibración Forzada con amortiguamiento.')
        print('0 - Salir\n')

        option = int(input('Escriba el número del caso para resolver: '))

        if 0 < option < 5:

            k = float(input("Ingrese el coeficiente elástica (N/m): "))
            m = float(input("Ingrese la Masa del cuerpo (Kg): "))
            time = np.linspace(0, int(input("Ingrese Tiempo de simulación (s): ")), 500)
            p = math.sqrt(k / m)

            # --- Listas 
            pos = []  # Lista valores posicion
            vel = []  # Lista valores velocidad
            ace = []  # Lista valores aceleracion

            if option == 1:
                title = "Vibración libre de traslacion"
                print_green_text(title)
                x0 = float(input("Ingrese posición inicial (m): "))
                v0 = float(input("Ingrese velocidad inicial (m/s): "))
                t, f, a = vibracion_libre_traslacion(v0, x0, p, m, k, pos, vel, ace, time)

                columns = ("Periodo", "Frecuencia", "Amplitud")
                lista = [round(t, 3), round(f, 3), round(a, 3)]
                lista_b = [lista]

            elif option == 2:
                title = "Vibración libre amortiguada"
                print_green_text(title)
                c = float(input("Ingrese el coeficiente de amortiguamiento (N/(m/s)): "))
                x0 = float(input("Ingrese posición inicial (m): "))
                v0 = float(input("Ingrese velocidad inicial (m/s): "))
                n = (c / (2 * m))
                ccr, Tn, fn = vibracion_libre_amortiguada(v0, x0, p, n, m, k, pos, vel, ace, time)

                columns = ("C. crítico amortiguamiento", "Periodo natural", "Frecuencia natural")
                lista = [round(ccr, 3), round(Tn, 3), round(fn, 3)]
                lista_b = [lista]
            
            elif option == 3:
                title = "Vibración forzada sin amortiguamiento"
                print_green_text(title)
                F = float(input("Ingrese fuerza exitatriz (N): "))
                Wf = float(input("Ingrese velocidad angular de la fuerza exitatriz (rad/s): "))
                x0 = float(input("Ingrese posición inicial (m): "))
                v0 = float(input("Ingrese velocidad incial (m/s): "))
                Tn, fn, T, f, Fa = vibracion_forzada_sin_amortiguamiento(x0, v0, m, F, p, Wf, time, pos, vel, ace)

                columns = ("Periodo (VL)", "Frecuencia (VL)", "Periodo (VF)", "Frecuencia (VF)", "Factor amplificación")
                lista = [round(Tn, 3), round(fn, 3), round(T, 3), round(f, 3), round(Fa, 3)]
                lista_b = [lista]

            elif option == 4:
                title = "Vibración forzada con amortiguamiento"
                print_green_text(title)
                F = float(input("Ingrese fuerza exitatriz (N): "))
                Wf = float(input("Ingrese velocidad angular de la fuerza exitatriz (rad/s): "))
                c = float(input("Ingrese el coeficiente de amortiguamiento (N/(m/s)): "))
                x0 = float(input("Ingrese posición inicial (m): "))
                v0 = float(input("Ingrese velocidad incial (m/s): "))
                n = (c / (2 * m))
                Tn, fn, T, f, ccr, Fa, A = vibracion_forzada_con_armotiguamiento(x0, v0, p, n, m, k, F, Wf, pos, vel, ace, time)

                columns = ("Periodo (VL)", "Frecuencia (VL)", "Periodo (VF)", "Frecuencia (VF)", "C. crit. amortiguamiento"
                           , "F. de amplificación", "Amplitud")
                lista = [round(Tn, 3), round(fn, 3), round(T, 3), round(f, 3), round(ccr, 3), round(Fa, 3), round(A, 3)]
                lista_b = [lista]

            # Plot
            grafico(time, pos, vel, ace, lista_b, columns, title)

        elif option == 0:
            print_blue_text('Fin del programa.')
            return
            
        else:
            print_red_text('Ingrese un número de opción válido.')


def main():
    menu()


if __name__ == "__main__":
    main()
