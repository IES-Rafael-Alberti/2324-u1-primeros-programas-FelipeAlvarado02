def divisionCesta(dinero):

    lista = dinero.split(",")

    for i in range(len(lista)):
        print(lista[i])

    return ""


if __name__ == "__main__":

    print(divisionCesta(input("Introduce la cesta de objetos")))