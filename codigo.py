#Este codigo es para hacer una interfaz o menu con Python para la clase de Automatizacion de Infraestructura Digital I.
#El autor de este codigo es el equipo de Gerardo Martinez, Miguel Cordova, Armando Tovar, Jose Rodriguez, Angel Hernandez. 

menu = """
Hola usuario bienvenido a nuestro programa de operaciones Matematicas, 
puede seleccionar del 1 al 8 de lo que desea realizar:

[1] Suma de numeros.
[2] Producto entre varios numeros.
[3] Division.
[4] Calcular factorial.
[5] Tablas de multiplicar (1 al 10).
[6] Calcular al cuadrado y al cubo.
[7] Determinacion del promedio.
[8] Cantidad de "N" numeros.
"""
print (menu)
#En los elif borraran el pass y meteran su codigo.
opcion = input('Selecciona una opcion entre 1 a 8:')

if opcion == '1':
    pass
elif opcion == '2':
    meconsol = """ Haz elegido la opcion 2, ahora dinos que numero
 deseas que sea el producto entre varios numeros:
    """
    print (meconsol)
    total = input("¿Cuántos numeros desea multiplicar(max 3): ")
    if total == '2':
        n1 = int(input("Ingrese su primer numero: "))
        n2 = int(input("Ingrese su segundo numero: "))
        print("La suma de",n1,"*",n2,"=",n1*n2)
    elif total == '3':
        n1 = int(input("Ingrese su primer numero: "))
        n2 = int(input("Ingrese su segundo numero: "))
        n3 = int(input("Ingrese su tercer numero: "))
        print("La multiplicacion de",n1,"*",n2,"*",n3,"=",n1*n2*n3)
    
    else:
        print('Solamente puedes multiplicar 3 números')

elif opcion == '3':
    meconsol = """Haz elegido la opcion 3, pulsa enter para continuar:
    """
    print (meconsol)
    total = input("que numeros deseas dividir")
    numero1= float(input("introduzca el primer numero: "))
    numero2= float(input("introduzca el segundo numero: "))
    if numero2 == 0:
        print ("el divisor no puede ser cero")
    else:
        print (numero1/numero2)
    pass
elif opcion == '4':
    pass
elif opcion == '5':
    meconsol = """Haz elegico la opcion 5: 
    """
    print (meconsol)
    tabla = int(input("que tabla desea mostrar: "))
    if tabla >=1 and tabla <=10:
        print(tabla,"x 1 =",tabla*1)
        print(tabla,"x 2 =",tabla*2)
        print(tabla,"x 3 =",tabla*3)
        print(tabla,"x 4 =",tabla*4)
        print(tabla,"x 5 =",tabla*5)
        print(tabla,"x 6 =",tabla*6)
        print(tabla,"x 7 =",tabla*7)
        print(tabla,"x 8 =",tabla*8)
        print(tabla,"x 9 =",tabla*9)
        print(tabla,"x 10 =",tabla*10)
    else:
        print("Escoja un numero entre el 1 y 10")    
    pass
elif opcion == '7':
    pass
elif opcion == '8':
    pass
else:
    print('Debes digitar un numero del 1 al 8')
    print('=='*20)

