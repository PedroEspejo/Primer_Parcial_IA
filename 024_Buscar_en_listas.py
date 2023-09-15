entrada = input('Introduce el color: \n')
colores = ['amarillo', 'verde', 'morado', 'rojo']

if entrada in colores[0]:
    print ('el color amarillo esta en la lista')

elif entrada in colores[1]:
    print ('el color verde esta en la lista')

elif entrada in colores[2]:
    print ('el color morado esta en la lista')

elif entrada in colores[3]:
    print ('el color rojo esta en la lista')

else:
    print ('El ccolor no esta en la lista')
