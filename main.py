from time import sleep

from cls_Stack import cls_Stack
from Subrutinas import validar_expresion, repartir_naipes


# CLASE JUGADOR

class Jugador:

    def __init__(self, nombre):

        self.nombre = nombre

        # Cada jugador tiene su propia pila
        self.pila = cls_Stack()

        # Lista de cartas obtenidas
        self.naipes_obtenidos = []


# PROBLEMA 1
# VALIDACION DE EXPRESIONES MATEMATICAS

def problema_1():

    print()
    print("====================================")
    print("          PROBLEMA 1")
    print("    EXPRESIONES MATEMATICAS")
    print("====================================")

    expresion = input(
        "Ingrese una expresion matematica: "
    )

    if validar_expresion(expresion):

        print("La expresion esta correctamente escrita")

    else:

        print("La expresion esta incorrectamente escrita")


# PROBLEMA 2
# BUSCANDO A LA REINA DE CORAZONES

def problema_2():

    print()
    print("====================================")
    print("          PROBLEMA 2")
    print("     REINA DE CORAZONES")
    print("====================================")

    # Crear los cuatro jugadores

    jugadores = [
        Jugador("Merlina"),
        Jugador("Tio Lucas"),
        Jugador("Pericles"),
        Jugador("Homero")
    ]

    print()
    print("Jugadores creados correctamente")

    for jugador in jugadores:

        print(
            jugador.nombre,
            "- Pila vacia:",
            jugador.pila.isempty()
        )

    # REPARTIR CARTAS

    print()
    print("Repartiendo cartas...")

    if not repartir_naipes(jugadores):
        return

    print()
    print("Cantidad de cartas por jugador:")

    for jugador in jugadores:

        print(
            jugador.nombre,
            ":",
            len(jugador.pila),
            "cartas"
        )

    # INICIAR EL JUEGO

    print()
    print("====================================")
    print("       INICIANDO EL JUEGO")
    print("====================================")

    ancho = 16

    # Encabezados de las columnas

    for jugador in jugadores:

        print(
            jugador.nombre.ljust(ancho),
            end=""
        )

    print()
    print("-" * 64)

    ganador = None

    # Continuar mientras haya cartas
    # y no se encuentre la Reina de Corazones

    while (
        any(not j.pila.isempty() for j in jugadores)
        and ganador is None
    ):

        for i, jugador in enumerate(jugadores):

            if not jugador.pila.isempty():

                # Sacar una carta
                naipe = jugador.pila.pop()

                # Guardar la carta obtenida
                jugador.naipes_obtenidos.append(naipe)

                # Mostrar carta en su columna
                print(
                    " " * (i * ancho) + naipe
                )

                # Verificar si es la Reina
                if naipe == "QC":

                    ganador = jugador

                    break

                # Esperar antes del siguiente turno
                sleep(2)

    # MOSTRAR RESULTADOS

    print()
    print("====================================")
    print("          RESULTADOS")
    print("====================================")

    if ganador is not None:

        print()
        print("GANADOR:", ganador.nombre)

        print("Encontro la Reina de Corazones (QC)")

        # List Comprehension
        # Obtener las cartas de corazon del ganador

        corazones = [
            naipe
            for naipe in ganador.naipes_obtenidos
            if naipe.endswith("C")
        ]

        print()
        print("Cartas de corazones obtenidas:")

        for carta in corazones:

            print(carta)

    else:

        print()
        print("No hubo ganador")

        print("La Reina de Corazones no fue encontrada")

    # VACIAR LAS PILAS

    print()
    print("Verificando las pilas...")

    for jugador in jugadores:

        while not jugador.pila.isempty():

            jugador.pila.pop()

        print(
            jugador.nombre,
            "- Pila vacia:",
            jugador.pila.isempty()
        )

    print()
    print("FIN DEL JUEGO")


# MENU PRINCIPAL

def main():

    while True:

        print()
        print("====================================")
        print("       PRIMERA PRUEBA PARCIAL")
        print("====================================")

        print("1. Validar expresion matematica")
        print("2. Buscar la Reina de Corazones")
        print("3. Salir")

        print()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            problema_1()

        elif opcion == "2":

            problema_2()

        elif opcion == "3":

            print("Programa finalizado")
            break

        else:

            print("Opcion incorrecta")


# EJECUTAR PROGRAMA

if __name__ == "__main__":

    main()
