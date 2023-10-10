def divisionPartes(num1,num2):
    cociente = num1//num2
    resto = num1-(num2*cociente)
    return (f"La division de {num1} y {num2} da un cociente de {cociente} y un resto de {resto}, "
            f"donde {num1} y {num2} son los números introducidos por el usuario, y {cociente} y {resto} son el cociente y el resto de la división entera respectivamente")



if __name__ == "__main__":

    print(divisionPartes(float(input("Introduce el dividendo")), float(input("Introduce eñ divisor "))))