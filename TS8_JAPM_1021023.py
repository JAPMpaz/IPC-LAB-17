#Introduccion a la programacion
#28/09/2023
#Jose Antonio Paz Marín
#objeivos: crear un programa que utilice While y For para seguir una secuencia de numeros
"""
entrada:
numeros de 1-25
numeros de 5-50
numeros de 20-0
"""
"""
proceso:
1. utilizando for dar una secuencia de 1-25 que aumente de 1 en 1
2. repetir lo anterior pero con while
3. repetir este proceso con las secuencias: 
*5-50 aumentando de 5 en 5
*20-0 decrementando de 2 en 2
"""
"""
salida:
secuencia de numeros definidos
"""
i=1
print("uso For 1-25")
for i in range (1,26):
    print (i)
    i=i+1
print ("uso de while 1-25")
n1=1
while n1<=25:
    print(n1)
    n1=n1+1
n2=5
print("uso For 5-50")
for n2 in range (5,51,5):
    print (n2)
    n2=n2+5
print ("uso de while 5-50")
n3=5
while n3<=50:
    print(n3)
    n3=n3+5
n4=20
print("uso For 20-0")
for n4 in range (20,0,-2):
    print (n4)
    n4=n4-2
print ("uso de while 20-0")
n5=20
while n5>0:
    print(n5)
    n5=n5-2