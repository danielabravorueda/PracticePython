
# Si la division es entre 0
try:
 division = 10/0

except ZeroDivisionError:
    print("No se puedo dividir entre 0 y 100")


# Si la edad es diferente de numeros
try:
    edad = (int(input("Ingrese edad:")))
    print(f"tu es edad: {edad}",end=" ")
except ValueError:
    print("Edad no valido")