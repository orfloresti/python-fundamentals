class Persona():
    def __init__(self):
        pass

    def brincar(self):
        print('brinco')
    
    #Decorador con @
    #Metodo de clase
    @classmethod
    def correr(cls):
        print('corro')
    
    #Metodo estatico
    @staticmethod
    def nadar():
        print('nado')
        
jose = Persona()
jose.nadar()
