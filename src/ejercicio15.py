
def calculoDeIntereses(numCuenta):

    print(numCuenta, "Entrada")

    numCuenta = numCuenta + (numCuenta*4/100)

    print((numCuenta*100//1/100), "año 1")

    numCuenta = numCuenta + (numCuenta * 4 / 100)

    print((numCuenta*100//1/100), "año 2")

    numCuenta = numCuenta + (numCuenta * 4 / 100)

    print((numCuenta*100//1/100), "año 3")

    return ""



if __name__ == "__main__":

    print(calculoDeIntereses(int(input("Introduce el dinero a depositar"))))