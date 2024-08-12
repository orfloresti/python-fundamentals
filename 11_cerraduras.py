#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:35:46 2017

@author: orlando
"""

def funcionA(x):
    def funcionB(y):
        return x+y
    return funcionB

funcion = funcionA(5)
print(funcion(3))