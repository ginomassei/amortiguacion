import math
import matplotlib.pyplot as plt
import mplcursors

def vibracion_forzada_sin_amortiguamiento(x0, v0, m, F, p, Wf, time, pos, vel, ace):
	global B, A, C
	sp = []
	sh = []
	sg = []
	q = (F / m)

	if x0 == 0 and v0 == 0:
		A = 0
		B = 0
	elif x0 != 0 and v0 == 0:
		A = 0
		B = x0
	elif x0 == 0 and v0 != 0:
		A = v0 / p
		B = 0
	else:
		A = v0 / p
		B = x0

	C = (q / p ** 2) * (1 / (1 - (Wf ** 2 / p ** 2)))

	for i in time:
		# Solucion particular (C.cos(Wf.t))
		solp = C * math.cos(Wf * i)
		sp.append(solp)

		#Solucion homogenea (A.sin(p.t) + B.cos(p.t) + sp)
		solh = (A * math.sin(p * i)) + (B * math.cos(p * i))
		sh.append(solh)

		#Solución general
		solg = solp + solh
		sg.append(solg)

		pos.append((A * math.sin(p * i)) + (B * math.cos(p * i)) + (C * math.cos(Wf * i)))
		vel.append(A * p * math.cos(p * i) - (B * p * math.sin(p * i)) - (C * Wf * math.sin(Wf * i)))
		ace.append(((-A) * p**2 * math.sin(p * i)) - (B * p**2 * math.cos(p * i)) - (C * Wf**2 * math.cos(Wf * i)))

	Tn = (2 * math.pi) / p #Periodo de Vibración libre
	fn = p / (2 * math.pi) #Frecuencia de Vibración libre
	T = (2 * math.pi) / Wf #Perido de Vibración forzada
	f = Wf / (2 * math.pi) #Frecuencia Vibración forzada
	Fa = Wf / p #Factor de amplificación

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

	return Tn, fn, T, f, Fa