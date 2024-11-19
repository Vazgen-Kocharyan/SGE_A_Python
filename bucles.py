### Bucles

## Exercici 1.
# Imprimir números de l’1 al 10 (amb for i amb while)

# Amb for
print("S'imprimeixen els numeros del 1 al 10 amb for")
for i in range(1,11):
	print(f'Numero: {i}')

# Amb while
print("S'imprimeixen els numeros del 1 al 10 amb while")
numero = 1
while (numero <= 10):
	print(f'Numero: {numero}')
	numero += 1


## Exercici 2.
# Sumar els primers 10 números utilitzant for i range().

suma = 0
for i in range(1, 11):
	suma += i
print(f"La suma dels primers 10 números dona {suma}")


## Exercici 3.
# Imprimir els elements d'una llista amb for. fruits = [“poma”,”pera”,”raïm”,”plàtan”]

fruits = ["poma","pera","raïm","plàtan"]

for i in fruits:
	print(f'Element de la llista fruits: {i}')


## Exercici 4.
# Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

parells = ""
imparells = ""
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50] 
for i in num:
	if i % 2 == 0:
		parells += str(i) + " "
	else:
		imparells += str(i) + " "
print(f'Numeros parells: {parells} \nNumeros imparells: {imparells}')


## Exercici 5.
# Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.

suma_parells = 0
suma_imparells = 0
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
for i in num:
	if i % 2 == 0:
		suma_parells += i
	else:
		suma_imparells += i
print(f'Suma de numeros parells: {suma_parells} \nSuma de numeros imparells: {suma_imparells}')


## Exercici 6.
# Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.

suma = 0
while suma < 100:
	print(f'Portas sumat {suma}')
	entrada = int(input("Numero per sumar (entre 0 i 100): "))
	if entrada >= 0 and entrada <= 100:
		suma += entrada
print(f'Has arribat a {suma} que es major que 100') if suma > 100 else print(f'Has arribat a 100')


## Exercici 7.
# Amb while indicar si el número guardat a una variable està entre 100 i 400.

num = int(input("Posa un numero entre 100 i 400: "))
while num < 100 or num > 400:
	print(f'{num} no esta entre 100 i 400')
	num = int(input("Posa un numero entre 100 i 400: "))
print(f'{num} esta entre 100 i 400')