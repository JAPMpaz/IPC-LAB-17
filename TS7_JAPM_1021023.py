#Introduccion a la programacion, seccion 17
#21/09/2023
#Jose Antonio Paz Marín
#objetivo: crar un programa que muestre la tabla de multiplicar del numero ingresado por elusuario
"""
Entrada
numeros enteros entre el 1 y 10
"""
"""
Proceso
1. solicitar un numero entre el 1 y el 10
2. verificar si el numero se encuentra en el rango solicitado
si en caso se encuentra dentro del rango, mostrar la tabla de multiplicar del numero ingresado.
4. si en caso no se encuentra en el rango solicitado, mostrar un error
"""
"""
Salida
1.tabla de multiplicar del numero ingresado, si este se encuentra en el rango solicitado
2.error en caso el numero ingresado no se encuentre en el rango solicitado.
"""
while True:
    print("Jose Antonio Paz Marin")
    try:
        n1=int(input("ingresar numero entre 1 y 10: "))
        if (n1<1 or n1>10):
            print("el numero ingresado no se encuentra en el rango solicitado")
        else:
            for i in range(1,11):
                resul=(n1*i)
                print(n1, "*", i, "=", resul)
    except ValueError:
        print("el valor ingresado no es un numero")
    loop=input("desea ingresar otro valor? S/N: ")
    if loop.upper() !="S":
        break
SystemExit

        
