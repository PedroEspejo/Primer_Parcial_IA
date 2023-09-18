import math

def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(2)



area2 = lambda radio: (math.pi * radio * radio)

print(area2(2))