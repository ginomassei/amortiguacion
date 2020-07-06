import math


def vibracion_libre_traslacion(v0, t0, x0, p, n, m, K, pos, vel, ace, time):
    # Definicion de casos.
    if v0 == 0 and t0 == 0 and x0 != 0:
        caso = 1
    elif t0 == 0 and x0 == 0 and v0 != 0:
        caso = 2
    elif t0 == 0 and x0 != 0 and v0 != 0:
        caso = 3
    else:
        raise Exception("Los datos ingresados son erroneos")

    # Calculo de propiedades.
    T = (2 * math.pi) / p
    f = 1 / ((2 * math.pi) / p)
    A = math.sqrt((m * 9.81) * (2 / K))

    # Calculo de valores

    if caso == 1:
        for i in time:
            pos.append(x0 * math.cos(p * i))
            vel.append(- (p * x0 * math.sin(p * i)))
            ace.append(- (((p**2) * x0 * math.cos(p * i)) - ((p ** 2) * x0 * math.cos(p * i))))

    elif caso == 2:
        for i in time:
            pos.append((v0 / p) * math.sin(p * i))
            vel.append(v0 * math.cos(p * i))
            ace.append(- v0 * math.sin(p * i))

    elif caso == 3:
        for i in time:
            pos.append(((v0 / p) * math.sin(p * i)) + (x0 * math.cos(p * i)))
            vel.append(((v0 * math.cos(p * i)) - (x0 * p * math.sin(p * i))))
            ace.append(-(v0 * p * math.sin(p * i)) - (x0 * (p ** 2) * math.cos(p * i)))

    return T, f, A