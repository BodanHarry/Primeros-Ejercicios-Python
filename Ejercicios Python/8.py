"""
Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.
"""

print("Bienvenido, le mostraremos el precio mas alto y mas bajo")
price=float(input("Digite el precio del producto\n"))
aux=float(input("Digite el precio del producto\n"))

if price>aux:
    highest=price
    lowest=aux
else:
    highest=aux
    lowest=price

while price!=0:
    price=float(input("Digite el precio del producto (Si presiona 0, deja de pedir precios)\n"))

    if price==0:
        lowest=lowest
        highest=highest
    else:
        if price<=lowest:
            lowest=price
        else:
            if price>lowest:
                if price>highest:
                    highest=price

print("El precio mayor es",highest)
print("El precio menor es",lowest)