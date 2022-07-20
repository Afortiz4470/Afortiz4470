import random

nombre = input ('Hola, como te llamas?')
print(f'{nombre} adivina en que numero estoy pensando entra 1 y 20')

intentos = 0

numero = random.randint(1,20)

while intentos <6:
    posible= int(input('Escribe el numero que crees que es:'))

    if posible < numero:
        print('Es mas grande')
    elif posible > numero:
        print('Es mas chico')
    elif posible == numero:
        break
    intentos += 1

if posible == numero:
    print(f'{nombre} adivinaste en {intentos} intentos')
if intentos == 6:
    print('Perdiste')