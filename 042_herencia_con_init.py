# Esta es la superclase
class Usuarios:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
	

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellido)

usuario1 = Usuarios('Pedro', 'Espejo')
usuario1.imprime_datos()

# Esta es la subclase
class UsuariosPremium(Usuarios):
	def __init__(self, nombre, apellido, instagram):
		self.nombre = nombre
		self.apellido = apellido
		self.instagram = instagram
	    
usuario2 = Usuarios('Pedro Espejo', 'Vargas')
usuario2.imprime_datos()