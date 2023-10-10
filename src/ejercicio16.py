def calculoBarras(numBarras):

    barra = 3.49

    return f"Una barra de pan cuesta {barra} normalmente, con el descuento {(barra*60)/100} y lo recaudado por barras no frescas es de " + str(numBarras*((barra*60)/100))

if __name__ == "__main__":

    print(calculoBarras(int(input("Introduce el número de barras"))))