class Colibri:
	def __init__(self, nom, pes, edat, tamany, color):
		self.nom = nom
		self.pes = pes
		self.edat = edat
		self.tamany = tamany
		self.color = color
	
	# Getters
	def getNom(self):
		return self.nom
	def getPes(self):
		return self.pes
	def getEdat(self):
		return self.edat
	def getTamany(self):
		return self.tamany
	def getColor(self):
		return self.color
	
	# Setters
	def setNom(self, newNom):
		self.nom = newNom
	def setPes(self, newPes):
		self.pes = newPes
	def setEdat(self, newEdat):
		self.edat = newEdat
	def setTamany(self, newTamany):
		self.tamany = newTamany
	def setColor(self, newColor):
		self.color = newColor
