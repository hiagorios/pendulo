def rungeKutta(a, b, n, y0, f):
	w = y0
	t = a
	h = (b-a)/n
	k1, k2, k3, k4 = 0, 0, 0, 0

	i = 0
	while i < n:
		k1 = f(t, w)
		k2 = f(t + (h/2), w + ((h/2)*k1))
		k3 = f(t + (h/2), w + ((h/2)*k2))
		k4 = f(t + h, w + (h*k3))

		t = t + h
		w = w + (h/6)*(k1 + (2*k2) + (2*k3) + k4)

		i = i + 1

	return w
	

