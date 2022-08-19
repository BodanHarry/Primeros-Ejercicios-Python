"""
Aplicar el IVA al precio de un producto
"""

print("Bienvenido, le mostraremos el precio total de su producto con IVA")
price= float(input("Digite el precio de los productos\n"))
iva= float(0.15)
total = price + (price*0.15)
print("Su total es de", total)