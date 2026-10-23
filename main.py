from cls_Stack import cls_Stack
from Subrutinas import validar_expresion

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

