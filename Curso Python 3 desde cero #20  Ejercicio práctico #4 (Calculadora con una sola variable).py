#CALCULADORA
'''1. LA CALCULADORA DEBERA SER CAPAZ DE CALCULAR LAS OPERACIONES DE SUMA, RESTA,
MULTIPLICACION, DIVISION, DIVISION ENTERA, EXPONENTE Y MODULO O RESTO.
2. LA CALCULADORA DEBERA TENER UN MENU DE OPCIONES DONDE EL USUARIO PUEDA ELEGIR
CUAL ES LA OPERACION QUE DESEA EJECUTA.
3. LA CALCULADORA DEBERA SOLICITAR UNICAMENTE DOS VALORES POR CADA OPERACION.

El codigo de este programa debera funcionar con una unica variable que se
llamara numero, es decir no se permite la implementacion de otra variable.'''

print('CALCULADORA\n\n')
print('Menu de opciones\n\n')
print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Division entera')
print('6. Exponente\n7. Modulo o resto\n')
numero=int(input('Introduce la opcion deseada:'))

if numero==1:
    print('Suma')
    numero=int(input('Introduce el primer valor'))
    print(numero+int(input('Introduce el segundo valor')))
    
elif numero==2:
    print('Resta')
    numero=int(input('Introduce el primer valor'))
    print(numero-int(input('Introduce el segundo valor')))
    
elif numero==3:
    print('Multipicacion')
    numero=int(input('Introduce el primer valor'))
    print(numero*int(input('Introduce el segundo valor')))
    
elif numero==4:
    print('Division')
    numero=float(input('Introduce el primer valor'))
    print(numero/float(input('Introduce el segundo valor')))
    
elif numero==5:
    print('Division entera')
    numero=int(input('Introduce el primer valor'))
    print(numero//int(input('Introduce el segundo valor')))
    
elif numero==6:
    print('Exponente')
    numero=int(input('Introduce el primer valor'))
    print(numero**int(input('Introduce el segundo valor')))
    
elif numero==7:
    print('Modulo o Resto')
    numero=int(input('Introduce el primer valor'))
    numero%=int(input('Introduce el segundo valor'))
    print(numero)

else:
    print("eliga una opcion valida")
