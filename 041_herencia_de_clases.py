# Esta es la clase madre
class Usuarios:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
	    
	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellido)

usuario1 = Usuarios('Pedro', 22)

usuario1.imprime_datos()

# Esta es la clase hija
class UsuariosPremium(Usuarios):
	pass