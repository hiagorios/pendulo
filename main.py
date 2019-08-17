'''
Problema de valor inicial do pendulo:
{ (d²Θ)/dt² = (-g/L)*senΘ
{ Θ(t0) = Θ0
'''

from sympy import lambdify, sin
from sympy.abc import x
from rungekutta import rungeKutta

def show ():
    print('Not implemented yet')

g = 9.6
L = float (input('Digite L: '))
t0 = float (input('Digite o Teta inicial: '))
n = int(input("Digite o número de subdivisões: "))

f = lambdify(x, (-g/L)*sin(x))

for i in range (0, 100):
    print(rungeKutta(i, 20, n, t0, f))

print(f(t0))