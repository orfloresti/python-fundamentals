#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:45:42 2017

@author: orlando
"""
#Programacion funcional
"""
def lower(elementos):return elementos.lower()

lista = ["JOSE", "JUlia", "nO"]
print(list(map(lower,lista)))

print([cad.lower() for cad in lista])
"""

"""
def saludo(idioma):
    def saludo_es():
        print("Hola")
    def saludo_en():
        print("Hi")
    idioma_func={"es":saludo_es,
                 "en":saludo_en
                 }    
    return idioma_func[idioma]

saludar = saludo("en")
saludar()
"""

from functools import reduce

numeros=(1,2,3,4)
def suma(x,y):
    return x+y

sumar=reduce(suma,numeros)
print(sumar)

#5.03