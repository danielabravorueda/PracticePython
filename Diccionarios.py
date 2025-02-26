

dicc = {1:"dani",2:"maria",3:"beto",4:"vero"}

# recorrer por key
for clave in dicc.keys():
  print(clave,end=" ")
print(f" ") #salto de linea

 #recoorre por valores
for valor in dicc.values():
     print(valor,end=" ")
print(f" ") #salto de linea

# mostrar clave y valor
for clave in dicc.keys():
    print(f"{clave} -> {dicc[clave]}")