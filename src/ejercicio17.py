
def repNombre(nombre, num):

    total = ""

    while num > 0:
        total = total + str(nombre) +"\n"
        num = num-1

    return total

if __name__ == "__main__":

    print(repNombre(str(input("Introduce tu nombre")), int(input("Introduce el número de veces a repetir "))))