def coversionTemperatura(temperatura:float):
    return f"El resultado es de: "+str(temperatura*(9/5)+32)+" Grados Fahrenheit."


if __name__ == "__main__":

    print(coversionTemperatura(float(input("Introduzca la temperatura para "
                                      "realizar su conversión en grados Fahrenheit.\n"))))
