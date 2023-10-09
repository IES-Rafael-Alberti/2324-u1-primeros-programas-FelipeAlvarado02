
def diferentesNombres(nombre):

    return nombre.lower(), nombre.upper(), nombre.title()

if __name__ == "__main__":

    print(diferentesNombres(str(input("Introduce tu nombre entero"))))