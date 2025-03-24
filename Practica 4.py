a=int(input("Ingrese el primer valor:"))
b=int(input("Ingrese el segundo valor:"))
print(f"Antes del intercambio: a = {a}, b = {b}")
a, b = b, a
print(f"Después del intercambio: a = {a}, b = {b}")
