documento=input("eres mayor de edad? (si/no): ").lower()


if documento=="si":
    verificacion=input("lo tienes en la mano? (si/no): ").lower()

    if verificacion=="si":
        print("puedes entrar al club estelar")
    else:
        print("no puedes entrar al club estelar")
else:
    print("entrada denegada")
