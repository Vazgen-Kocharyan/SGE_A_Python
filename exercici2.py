dia_setmana = "dimarts"

if dia_setmana == "dilluns":
	print("Avui és dilluns")
elif dia_setmana == "dimarts":
	print("Avui és dimarts")
elif dia_setmana == "dimecres":
	print("Avui és dimecres")
elif dia_setmana == "dijous":
	print("Avui és dijous")
elif dia_setmana == "divendres":
	print("Avui és divendres")
elif dia_setmana == "dissabte":
	print("Avui és dissabte")
elif dia_setmana == "diumenge":
	print("Avui és diumenge")
else:
	print("Aquest dia no existeix")


# Un altra forma de fer-ho mes eficient seria amb el match, es com el switch de Java
#
# match dia_setmana:
# 	case "dilluns":
# 		print("Avui és dilluns")
# 	case "dimarts":
# 		print("Avui és dimarts")
# 	case "dimecres":
# 		print("Avui és dimecres")
# 	case "dijous":
# 		print("Avui és dijous")
# 	case "divendres":
# 		print("Avui és divendres")
# 	case "dissabte":
# 		print("Avui és dissabte")
# 	case "diumenge":
# 		print("Avui és diumenge")
# 	case _:
# 		print("Aquest dia no existeix")
