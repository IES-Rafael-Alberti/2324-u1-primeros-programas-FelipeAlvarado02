def calcularIva(producto:float,iva:float):
    while producto < 0:
        producto = float(input("Introduce el precio del producto.\n"))

    while (iva < 0) or (iva > 100):
        iva = float(input("Introduce el valor del IVA correcto.\n"))

    return f"El valor total es de: "+ str(producto + producto * (iva / 100))+ " €"

if __name__ == "__main__":

    print(calcularIva(float(input("Introduce el precio del producto.\n")),float(input("Introduce el valor del IVA correcto."))))
