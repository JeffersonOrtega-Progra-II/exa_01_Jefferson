import random

from cls_Stack import cls_Stack

# means of char
# B = Bastos o pica
# C = Corazones
# D = Diamantes
# T = Treboles

baraja = [
    ["1B", "2B", "3B", "4B", "5B", "6B", "7B",
     "8B", "9B", "10B", "JB", "QB", "KB"],

    ["1C", "2C", "3C", "4C", "5C", "6C", "7C",
     "8C", "9C", "10C", "JC", "QC", "KC"],

    ["1D", "2D", "3D", "4D", "5D", "6D", "7D",
     "8D", "9D", "10D", "JD", "QD", "KD"],

    ["1T", "2T", "3T", "4T", "5T", "6T", "7T",
     "8T", "9T", "10T", "JT", "QT", "KT"]
]
def validar_expresion(expresion):
    pila = cls_Stack()

    if not pila.isempty():
        return False

    parejas = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    correcta = True

    for caracter in expresion:

        if caracter in "([{":
            if pila.isfull():
                correcta = False
                break

            pila.push(caracter)

        elif caracter in ")]}":
            if pila.isempty():
                correcta = False
                break

            apertura = pila.pop()

            if apertura != parejas[caracter]:
                correcta = False
                break

    if not pila.isempty():
        correcta = False

    while not pila.isempty():
        pila.pop()

    return correcta

    while not pila.isempty():
        pila.pop()

    return correcta

    while not pila.isempty():
        pila.pop()

    return correcta

def repartir_naipes(jugadores):

    # Crear una lista con todas las cartas de la baraja
    naipes_disponibles = []

    for palo in baraja:
        for naipe in palo:
            naipes_disponibles.append(naipe)

    # Mezclar las cartas aleatoriamente
    random.shuffle(naipes_disponibles)

    # Comprobar que las pilas estén vacías
    for jugador in jugadores:
        if not jugador.pila.isempty():
            print("Error: la pila debe iniciar vacia")
            return

    # Repartir una carta por turno a cada jugador
    while not all(jugador.pila.isfull() for jugador in jugadores):

        for jugador in jugadores:

            if not jugador.pila.isfull():
                naipe = naipes_disponibles.pop()
                jugador.pila.push(naipe)

    print("Cartas repartidas correctamente")

    
