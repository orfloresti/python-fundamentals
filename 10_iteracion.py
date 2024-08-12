#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:29:37 2017

@author: orlando
"""

lista = [1,2,3,4,5,6]

for elemento in lista:
    print(elemento)
    
def numeros():
    n=1
    while True:
        yield n
        n= n+1
        
i = numeros()
print(i)
print(i.__next__())
print(i.__next__())

