"""
Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
enteros
"""
print("Bienvenido, le mostraremos los numeros pares comprendidos entre dos números")
x = int(input("Ingrese el valor inicial\n"));
y = int(input("Ingrese el valor final\n"));

print("La secuencia de números es:")
for i in range (x,y+1,1):
    if i % 2 == 0:
        print(i)