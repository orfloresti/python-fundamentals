class Intro():
    def __init__(self,valor):
        self.valor = valor
        
    def segundo(self):
        print("segundo")
    
    def tercero(self):
        print(tercero)

#Propiedades de python        
dato= Intro("valor")
dir(dato)
print(dir(dato))

#Si una variable es instancia de una clase
print(isinstance(dato,Intro))

#Pregunta si la clase puede acceder al atributo
print(hasattr(dato,"doc"))


