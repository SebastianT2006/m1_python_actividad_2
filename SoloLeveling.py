dias=int(input("ingrese la cantidad de dias que ha entrenado en la semana: "))
conti=True
while conti:
    if (dias>=4 and dias<=7):
        conti=False
        print("¡Excelente disciplina! + gana 1 punto de energía" )
    elif (dias>=2 and dias<=3):
        conti=False
        print("Bien, pero puedes dar más.")
    elif (dias==1 or dias==0):
        conti=False
        print("No aflojes, tú puedes mejorar")
        
    else:
        print("Número de días inválido. Por favor ingrese un número entre 0 y 7.")
        dias=int(input("ingrese la cantidad de dias que ha entrenado en la semana: "))
