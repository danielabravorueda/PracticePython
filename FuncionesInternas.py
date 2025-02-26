

def funcion_externa():
    print("Funcion externa se ejecuta primero")
    def funcion_interna():
        print("Funcion interna se ejecuta segundo")
    funcion_interna()

funcion_externa()