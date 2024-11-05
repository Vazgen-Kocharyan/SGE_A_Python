nota = float(input("Nota: "))

if nota >= 0 and nota <= 4.99:
	print("L'alumne ha suspès")
elif nota >= 5 and nota <= 6.5:
	print("L'alumne ha aprovat")
elif nota >= 6.6 and nota <= 8:
	print("L'alumne te un notable")
elif nota > 8:
	print("L'alumne te un excel·lent")
else:
	print("Nota no valida")