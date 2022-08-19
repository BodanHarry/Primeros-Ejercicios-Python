"""
Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95.
"""
option = int(1)
average= float(0)
firstName= input("Digite su primer nombre\n")
secondName= input("Digite su segundo nombre\n")
firstSurname= input("Digite su primer apellido\n")
secondSurname= input("Digite su segundo apellido\n")

print("Bienvenido", firstName ,"digite su carrera")
print("1. Ingeniería en sistemas de información")
print("2. Otra carrera")
option=int(input("Digite el número\n"))

if option==1:
    carrer= "Ingeniería en Sistemas de Información"
    average=float(input("Digite su promedio\n"))
    if average>=95:
        scholarship= "La beca ha sido aprobada\n"
    else:
        scholarship= "La beca ha sido denegada\n"
    
    print("Nombre:",firstName,firstSurname)
    print("Carrea:", carrer)
    print ("Su promedio es de:",average)
    print(scholarship,"\n")

else:
    carrer= input("Digite su carrera\n")
    average=float(input("Digite su promedio\n"))
    if average>=85:
        scholarship= "La beca ha sido aprobada\n"
    else:
        scholarship= "La beca ha sido denegada\n"
    
    print("Nombre:",firstName,firstSurname)
    print("Carrea:", carrer)
    print ("Su promedio es de:",average)
    print(scholarship,"\n")