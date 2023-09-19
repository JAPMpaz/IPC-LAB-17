#Introduccion a la programacion-seccion 17
#Jose Antonio Paz Marìn-10231023
#objetivo: crear un programa que utilize dos digitos numericos ingresados por el usuario con los cuales se apliquen los operadores aritmeticos
#Entrada: dos digitos numericos enteros.
"""
Proceso:
1.solicitar dos numeros al usuario
2.aplicar los operadores aritmeticos a los dos numero ingresados anterirormente
"""
"""
Salidas:
resultados de los operadores aritmeticos
"""
print ("ejercicio 1 :operaciones aritmeticas")
N1=int(input("Numero 1: "))
N2=int(input("numero 2: "))
print("1=suma")
print("2=resta")
print("3=multiplicacion")
print("4=division")
print("5=exponente")
print("6=cociente")
print("7=terminar programa")
O123=int(input("OPERACION QUE DEESEA REALIZAR (1-7)= "))
while O123 !=7:
    O123=int(input("OPERACION QUE DEESEA REALIZAR (1-7)= "))
    if(O123==1):
      print (N1, "+", N2, "=", N1+N2)
    elif(O123==2):
        print (N1, "-", N2, "=", N1-N2)
    elif(O123==3):
        print(N1, "*", N2, "=", N1*N2)
    elif(O123==4):
        print(N1, "/", N2, "=", N1/N2)
    elif(O123==5):
        print(N1, "elevado a ", N2, "=", N1**N2)
    elif(O123==6):
        print(N1, "cociente", N2, "=", N1//N2)
    if(O123==7):
        print("fin del programa")

    