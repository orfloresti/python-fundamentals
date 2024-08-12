#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lista = [2,4]

try: 
    print(lista[1])
except IndexError:
    print("Error: error en el indice")
else:
    print("No hay error")
finally:
    print("Se ejecuto")