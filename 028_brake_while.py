"""
x=1

while x <= 10:
    x += 1
    
    if x==5:
        continue
    print(x)
"""
x = 0
while x <= 30:
    x +=1
    if x==4 or x==6 or x==10:
        print('se salto el valor ', x, ' de x')

    if x==15:
        print ("Se rompe el bucle cuando x vale ",x)
        break

    print(x)

