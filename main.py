'''
t -> tempo
Θ -> angulo entre a "corda" do pendulo e a posicao de repouso
Θ0 -> angulo inicial e também máximo que o pendulo atinge

(d²Θ)/dt² = (-g/L)*senΘ -> equacao do oscilador harmonico
Θ(t) = Θ0*cos(raiz(g/l)*t)

x(teta) = l*sen(teta)
y(teta) = l*cos(teta)
'''

import numpy as np
import matplotlib.pyplot as plt

# Inicializacao das variaveis #
g = 9.8
L = 2
n = 1000
t = 60
teta = {}
w = {}

teta[0] = np.pi/6
w[0] = 0

######################################################

def rungeKutta(n, teta, w, h):
	k1, k2, k3, k4 = 0, 0, 0, 0

	i = 0
	while i < n - 1:
		k1 = h*w[i]
		k2 = h*(w[i] + k1/2)
		k3 = h*(w[i] + k2/2)
		k4 = h*(w[i] + k3)

		teta[i + 1] = teta[i] + (k1 + 2*k2 + 2*k3 + k4)*h/6

		k1 = (-g/L)*np.sin(teta[i])*h
		k2 = (-g/L)*np.sin(teta[i] + k1/2)*h
		k3 = (-g/L)*np.sin(teta[i] + k2/2)*h
		k4 = (-g/L)*np.sin(teta[i] + k3)*h

		w[i + 1] = w[i] + (k1 + 2*k2 + 2*k3 + k4)*h/6

		i = i + 1
######################################################

def oscilacao():
	x = np.linspace(0, n-1, n)
	plt.plot(x, teta, 'r--')
	plt.plot(x, w, 'b--')
	plt.legend(['Teta', 'Omega'])
	plt.show()

######################################################

def pendulo():
	x = np.zeros(n, dtype=float)
	y = np.zeros(n, dtype=float)
	for i in range (n):
		x[i] = L*np.sin(teta[i])
		y[i] = L*np.cos(teta[i])
	graph = plt.subplot()
	i = 0
	plt.grid()
	plt.axis([-L, L, -L - 1, 0])
	while i < n:
		graph.scatter(x[i], -y[i], color='black', s=200)
		plt.pause(0.0001)
		# nao consegui usar as funcoes de update do grafico
		graph.scatter(x[i], -y[i], color='white', s = 300)
		i = i + 10

######################################################

rungeKutta(n, teta, w, t/n)
teta = np.array([v for v in teta.values()])
w = np.array([v for v in w.values()])

oscilacao()
pendulo()
