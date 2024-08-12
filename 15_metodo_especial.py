class Clase():
    
    #Primero se invoca a __new__
    def __new__(cls):
        print('new')
        return super().__new__(cls)
    
    #El __init__ es un metodo especial
    def __init__(self):
        print('init')
    
c = Clase()
    
    
