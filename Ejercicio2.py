#Hacer que el sistema genere un numero aleatorio entre 1 y 10. Luego hacer que el usuario
#adivine el número. La aplicación debe terminar cuando el usuario adivine.
import random 


n= random.randint(1,10)
while True:
    a= int(input("Adivine número del sistema (1,10)"))
    if n==a:
        print("Adivinaste!")
        break
    else:
        print("Numero incorrecto")

