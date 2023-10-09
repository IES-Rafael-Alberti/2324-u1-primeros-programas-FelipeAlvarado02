def fraseConVocalMayuscula(frase,vocal):

    frase = frase.replace(vocal.lower(),vocal.upper())

    return frase

if __name__ == "__main__":

    print(fraseConVocalMayuscula(str(input("Introduce una frase")), input("Introduce la vocal")))