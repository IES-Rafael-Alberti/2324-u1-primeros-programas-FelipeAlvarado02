
def calcularPrecio(precio):
    iva = 10
    return (f"El valor original sin iva es de: "+ str(precio - precio * (iva / 110))
            +"€, y su iva es de " + str(precio * (iva / 110)) +" €")

if __name__ == "__main__":

    print(calcularPrecio(float(input("Introduzca el precio del producto:\n"))))