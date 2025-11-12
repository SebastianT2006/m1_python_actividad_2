pan = 300
canidad = int(input("Ingrese la cantidad de panes que desea comprar: "))
if canidad >=20 and canidad <50:
    total= (pan*canidad) * 0.90
    print(f"El total a pagar por {canidad} panes es: {total}") 

elif canidad >=50:
    total= (pan*canidad) * 0.80
    print(f"El total a pagar por {canidad} panes es: {total}")
else:
    total= pan*canidad
    print(f"El total a pagar por {canidad} panes es: {total}")

