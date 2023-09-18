class Usuario():
	
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos
		
	
	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario1 = Usuario('Enrique', 'Espejo')
usuario1.imprime_datos()

usuario1.nombre = 'Pedro'
usuario1.imprime_datos()