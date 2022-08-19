"""
Leer dos números y decir cual es mayor y cual es menor
"""
print("Bienvenido, le mostraremos el número mayor y menor de dos números")
x = float(input("Ingrese el primer valor\n"));
y = float(input("Ingrese el segundo valor\n"));

if x>y:
    print("El número mayor es",x)
    print("El número menor es",y)
else:
    print("El número mayor es",y)
    print("El número menor es",x)