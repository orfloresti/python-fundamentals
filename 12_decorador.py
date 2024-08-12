#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:39:34 2017

@author: orlando
"""
def primerD(funcion):
    def funcionDecorada(*args, **kkwars):
        print("Primer decorador")
    return funcionDecorada

@primerD
def funcion():
    print("Mi primer decorador")
    
funcion()