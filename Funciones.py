



def suma(n1,n2):
  return n1+n2;

def multiplicacion(n1,n2):
  return n1*n2;

def division(n1,n2):
    try:
      return n1/n2;
    except ZeroDivisionError:
     return -1;

def resta(n1,n2):
    return n1-n2




#variable local
cont =0

#metodos void o cambio de estado del metodo
def incrementar():
    global cont
    cont += 1
def decrementar():
    global cont
    cont -= 1

#metodo get o devuelve valor modificado
def getContador():
    return cont



# FUNCIONES MATEMATICAS
print(f"La suma es :{suma(3,4)}")
print(f"La multiplicacion es :{multiplicacion(3,4)}")
print(f"La division es:{division(3,0)}")
print(f"La resta es:{resta(5,4)}")

# Estado de Variable
incrementar()
incrementar()
incrementar()
print(f"incrementar:{getContador()}")
decrementar()
print(f"decrementar en 1: {getContador()}")




