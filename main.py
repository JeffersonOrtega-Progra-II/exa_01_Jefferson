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

