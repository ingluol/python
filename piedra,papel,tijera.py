import random

mano = ["piedra", "papel", "tijeras"]

x=0
continuar=0
while continuar==0:
    x=0
    eleccion = 0
    while eleccion not in [1, 2, 3]:
        entrada = input("\n\nPara elegir piedra digite 1\npara elegir papel digite 2\npara elegir tijeras digite 3\neleccion: ")
        if entrada.isdigit():
            eleccion = int(entrada)
        else:
            print("Por favor, ingresa una opcion valida: ")
    
    eleccion-=1
    manojugador=mano[eleccion]
    manomaquina = random.choice(mano)

    if manojugador==mano[0] and manomaquina==mano[2]:
        print("\nGanaste")

    elif manojugador==mano[1] and manomaquina==mano[0]:
        print("\nGanaste")

    elif manojugador==mano[2] and manomaquina==mano[1]:
        print("\nGanaste")

    elif manojugador==mano[2] and manomaquina==mano[0]:
        print("\nPerdiste")

    elif manojugador==mano[0] and manomaquina==mano[1]:
        print("\nPerdiste")

    elif manojugador==mano[1] and manomaquina==mano[2]:
        print("\nPerdiste")

    elif manojugador==manomaquina:
        print("\nEmpate")


    print("\nTu elegiste: "+manojugador)
    print("\nLa maquina eligio: "+manomaquina)

    while x==0:
        continuar=input("\ndesea continuar jugando y/n?")
        if continuar!="y" and continuar!="n":
            print("opcion invalida")
        if continuar=="y":
            continuar=0
            x=1
        if continuar =="n":
            break

print("Gracias por jugar")
