from cls_Stack import cls_Stack

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

