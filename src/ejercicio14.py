
def calculoEnvio(numPayasos,numMuyecas):
    pesopayasos = 112
    pesomuyecas = 75
    return "El peso total del envío es de: " +str((numPayasos*pesopayasos + pesomuyecas*numMuyecas)/1000) + " Kilogramos"


if __name__ == "__main__":

    print(calculoEnvio(float(input("Introduce el número de payasos")), float(input("Introduce el número de muñecas "))))