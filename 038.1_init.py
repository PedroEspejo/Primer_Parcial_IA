class Usuario():
	
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos
		
	    
	def imprime_datos(self):
		print('Nombre:', self.nombre, '\n Apellidos:', self.apellidos)


usuario1 = Usuario('Enrique', 'Barros Fernández')
usuario2 = Usuario('Javier', 'Gomila Reyes')

usuario1.imprime_datos()
usuario2.imprime_datos()