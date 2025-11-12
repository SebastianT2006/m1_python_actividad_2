print("Ingrese dos notas del 0.0 al 5.0")
nota1=float(input())
nota2=float(input())
promedio=float(((nota1*0.70)+(nota2*0.30)))
print(promedio)

if promedio >= 3:
    print("aprobado")
elif promedio >= 2 and promedio<3:
    print("revision")
else:
    print("Reprobado")