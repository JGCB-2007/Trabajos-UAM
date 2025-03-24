precio = float(input("Ingresa el precio del producto: "))
impuesto = precio * 0.10
precioimpuesto = precio + impuesto
descuento = precioimpuesto * 0.05
precio_final = precioimpuesto - descuento

print(f"Precio original: ${precio:.2f}")
print(f"Impuesto (10%): ${impuesto:.2f}")
print(f"Precioimpuesto: ${precioimpuesto:.2f}")
print(f"Descuento (5%): -${descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")
