def divisionFecha(dinero):

    lista = dinero.split("/")

    dia = lista[0]

    mes = str(lista[1])

    año = str(lista[2])





    return "Es el día "  + dia + " del mes "+ mes +" y del año "  + año


if __name__ == "__main__":

    print(divisionFecha(input("Introduce la fecha en el formato xx/xx/xxxx")))