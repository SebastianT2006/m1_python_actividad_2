horas=0
valor_pagar=0
porHora=2000
horas=int(input("ingrese la cantidad de horas que ha permanecido en el parqueadero: "))
while horas<0:
    print("Error: La cantidad de horas no puede ser negativa.")
    horas=int(input("ingrese la cantidad de horas que ha permanecido en el parqueadero: "))
if horas==0:
    horas=1
    valor_pagar=porHora*horas
    print(f"El valor a pagar es: {valor_pagar} pesos")
    
elif horas <=5:
    valor_pagar=porHora*horas
    print(f"El valor a pagar es: {valor_pagar} pesos")
elif horas >5:
    valor_pagar=5000+(horas*porHora)
    print(f"El valor a pagar es: {valor_pagar} pesos")


