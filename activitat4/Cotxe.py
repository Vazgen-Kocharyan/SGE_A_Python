class Cotxe:
	def __init__(self, marca, model, color, potencia, transmisio):
		self.marca = marca
		self.model = model
		self.color = color
		self.potencia = potencia


	# Getters
	def getMarca(self):
		return self.marca
	def getModel(self):
		return self.model
	def getColor(self):
		return self.color
	def getPotencia(self):
		return self.potencia
	def getTransmisio(self):
		return self.transmisio
	
	# Setters
	def setMarca(self, newMarca):
		self.marca = newMarca
	def setModel(self, newModel):
		self.model = newModel
	def setColor(self, newColor):
		self.color = newColor
	def setPotencia(self, newPotencia):
		self.potencia = newPotencia
	def setTransmisio(self, newTransmisio):
		self.transmisio = newTransmisio