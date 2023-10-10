from src.ejercicio1 import nombre
from src.ejercicio2 import calculoHoras
from src.ejercicio4 import coversionTemperatura
from src.ejercicio5 import calcularIva
from src.ejercicio6 import calcularPrecio
from src.ejercicio7 import sumar1
from src.ejercicio8 import sumar2
from src.ejercicio9 import sumar3
from src.ejercicio10 import calculofraccionario
from src.ejercicio11 import sumaDeSusAnteriores
from src.ejercicio12 import calculoIMC
from src.ejercicio13 import divisionPartes
from src.ejercicio14 import calculoEnvio
from src.ejercicio16 import calculoBarras
from src.ejercicio17 import repNombre
from src.ejercicio18 import diferentesNombres
from src.ejercicio19 import mayusNombre
from src.ejercicio21 import fraseReves
from src.ejercicio22 import fraseConVocalMayuscula
from src.ejercicio23 import cambioArroba
from src.ejercicio24 import divisionDineroEurosCentimos
from src.ejercicio25 import divisionFecha


def test_nombre():
    assert nombre("Al") == "Hola, Al."

def test_calculoHoras():
    assert calculoHoras(40,12) == "El importe por las horas trabajadas es de 480 €."

def test_coversionTemperatura():
    assert coversionTemperatura(32) == "El resultado es de: 89.6 Grados Fahrenheit."

def test_calcularIva():
    assert calcularIva(100,10) == "El valor total es de: 110.0 €"

def test_calcularPrecio():
    assert calcularPrecio(110) == "El valor original sin iva es de: 100.0€, y su iva es de 10.0 €"

def test_sumar1():
    assert sumar1(5,2,3) == "10"

def test_sumar2():
    assert sumar2(5,2) == "7"

def test_sumar3():
    assert sumar3(5,2,3) == "10"

def test_scalculofraccionario():
    assert calculofraccionario() == "10.240000000000002"

def test_sumaDeSusAnteriores():
    assert sumaDeSusAnteriores(3) == "6"

def test_calculoIMC():
    assert calculoIMC(66,1.70) == "22.83"

def test_divisionPartes():
    assert divisionPartes(12,5) == "La division de 12.0 y 5.0 da un cociente de 2.0 y un resto de 2.0, donde 12.0 y 5.0 son los números introducidos por el usuario, y 2.0 y 2.0 son el cociente y el resto de la división entera respectivamente"

def test_calculoEnvio():
    assert calculoEnvio(30,30) == "El peso total del envío es de: 5.61 Kilogramos"

def test_calculoBarras():
    assert calculoBarras(8) == "Una barra de pan cuesta 3.49 normalmente, con el descuento 2.094 y lo recaudado por barras no frescas es de 16.752"

def test_repNombre():
    assert repNombre("Alan",4) == ("Alan"
                                   " Alan "
                                   "Alan "
                                   "Alan")

def test_diferentesNombres():
    assert diferentesNombres("Alan", 4) == ('alan', 'ALAN', 'Alan')

def test_mayusNombre():
    assert mayusNombre("Beatriz") == "El nombre BEATRIZ y tiene 7 letras"

def test_fraseReves():
    assert fraseReves("alakazam olorosa Albertosaurio") == "oiruasotreblA asorolo mazakala"

def test_fraseConVocalMayuscula():
    assert fraseConVocalMayuscula("alakazam olorosa Albertosaurio","A") == "AlAkAzAm olorosA AlbertosAurio"

def test_cambioArroba():
    assert cambioArroba("alalalalala@gmail.com") == "alalalalala@ceu.es"

def test_divisionDineroEurosCentimos():
    assert divisionDineroEurosCentimos(13.13) == "Son 13 euros con 13 centimos."

def test_divisionFecha():
    assert divisionFecha("23/25/2027") == "Es el día 23 del mes 25 y del año 2027"

