libro=25000
codigo="LIBRO10"
estudiante=input("eres estudiantes (si/no): ").lower()
cupon=input("tienes cupon de descuento (si/no): ").lower()

if estudiante=="si":
    libro*=0.85
    if cupon=="si":
        codigo_ingresado=input("ingrese el codigo de su cupon: ")
        if codigo_ingresado==codigo:
            libro*=0.90
        else:
            libro=libro
elif estudiante=="no":
    if cupon=="si":
        codigo_ingresado=input("ingrese el codigo de su cupon: ")
        if codigo_ingresado==codigo:
            libro*=0.90
        else:
            libro=libro
    else:
        libro=libro


        
print(f"el costo total del libro es: ${libro}")

