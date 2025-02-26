
edad = int(input("Ingresar edad:"))
if edad>0:
  if edad<=12:
    print("Es Niño")
  if edad<=17:
    print("Es Adolecente")
  if(edad>=18 and  edad<=60):
     print("Es Adulto")
  if(edad>=60 and edad<=90):
    print("Es de la Tercera edad")
else:
    print("La edad es negativa o no Valida")