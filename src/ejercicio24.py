def divisionDineroEurosCentimos(dinero):

    lista = dinero.rsplit(".")

    euro = lista[0]

    centimo = str(lista[1])

    while len(centimo) >2:
        dinero = input("Introduce un formato de número correcto")

        lista = dinero.rsplit(".")

        euro = lista[0]

        centimo = str(lista[1])



    return "Son "  + euro + " euros con "+ centimo +" centimos."

if __name__ == "__main__":

    print(divisionDineroEurosCentimos(input("Introduce el dinero")))