"""
Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro.

Mejor hice un banco
"""

option = int(1)
AccountStatus = float(0)

while option!=0:
    print("Bienvenido, digite el numero segun la opción que desea ejecutar")
    print("1. Introducir dinero")
    print("2. Retirar dinero")
    print("3. Revisar estado de cuenta")
    print("0. Salir")
    option=int(input("Digite el número"))

    if option==1:
        AccountStatus= AccountStatus + float(input("Cuanto dinero desea ingresar?\n"))
    elif option==2:
        retire = float(input("Cuanto dinero desea retirar?\n"))
        if AccountStatus>=retire:
            AccountStatus= AccountStatus - retire
        else:
            print("No cuenta con los suficientes fondos\n")
    elif option==3:
        print(AccountStatus)
    else:
        print("Saliste")