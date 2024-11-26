from Cotxe import Cotxe
from Colibri import Colibri

# Crear 3 instancias de Cotxe
cotxe1 = Cotxe("Honda", "Civic", "Vermell", 400, "Manual")
cotxe2 = Cotxe("Toyota", "Corolla", "Gris", 120, "Automatic")
cotxe3 = Cotxe("Mercedes", "GLC", "Blau", 210, "Automatic")

# Mostrar 3 Getters de Cotxe
print(f'El cotxe es un {cotxe1.getMarca()}')
print(f'El color del cotxe es {cotxe1.getColor()}')
print(f'La potencia del cotxe es de {cotxe1.getPotencia()} cv\n')


# Modificar 2 atributs de Cotxe amb els Setters
print('Modificant marca i model del cotxe...')
cotxe1.setMarca("Audi") # La marca sera Audi
cotxe1.setModel("A4") # El model sera A4

# Mostrar atributs modificats de Cotxe
print(f"La marca del cotxe s'ha modificat, ara es un {cotxe1.getMarca()}")
print(f"El model del cotxe tambe s'ha modificat, el nou model es un {cotxe1.getModel()}\n")


# Crear 3 instancias de Colibrí
colibri1 = Colibri("Juan", 5, 2, 10, "Blau")
colibri2 = Colibri("Luis", 7, 1, 9.5, "Vermell")
colibri3 = Colibri("Pablo", 6.5, 4, 12, "Groc")

# Mostrar 4 Getters de Colibrí
print(f'El colibrí es diu {colibri1.getNom()}')
print(f'Pesa {colibri1.getPes()} grams i te {colibri1.getEdat()} anys')
print(f'Es de color {colibri1.getColor()}\n')

# Modificar 2 atibuts de Colibrí amb els Setters
print('Modificant edat i tamany del Colibrí...')
colibri1.setEdat(3) # La edat sera de 3 anys
colibri1.setTamany(13) # El tamany sera de 13 cm

# Mostrar atributs modificats de Colibrí
print(f'La edat del Colbrí ha estat modificada, la nova edat es {colibri1.getEdat()} anys')
print(f'El tamany del Colibri ha canviat, el nou tamany es de {colibri1.getTamany()} cm')