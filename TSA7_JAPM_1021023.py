#Introduccion a la Programacion - seccion: 17
#19/10/2023
#José Antonio Paz Marin
#Objetivo: programa que solicite una palabra
"""Entrada:
palabra ingresada por el usuario
"""
"""Proceso: 
solicitar una palabra al usuario
mostrar las primeras tres letras de la palabra ingresada
solicitar una segunda palabra o una frese
cambiar las "o" por "x"
"""
"""Salida:
3 primeras letras de la palabra ingresada
texto modificado cambiando "o" por "x"
"""
palabra = input("Ingrese una palabra: ")
Letras = ""
for i in range(3):
    if i < len(palabra):
        letra = palabra[i]
        print(f"Letra {i + 1}: {letra}")
        Letras = Letras + letra
print("Las primeras tres letras de su palabra son:", Letras)
input("Presione Enter para continuar...")
palabra2 = input("Ingrese una palabrao frase: ")
TxtM = ""
for letra in palabra2:
    if letra == "o":
        TxtM =TxtM + "x"
    else:
        TxtM += letra
print("Texto modificado:", TxtM)

"""SITUACIONES EN LAS QUE ES UTIL ESTE TIPO DE FUNCION
1. Validar la entrada del usuario al momento de ingresar en algún tipo de formulario.
2. Procesar y corregir un texto. (Ejemplo: Cuando Word lee algún error gramatical)
3. Sustituir palabras en un texto por otras.
"""