#Introduccion a la programacion, seccion 17
#10/10/2023
#Jose Antonio Paz Marín
#objetivo: crar un programa que ralize converciones a partir de los centimetros ingresados por el usuario
"""
Entrada
centimetros ingresados por el usuario
"""
"""
Proceso
1. solicitar la longitud en centimetros
2. llamar el modulo guardado con las converciones
"""
"""
Salida
1.resultado en la unidad de medida seleccionada
"""
Cm=float(input("ingrese la longitud en centimetros que desea convertir: "))

while True:
    print("centimetro a metro=1")
    print("centimetro a kilometro=2")
    print("centimetro a pie=3")
    print("centimetro a pulgada=4")
    print("salir del programa=5")
    Cn=int(input("ingrese el numero de convercion que desea realizar: "))
    if(Cn==1):
        import centimetro
        metro=round(centimetro.centimetro_metro(Cm),2)
        print(Cm,"cm",  "equivale a : ", metro, "m")
    elif(Cn==2):
        import centimetro
        kilometro=round(centimetro.centimeto_kilometro(Cm),2)
        print(Cm,"cm", "equivale a : ", kilometro, "Km")
    elif(Cn==3):
      import centimetro
      pie=round(centimetro.centimetro_pies(Cm),2)
      print(Cm,"cm",  "equivale a : ", pie, "ft")   
    elif(Cn==4):
        import centimetro
        pulgada=round(centimetro.centimetro_pulgada(Cm),2)
        print(Cm,"cm",  "equivale a : ", pulgada, "in")  
    if(Cn==5):
        break
    SystemExit
    


