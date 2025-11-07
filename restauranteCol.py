menu=12000
costoT=0
IVA=12000+(12000*0.08)
print("Bienvenido a restaurante El sabor colombiano el menu tiene un costo de 12000")
bebida=input("Desea bebida? (s/n): la bebida tiene un costo adicional de 3000 ")
if bebida.lower() != "s":
    costoT=12000
    IVA=costoT*1.08
    print(f"El costo total de su pedido es de: {costoT} incluyendo el iva es de {IVA}" )
else:
    costoT=12000+3000
    IVA=costoT+(costoT*0.08)
    print(f"El costo total de su pedido es de: {costoT} incluyendo el iva es de {IVA}" )