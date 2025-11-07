precio=0
edad = int(input("Ingrese su edad: "))
if edad < 5:
    precio = 0
    print("El precio de la entrada a niños menores o igual a 5 años es gratis.")
elif edad >= 5 and edad <= 11:
    precio = 5000
    print("El precio de la entrada para niños entre 6 y 11 años es de $5000.")
elif edad >= 12 and edad <= 59:
    precio = 8000
    print("El precio de la entrada para adultos entre 12 y 59 años es de $8000.")
else:
    precio = 4000
    print("El precio de la entrada para adultos mayores de 60 años es de $4000.")
