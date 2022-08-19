"""
Leer x cantidad de edades y mostrar el promedio de dichas edades.
"""

print("Bienvenido, le mostraremos el promedio de las edades que digite")
num=float(1)
summation=float(0)
counter=float(0)

while num!=0:
    num=float(input("Digite la edad (Si presiona 0, deja de pedir edades)\n"))
    if num==0:
        summation=summation
        counter=counter
    else:
        summation+=num
        counter+=1

average= summation/counter

print("El promedio de edades es de",average)