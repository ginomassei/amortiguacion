import math

def vibracion_libre_amortiguada(v0, x0, p, n, m, K, pos, vel, ace, time):
	r1 = -n + (math.sqrt((n**2) + (p**2)))
	r2 = -n - (math.sqrt((n**2) + (p**2)))

	if n > p:
		caso=1

	else:
		if n < p:
			caso=3

		else:
			caso=2

# Caso donde n > p "Amortiguamiento supercrítico" caso = 1
	if caso == 1:
		C1 = (v0-(r1*x0))/(r2 - r1)
		C2 = x0 - C1

		for i in time:
			pos.append((C1 * (math.e**(r1 * i))) + (C2 * (math.e**(r2 * i))))
			vel.append((C1 * r1 * (math.e**(r1*i)))+(C2 * r2 * (math.e**(r2*i))))
			ace.append((C1 * (r1**2) * (math.e**(r1*i)))+(C2 * (r2**2) * (math.e**(r2*i))))
	
	elif caso == 2:
# Caso donde n = p "amortiguamiento critico" caso = 2
		C1 = x0
		C2 = 0

		for i in time:
			pos.append((C1*(math.e**(-n*i)))+(C2*i*(math.e**(-n*i))))
			vel.append((C1*(-n)*(math.e**((-n)*i)))+(C2*(-n)*i*(math.e**((-n)*i))))
			ace.append((C1*(n**2)*(math.e**((-n)*i)))+(C2*i*(n**2)*(math.e**((-n)*i))))

# Coeficiente de amortiguamiento critico
		ccr= 2* math.sqrt(K*m)

 # Caso donde n<p "amortiguamiento subcritico" caso = 3
	elif caso == 3:
		C1 = x0
		C2 = ((v0 + (n*x0))/ (math.sqrt((p**2)-(n**2))))
		p1 = math.sqrt((p**2)-(n**2))

		for i in time:
			pos.append((math.e**((-n)*i))*((C1*math.cos(p1*i))+(C2*math.sin(p1*i))))
			vel.append(((-n*(math.e**(-n*i)))*((C1*math.cos(p1*i))+(C2*math.sin(p1*i)))) +\
			 		((math.e**((-n)*i))*(((-C1)*p1*math.sin(p1*i))+(C2*p1*math.cos(p1*i)))))
			ace.append((((n**2)*(math.e**(-n*i)))*((C1*math.cos(p1*i))+(C2*math.sin(p1*i))))+((-n*(math.e**(-n*i)))*\
                    ((-C1*p1*math.sin(p1*i))+(C2*p1*math.cos(p1*i))))+((-n*(math.e**(-n*i)))*((-C1*p1*math.sin(p1*i))+\
                    (C2*p1*math.cos(p1*i))))+((math.e**(-n*i))*((-C1*(p1**2)*math.cos(p1*i))-(C2*(p1**2)*math.sin(p1*i)))))
	
	Tn= 2*math.pi*math.sqrt(m/K)
	fn = 1/(2*math.pi*math.sqrt(m/K))

	return ccr, Tn, fn