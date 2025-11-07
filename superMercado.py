

producto = 2000
cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))

if cantidad <= 0:
    print("Cantidad no válida")
else:
    total = cantidad * producto

    
    if cantidad >= 30:
        total *= 0.85   
    elif cantidad >= 10:
        total *= 0.95
    else:
        total = total   

    
    if total < 50000:
        total += 5000
    else:
        total += 0

    print(f"El costo total es: ${total:.0f}")


    