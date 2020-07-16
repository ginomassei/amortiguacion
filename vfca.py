import math
import cmath
import matplotlib.pyplot as plt
import mplcursors

def vibracion_forzada_con_armotiguamiento(x0, v0, p, n, m, K, F, Wf, pos, vel, ace, time):

    #Listas
    sp = []
    sh = []
    sg = []

    #Constantes
    q = F / m
    M = (q * 2 * n * Wf) / ((-Wf**2 + p**2)**2 + 4 * n**2 * Wf**2)
    N = (q * (-Wf**2 + p**2)) / ((-Wf**2 + p**2) + 4 * n**2 * Wf**2)

    #Selección de caso
    if n > p:
        caso = 1

    else:
        if n < p:
            caso = 3

        else:
            caso = 2

    t1 = complex(-n + (cmath.sqrt((n**2) - (p**2))))
    t2 = complex(-n - (cmath.sqrt((n**2) - (p**2))))
    r1 = t1.real
    r2 = t2.real

    # Caso donde n > p "Amortiguamiento supercrítico"
    if caso == 1:
        C1 = (v0-(r2 * x0))/(r1 - r2)
        C2 = x0 - C1

        for i in time:
            #Solución particular (M.sin(Wf.t) + N.cos(Wf.t))
            solp = M * math.sin(Wf * i) + N * math.cos(Wf * i)
            sp.append(solp)

            #Solución homogenea
            solh = ((C1 * (math.e**(r1 * i))) + (C2 * (math.e**(r2 * i))))
            sh.append(solh)

            #Solución general
            solg = (solp + solh)
            sg.append(solg)

            pos.append(solg)
            vel.append((-((C1 * r1 * (math.e**(r1*i)))+(C2 * r2 * (math.e**(r2*i))))
                    + (M * Wf * math.cos(Wf * i)) - (N * Wf * math.sin(Wf * i))))
            ace.append(-((C1 * (r1**2) * (math.e**(r1*i)))+(C2 * (r2**2) * (math.e**(r2*i))))
                    - (M * Wf**2 * math.sin(Wf * i)) - (N * Wf**2 *math.sin(Wf * i)))

    # Caso donde n = p "amortiguamiento critico" caso = 2
    elif caso == 2:
        C1 = x0
        C2 = 0

        for i in time:
            #Solución particular
            solp = M * math.sin(Wf * i) + N * math.cos(Wf * i)
            sp.append(solp)

            #Solución homogenea
            solh = ((C1*(math.e**(-n*i)))+(C2*i*(math.e**(-n*i))))
            sh.append(solh)

            # Solución general
            solg = (solp + solh)
            sg.append(solg)

            pos.append(solg)
            vel.append((C1*(-n)*(math.e**((-n)*i)))+(C2*(-n)*i*(math.e**((-n)*i)))
                        + (M * Wf * math.cos(Wf * i)) - (N * Wf * math.sin(Wf * i)))
            ace.append((C1*(n**2)*(math.e**((-n)*i)))+(C2*i*(n**2)*(math.e**((-n)*i)))
                        - (M * Wf**2 * math.sin(Wf * i)) - (N * Wf**2 *math.sin(Wf * i)))

    # Caso donde n<p "amortiguamiento subcritico" caso = 3
    else:
        C1 = x0
        C2 = ((v0 + (n*x0))/ (math.sqrt((p**2)-(n**2))))
        p1 = math.sqrt((p ** 2) - (n ** 2))

        for i in time:
            #Solución particular
            solp = M * math.sin(Wf * i) + N * math.cos(Wf * i)
            sp.append(solp)

            #Solución homogenea
            solh = ((math.e**((-n)*i))*((C1*math.cos(p1*i))+(C2*math.sin(p1*i))))
            sh.append(solh)

            # Solución general
            solg = (solp + solh)
            sg.append(solg)

            pos.append(solg)
            vel.append(-(((-n*(math.e**(-n * i)))*((C1*math.cos(p1*i))+(C2*math.sin(p1*i)))) +
                        ((math.e**((-n)*i))*(((-C1)*p1*math.sin(p1*i))+(C2*p1*math.cos(p1*i)))))
                        + (M * Wf * math.cos(Wf * i)) - (N * Wf * math.sin(Wf * i)))
            ace.append(-((((n**2)*(math.e**(-n * i)))*((C1*math.cos(p1*i))+(C2*math.sin(p1*i))))+((-n*(math.e**(-n*i)))*
                        ((-C1*p1*math.sin(p1*i))+(C2*p1*math.cos(p1*i))))+((-n*(math.e**(-n * i)))*((-C1*p1*math.sin(p1*i))+
					    (C2*p1*math.cos(p1*i))))+((math.e**(-n * i))*((-C1*(p1**2)*math.cos(p1*i))-(C2*(p1**2)*math.sin(p1*i)))))
                        - (M * Wf**2 * math.sin(Wf * i)) - (N * Wf**2 *math.sin(Wf * i)))


    Tn = (2 * math.pi) / p #Periodo natural
    fn = p / (2 * math.pi) #Frecuencia natural
    T = (2 * math.pi) / Wf #Periodo forzado
    f = Wf / (2 * math.pi) #Frecuencia forzado
    ccr = 2 * math.sqrt(K*m) #Coeficiente de amortiguamiento crítico
    Fa = 1 / (math.sqrt((1 - (Wf**2 / p**2))**2 + (((2 * n) / p) * (Wf / p))**2)) #Factor de amplificación
    A = (F / K) * (p / (2 * n)) #Amplitud

    #Grafico
    fig = plt.figure()
    fig.subplots_adjust(hspace=0)
    fig.suptitle("Vibración libre y forzada")

    plt.subplot(3, 1, 1)
    plt.plot(time, sp, color="green", label="Vibracion forzada")
    plt.axhline(y=0, color="red", linewidth=0.4)
    plt.axvline(x=0, color="red", linewidth=0.4)
    plt.grid(color="black", linestyle="-", linewidth=0.3)
    plt.legend()
    plt.ylabel("$Posición(m)$", fontsize=10)

    plt.subplot(3, 1, 2)
    plt.plot(time, sh, color="orange", label="Vibración libre")
    plt.axhline(y=0, color="red", linewidth=0.4)
    plt.axvline(x=0, color="red", linewidth=0.4)
    plt.grid(color="black", linestyle="-", linewidth=0.3)
    plt.legend()
    plt.ylabel("$Posición(m)$", fontsize=10)
    plt.xlabel("$Tiempo(s)$", fontsize=10)

    plt.subplot(3, 1, 3)
    plt.plot(time, sg, color="blue", label="Vibración resultante")
    plt.axhline(y=0, color="red", linewidth=0.4)
    plt.axvline(x=0, color="red", linewidth=0.4)
    plt.grid(color="black", linestyle="-", linewidth=0.3)
    plt.legend()
    plt.ylabel("$Posición(m)$", fontsize=10)
    plt.xlabel("$Tiempo(s)$", fontsize=10)

    mplcursors.cursor()

    plt.show()

    return Tn, fn, T, f, ccr, Fa, A