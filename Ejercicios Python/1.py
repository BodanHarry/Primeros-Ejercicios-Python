"""
Mostrar el total a pagar por la compra de n cantidad de productos a un precio
desconocido
"""

print("Bienvenido, le mostraremos su total de compra")
quantity= int(input("Digite la cantidad de productos que lleva\n"))
price= int(input("Digite el precio de los productos\n"))
total = quantity*price
print("Su total es de", total)