salari = int(input("Salari: "))

if salari < 15000:
	print(f"- L'IVA es del 0% \n- El salari base son: {salari}€ \n- L'IVA son: {salari * 0/100}€ \n- El total son: {salari * 1}€")
elif salari < 30000 and salari >= 15000:
	print(f"- L'IVA es del 10% \n- El salari base son: {salari}€ \n- L'IVA son: {salari * 10/100}€ \n- El total son: {salari * 1.10}€")
elif salari < 60000 and salari >= 30000:
	print(f"- L'IVA es del 21% \n- El salari base son: {salari}€ \n- L'IVA son: {salari * 21/100}€ \n- El total son: {salari * 1.21}€")
else:
	print(f"A {salari}€ no s'aplica ningun IVA")