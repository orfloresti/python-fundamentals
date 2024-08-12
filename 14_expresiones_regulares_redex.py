import re

#patron = re.compile("\d\d\d")
#print(patron.search("kilo912metro").group())

## Busquedas
#if(re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
#    print("Se encontró el patrón")

## Sustitucion
#print(re.sub(r"\d","*", "mpang8uera990",2))

regex = re.compile(r"ab", re.IGNORECASE)
print(regex.search("jutanmilajABbuimnhtr"))
