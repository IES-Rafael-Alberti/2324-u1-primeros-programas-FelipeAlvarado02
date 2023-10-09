def calculoIMC(peso, estatura):
    resultado = peso/(estatura*estatura)
    total = str(((resultado*100)//1)/100)
    return total


if __name__ == "__main__":

    print(calculoIMC(float(input("Introduce tu peso")), float(input("Introduce tu estatura en metros "))))