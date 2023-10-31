import datetime
nombre=input("ingrese su nombre: ")
apellido=input("ingrese sus apellidops: ")
apellidocasada=input("ingresesu apellido de casada: ")
dia_nacimiento=input("ingrese su dia de nacimiento: ")
mes_nacimiento=input("ingrese su mes de nacimiento: ")
año_nacimiento=input("ingrese su año de nacimiento: ")
class INFORMACION:
    def _init_(self):
        self.Nombre=""
        self.Apellidos=""
        self.ApellidoCasada=""
        self.nacimiento=""
    def nombres(self):
        self.Nombre=nombre
    def Apellido(self):
        self.Apellidos=apellido
    def Apellidocasada(self):
        self.ApellidoCasada=apellidocasada
    def edad(self):
        hoy= datetime.date.today()
        edad= hoy.year-año_nacimiento
        return edad