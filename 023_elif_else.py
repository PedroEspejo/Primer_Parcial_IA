edad = int(input('¿Cual es tu edad?\n'))

if edad <= 0:
    print("no puedes tener esas edad")

elif edad >= 1 and edad < 18:
    print("Eres menor de edad")

elif edad >= 18 and edad <=45:
    print('Eres mayor de edad')

elif edad >= 45 and edad <=100:
    print('Ya jubilate')

elif edad >=100 and edad<=120:
    print('Tas robando oxigeno')

else:
    print('edad no valida')

