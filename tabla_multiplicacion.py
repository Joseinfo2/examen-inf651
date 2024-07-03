n=int(input("ingrese un numero menor a 10: "))
if n>=10:
    print("el numero tiene que ser menor a 10")
else:
    print("la tabla de multiplicacion del {n} :")
    for i in range(1,11):
        resultado=n*i
        print(f"{n}x{i}={resultado}")
