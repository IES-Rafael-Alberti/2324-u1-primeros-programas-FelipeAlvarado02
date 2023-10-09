
def calculoHoras(horasTrabajadas:int,pagoHora:int):

    while (horasTrabajadas < 0):
        horasTrabajadas = int(input("Por favor, introduzca un número mayor o igual a 0."))
    while (pagoHora <= 0):
        pagoHora = int(input("Por favor, introduzca un número positivo."))
    return f"El importe por las horas trabajadas es de " + str(horasTrabajadas * pagoHora) + " €."

if __name__ == "__main__":

    calculoHoras(int(input("Introduzca las horas trabajadas.")),int(input("Introduzca el pago por hora")))