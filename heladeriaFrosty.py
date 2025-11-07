chococalte=4000
vainilla=3500
toping=1000
cant_toping=0

eleccion = input("bienvenido a heladeria Frosty, quieres un toping?: ").lower()
if eleccion == "si":
    cant_toping = int(input("cuantos topings desea (el toping tiene un costo de $1000) "))
else:
    cant_toping = 0

helado = input("ingrese el sabor de helado que desea (chocolate/vainilla): ").lower()
costo_total=0


if helado == "chocolate":
    costo_total = chococalte+(toping*cant_toping)
    print(f"el costo total de su helado es: {costo_total}")
elif helado == "vainilla":
    costo_total = vainilla+(toping*cant_toping)
    print(f"el costo total de su helado es: {costo_total}")
else:
    print("sabor no disponible")

