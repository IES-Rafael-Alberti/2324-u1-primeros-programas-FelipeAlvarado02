def mayusNombre(nombre):


    return "El nombre " + nombre.upper() + " y tiene " + str(len(nombre)) + " letras"


if __name__ == "__main__":

    print(mayusNombre(input("Introduce tu nombre\n")))
