"""
Calcular la edad de una persona
"""

print("Bienvenido, le mostraremos su edad")
actualYear = int(input("Ingrese el año actual:\n"));
bornYear = int(input("Ingrese su año de nacimiento:\n"));
result = actualYear - bornYear;
print("Usted tiene", result, "años")