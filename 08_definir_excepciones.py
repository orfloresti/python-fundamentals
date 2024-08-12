#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Err(Exception):
    def __init__(self,valor):
        print("Fue el error por", valor)
        
try: 
    raise Err(4)
    
except Err:
    print("Error escrito")