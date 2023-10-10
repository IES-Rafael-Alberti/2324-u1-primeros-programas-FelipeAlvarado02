def cambioArroba(frase):

    lista = frase.rsplit("@")

    frase = lista[0]+"@ceu.es"

    return frase

if __name__ == "__main__":

    print(cambioArroba(str(input("Introduce tu correo"))))