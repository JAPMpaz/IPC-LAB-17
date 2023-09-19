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
print (N1, "+", N2, "=", N1+N2)
print (N1, "-", N2, "=", N1-N2)
print(N1, "*", N2, "=", N1*N2)
print(N1, "/", N2, "=", N1/N2)
print(N1, "elevado a ", N2, "=", N1**N2)
print(N1, "cociente", N2, "=", N1//N2)