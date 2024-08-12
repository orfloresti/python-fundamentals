 class Persona():

    def __init__(self):
        pass

    def despedir(self):
        print('Adios')

    #Metodo de clase
    @classmethod
    def saludar(cls, nombre):
        print('Estoy saludando')

Persona.saludar('Juan')
