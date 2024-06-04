from random import *


nombre = input("ingrese su nombre: ")

print(f"Hola {nombre} !Vamos a jugar!\n")

print(f"\n{nombre} la maquina eligio un numero al alzar, !tienes solo 8 intentos para adivinarlo!\n")

contador = 0

numero = list(range(1,101))
elige = choice(numero)


while contador < 9:
    random = int(input("ingrese su numero: "))
    
    if random == elige:
        print("Felicidades, adivinaste el numero")
        break
    elif contador > 8:
        print("Lo siento, no adivinaste el numero")
        
    elif random > elige:
        print("El numero es menor al que elegiste")
    elif random < elige:
        print("El numero es mayor al que elegiste")
   
    else :
        continue
    
    contador += 1
    