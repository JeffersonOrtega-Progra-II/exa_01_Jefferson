from cls_Stack import cls_Stack
from Subrutinas import validar_expresion, repartir_naipes

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pila = cls_Stack()
        self.naipes_obtenidos = []

print("====================================")
print("       PRIMERA PRUEBA PARCIAL")
print("====================================")

print("Estructura de datos: Pilas")
print()

pila = cls_Stack()

print("La pila está vacía:", pila.isempty())

pila.push("A")
pila.push("B")
pila.push("C")

print("Elementos agregados correctamente")

print()
print("Contenido de la pila:")

while not pila.isempty():
    print(pila.pop())

print()
print("La pila quedó vacía:", pila.isempty())

print()
print("PROBLEMA 1 - EXPRESIONES MATEMATICAS")

expresion = input("Ingrese una expresion matematica: ")

if validar_expresion(expresion):
    print("La expresion esta correctamente escrita")
else:
    print("La expresion esta incorrectamente escrita")

print()
print("PROBLEMA 2 - REINA DE CORAZONES")

jugadores = [
    Jugador("Merlina"),
    Jugador("Tio Lucas"),
    Jugador("Pericles"),
    Jugador("Homero")
]

print("Jugadores creados correctamente:")

for jugador in jugadores:
    print(jugador.nombre)
    print("Pila vacia:", jugador.pila.isempty())

print()
print("REPARTIENDO NAIPES...")

repartir_naipes(jugadores)

print()
print("Cantidad de cartas por jugador:")

for jugador in jugadores:
    print(jugador.nombre, ":", len(jugador.pila), "cartas")

from time import sleep

# INICIO DEL JUEGO

print()
print("====================================")
print("      BUSCANDO A LA REINA")
print("====================================")

ancho = 16

# Mostrar los nombres de los jugadores en columnas
for jugador in jugadores:
    print(jugador.nombre.ljust(ancho), end="")

print()
print("-" * 64)

ganador = None

# Jugar mientras existan cartas y no haya ganador
while any(not j.pila.isempty() for j in jugadores) and ganador is None:

    for i, jugador in enumerate(jugadores):

        if not jugador.pila.isempty():

            # Sacar una carta de la pila
            naipe = jugador.pila.pop()

            # Guardar las cartas obtenidas
            jugador.naipes_obtenidos.append(naipe)

            # Mostrar la carta en la columna del jugador
            print(" " * (i * ancho) + naipe)

            # Buscar la Reina de Corazones
            if naipe == "QC":
                ganador = jugador
                break

            # Esperar 2 segundos para el siguiente turno
            sleep(2)


# RESULTADOS DEL JUEGO

print()
print("====================================")
print("          RESULTADOS")
print("====================================")

if ganador is not None:

    print("El ganador es:", ganador.nombre)
    print("Encontro la Reina de Corazones (QC)")

    # Obtener todos los corazones del ganador
    corazones = [
        naipe
        for naipe in ganador.naipes_obtenidos
        if naipe.endswith("C")
    ]

    print()
    print("Cartas de corazones del ganador:")

    for carta in corazones:
        print(carta)

else:
    print("No hubo ganador.")
    print("La Reina de Corazones no fue encontrada.")


# VACIAR LAS PILAS AL FINALIZAR

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

