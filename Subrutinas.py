import random
from cls_Stack import cls_Stack

# B = Bastos o Picas
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


# PROBLEMA 1
# Validar expresiones matematicas

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

    # Vaciar la pila al finalizar
    while not pila.isempty():
        pila.pop()

    return correcta


# PROBLEMA 2
# Repartir naipes aleatoriamente

def repartir_naipes(jugadores):

    naipes_disponibles = []

    # Cargar todas las cartas de la baraja
    for palo in baraja:
        for naipe in palo:
            naipes_disponibles.append(naipe)

    # Mezclar las cartas
    random.shuffle(naipes_disponibles)

    # Verificar que las pilas esten vacias
    for jugador in jugadores:

        if not jugador.pila.isempty():
            print("Error: las pilas deben iniciar vacias")
            return False

    # Repartir una carta por turno
    while not all(jugador.pila.isfull() for jugador in jugadores):

        for jugador in jugadores:

            if not jugador.pila.isfull():

                if not naipes_disponibles:
                    print("Error: no hay cartas suficientes")
                    return False

                naipe = naipes_disponibles.pop()

                jugador.pila.push(naipe)

    print("Cartas repartidas correctamente")

    return True

    
